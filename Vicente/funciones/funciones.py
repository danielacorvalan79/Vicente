
def solo_digitos():    
    while True:
        numero_original = input("Ingrese un número entero: ")    
        try:        
            numero_original = int(numero_original)        
            if numero_original >= 0 and numero_original <= 999999:            
                return numero_original        
            else:            
                print("Ingrese un número entre 0 y 999.999")    
        except ValueError:        
            if numero_original == "salir":
                return "salir"
            else:
                print("Ingresa un número entero. No letras ni decimales.")


def convertir_numero(numero): 
	return ("{:,}".format(numero)).replace(",", ".")

def guardar_numero(numero, lista):
    lista.append(numero)
    return lista

def crea_historial():
    lista=[]
    return lista

def muestra_historial(historial):
    print("Estos son sus números: ")
    for element in historial:
        print(element)
        