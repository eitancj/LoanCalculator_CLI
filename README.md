# Loan Calculator - Calculadora de Préstamos

Una herramienta interactiva para calcular préstamos.

#### Entradas
- Cantidad prestada
- Interes anual
- Presupuesto mensual

#### Resultados
- El tiempo que tardarías en pagarlo todo
- Total intereses acumulados
- Total pagado

#### Tech Stack
- Python 3.11.4
- - pandas 2.1.0

#### Ejecutar Programa
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
```sh
python3 loan_calculator.py
```

## Asuntos Pendientes
1. Arreglar: Las columnas de la tabla de cálculos mensuales no están bien alineadas
2. Añadir: Opción para cambiar el tipo de moneda
3. Añadir: README en Inglés

## Notas
1. El tipo de préstamo que pretende calcular es el TIN en España.
2. Solo intereses fijos, no variables.
3. No se pide la duración del préstamo,\
    sino que se hace una estimación de ella según los demás datos ingresados.
4. Se da por sentado que los pagos son mensuales.
5. No se toman en cuenta las comisiones,\
    el crédito personal ni otras tarifas y productos adicionales.
6. Esta herramienta es un ejercicio personal para practicar el uso de Python3.\
    Ignoro si los cálculos son precisos, ya que no soy ningún profesional financiero.