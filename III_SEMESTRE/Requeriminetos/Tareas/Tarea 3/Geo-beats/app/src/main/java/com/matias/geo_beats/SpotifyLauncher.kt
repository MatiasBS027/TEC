package com.matias.geo_beats


import android.content.Context
import android.content.Intent
import android.net.Uri
import android.content.pm.PackageManager

fun launchRandomPlaylist(context: Context): Boolean {
    val packageManager = context.packageManager
    val launchIntent = packageManager.getLaunchIntentForPackage("com.spotify.music")
    if (launchIntent != null) {
        val playlists = listOf(
            "spotify:playlist:37i9dQZF1DXcBWIGoYBM5M",
            "spotify:playlist:37i9dQZF1DX0XUsuxWHRQd",
            "spotify:playlist:37i9dQZF1DX4WYpdgoIcn6",
            "spotify:playlist:37i9dQZF1DWUa8ZRTfalHk"
        )
        val randomUri = playlists.random()
        val intent = Intent(Intent.ACTION_VIEW, Uri.parse(randomUri))
        context.startActivity(intent)
        return true
    } else {
        return false
    }
}
