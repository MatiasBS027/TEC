package com.matias.geo_beats

import com.google.android.gms.maps.model.LatLng

//Nota, esto puede ser que despues deba cambiarse porque ahorita estaria tirando las playlist aleatoriamente
//Spotifylauncher las tira aleatoriamente.

// Clase que representa un punto de interes en el mapa
data class PuntoDeInteres(val nombre: String, val coordenadas: LatLng, )

// Lista de puntos de interes cercanos al TEC
val puntosDeInteres = listOf(
    PuntoDeInteres(
        nombre = "TEC Cartago",
        coordenadas = LatLng(9.8558, -83.9114)

    ),
    PuntoDeInteres(
        nombre = "Basílica de los Angeles",
        coordenadas = LatLng(9.8645, -83.9193)
    ),
    PuntoDeInteres(
        nombre = "Capilla San Agustín",
        coordenadas = LatLng(9.8567, -83.9101)
    )
)