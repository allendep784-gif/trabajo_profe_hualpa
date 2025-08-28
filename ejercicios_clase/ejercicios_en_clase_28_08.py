nombre = ""
apellido = ""
cuit = ""
ingresos_mensuales = ""
antiguedad_laboral = ""
historial_crediticio = ""
calidad = {"bueno", "regular", "malo"}
monto_aprobado = (None)

def validador_de_entrada(entrada, texto):
    while True:
        if entrada.isalpha():
            print(f"{texto} ingresado correcto")
            return entrada
        else:
            print(f"{texto} ingresado incorrecto, solo se permiten letras")
            entrada = input(f"Ingrese su {texto} nuevamente\n"">> ")

def validador_de_cuit():
    try:
        cuit = int(input("Ingrese su cuit/cuil sin guiones\n"">> "))
    except ValueError:
         print("Cuit ingresado incorrecto, solo se permiten numeros")
         return validador_de_cuit()
    if len(str(cuit)) == 11:
        print("Cuit ingresado correcto")
        return cuit
    else:
        print("Cuit ingresado incorrecto, debe tener 11 digitos")
        return validador_de_cuit()
    
def validador_de_ingresos():
    try:
        ingresos = float(input("Ingrese sus ingresos mensuales en pesos \n"">> "))
    except ValueError:
        print("Ingreso mensual ingresado incorrecto, solo se permiten numeros")
        return validador_de_ingresos()
    if ingresos > 0:
        print("Ingreso mensual ingresado correcto")
        return ingresos
    else:
        print("Ingreso mensual ingresado incorrecto, debe ser mayor a 0")
        return validador_de_ingresos()

def validador_de_antiguedad():
    try:
        antiguedad = int(input("Ingrese su antiguedad laboral en años \n"">> "))
    except ValueError:
        print("Antiguedad ingresada incorrecta, solo se permiten numeros.")
        return validador_de_antiguedad()
    if antiguedad > 0:
        print("Antiguedad ingresada correcta")
        return antiguedad
    else:
        print("Antiguedad ingresada incorrecta")
        return validador_de_antiguedad()

def validador_crediticio():
    historial = str(input("Ingrese su historial crediticio [Bueno, regular, malo] \n"">> ")).lower()
    if historial in calidad:
        print("Historial crediticio ingresado correctamente \n"">> ")
        return historial
    else:
        print("Historial crediticio ingresado incorrecto, solo se permite [bueno, malo, regular]")
        return validador_crediticio()

def evaluacion_de_credito():
    print("Bienvenido a la evaluación de creditos personales")
    nombre = validador_de_entrada(input("Ingrese su nombre \n"">> "), "nombre")
    apellido = validador_de_entrada(input("Ingrese su apellido \n"">> "), "apellido")
    cuit = validador_de_cuit()
    ingresos_mensuales = validador_de_ingresos()
    antiguedad_laboral = validador_de_antiguedad()
    historial_crediticio = validador_crediticio()
    
    historial_crediticio = historial_crediticio.lower()
    if historial_crediticio == "malo":
        print("La solicitud de credito fue rechazado")
        exit()
    elif ingresos_mensuales < 200000:
        print("Solicitud de crédito rechazada")
        exit()
    elif ingresos_mensuales >= 200000 and antiguedad_laboral < 2:
        print("Podras pedir hasta $500000")
        monto_aprobado = 500000
    else:
        if ingresos_mensuales >= 200000 and antiguedad_laboral >= 2:
            if historial_crediticio == "regular":
                print("puede pedir hasta $1000000")
                monto_aprobado = 1000000
            elif historial_crediticio == "bueno":
                print("Puedes pedir hasta $3000000")
                monto_aprobado = 3000000

    print("Cliente:", nombre, apellido)
    print(f"Cuit: {cuit}")
    print(f"Ingresos: {ingresos_mensuales:.2f}")
    print("Antigüdad: ", antiguedad_laboral, "años")
    print("Historial crediticio: ", historial_crediticio)
    print("Monto aprobado: $", monto_aprobado)

if __name__ == "__main__":
    evaluacion_de_credito()