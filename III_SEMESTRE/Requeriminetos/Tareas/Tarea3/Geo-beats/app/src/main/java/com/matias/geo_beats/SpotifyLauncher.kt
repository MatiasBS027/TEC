package com.matias.geo_beats


import android.content.Context
import android.content.Intent
import android.net.Uri
import android.content.ActivityNotFoundException
import android.util.Log

fun launchPlaylist(context: Context, spotifyUri: String): Boolean {
    return try {
        val intent = Intent(Intent.ACTION_VIEW, Uri.parse(spotifyUri))
        context.startActivity(intent)
        true
    } catch (e: ActivityNotFoundException) {
        Log.e("SpotifyLauncher", "Spotify no está instalado", e)
        false
    }
}

fun launchRandomPlaylist(context: Context): Boolean {
    return try {
        val playlists = listOf(
            "spotify:playlist:37i9dQZF1DXcBWIGoYBM5M",
            "spotify:playlist:37i9dQZF1DX0XUsuxWHRQd",
            "spotify:playlist:37i9dQZF1DX4WYpdgoIcn6",
            "spotify:playlist:37i9dQZF1DWUa8ZRTfalHk"
        )
        val randomUri = playlists.random()
        return launchPlaylist(context, randomUri)
    } catch (e: ActivityNotFoundException) {
        Log.e("SpotifyLauncher", "Spotify no está instalado", e)
        false
    }
}

