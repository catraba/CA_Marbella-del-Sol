#from django.test import TestCase

# Create your tests here.

from re import findall


records = {
        'M': {
            '100m': 10.06,
            '200m': 20.04,
            '400m': 44.69,
            '800m': 1.43,
            '1500m': 3.28,
            '5000m': 12.50,
            '10000m': 27.14
        },
        'F': {
            '100m': 11.06,
            '200m': 22.38,
            '400m': 49.67,
            '800m': 1.57,
            '1500m': 3.59,
            '5000m': 14.44,
            '10000m': 30.51
        }
    }


MMPS = {'800m': 1.59, '1500m': 3.41}

comparacion = {}

for key in MMPS:
    ref = records['M'][key]
    tiempo = MMPS[key]

    porcentaje = (ref * 100) / tiempo
    distancia = findall(r'\d+', key)[0]

    metros = int(distancia) * (porcentaje / 100)

    comparacion[key] = {'Porcentaje': round(porcentaje, 2), 'Distancia': round(metros, 2)}

print(comparacion)