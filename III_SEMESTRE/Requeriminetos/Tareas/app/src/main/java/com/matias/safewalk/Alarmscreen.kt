package com.matias.safewalk

import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.ui.Modifier
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.ButtonDefaults.buttonColors
import androidx.compose.material3.Text
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp
import androidx.compose.ui.Alignment
import androidx.compose.material3.Switch
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.graphics.Color
import androidx.navigation.NavController

@Composable
fun AlarmScreen(viewModel: SensorViewModel, navController: NavController) {
    val modoVigilancia by viewModel.modoVigilancia.collectAsState()
    val caídaDetectada by viewModel.caídaDetectada.collectAsState()

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
        Button(
            onClick = { },
            colors = buttonColors(
                containerColor = if (modoVigilancia) Color.Red else Color.Gray
            )
        ) {
            Text(text = "PÁNICO")
        }

        Button(onClick = { navController.navigate("settings") }) {
            Text("Configurar Contacto")
        }
    }
    if (caídaDetectada) {
        AlertDialog(
            onDismissRequest = { },
            title = { Text("¡Caída Detectada!") },
            text = { Text("Se enviará una alerta en 10 segundos") },
            confirmButton = {
                Button(onClick = { viewModel.resetCaida() }) {
                    Text("Cancelar Alerta")
                }
            }
        )
    }

}