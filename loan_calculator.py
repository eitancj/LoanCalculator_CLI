### Calculadora de Préstamos ###
#       Loan Calculator        #
#         EitanCJ 2023         #
#         Python 3.11.4        #
### ------------------------ ###


## Módulos ##

import sys
import pandas as pd

## Constantes ##

# Colores
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

## Parar y Salir – Version Incompatible de Python
if sys.version_info < (3, 11, 0):
    print(f"Requisito incumplido/Requirement unmet: Python >= {dYlw}3.11.0{clrOff}\n")
    raise SystemExit(999)

# Mensajes
msgs = {'entradaNoNum':
        {'es': dYlw + "Ingresa un número válido por favor:",
         'en': dYlw + "Please enter a valid number:"},
        'entrada0':
        {'es': dYlw + "Mayor que zero por favor:",
         'en': dYlw + "Must be greater than zero:"}}

preguntas = {'capital':
             {'es': '¿De cuánto es el préstamo, en euros?',
              'en': 'How much is the loan, in euros?'},
             'interes':
             {'es': '¿Qué porcentaje tiene el interés anual?',
              'en': 'What is the annual interest rate?'},
             'cuota':
             {'es': '¿La cuota mensual, en euros?'
              f'\n{iwht}(sin tomar en cuenta el interés){clrOff}',
              'en': 'Monthly payments of how much, in euros?'
              f'\n{iwht}(not taking into account the interest fees){clrOff}'},
             'moneda':
             {'es': '¿Tipo de Moneda?',
              'en': 'Which Currency?'},
             'tabla':
             {'es': '\n¿Mostar tabla de pagos mensuales? [sí/no] ',
                 'en': '\nShow monthly-payment table? [yes/no] '},
             'seguir':
             {'es': f"\n¿Seguir con otro cálculo [sí/{uwht}no{clrOff}]? ",
                 'en': f"\nProceed with another loan [yes/{uwht}no{clrOff}]? "}}

ejemplos = {'capital': '1000, 345.42, 22500',
            'interes': '5, 0.9, 2.6',
            'cuota': '80, 1200, 55.5'}

periodos = {'año':
            {'es': '1 año',
             'en': '1 year'},
            'años':
            {'es': 'años',
             'en': 'years'},
            'mes':
            {'es': '1 mes',
             'en': '1 month'},
            'meses':
            {'es': 'meses',
             'en': 'months'},
            'y':
            {'es': ' y ',
             'en': ' and '}}

calculos = {'interes':
            {'es': 'Interés',
             'en': 'Interest'},
            'pago':
            {'es': 'Pago',
             'en': 'Payment'},
            'deuda':
            {'es': 'Deuda',
             'en': 'Debt'},
            'totalInt':
            {'es': 'Total Int',
             'en': 'Total Int'}}

# Opciones
sis = ['sí', 'si', 's', 'yes', 'y']
nos = ['no', 'n']

# Opciones – Monedas
monedas = {'es': ['euro', 'dólar', 'libra', 'bitcóin'],
           'en': ['euro', 'dollar', 'pound', 'bitcoin'],
           'sim': ['€', '$', '£', '₿']}
lrSim = {'€': 'L', '$': 'L', '£': 'L', '₿': 'R'}
acentos = str.maketrans('áéóúíçñ', 'aeouicn')


# Preferencias de Fábrica
prefEng = 'n'
prefMon = 'euro'
plMon = 'euros'
prefTab = 'n'


## Funciones ##

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


def siOno(preg: str, pref: str):
    # Separar opciones [/] en partes
    d1 = '['
    d2 = '/'
    d3 = ']'
    x1 = preg.find(d1)
    x2 = preg.find(d2)
    x3 = preg.find(d3)

    sStr1 = preg[x1 + 1: x2]  # length of all delimiters is 1
    sStr2 = preg[x2 + 1: x3]

    # Formatear opción elegida
    if pref == 'y':
        newp = preg.replace(d1+sStr1, d1+uwht+sStr1+clrOff)
    else:
        newp = preg.replace(sStr2+d3, uwht+sStr2+clrOff+d3)

    return newp


## Bienvenida ##
print(f'\n{gold}€€€                        £££'
      f'\n{dGrn}   Calculadora de Préstamos'
      f'\n       Loan Calculator'
      f'\n{gold}₿₿₿                        $$${clrOff}')

