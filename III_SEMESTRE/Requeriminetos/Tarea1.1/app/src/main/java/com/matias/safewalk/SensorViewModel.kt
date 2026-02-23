package com.matias.safewalk

import android.Manifest
import android.app.Application
import android.content.Context
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.os.Build
import android.os.Handler
import android.os.Looper
import android.os.VibrationEffect
import android.os.Vibrator
import android.telephony.SmsManager
import android.widget.Toast
import androidx.annotation.RequiresApi
import androidx.annotation.RequiresPermission
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import kotlin.math.sqrt

class SensorViewModel(
    application: Application,
    private val dataStoreManager: DataStoreManager
) : AndroidViewModel(application), SensorEventListener {

    private val umbral = 15f
    private var ultimoFueFuerte = false

    private val _alertaEnviada = MutableStateFlow(false);
    val alertaEnviada: StateFlow<Boolean> = _alertaEnviada
    private val context = getApplication<Application>()

    private lateinit var alertaJob: Job
    private val vibrator = context.getSystemService(Context.VIBRATOR_SERVICE) as Vibrator

    private val _modoVigilancia = MutableStateFlow(false)
    val modoVigilancia: StateFlow<Boolean> = _modoVigilancia

    private val _caídaDetectada = MutableStateFlow(false)
    val caídaDetectada: StateFlow<Boolean> = _caídaDetectada

    private var alertaEnProceso = false

    private val _cuentaRegresiva = MutableStateFlow(10)
    val cuentaRegresiva: StateFlow<Int> = _cuentaRegresiva

    private var numeroEmergencia: String = ""

    init {
        viewModelScope.launch {
            dataStoreManager.contactoEmergencia.collect { numero ->
                numeroEmergencia = numero ?: ""
            }
        }
    }

    fun toggleModoVigilancia() {
        _modoVigilancia.value = !_modoVigilancia.value
    }

    fun resetCaida() {
        if (::alertaJob.isInitialized) { //referencia a la variable, para asi cancelar el sub proceso ese
            alertaJob.cancel()
        }

        _caídaDetectada.value = false
        alertaEnProceso = false
        vibrator.cancel()
        ultimoFueFuerte = false
        _alertaEnviada.value = false
    }

    override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) {

    }
    @RequiresPermission(Manifest.permission.VIBRATE)
    @RequiresApi(Build.VERSION_CODES.O)
    override fun onSensorChanged(event: SensorEvent) { //aca es donde llegan los datos del sensor de movimiento

        val x = event.values[0] //eje x
        val y = event.values[1] //eje y
        val z = event.values[2] //eje z

        val magnitud = sqrt(x * x + y * y + z * z) //la formula del profe

        if (magnitud > umbral && !alertaEnProceso) {
            ultimoFueFuerte = true
            _caídaDetectada.value = true

        } else {
            if (ultimoFueFuerte && !alertaEnProceso) {
                alertaEnProceso = true
                ultimoFueFuerte = false

                val efecto = VibrationEffect.createOneShot(10_000, VibrationEffect.DEFAULT_AMPLITUDE)
                vibrator.vibrate(efecto)

                alertaJob = viewModelScope.launch {

                    for (i in 10 downTo 0) {
                        _cuentaRegresiva.value = i
                        delay(1000)
                    }

                    enviarSmsAlerta()
                    _caídaDetectada.value = false
                    _alertaEnviada.value = true
                    alertaEnProceso = false
                }
            }
        }
    }

    fun enviarSmsAlerta() {
        if (numeroEmergencia.isEmpty()) return
        val mensaje = "ALERTA: AYUDA NO RESPONDO"
        val sms = SmsManager.getDefault()
        sms.sendTextMessage(numeroEmergencia, null, mensaje, null, null)
    }
    fun enviarSmsAlertaPanico() {
        if (numeroEmergencia.isEmpty()) return
        val mensaje = "ALERTA: AYUDA NO RESPONDO"
        val sms = SmsManager.getDefault()
        sms.sendTextMessage(numeroEmergencia, null, mensaje, null, null)
        _alertaEnviada.value = true
    }

}