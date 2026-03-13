# Caso de Uso: CU-01 – Retirar efectivo del cajero automático

**Actor Principal:** Cliente  
**Actores Secundarios:** Red Blockchain, Exchange API, Sensor de Efectivo

---

## 1. Resumen
El cliente intercambia el saldo de su wallet de criptomonedas por dinero en efectivo físico de forma segura.

---

## 2. Precondiciones

- El usuario debe tener una wallet vinculada y saldo suficiente.
- El cajero debe tener conexión a internet y efectivo disponible.

---

## 3. Flujo Básico (Happy Path)

1. El **Cliente** solicita un monto específico de retiro.
2. El sistema valida la identidad del usuario mediante el servicio biométrico.
3. El sistema consulta la tasa de cambio actual mediante la **Exchange API**.
4. El sistema verifica que el saldo en la **Blockchain** cubra el monto más comisiones.
5. El sistema solicita confirmación final del **Cliente**.
6. El sistema procesa la transacción en la **Blockchain**.
7. El sistema verifica el estado del dispensador y entrega el efectivo.
8. El sistema registra la transacción y actualiza el log de auditoría.

---

## 4. Flujos Alternos / Excepciones

### 4.1 Falla de Hardware (El Limbo)
Si en el **paso 7** el dispensador se atasca, el sistema dispara un mensaje a la **API de compensación** para revertir el cobro en la Blockchain.

### 4.2 Crisis de Identidad
Si en el **paso 2** el servicio de **FaceID** falla, el sistema habilita el ingreso mediante **PIN o código de emergencia** (Modo de Degradación Segura).

### 4.3 Volatilidad Extrema
Si entre el **paso 3 y el paso 5** el precio de la criptomoneda cae más del **10%**, el sistema revalida los fondos y solicita una nueva confirmación de la tasa de cambio.

### 4.4 Error de Conexión
Si se pierde la conexión con la **Blockchain** en el **paso 6**, el sistema cancela la operación y devuelve la tarjeta.

---

## 5. Postcondiciones

- **Éxito:** El saldo se actualiza en la Blockchain, se entrega el dinero y se genera el log de auditoría.
- **Fallo:** No se realiza el cobro, se notifica al usuario el motivo y se registra el error para mantenimiento.