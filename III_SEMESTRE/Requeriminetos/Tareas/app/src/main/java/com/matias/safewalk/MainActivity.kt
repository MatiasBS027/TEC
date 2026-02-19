package com.matias.safewalk

import android.content.Context
import android.content.pm.PackageManager
import android.hardware.Sensor
import android.hardware.SensorManager
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.viewModels
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewmodel.compose.viewModel
import com.matias.safewalk.ui.theme.SafeWalkTheme
import android.Manifest

class MainActivity : ComponentActivity() {

    private lateinit var viewModel: SensorViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        pedirPermisoSms()

        val dataStoreManager = DataStoreManager(this)
        viewModel = ViewModelProvider(
            this,
            SensorViewModelFactory(application, dataStoreManager)
        )[SensorViewModel::class.java]
        setContent {
            SafeWalkTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { _ ->
                    NavGraph(viewModel = viewModel,
                        dataStoreManager = dataStoreManager
                    )
                }
            }
        }
    }
    override fun onResume() {
        super.onResume()
        val sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager
        val accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
        accelerometer?.let {
            sensorManager.registerListener(viewModel, it, SensorManager.SENSOR_DELAY_NORMAL)
        }
    }

    override fun onPause() {
        super.onPause()
        val sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager
        sensorManager.unregisterListener(viewModel)
    }

    private fun pedirPermisoSms() {
        if (ContextCompat.checkSelfPermission(
                this,
                Manifest.permission.SEND_SMS
            ) != PackageManager.PERMISSION_GRANTED
        ) {
            ActivityCompat.requestPermissions(
                this,
                arrayOf(Manifest.permission.SEND_SMS),
                1
            )
        }
    }

}