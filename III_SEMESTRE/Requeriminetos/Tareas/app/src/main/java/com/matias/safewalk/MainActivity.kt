package com.matias.safewalk

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.viewModels
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.lifecycle.viewmodel.compose.viewModel
import com.matias.safewalk.ui.theme.SafeWalkTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        val viewModel: SensorViewModel by viewModels()
        val dataStoreManager = DataStoreManager(this)
        setContent {
            SafeWalkTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { _ ->
                    NavGraph(viewModel = viewModel,
                        dataStoreManager = dataStoreManager
                    )
                }
            }
        }
    }
}