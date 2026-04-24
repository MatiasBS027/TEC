package com.matias.safewalk

import androidx.compose.runtime.*
import androidx.compose.material3.*
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import kotlinx.coroutines.launch

@Composable
fun SettingsScreen(dataStoreManager: DataStoreManager, navController: NavController) {

    val nombreGuardado by dataStoreManager.nombreEmergencia.collectAsState(initial = "")
    var nombreContacto by remember(nombreGuardado) { mutableStateOf(nombreGuardado ?: "") }
    val contactoGuardado by dataStoreManager.contactoEmergencia.collectAsState(initial = "")
    var numeroContacto by remember(contactoGuardado) { mutableStateOf(contactoGuardado ?: "") }
    val scope = rememberCoroutineScope()
    val snackbarHostState = remember { SnackbarHostState() }



    Box(modifier = Modifier.fillMaxSize()) {

        Column(
            modifier = Modifier
                .fillMaxSize(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {

            Text(text = "Contacto de Emergencia")

            OutlinedTextField(
                value = nombreContacto,
                onValueChange = { nombreContacto = it },
                label = { Text("Nombre del contacto") }
            )

            OutlinedTextField(
                value = numeroContacto,
                onValueChange = {numeroContacto = it },
                label = { Text("Número de teléfono") },
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Phone)
            )

            Button(onClick = {
                scope.launch {
                    dataStoreManager.guardarContacto(
                        numeroContacto,
                        nombreContacto
                    )
                    snackbarHostState.showSnackbar("Contacto guardado!")
                }
            }) {
                Text("Guardar")
            }

            Button(onClick = { navController.popBackStack() }) {
                Text("Volver")
            }
        }

        //
        SnackbarHost(
            hostState = snackbarHostState,
            modifier = Modifier
                .align(Alignment.TopCenter)
                .padding(top = 16.dp)
        )
        }
    }


