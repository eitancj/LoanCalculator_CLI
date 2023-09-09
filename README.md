# Calculadora de Préstamos

![](https://github.com/eitancj/preview_images/blob/main/loancalc_cli_2.png?raw=true)

\
Una herramienta interactiva para calcular préstamos personales.

### Entradas
- Cantidad prestada
- Interés anual
- Cuota mensual

### Resultados
- El tiempo que tardarías en pagarlo todo
- Total intereses acumulados
- Total pagado
- Tabla de gastos mensuales [opcional] 

### Funcionalidades
- Principal:  
Calcular duración, intereses pagados y total pagado de un préstamo personal,   
dados unos datos del usuario. 

- Idiomas: Español, Inglés
- Tipos de Moneda: Euro, Dólar, Libra, Bitcóin
- Mostrar Tabla de Pagos Mensuales
- Salida Formateada y Colorida
- Comenzar Otro Cálculo seguidamente e indefinidamente
- Recordar Preferencias del Usuario a la hora de comenzar otro cálculo

### Tech Stack
- Python 3.11.4
- - pandas 2.1.0
- macOS X

### Requisitos
- Python >= 3.11.0

### Ejecutar Programa
> [opcional] Crear un *venv* nuevo por si prefieres instalar los módulos en un entorno aislado.
```sh
python3 -m venv loan_calc
source 'loan_calc/bin/activate'
```
> Instalar Requisitos
```sh
python3 -m pip install -r requirements.txt
``` 
>  Ejecutar Calculadora de Préstamos
>> *puede que el módulo de pandas tarde un poco en cargarse la primera vez*
```sh
python3 loan_calculator.py
```

### Limpiar
> Devolver el PATH de los ejecutables a los valores originales (*si creaste el venv*)
```sh
deactivate
```

> Borrar —con prudencia— la carpeta del repositorio clonado  

> Si quieres deshacerte de los paquetes instalados de forma comprensiva, yo recomiendo usar el paquete *pip-autoremove*

### Asuntos Pendientes
1. Añadir: Opción para elegir otro período de pago
2. Añadir: README en Inglés

### Notas
1. El tipo de préstamo que la herramienta **pretende** calcular es el TIN en España de interés fijo.
2. No se pide la duración del préstamo,\
    sino que se hace una estimación de ella según los demás datos ingresados.
3. No se calculan las comisiones, el crédito personal,\
ni otras tarifas y productos adicionales.
4. Esta herramienta es un ejercicio personal para practicar el uso de Python3 y Pandas.\
    Ignoro si los cálculos son precisos, ya que no soy ningún profesional financiero.