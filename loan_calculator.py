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
fgB = clrOn + "1;" + "38;5;"
bg = clrOn + "48;5;"
lGrn = fg + "010m"
dGrn = fg + "002m"
uGrn = fg_ + "002m"
lYlw = fg + "227m"
dYlw = fg + "003m"
slvr = fg + "007m"
gold = fg + "221m"
iwht = fgi + "015m"
uwht = fg_ + "015m"

# # Mensajes
msgs = {'entradaNoNum':
        {'es': dYlw + "Ingresa un número válido por favor:",
         'en': dYlw + "Please enter a valid number:"},
        'entrada0':
        {'es': dYlw + "Mayor que zero por favor:",
         'en': dYlw + "Must be greater than zero:"}}

preguntas = {'capital':
             {'es': '¿De cuántos euros es el préstamo?',
              'en': 'How much is the loan, in euros?'},
             'interes':
             {'es': '¿Qué porcentaje tiene el interés anual?',
              'en': 'What is the anual interest percentage?'},
             'cuota':
             {'es': 'Tu cuota mensual?'
              f'\n{iwht}(sin tomar en cuenta el interés){clrOff}',
              'en': 'A monthly payment of...?'
              f'\n{iwht}(not taking into account the interest fees){clrOff}'}}

ejemplos = {'capital': '1000, 345.42, 22500',
            'interes': '5, 0.9, 2.6',
            'cuota': '80, 1200, 55.5'}


# # Preferencias
monedas = {'euro': '€'}, {'dólar': '$'}, {'libra': '£'}, {'bitcoin': '₿'}

# # Diverso
deNuevo = ['sí', 'si', 's', 'yes', 'y']
QuiereIngles = deNuevo


# Funciones
def valNum(msg: str, ex: str):
    while True:
        try:
            respuesta = float(input(f'\n{msg} {dGrn}'))
            if respuesta <= 0:
                print(msgs['entrada0'][abc], ex + clrOff)
            else:
                # entrada válida
                print(clrOff, end='')
                return respuesta
        except ValueError:
            print(msgs['entradaNoNum'][abc], ex + clrOff)


# Mensaje de bienvenida
print(f'\n{gold}€€€                        £££'
      f'\n{dGrn}   Calculadora de Préstamos'
      f'\n       Loan Calculator'
      f'\n{gold}₿₿₿                        $$${clrOff}')

# Preferencias del Usuario
# # Preguntar –  idioma
ingles = (input(f'\n\nEnglish? [y/{uwht}n{clrOff}] ' + lGrn) or 'n').strip().lower()
print(clrOff, end='')
abc = f"{'en' if ingles in QuiereIngles else 'es'}"

# main
seguir = 'sí'
while seguir in deNuevo:
    #  Datos del Usuario
    # # Preguntar – préstamo en euros
    cantidadPrestada = valNum(preguntas['capital'][abc], ejemplos['capital'])

    # # Iniciar deuda
    cantidadDebida = cantidadPrestada

    # # Preguntar – interés anual
    interesAnual = valNum(preguntas['interes'][abc], ejemplos['interes'])

    # # Calcular interés mensual
    interesMensual = interesAnual / 100 / 12

    # # Preguntar – presupuesto mensual
    cuotaMensual = valNum(preguntas['cuota'][abc], ejemplos['cuota'])

    # ¡ Cálculos :s !
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
          f'\nhaciendo un pago mensual de {cuotaMensual}€ con un interés anual de '
          f'{interesAnual}%.\n'
          f'\nLo harías con un total de {totalIntereses}€ en intereses acumulados,'
          f'\nel último pago siendo de {cantidadDebida}€,'
          f'\ny pagando {cantidadPagada:}€ en total.\n')

    # Seguir o Salir
    while True:
        seguir = str(
            input((f"\n¿Seguir con otro cálculo [sí/no]? " + dGrn))).strip().lower()

        # # Insistir en que la entrada no sea vacía
        if seguir != "":
            print(gold + '\n€          $          £          ₿\n' + clrOff)
            break
        else:
            print(clrOff, end='')
