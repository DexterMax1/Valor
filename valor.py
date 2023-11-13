valor = int(input('Escribir el valor: '))
Minimo = 5
Maximo = 30

dentroRango = valor >= Minimo and valor <= Maximo

if dentroRango: 
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} esta fuera de rango')