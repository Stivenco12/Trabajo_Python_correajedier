# Proyecto de Gestión de Ventas y Compras

## Descripción

Este proyecto es un sistema de gestión de compras y ventas, estructurado en módulos que permiten registrar y consultar información de clientes, empleados, productos, proveedores y fechas de transacciones.

## Estructura del Proyecto

```
Trabajo_Python_correajedier-main/
│── prin.py                      # Punto de entrada del sistema
│── compras.py                   # Módulo de gestión de compras
│── ventas.py                    # Módulo de gestión de ventas
│── guardar_informacion.json      # Archivo para almacenar datos
│
├── funcionalidades/              # Funciones relacionadas con ventas
│   ├── info_cliente.py           # Información de clientes
│   ├── infor_empleado.py         # Información de empleados
│   ├── producto_vendidos.py      # Productos vendidos
│   ├── ventas_fecha.py           # Ventas por fecha
│
├── funcionalidades2/             # Funciones relacionadas con compras
│   ├── fecha_compra.py           # Registro de fechas de compras
│   ├── infor_proevedor.py        # Información de proveedores
│   ├── productos_comprados.py    # Productos adquiridos
```

## Instalación y Uso

1. Clonar o descargar el repositorio.
2. Asegurarse de tener Python instalado.
3. Ejecutar el archivo principal:
   ```sh
   python prin.py
   ```
4. Seguir las instrucciones en pantalla para navegar por el menú del sistema.

## Funcionalidades

- **Ventas:** Registrar información de clientes, empleados y productos vendidos.
- **Compras:** Registrar información de proveedores y productos adquiridos.
- **Interfaz con Menú:** Permite seleccionar entre gestión de ventas y compras.

##

