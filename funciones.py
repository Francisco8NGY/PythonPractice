#Lenguaje de programacion python
#Uso de gunciones
# funciones del lenguaje
#funciones definidas por el usuario
#sesion: sabado 1-febrero-2020

valores=[]
num = 0
def promedio(valores):
    while True:
        num=input('ingrese un numero [o CERO para terminar]')
        if (int(num)==0):
            break
        else:
           valores+=[num]
    prom = sum(valores)/len(valores)
    return prom
    


print("El promedio de los valores es: ", promedio(valores)) 
print("Linea agregada")