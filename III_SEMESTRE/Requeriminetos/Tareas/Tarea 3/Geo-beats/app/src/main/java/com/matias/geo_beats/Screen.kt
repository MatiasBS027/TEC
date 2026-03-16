package com.matias.geo_beats

import androidx.compose.runtime.Composable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.ui.Modifier
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults.buttonColors
import androidx.compose.material3.Text
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp
import androidx.compose.ui.Alignment
import androidx.compose.ui.unit.dp
import androidx.compose.ui.platform.LocalContext
import androidx.compose.runtime.remember
import androidx.compose.runtime.mutableStateOf
import androidx.compose.material3.AlertDialog

@Composable
fun Screen(){
    val context = LocalContext.current
    val showDialog = remember { mutableStateOf(false) }
    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center

    ) {
        Text(
            text = "Geo Beats",
            fontSize = 32.sp,
            fontWeight = FontWeight.Bold
        )
        Button(
            onClick = {
                if (!launchRandomPlaylist(context)) {
                    showDialog.value = true
                }
            },
            modifier = Modifier.size(width = 200.dp, height = 200.dp),
            shape = CircleShape,
            colors = buttonColors()
        ) {
            Text("Reproducir playlist")
        }
    }
    if (showDialog.value) {
        AlertDialog(
            onDismissRequest = { showDialog.value = false },
            title = { Text("Spotify no encontrado") },
            text = { Text("No tienes Spotify instalado en el dispositivo.") },
            confirmButton = {
                Button(onClick = { showDialog.value = false }) {
                    Text("OK")
                }
            }
        )
    }
}