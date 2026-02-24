package com.matias.safewalk


import android.provider.ContactsContract
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.ui.Modifier
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults.buttonColors
import androidx.compose.material3.Text
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp
import androidx.compose.ui.Alignment
import androidx.compose.material3.Switch
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController

@Composable
fun AlarmScreen(viewModel: SensorViewModel, navController: NavController, dataStorage: DataStoreManager) {
    val modoVigilancia by viewModel.modoVigilancia.collectAsState()
    val caídaDetectada by viewModel.caídaDetectada.collectAsState()
    val cuentaRegresiva by viewModel.cuentaRegresiva.collectAsState()
    val alertaEnviada by viewModel.alertaEnviada.collectAsState()
    val nombreContacto by dataStorage.nombreEmergencia.collectAsState(initial = "")

    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center

    ) {
        Text(
            text = "SafeWalk",
            fontSize = 32.sp,
            fontWeight = FontWeight.Bold
        )

        Row(
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text(text = "Modo Vigilancia")
            Switch(
                checked = modoVigilancia,
                onCheckedChange = { viewModel.toggleModoVigilancia() }
            )
        }
        Spacer(modifier = Modifier.height(40.dp))

        Button(
            onClick = { if(modoVigilancia)viewModel.enviarSmsAlertaPanico() },
            modifier = Modifier
                .size(width = 200.dp, height = 200.dp),
            shape = CircleShape,
            colors = buttonColors(
                containerColor = if (modoVigilancia) Color.Red else Color.Gray
            )
        ) {
            Text(text = "PÁNICO", fontSize = 24.sp, fontWeight = FontWeight.Bold)
        }
        Spacer(modifier = Modifier.height(80.dp))

        Button(onClick = { navController.navigate("settings") }) {
            Text("Configurar Contacto")
        }
    }
    if (caídaDetectada) {
        AlertDialog(
            onDismissRequest = { },
            title = { Text("¡Caída Detectada!") },
            text = { Text("Se enviará una alerta en $cuentaRegresiva segundos") },
            confirmButton = {
                Button(onClick = { viewModel.resetCaida() }) {
                    Text("Cancelar Alerta")
                }
            }
        )
    }
    if (alertaEnviada) {
        AlertDialog(
            onDismissRequest = {
                viewModel.resetCaida()
            },
            title = { Text("Alerta enviada") },
            text = { Text("Alerta enviada al contacto: $nombreContacto") },
            confirmButton = {
                Button(onClick = { viewModel.resetCaida() }) {
                    Text("Aceptar")
                }
            }
        )
    }

}