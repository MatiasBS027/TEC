package com.matias.geo_beats

/* Joha
 *En este kt se maneja lo relacionado con el mapa.
 *Pido permiso de ubicacion al user, obtinie su posiciona actual
 * y se muestran marcadores en los puntos de interes cercanos.
 */
import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.location.Location
import android.os.Looper
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

// Funcion que solicita la ubicacion actual del dispositivo
@RequiresPermission(Manifest.permission.ACCESS_FINE_LOCATION)
fun obtenerUbicacionActual(contexto: Context,
    alObtenerUbicacion: (LatLng) -> Unit
) {
    val cliente = LocationServices.getFusedLocationProviderClient(contexto)

    val solicitud = LocationRequest.Builder(Priority.PRIORITY_HIGH_ACCURACY, 1000)
        .setMaxUpdates(1)
        .build()

    val callback = object : LocationCallback() {
        override fun onLocationResult(resultado: LocationResult) {
            resultado.lastLocation?.let { location ->
                alObtenerUbicacion(LatLng(location.latitude, location.longitude))
            }
            cliente.removeLocationUpdates(this)
        }
    }
    cliente.requestLocationUpdates(solicitud, callback, Looper.getMainLooper())
}
@Composable
fun MapaScreen() {
    //Contexto pa acceder al GPS y el resto de servicios
    val contexto = LocalContext.current

    //variable que empieza en null (sin ubicacion) y que puede guardar coordenadas (latitud y longitud(LatLng))
    //el rembember es para que no se restee cada que la pantalla se redibuja
    var ubiUsuario by remember { mutableStateOf<LatLng?>(null) }

    // Launcher que maneja la respuesta del usuario al pedir permiso
    val launcher = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission())

    { concedido ->
        if (concedido) {
            obtenerUbicacionActual(contexto) { ubicacion ->
                ubiUsuario = ubicacion
            }
        }
    }

    // Al iniciar la pantalla, verificamos si ya tenemos permiso o lo pedimos, se ejecuta una vez cuando la pantalla aparece
    LaunchedEffect(Unit) {
        val permiso = ContextCompat.checkSelfPermission(
            contexto, Manifest.permission.ACCESS_FINE_LOCATION
        )
        //Si ya tiene permiso, obtenemos la ubicacion directo
        if (permiso == PackageManager.PERMISSION_GRANTED) {
            obtenerUbicacionActual(contexto) { ubicacion ->
                ubiUsuario = ubicacion
            }
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
                onClick = {launchRandomPlaylist(contexto)
                    true
                }
            )
        }

        }
    }
}
