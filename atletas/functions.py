# Cálculo de la categoría en función de la edad

from re import findall


def calcularCategoria(edad):
    """
    Recibe una edad y responde con su categoría
    """
    if (edad >= 35):
        return "VETERANO"

    elif (edad < 35 and edad >= 23):
        return "SENIOR"

    elif (edad < 23 and edad >= 20):
        return "SUB23"

    elif (edad < 20 and edad >= 18):
        return "SUB20"

    elif (edad < 18 and edad >= 16):
        return "SUB18"

    elif (edad < 16 and edad >= 14):
        return "SUB16"
        
    elif (edad < 14 and edad >= 12):
        return "SUB14"

    elif (edad < 12 and edad >= 10):
        return "SUB12"

    elif (edad < 10 and edad >= 8):
        return "SUB10"

    elif (edad < 8 and edad >= 6):
        return "SUB8"

    elif (edad < 6):
        return "PREBENJAMÍN"



# MMP de un atleta

def disciplina_por_atleta(disciplina):
    disciplinas = {'Velocista': ['60m', '100m', '200m', '400m'],
                'Medio fondo': ['800m', '1500m'],
                'Fondista': ['3000m', '5000m', '10000m']}

    if disciplina in disciplinas.keys():
        return disciplinas[disciplina]

    return False


def lugar_por_atleta():
    andaluza = ['Antequera', 'Chiclana', 'Granada-CAR', 'Granada-JUV', 'Málaga-CAR', 'Málaga-CIU', 'Monzón']

    return andaluza


def establecerFechas(fecha):
    return int(fecha.strftime('%W'))


def calculoMMP(ficha):
    MMPs = {}

    for key in ficha:
        try:
            MMPs[key] = min(ficha[key]['Tiempos'])
        except:
            pass

    return MMPs


def calculoMaxSpeed(MMPs):

    velocidades = []

    for key in MMPs:
        tiempo = MMPs[key]
        distancia = findall(r'\d+', key)[0]
            
        top_speed = (((int(distancia) / tiempo) * 3600) / 1000)

        velocidades.append(round(top_speed, 2))

    return max(velocidades)


def calculoDisTotal(ficha):
    dis_total = 0

    for key in ficha:
        veces = len(ficha[key]['Tiempos'])

        prueba = findall(r'\d+', key)[0]

        dis_total = dis_total + (int(prueba) * veces)

    return dis_total / 1000


def comparacionRecordMundial(MMPs, sexo):
    records = {
        'M': {
            '60m': 6.52,
            '100m': 9.58,
            '200m': 19.19,
            '400m': 43.03,
            '800m': 1.4,
            '1500m': 3.26,
            '5000m': 12.35,
            '10000m': 26.11
        },
        'F': {
            '60m': 7.23,
            '100m': 10.49,
            '200m': 21.34,
            '400m': 47.60,
            '800m': 1.53,
            '1500m': 3.50,
            '5000m': 14.06,
            '10000m': 29.17
        }
    }

    comparacion = {}

    for key in MMPs:
        ref = records[sexo][key]
        tiempo = MMPs[key]

        porcentaje = (ref * 100) / tiempo
        distancia = int(findall(r'\d+', key)[0])

        metros = distancia - (distancia * (porcentaje / 100))

        comparacion[key] = {'Porcentaje': round(porcentaje, 2), 'Distancia': round(metros, 2)}

    return comparacion


def toSlug(nombre, apellido):
    return nombre.lower().translate(str.maketrans('áéíóú', 'aeiou')) + '-' + apellido.lower().translate(str.maketrans('áéíóú', 'aeiou'))


def hourToMarca(tiempo):
    return float(tiempo.replace(':', '.'))