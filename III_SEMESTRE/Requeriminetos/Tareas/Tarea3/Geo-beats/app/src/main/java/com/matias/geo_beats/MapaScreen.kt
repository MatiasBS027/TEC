package com.matias.geo_beats

/* Joha
 *En este kt se maneja lo relacionado con el mapa.
 *Pido permiso de ubicacion al user, obtinie su posiciona actual
 * y se muestran marcadores en los puntos de interes cercanos.
 */
import android.Manifest
import android.content.pm.PackageManager
import android.location.Location
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.core.content.ContextCompat
import androidx.annotation.RequiresPermission
import com.google.android.gms.location.LocationServices
import com.google.android.gms.maps.model.CameraPosition
import com.google.android.gms.maps.model.LatLng
import com.google.maps.android.compose.*
import com.google.android.gms.location.LocationCallback
import com.google.android.gms.location.LocationRequest
import com.google.android.gms.location.LocationResult
import com.google.android.gms.location.Priority
import androidx.compose.material3.Button
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Text

// Funcion que solicita la ubicacion actual del dispositivo
@RequiresPermission(android.Manifest.permission.ACCESS_FINE_LOCATION)
fun obtenerUbicacionActual(
    contexto: android.content.Context,
    alObtenerUbicacion: (LatLng) -> Unit
): Pair<com.google.android.gms.location.FusedLocationProviderClient, LocationCallback> {
    val cliente = LocationServices.getFusedLocationProviderClient(contexto)

    //solicita la ubicacion cada 5 seg, con un minimo de 3 seg entre actualizaciones, cambio que hice con respecto a como estaba.
    val solicitud = LocationRequest.Builder(Priority.PRIORITY_HIGH_ACCURACY, 5000)
        .setMinUpdateIntervalMillis(3000)
        .build()

    //Este callback se ejecuta cada vez que llega a una nueva ubicacion
    val callback = object : LocationCallback() {
        override fun onLocationResult(resultado: LocationResult) {
            resultado.lastLocation?.let { location ->
                alObtenerUbicacion(LatLng(location.latitude, location.longitude))
            }
        }
    }
    cliente.requestLocationUpdates(solicitud, callback, android.os.Looper.getMainLooper())
    return Pair(cliente, callback)
}
@Composable
fun MapaScreen() {
    //Contexto pa acceder al GPS y el resto de servicios
    val contexto = LocalContext.current

    //variable que empieza en null (sin ubicacion) y que puede guardar coordenadas (latitud y longitud(LatLng))
    //el rembember es para que no se restee cada que la pantalla se redibuja
    var ubiUsuario by remember { mutableStateOf<LatLng?>(null) }

    // Estado para mostrar el diálogo cuando Spotify no esté instalado
    val showDialog = remember { mutableStateOf(false) }

    //guardamos el cliente y el callback para cancelarlos cuando la pantalla se cieree
    var locationClient by remember { mutableStateOf<com.google.android.gms.location.FusedLocationProviderClient?>(null) }
    var locationCallback by remember { mutableStateOf<LocationCallback?>(null) }

    // Launcher que maneja la respuesta del usuario al pedir permiso
    val launcher = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission())

    { concedido ->
        if (concedido) {
            val (cliente, callback) =obtenerUbicacionActual(contexto) { ubicacion ->
                ubiUsuario = ubicacion

                // Ver si el user esta cerca de algun punto de interes
                puntosDeInteres.forEach { punto ->
                    val distancia = calcularDistancia(ubicacion, punto.coordenadas)
                    if (distancia < 50) {
                        launchPlaylist(contexto, punto.uriSpotify)
                    }
                }
            }
            locationClient = cliente
            locationCallback = callback
        }
    }

    // Al iniciar la pantalla, verificamos si ya tenemos permiso o lo pedimos, se ejecuta una vez cuando la pantalla aparece
    LaunchedEffect(Unit) {
        val permiso = ContextCompat.checkSelfPermission(
            contexto, Manifest.permission.ACCESS_FINE_LOCATION
        )
        //Si ya tiene permiso, obtenemos la ubicacion directo
        if (permiso == PackageManager.PERMISSION_GRANTED) {
            val (cliente,callback) = obtenerUbicacionActual(contexto) { ubicacion ->
                ubiUsuario = ubicacion

                // Ver si el user esta cerca de algun punto de interes
                puntosDeInteres.forEach { punto ->
                    val distancia = calcularDistancia(ubicacion, punto.coordenadas)
                    if (distancia < 50) {
                        launchPlaylist(contexto, punto.uriSpotify)
                    }
                }
            }
            locationClient = cliente
            locationCallback = callback
        } else {
            // No tiene permiso, le pedimos el permiso al usuario
            launcher.launch(Manifest.permission.ACCESS_FINE_LOCATION)
        }
    }

    //Parte visual: el mapa

    //Si la ubicacion es != de null
    ubiUsuario?.let { pos ->
        val estadoCamara = rememberCameraPositionState {
            position = CameraPosition.fromLatLngZoom(pos, 15f)
        }

        GoogleMap(
            modifier = Modifier.fillMaxSize(),
            cameraPositionState = estadoCamara
        ) {
            ubiUsuario?.let { pos ->
                Marker(
                    state = MarkerState(position = pos),
                    title = "Estás aquí"
                )
            }


            //Los markers de puntos de interes
            puntosDeInteres.forEach { punto ->
                Marker (
                    state = MarkerState (position = punto.coordenadas),
                    title = punto.nombre,
                    onClick = {
                        if (!launchPlaylist(contexto, punto.uriSpotify)) {
                            showDialog.value = true
                        }
                        true
                    }
                )
            }

        }
    }

    // Cancelar actualizaciones de ubicacion cuando la pantalla se cierre
    DisposableEffect(Unit) {
        onDispose {
            locationClient?.removeLocationUpdates(locationCallback!!)
        }
    }

    // Diálogo que aparece cuando Spotify no está instalado
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