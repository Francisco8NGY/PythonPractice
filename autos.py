#Francisco Vazquez Delgado
#Instituto Tecnologico de Colima
#Ing. sistemas computacionales.
#Programacion en python

#creamos clase auto
class Auto:
#inicializamos attibutos *(constructor)
    def __init__(self,Nserie,marca,year,precio):
        self.Nserie = Nserie
        self.marca = marca
        self.year = year
        self.precio = precio
    #retornasmos los atributos
    def getNserie(self):
        return self.Nserie

    def getMarca(self):
        return self.marca

    def getyear(self):
        return self.year

    def getPrecio(self):
        return self.precio

#creamos clase vagoneta que extiende de auto
class vagonetas(Auto):
#inicializamos los atributos
    def __init__(self,Nserie,marca,year,precio, pasajeros):
        Auto.__init__(self,Nserie,marca,year,precio)#funcion super atributos clase padre
        self.pasajeros = pasajeros
    #retornoamos pasajeros
    def getPasajeros(self):
        return self.pasajeros

    
#creamos clase lujo que extiende de auto
class Lujo(Auto):
#inicializamos los atributos
    def __init__(self,Nserie,marca,year,precio ,pasajeros):
        #funcion super atributos clase padre
        Auto.__init__(self,Nserie,marca,year,precio )
        self.pasajeros =pasajeros
    #retornoamos 
    def getPasajerosLujo(self):
        return self.pasajeros

    
#creamos clase camioneta que extiende de auto
class camioneta(Auto):
#inicializamos los atributos
    def __init__(self,Nserie,marca,year,precio,carga,ejes,rodada):
         #funcion super atributos clase padre
        Auto.__init__(self,Nserie,marca,year,precio)
        self.carga = carga
        self.ejes = ejes
        self.rodada = rodada
#retornoamos 
    def getCarga(self):
        return self.carga

    def getEjes(self):
        return self.ejes
    
    def getRodada(self):
        return self.rodada


#Creamos objeto camioneta inicializamos valores
camioneta1 = camioneta(34454,'nissan','2020',500000,5000,2, 'rodada')
#imprimimos
print(camioneta1.getNserie())
print(camioneta1.getMarca())
print(camioneta1.getPrecio())
print(camioneta1.getCarga())