package com.matias.geo_beats

import com.google.android.gms.maps.model.LatLng

//Nota, esto puede ser que después deba cambiarse porque ahorita estaria tirando la playlist aleatoriamente
//Spotifylauncher las tira aleatoriamente.

// Clase que representa un punto de interes en el mapa
data class PuntoDeInteres(val nombre: String, val coordenadas: LatLng, val uriSpotify: String)

// Lista de puntos de interes cercanos al TEC
val puntosDeInteres = listOf(
    PuntoDeInteres(
        nombre = "TEC Cartago",
        coordenadas = LatLng(9.8558, -83.9114),
        uriSpotify ="spotify:playlist:37i9dQZF1DX4WYpdgoIcn6"

    ),
    PuntoDeInteres(
        nombre = "Basílica de los Angeles",
        coordenadas = LatLng(9.8645, -83.9193),
        uriSpotify = "spotify:playlist:37i9dQZF1DXcBWIGoYBM5M",

    ),
    PuntoDeInteres(
        nombre = "Capilla San Agustín",
        coordenadas = LatLng(9.8567, -83.9101),
        uriSpotify ="spotify:playlist:37i9dQZF1DWUa8ZRTfalHk"
    )
)