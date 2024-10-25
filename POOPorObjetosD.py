# Creación de la clase Coche 

class Coche(): 

#  Declaración del constructor de la clase Coche 

    def __init__(self): 
        self.largo = 250 
        self.ancho = 120 
        self.ruedas = 4 
        self.peso = 900 
        self.color = "rojo" 
        self.is_enMarcha = False 
        print ('¡No Arrancado!')
 
# Declaración de métodos 

    def arrancar(self):     #self hace referencia a la instancia de clase. 
        self.is_enMarcha = True   #Es como si pusiésemos miCoche.is_enMarcha = True
        return 'SÍ'
 
    def estado(self): 
        if (self.is_enMarcha == True): 
            return "El coche está arrancado" 
        else: 
            return "El coche está parado"     
 
# Declaración de una instancia de clase, 
# objeto de clase o ejemplar de clase. 

coche_1 = Coche() 
 
# Acceso a un atributo de la clase Coche. 
# Nomenclatura del punto. 

coche_1.ruedas = 7
print ("¿ Número de ruedas :", coche_1.ruedas, "?")

print ("El largo del coche es de", coche_1.largo, "cm.") 

coche_1.arrancar() 
print(coche_1.estado()) 
 
# Acceso a un método de la clase Coche. 
# Nomenclatura del punto. 

print("El coche está arrancado:", coche_1.arrancar()) 
