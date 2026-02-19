package com.matias.safewalk

import androidx.compose.runtime.*
import androidx.compose.material3.*
import androidx.compose.foundation.layout.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import kotlinx.coroutines.launch

@Composable
fun SettingsScreen(dataStoreManager: DataStoreManager) {

    val contactoGuardado by dataStoreManager.contactoEmergencia.collectAsState(initial = "")
    var numeroContacto by remember(contactoGuardado) { mutableStateOf(contactoGuardado ?: "") }
    val scope = rememberCoroutineScope()
    val snackbarHostState = remember { SnackbarHostState() }



    Scaffold(
        snackbarHost = { SnackbarHost(snackbarHostState) }
    ) { _ ->
        Column(
            modifier = Modifier.fillMaxSize(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            Text(text = "Contacto de Emergencia")

            OutlinedTextField(
                value = numeroContacto,
                onValueChange = { numeroContacto = it },
                label = { Text("Número de teléfono") }
            )

            Button(onClick = {
                scope.launch {
                    dataStoreManager.guardarContacto(numeroContacto)
                    snackbarHostState.showSnackbar("Contacto guardado!")
                }
            }) {
                Text("Guardar")
            }
        }
    }


}