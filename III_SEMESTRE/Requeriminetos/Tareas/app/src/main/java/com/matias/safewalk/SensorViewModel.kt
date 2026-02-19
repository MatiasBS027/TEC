package com.matias.safewalk

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class SensorViewModel : ViewModel() {

    private val _modoVigilancia = MutableStateFlow(false)
    val modoVigilancia: StateFlow<Boolean> = _modoVigilancia

    private val _caídaDetectada = MutableStateFlow(false)
    val caídaDetectada: StateFlow<Boolean> = _caídaDetectada

    fun toggleModoVigilancia() {
        _modoVigilancia.value = !_modoVigilancia.value
    }

    fun resetCaida() {
        _caídaDetectada.value = false
    }

}