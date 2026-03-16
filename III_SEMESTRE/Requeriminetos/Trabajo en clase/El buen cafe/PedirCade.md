# Caso de Uso: CU-01 – Pedir café

**Actor Principal:** Cajero  
**Actores Secundarios:** Redes Sociales (API), Sistema de Inventario

---

## 1. Resumen

El cajero registra los productos seleccionados por un cliente, ya sea de forma presencial o mediante una notificación de redes sociales, para preparar el pedido y calcular el monto adeudado.

---

## 2. Precondiciones

- El Cajero debe estar autenticado en el sistema.
- El sistema debe tener conexión activa con las APIs de Redes Sociales para recibir pedidos externos.

---

## 3. Flujo Básico (Happy Path)

1. El **Cajero** inicia una nueva orden de pedido.
2. El sistema muestra la lista de productos y estilos de café disponibles (nombres y precios).
3. El **Cajero** selecciona los productos solicitados por el cliente.
4. El sistema calcula automáticamente el subtotal basado en los precios unitarios.
5. El **Cajero** confirma la lista de productos.
6. El sistema guarda el pedido con estado "Pendiente de cobro".

---

## 4. Flujos Alternos / Excepciones

### 4.1 Pedido por Redes Sociales

Si en el **paso 1** la orden proviene de una red social, el sistema precarga los datos del cliente y los productos mencionados en la notificación para que el **Cajero** solo deba validarlos.

### 4.2 Producto no disponible

Si en el **paso 3** un producto seleccionado no tiene existencias, el sistema bloquea la selección y emite una alerta para que el **Cajero** informe al cliente.

---

## 5. Postcondiciones

- **Éxito:** El pedido queda registrado en el historial diario y listo para la fase de cobro.
- **Fallo:** No se crea el pedido y se informa al usuario sobre el error técnico o falta de datos.
