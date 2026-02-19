package com.matias.safewalk

import android.content.Context
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

val Context.dataStore by preferencesDataStore(name = "safewalk_prefs")

class DataStoreManager(private val context: Context) {

    companion object {
        val EMERGENCY_CONTACT = stringPreferencesKey("emergency_contact")
    }

    suspend fun guardarContacto(numero: String) {
        context.dataStore.edit { preferences ->
            preferences[EMERGENCY_CONTACT] = numero
        }
    }

    val contactoEmergencia: Flow<String?> = context.dataStore.data
        .map { preferences ->
            preferences[EMERGENCY_CONTACT]
        }

}