## Idioma ##

# Preguntar – Inglés
ingles = str(
    input(f'\n\nEnglish? [' +
          (f'{uwht}yes{clrOff}/no' if prefEng == 'y' else f'yes/{uwht}no{clrOff}')
          + '] ' + dGrn)).strip().lower()
if not ingles:
    print(prefEng)
print(clrOff)

# Configurar – Preferencias de Idioma
if ingles in sis:
    abc = 'en'
    prefEng = 'y'
else:
    abc = 'es'
    prefEng = 'n'


## MAIN ##

seguir = 'sí'
while seguir in sis:

    ## Preferencias del Usuario ##

    # Preparar – Pregunta de Moneda
    msg = f"{preguntas['moneda'][abc]}\n[ "
    for i, m in enumerate(monedas[abc]):
        up = m[0].upper() + (m[1::])  # uppercase first letter
        msg += f"{ uwht+up+clrOff if m == prefMon else up }" + \
            f"{', ' if i+1 < len(monedas[abc]) else ' ] ' }"

    # Preguntar – Moneda
    rMoneda = input(msg + '' + dGrn).strip().lower()

    # Comprobar – Moneda Válida
    if rMoneda not in monedas[abc]:
        if abc == 'es':
            # Aceptar entradas sin acento
            for m in monedas['es']:
                normalizado = m.translate(acentos)
                if rMoneda == normalizado:
                    prefMon = m
                    break
        print(prefMon)
    else:
        prefMon = rMoneda
    print(clrOff, end='')

    # Configurar - Variables de Moneda [acorde a la selección del usuario]
    moneda = prefMon
    iMoneda = monedas[abc].index(moneda)
    sim = monedas['sim'][iMoneda]  # símbolo de la moneda

    # Configurar - Moneda en Plural
    oldPlural = plMon
    plMon = moneda
    if abc == 'es' and moneda[-1] not in ['a', 'e', 'i', 'u', 'o']:
        # Excepciones Español
        if moneda in ['bitcóin']:
            plMon.replace('ó', 'o')
        plMon += 'es'
    else:
        plMon += 's'

    # Actualizar las preguntas relevants si el tipo de moneda deseado ha cambiado
    if plMon != oldPlural:
        preguntas['capital'] |= {abc:
                                 preguntas['capital'][abc].replace(oldPlural, plMon)}
        preguntas['cuota'] |= {abc:
                               preguntas['cuota'][abc].replace(oldPlural, plMon)}

    ## Datos del Usuario ##

    # Preguntar – Capital del préstamo
    cantidadPrestada = valNum(preguntas['capital'][abc], ejemplos['capital'])

    # Iniciar Deuda
    cantidadDebida = cantidadPrestada

    # Preguntar – Interés Anual
    interesAnual = valNum(preguntas['interes'][abc], ejemplos['interes'])

    # Calcular – Interés Mensual
    interesMensual = interesAnual / 100 / 12

    # Preguntar – Cuota Mensual
    cuotaMensual = valNum(preguntas['cuota'][abc], ejemplos['cuota'])

    ## Cálculos ##

    # Iniciar variables
    meses = int(0)
    totalIntereses = 0
    df = pd.DataFrame(columns=[sim + ' ' + calculos['interes'][abc],
                               sim + ' ' + calculos['pago'][abc],
                               sim + ' ' + calculos['deuda'][abc],
                               sim + ' ' + calculos['totalInt'][abc]])
    df.loc[''] = ''  # fila vacía

    # Cálcular Intereses
    while cantidadDebida > 0:

        # Sumar este mes
        meses += 1

        # Cálculos mensuales
        interesDelMes = cantidadDebida * interesMensual
        cantidadDebida += interesDelMes
        totalIntereses += interesDelMes
        pagoDelMes = cuotaMensual + interesDelMes

        # Pandas DataFrame – Actualizar tabla de cálculos con las cifras del mes
        ds = [f'{round(interesDelMes,3):,}', f'{round(pagoDelMes,3):,}',
              f'{round(cantidadDebida,3):,}', f'{round(totalIntereses,3):,}']
        df.loc['m' + str(meses)] = ds

        # Salir del bucle cuando llegamos al último mes
        # ^^ el último pago será almacenado en cantidadDebida
        if cantidadDebida <= pagoDelMes:
            break

        # Haciendo el pago mensual
        cantidadDebida -= pagoDelMes

    # Calcular el total pagado
    cantidadPagada = cantidadPrestada + totalIntereses  # type: ignore

    ## Formatear Resultados ##

    # Formatear – Duración
    duracion = ""
    duracionAños = int(meses / 12)
    duracionMeses = int(meses % 12)

    if duracionAños > 1:
        duracion = str(duracionAños) + ' ' + periodos['años'][abc]
    elif duracionAños == 1:
        duracion = periodos['año'][abc]

    if duracionMeses > 1:
        if duracion == "":
            duracion = str(duracionMeses) + ' ' + periodos['meses'][abc]
        else:
            duracion += periodos['y'][abc] + \
                str(duracionMeses) + ' ' + periodos['meses'][abc]
    elif duracionMeses == 1:
        if duracion == "":
            duracion = periodos['mes'][abc]
        else:
            duracion += periodos['y'][abc] + periodos['mes'][abc]
    duracion = lYlw + duracion + clrOff

    # Formatear – Números
    numVars = ['cantidadPrestada', 'totalIntereses',
               'cuotaMensual', 'cantidadDebida', 'cantidadPagada']

    interesAnual = lYlw + \
        (f'{int(interesAnual):,}' if str(interesAnual).endswith(".0") else f'{round(interesAnual,2):,}') + \
        clrOff

    for var in numVars:
        val = globals()[var]
        globals().update(
            {var: f"{int(val):,}" if str(val).endswith(".0") else f"{round(val,2):,}"})
        val = globals()[var]
        globals().update(
            {var: lYlw+sim+val+clrOff if lrSim[sim] == 'L' else lYlw+val+sim+clrOff})
        # ^^ usando el diccionario builtin de Python 'globals', y los f-string para convertir los valores de los variables de tipo 'int' y 'float' a strings más human-friendly. Con los decimales, uso la función round() y luego ':,' en lugar de directamente ':,.2f' pq el round acorta los zeros y el '.2f' los deja. Más limpio así.

    ## Imprimir Conclusión ##

    conclusiones = {
        'es': f'\n\n{uGrn}Conclusión{clrOff}\n'
        f'\nSe tardaría {duracion} en pagar un préstamo de {cantidadPrestada}'
        f'\nhaciendo pagos mensuales de {cuotaMensual} con un interés anual de '
        f'{interesAnual}%.\n'
        f'\nSe haría con un total de {totalIntereses} en intereses acumulados,'
        f'\nel último pago siendo de {cantidadDebida},'
        f'\ny pagando {cantidadPagada} en total.\n',

        'en': f'\n\n{uGrn}Conclusion{clrOff}\n'
        f'\nIt would take {duracion} to pay off a loan of {cantidadPrestada},'
        f'\ngiven a monthly payment of {cuotaMensual} and an annual interest rate of '
        f'{interesAnual}%.\n'
        f'\nThis would be accomplished by paying {totalIntereses} of accumulated interest fees,'
        f'\nthe last payment amounting to {cantidadDebida},'
        f'\nand paying a total of {cantidadPagada} all together.\n'
    }
    print(conclusiones[abc])

    ## Tabla de Cálculos ##

    # Preparar – Pregunta de Tabla
    pTabla = siOno(preguntas['tabla'][abc], prefTab)

    # Preguntar – Mostrar Tabla
    rTabla = input(pTabla + dGrn).strip().lower()

    if rTabla not in nos and rTabla not in sis:  # Derivar - prefTab previamente establecida
        print(prefTab)
    elif rTabla in nos:  # No Mostrar Tabla
        prefTab = 'n'
    else:  # Mostrar Tabla
        prefTab = 'y'
    print(clrOff, end='')

    # Mostrar Tabla
    if prefTab in sis:
        print('')
        print(df)

    ## Salir o Seguir ##

    # Preguntar – Seguir o Salir
    seguir = input((preguntas['seguir'][abc] + dGrn) or 'n').strip().lower()

    if seguir not in sis and seguir not in nos: # Por defecto no seguir
        print('n')

    # Imprimir Footer
    print(f"{gold}\n€          $          £          ₿{clrOff}\n")
