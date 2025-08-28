#Ejercicio 6
#Entrada
print("Ejercicio 6")
nota_parcial_1 = float(input("Ingrese la nota del primer parcial: "))
nota_parcial_2 = float(input("Ingrese la nota del segundo parcial: "))
nota_parcial_3 = float(input("Ingrese la nota del tercer parcial: "))
nota_examen_final = float(input("Ingrese su calificación en el examen final: "))
nota_trabajo_final = float(input("Ingrese su calificación en el trabajo dinal: "))
nota_final = (None) 
promedio_parciales = (None)
porcentaje_promedio_parcial = (None)
porcentaje_trabajo_final = (None)

#Proceso
promedio_parciales = nota_parcial_1 + nota_parcial_2 + nota_parcial_3
promedio_parciales /= 3

#Calculamos el 55% del promedio de los 3 parciales
porcentaje_promedio_parcial = promedio_parciales * 55 / 100
porcentaje_promedio_parcial = round(porcentaje_promedio_parcial, 2)

#Calculamos el 30% de la nota del examen final
porcentaje_examen_final = nota_examen_final * 30 / 100
porcentaje_examen_final = round(porcentaje_examen_final, 2)

#Calculamos el 15% de la nota del trabajo final
porcentaje_trabajo_final = nota_trabajo_final * 15 / 100
porcentaje_trabajo_final = round(porcentaje_trabajo_final, 2)

nota_final = porcentaje_promedio_parcial + porcentaje_examen_final + porcentaje_trabajo_final

#Salida
print(f"La nota final es de: {nota_final} \n")

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
print(f"${dolares} Dólares equivalen a ${pesos_argentinos} Pesos Argentinos")
print(f"${dolares} Dólares equivalen a ${pesos_colombianos} Pesos Colombianos")
print(f"${dolares} Dólares equivalen a €{euros} euros \n")

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
print(f"Para recorrer {kilometros_recorridos} kilómetros se necesitan {litros_necesarios} litros de gasolina")
print(f"El viaje costara: ${costo_viaje} pesos")
print(f"Te demoraras {hora} horas y {minutos} minutos en recorrer {kilometros_recorridos} kilómetros \n")

#Ejercicio 9
#Entrada
print("Ejercicio 9")
prestamo_solicitado = float(input("Ingrese el monto del prestamo a solicitar: "))
interes_fijo_mensual = 0.02
cuotas = 12
interes_a_pagar_por_mes = (None)
interes_a_pagar_en_total = (None)
monto_total_a_devolver = (None)
valor_cada_cuota = (None)

#Proceso
interes_a_pagar_por_mes = prestamo_solicitado * interes_fijo_mensual
interes_a_pagar_en_total = interes_a_pagar_por_mes * cuotas
monto_total_a_devolver = prestamo_solicitado + interes_a_pagar_en_total
valor_cada_cuota = monto_total_a_devolver / cuotas
valor_cada_cuota = round(valor_cada_cuota, 2)

#Salida
print(f"El monto total a delvolver es de: ${monto_total_a_devolver}, esto se debe pagar en {cuotas} cuotas de ${valor_cada_cuota} \n")