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
        coordenadas = LatLng(9.855538623075114, -83.91243989944289),
        uriSpotify ="spotify:playlist:3NZmK2cRzjWoxFz9vskf14"

    ),
    PuntoDeInteres(
        nombre = "Basílica de los Angeles",
        coordenadas = LatLng(9.86392737928863, -83.91299357259486),
        uriSpotify = "spotify:playlist:37i9dQZF1DXcBWIGoYBM5M",

        ),
    PuntoDeInteres(
        nombre = "Capilla San Agustín",
        coordenadas = LatLng(9.859519790305464, -83.91318982277447),
        uriSpotify ="spotify:playlist:37i9dQZF1DWUa8ZRTfalHk"
    ),

    PuntoDeInteres(
        nombre = "Subway",
        coordenadas = LatLng(9.858586240487393, -83.9172888625244),
        uriSpotify ="spotify:playlist:1Y4ZYrgsYaThTO6sUQIL7L"
    )
)