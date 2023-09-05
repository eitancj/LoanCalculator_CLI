### Calculadora de Préstamos ###
#       Loan Calculator        #
#         EitanCJ 2023         #
#         Python 3.11.4        #
### ------------------------ ###

# modules
import pandas as pd


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
         'en': dYlw + "Must be greater than zero:"},
        'tabla':
        {'es': f"\n¿Mostar tabla de cálculos mensuales? [sí/{uwht}no{clrOff}]? ",
         'en': f"\nShow monthly calculation table? [y/{uwht}n{clrOff}]? "},
        'seguir':
        {'es': f"\n¿Seguir con otro cálculo [sí/{uwht}no{clrOff}]? ",
         'en': f"\nProceed with another loan [y/{uwht}n{clrOff}]? "}}

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

periodos = {'año':
            {'es': 'año',
             'en': 'year'},
            'años':
            {'es': 'años',
             'en': 'years'},
            'mes':
            {'es': 'mes',
             'en': 'month'},
            'meses':
            {'es': 'meses',
             'en': 'months'},
            'y':
            {'es': ' y ',
             'en': ' and '}}

calculos = {'interes':
            {'es': dYlw + 'Interés' + clrOff,
             'en': dYlw + 'Interest' + clrOff},
            'pago':
            {'es': dYlw + 'Pago' + clrOff,
             'en': dYlw + 'Payment' + clrOff},
            'deuda':
            {'es': dYlw + 'Deuda' + clrOff,
             'en': dYlw + 'Debt' + clrOff},
            'totalInt':
            {'es': dYlw + 'Total Int.' + clrOff,
             'en': dYlw + 'Total Int.' + clrOff}}

# # Preferencias
monedas = {'euro': '€'}, {'dólar': '$'}, {'libra': '£'}, {'bitcoin': '₿'}

# # Diverso
sis = ['sí', 'si', 's', 'yes', 'y']


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
ingles = str(
    input(f'\n\nEnglish? [y/{uwht}n{clrOff}] ' + dGrn) or 'n').strip().lower()
print(clrOff, end='')
abc = f"{'en' if ingles in sis else 'es'}"

# main
seguir = 'sí'

while seguir in sis:
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
    completeDF = pd.DataFrame()

    while cantidadDebida > 0:
        # Sumar este mes
        meses += 1

        # Cálculos mensuales
        interesDelMes = cantidadDebida * interesMensual
        cantidadDebida += interesDelMes
        totalIntereses += interesDelMes
        pagoDelMes = cuotaMensual + interesDelMes

        monthlyDS = {
            calculos['interes'][abc]: [f'{round(interesDelMes,2):,}'],
            calculos['pago'][abc]: [f'{round(pagoDelMes,2):,}'],
            calculos['deuda'][abc]: [f'{round(cantidadDebida,2):,}'],
            calculos['totalInt'][abc]: [f'{round(totalIntereses,2):,}']
        }
        monthlyDF = pd.DataFrame(monthlyDS, index=[f"{periodos['mes'][abc].upper()} {str(meses)}"])
        completeDF = pd.concat([completeDF, monthlyDF], )

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
        duracion = str(duracionAños) + ' ' + periodos['años'][abc]
    elif duracionAños == 1:
        duracion = '1 ' + periodos['año'][abc]

    if duracionMeses > 1:
        if duracion == "":
            duracion = str(duracionMeses) + ' ' + periodos['meses'][abc]
        else:
            duracion += periodos['y'][abc] + \
                str(duracionMeses) + ' ' + periodos['meses'][abc]
    elif duracionMeses == 1:
        if duracion == "":
            duracion = '1 ' + periodos['mes'][abc]
        else:
            duracion += periodos['y'][abc] + periodos['mes'][abc]
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
    conclusiones = {
        'es': f'\n\n{uGrn}Conclusión{clrOff}\n'
        f'\nTardarías {duracion} en pagar un préstamo de {cantidadPrestada}€'
        f'\nhaciendo un pago mensual de {cuotaMensual}€ con un interés anual de '
        f'{interesAnual}%.\n'
        f'\nLo harías con un total de {totalIntereses}€ en intereses acumulados,'
        f'\nel último pago siendo de {cantidadDebida}€,'
        f'\ny pagando {cantidadPagada:}€ en total.\n',
        'en': f'\n\n{uGrn}Conclusion{clrOff}\n'
        f'\nIt would take you {duracion} to pay off a loan of {cantidadPrestada}€'
        f'\ngiven a monthly payment of {cuotaMensual}€ and an annual interest rate of '
        f'{interesAnual}%.\n'
        f'\nThis would be accomplished by paying {totalIntereses}€ of accumulated interest fees,'
        f'\nthe last payment amounting to {cantidadDebida}€,'
        f'\nand paying a total of {cantidadPagada:}€ all together.\n'
    }
    print(conclusiones[abc])

    # Preguntar – Mostrar tabla
    quiereTabla = str(input(msgs['tabla'][abc] + dGrn) or 'no').strip().lower()
    print(clrOff, end='')
    if quiereTabla in sis:
        print(completeDF)

    # Preguntar – Seguir o Salir
    seguir = str(input(msgs['seguir'][abc] + dGrn) or 'no').strip().lower()
    print(gold + '\n€          $          £          ₿\n' + clrOff)
