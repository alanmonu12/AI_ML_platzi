def enum_ex(objetivo):
    resultado = 0;
    paso = 1;

    while resultado**2 < objetivo:
        resultado += paso

    if resultado < objetivo:
        return resultado
    else:
        return -1

def aprox_soluciones(objetivo, epsilon):
    resultado = 0.0
    paso = epsilon**2
    
    while abs(resultado**2 - objetivo) >= epsilon and resultado <= objetivo:
        resultado += paso

    if abs(resultado ** 2 - objetivo) >= epsilon:
        return - 1
    else:
        return resultado

def busqueda_binaria(objetivo, epsilon):
    resultado = 0.0
    
    bajo = 0.0
    alto = max(1.0, objetivo)

    resultado = (bajo + alto) / 2

    while abs(resultado**2 - objetivo) >= epsilon:
        if resultado**2 < objetivo:
            bajo = resultado
        else:
            alto = resultado

        resultado = (alto + bajo) / 2

    return resultado


tipo_algoritmo = int(input('Ingresa el metodo de busqueda que quieres usar para encontrar la respuesta\r\n \
1. Enumeración exahustiva\r\n \
2. Aproximacion de soluciones\r\n \
3. Busqueda binaria\r\n \
 -> '))

objetivo = int(input('Ingresa un numero: '))
respuesta = 0.0

if tipo_algoritmo == 1:
    respuesta = enum_ex(objetivo)
elif tipo_algoritmo == 2:
    epsilon = float(input('Ingresa epsilon: '))
    respuesta = aprox_soluciones(objetivo, epsilon)
elif tipo_algoritmo == 3:
    epsilon = float(input('Ingresa epsilon: '))
    respuesta = busqueda_binaria(objetivo, epsilon)
else:
    print('No es una opcion valida')


if (respuesta > 0):
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print('No se pudo encontrar la respuesta')