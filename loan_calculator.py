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
entradaNoNum = dYlw + "Ingresa un número válido por favor:"
entrada0 = dYlw + "Mayor que zero por favor:"

# # Monedas
monedas = {'euro': '€'}, {'dollar': '$'}, {'pound': '£'}

# # Diverso
deNuevo = ['sí', 'si', 's', 'yes', 'y', '1ra ronda']
seguir = '1ra ronda'

# Dar La Bienvenida
print(f'\n{gold}€€€                        £££'
      f'\n{dGrn}   Calculadora de Préstamos'
      f'\n       Loan Calculator'
      f'\n{gold}₿₿₿                        $$${clrOff}')


# funciones
def valNum(msg: str, ex: str):
    while True:
        try:
            respuesta = float(input(f'\n{msg} {dGrn}'))
            if respuesta <= 0:
                print(entrada0, ex + clrOff)
            else:
                # entrada válida
                print(clrOff, end='')
                return respuesta
        except ValueError:
            print(entradaNoNum, ex + clrOff)


# main
while seguir in deNuevo:
    #  Datos del Usuario

    # # Preguntar – préstamo en euros
    pregunta = '¿De cuántos euros es el préstamo?'
    ejemplos = '1000, 345.42, 22500'
    cantidadPrestada = valNum(pregunta, ejemplos)

    # # Iniciar deuda
    cantidadDebida = cantidadPrestada

    # # Preguntar – interés anual
    pregunta = '¿Qué porcentaje tiene el interés anual?'
    ejemplos = '5, 0.9, 2.6'
    interesAnual = valNum(pregunta, ejemplos)

    # # Calcular interés mensual
    interesMensual = interesAnual / 100 / 12

    # # Preguntar – presupuesto mensual
    pregunta = '¿Cuántos euros podrías pagar cada mes?'
    f'\n({iwht}sin tomar en cuenta el interés{clrOff})'
    ejemplos = '80, 1200, 55.5'
    cuotaMensual = valNum(pregunta, ejemplos)
    

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
        val = globals()[var]
        globals().update(
            {var: f'{ f"{lYlw}{int(val):,}{clrOff}" if str(val).endswith(".0") else f"{lYlw}{round(val,2):,}{clrOff}" }'})
        # ^^ usando el diccionario builtin de Python 'globals', y los f-string para convertir los valores de los variables de tipo 'int' y 'float' a strings más human-friendly. Con los decimales, uso la función round() y luego ':,' en lugar de directamente ':,.2f' pq el round acorta los zeros y el '.2f' los deja. Más limpio así.

    # Imprimir Conclusión
    print(f'\n\n{uGrn}Conclusión{clrOff}')
    print(f'\nTardarías {duracion} en pagar un préstamo de {cantidadPrestada}€'
          f'\nhaciendo un pago mensual de {cuotaMensual}€ con un interes anual de '
          f'{interesAnual}%.\n'
          f'\nLo harías con un total de {totalIntereses}€ en intereses acumulados,'
          f'\nel último pago siendo de {cantidadDebida}€,'
          f'\ny pagando {cantidadPagada:}€ en total.\n')

    # Seguir o Salir
    while True:
        seguir = str(input((f"\n¿Seguir con otro cálculo [sí/no]? " + dGrn))).strip().lower()
        
        # # Insistir en que la entrada no sea vacía
        if seguir != "":
            print(gold + '\n€          $          £          ₿\n' + clrOff)
            break
        else:
            print(clrOff, end='')
