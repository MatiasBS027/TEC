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
        val EMERGENCY_CONTACT_NAME = stringPreferencesKey("emergency_contact_name")
    }

    suspend fun guardarContacto(numero: String, nombre: String) {
        context.dataStore.edit { preferences ->
            preferences[EMERGENCY_CONTACT] = numero
            preferences[EMERGENCY_CONTACT_NAME] = nombre
        }
    }

    val contactoEmergencia: Flow<String?> = context.dataStore.data
        .map { preferences ->
            preferences[EMERGENCY_CONTACT]
        }

    val nombreEmergencia: Flow<String?> = context.dataStore.data
        .map { preferences ->
            preferences[EMERGENCY_CONTACT_NAME]
        }

}