### Calculadora de Préstamos ###
#       Loan Calculator        #
#         EitanCJ 2023         #
#         Python 3.11.4        #
### ------------------------ ###


# Constantes
# # Colores
clrOn = "\033["
clrOff = "\033[0;0m"
fg = clrOn + "38;5;"
fg_ = clrOn + "4;" + "38;5;"
fgi = clrOn + "3;" + "38;5;"
bg = clrOn + "48;5;"
lGrn = fg + "010m"
dGrn = fg + "002m"
uGrn = fg_ + "002m"
lYlw = fg + "227m"
dYlw = fg + "003m"
slvr = fg + "007m"
gold = fg + "221m"
iwht = fgi + "015m"

# # Mensajes
malaEntrada = dYlw + "Ingresa un número válido por favor:"

# # Monedas
monedas = {'euro': '€'}, {'dollar': '$'}, {'pound': '£'}


# Dar La Bienvenida
print(f'\n{gold}€€€                        £££'
      f'\n{dGrn}   Calculadora de Préstamos'
      f'\n       Loan Calculator'
      f'\n{gold}₿₿₿                        $$${clrOff}')


# Datos del Usuario
# # Preguntar – préstamo en euros
while True:
    try:
        cantidadPrestada = float(
            input('\n¿De cuántos euros es el préstamo? ' + dGrn))
        # entrada válida
        print(clrOff, end='')
        break
    except ValueError:
        print(malaEntrada, '1000, 345.42, 22500' + clrOff)

# # Iniciar deuda
cantidadDebida = cantidadPrestada

# # Preguntar – interés anual
while True:
    try:
        interesAnual = float(
            input('\n¿Qué porcentaje tiene el interés anual? ' + dGrn))
        print(clrOff, end='')
        break  # entrada válida
    except ValueError:
        print(malaEntrada, '3, 1.8, 2.2' + clrOff)

# # Calcular interés mensual
interesMensual = interesAnual / 100 / 12

# # Preguntar – presupuesto mensual
while True:
    try:
        cuotaMensual = float(input('\n¿Cuántos euros podrías pagar cada mes?'
                                   f'\n({iwht}sin tomar en cuenta el interés{clrOff}) ' + dGrn))
        # entrada válida
        print(clrOff, end='')
        break
    except ValueError:
        print('\n' + malaEntrada, '250, 80.5, 800' + clrOff)


# ¡Cálculos!
# # Iniciar variables
meses = int(0)
totalIntereses = 0

# # Cálcular intereses
while cantidadDebida > 0:
    # Sumar este mes
    meses += 1
    # print("meses:", meses)
    
    # Cálculos mensuales
    interesDelMes = cantidadDebida * interesMensual
    cantidadDebida += interesDelMes
    totalIntereses += interesDelMes
    pagoDelMes = cuotaMensual + interesDelMes

    # print("\ninteresDelMes:", interesDelMes)
    # print("cantidadDebida:", cantidadDebida)
    # print("totalIntereses:", totalIntereses)

    # Salir del bucle cuando llegamos al último mes
    # ^^ el último pago será almacenado en cantidadDebida
    if cantidadDebida <= pagoDelMes:
        break

    # Haciendo el pago mensual
    cantidadDebida -= pagoDelMes

# # Calcular el total pagado
cantidadPagada = cantidadPrestada + totalIntereses  # type: ignore


# Formatear Resultados
# # Formateando la duración
duracion = ""
duracionAños = int(meses / 12)
duracionMeses = int(meses % 12)

if duracionAños > 1:
    duracion = str(duracionAños) + " años"
elif duracionAños == 1:
    duracion = "1 año"

if duracionMeses > 1:
    if duracion == "":
        duracion = str(duracionMeses) + " meses"
    else:
        duracion += f' y {str(duracionMeses)} meses'
elif duracionMeses == 1:
    if duracion == "":
        duracion = "1 mes"
    else:
        duracion += " y 1 mes"
duracion = lYlw + duracion + clrOff

# # Formateando los números
numVars = ['cantidadPrestada', 'interesAnual', 'totalIntereses',
           'cuotaMensual', 'cantidadDebida', 'cantidadPagada']

for var in numVars:
    # ^^ usando el diccionario builtin de Python 'globlas', y los f-string, para actualizar y convertir los valores de los variables del tipo 'int' y 'float', a strings más human-friendly
    val = globals()[var]
    globals().update(
        {var: f'{ f"{lYlw}{int(val):,}{clrOff}" if str(val).endswith(".0") else f"{lYlw}{val:,.2f}{clrOff}" }'})


# Imprimir Conclusión
print(f'\n\n{uGrn}Conclusión{clrOff}')
print(f'\nTardarías {duracion} en pagar un préstamo de {cantidadPrestada}€,'
      f'\nhaciendo un pago mensual de {cuotaMensual}€ con un interes anual de '
      f'{interesAnual}%.\n'
      f'\nLo harías con un total de {totalIntereses}€ en intereses acumulados,'
      f'\nel último pago siendo de unos {cantidadDebida}€,'
      f'\ny pagando {cantidadPagada:}€ en total.\n')
