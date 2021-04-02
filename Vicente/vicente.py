
#from funciones import convertir_numero, guardar_numero, crea_historial, solo_digitos, muestra_historial
import funciones as num

print("Bienvenido! Ingrese un número del 0 al 999999\nPara salir digite -> salir")
print("")

#Creando historial
historial = num.crea_historial()

estado = " "
while estado != "salir":
    numero = num.solo_digitos() 
    if numero != "salir":
       #Funcion que retorna numero con punto separador de miles
        guarda_numero = num.convertir_numero(numero)
        historial = num.guardar_numero(guarda_numero, historial)    
    elif numero == 'salir':
        estado = "salir"

#Funcion para mostrar historial
num.muestra_historial(historial)
    
