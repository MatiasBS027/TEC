    package com.matias.geo_beats

import com.google.android.gms.maps.model.LatLng
import kotlin.math.*

/*
* Haversine.kt
* Contiene la formula de Haversine para calcular la distancia
* en metros entre dos coordenadas geograficas.
*/

// Radio de la Tierra en metros
//100% hecho por Claude xd, esto si que no sé ni que hace, lo entenderé cuando ya tenga el resto hecho.
private const val RADIO_TIERRA = 6371000.0

fun calcularDistancia(punto1: LatLng, punto2: LatLng): Double {
    val lat1 = Math.toRadians(punto1.latitude)
    val lat2 = Math.toRadians(punto2.latitude)
    val diffLat = Math.toRadians(punto2.latitude - punto1.latitude)
    val diffLng = Math.toRadians(punto2.longitude - punto1.longitude)

    val a = sin(diffLat / 2).pow(2) +
            cos(lat1) * cos(lat2) *
            sin(diffLng / 2).pow(2)

    val c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return RADIO_TIERRA * c
}