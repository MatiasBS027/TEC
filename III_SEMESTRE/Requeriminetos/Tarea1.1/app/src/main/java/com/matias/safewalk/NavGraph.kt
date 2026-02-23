package com.matias.safewalk

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController

@Composable
fun NavGraph(viewModel: SensorViewModel, dataStoreManager: DataStoreManager) {

    val navController = rememberNavController()

    NavHost(
        navController = navController,
        startDestination = "alarm"
    ) {
        composable("alarm") {
            AlarmScreen(viewModel = viewModel, navController = navController, dataStorage = dataStoreManager,)
        }
        composable("settings") {
            SettingsScreen(dataStoreManager = dataStoreManager, navController = navController)
        }
    }
}