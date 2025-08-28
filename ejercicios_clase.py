#Ejercicio 6

#Ejercicio 7
#Entrada
print("Ejercicios 7")
dolares = float(input("Ingrese un monto en Dólares, para mostrar su equivalencia en Pesos Argentinos, Pesos Colombianos y en Euros: "))
pesos_argentinos = (None)
pesos_colombianos = (None)
euros = (None)
tasa_fija_pesos_argentinos = 1350
tasa_fija_pesos_colombianos = 4031
tasa_fija_euros = 0.86

#Proceso
pesos_argentinos = tasa_fija_pesos_argentinos * dolares
pesos_colombianos = tasa_fija_pesos_colombianos * dolares
euros = tasa_fija_euros * dolares

#Salida
print()
print(f"${dolares} Dólares equivalen a ${pesos_argentinos} Pesos Argentinos")
print(f"${dolares} Dólares equivalen a ${pesos_colombianos} Pesos Colombianos")
print(f"${dolares} Dólares equivalen a €{euros} euros")
print()

#Ejercicio 8
#Entrada
print("Ejercicio 8")
kilometros_recorridos = float(input("Ingrse los kilómetros recorridos: "))
precio_litro = float(input("Ingrese a cuanto esta el litro de gasolina: "))
kilometro_por_hora = 90
litros_necesarios = (None)
costo_viaje = (None)
hora_no_definida = (None)
hora = (None)
minutos = (None)

#Proceso
litros_necesarios = 8 * kilometros_recorridos / 100
costo_viaje = precio_litro * litros_necesarios

#Calculamos parcialmente las horas que se demora en recorrer lo kilómetros
hora_no_definida = kilometros_recorridos / kilometro_por_hora
#Obtenemos la parte entera de la división para la hora
hora = int(hora_no_definida)
#Obtenemos la parte decimal  de la división
minutos = hora - hora_no_definida
#Obtenemos la cantidad de minutos multiplicando los decimales por 60 y calculamos su valor absoluto para que sea un valor positivo
minutos = abs(int(minutos * 60))

#Salida
print()
print(f"Para recorrer {kilometros_recorridos} kilómetros se necesitan {litros_necesarios} litros de gasolina")
print(f"El viaje costara: ${costo_viaje} pesos")
print(f"Te demoraras {hora} horas y {minutos} minutos en recorrer {kilometros_recorridos} kilómetros")
print()

#Ejercicio 9
