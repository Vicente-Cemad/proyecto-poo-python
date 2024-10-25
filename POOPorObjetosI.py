#CLASES PADRES

class Vehículos(): 
    def __init__(self, marca, modelo): 
        self.marca = marca 
        self.modelo = modelo 
        self.color = "negro" 
        self.arrancado = False 
        self.parado = True

    def arrancar(self): 
        self.arrancado = True 
        self.parado = False 
 
    def parar(self): 
        self.parado = True 
        self.arrancado = False 
         
    def resumen(self): 
        print("El modelo es un coche", "\n", 
            "Marca:", self.marca, "\n", 
              "Modelo:", self.modelo, "\n", 
              "Color:", self.color, "\n", 
              "Está arrancado:", self.arrancado,"\n", 
              "Está parado:", self.parado 
              )
class V_electricos(): 
    def __init__(self, marca, modelo): 
        self.marca = marca 
        self.modelo = modelo 
        self.color = "negro" 
        self.arrancado = False 
        self.parado = True

    def arrancar(self): 
        self.arrancado = True 
        self.parado = False 
 
    def parar(self): 
        self.parado = True 
        self.arrancado = False 
         
    def resumen(self): 
        print("El modelo es un coche", "\n", 
            "Marca:", self.marca, "\n", 
              "Modelo:", self.modelo, "\n", 
              "Color:", self.color, "\n", 
              "Está arrancado:", self.arrancado,"\n", 
              "Está parado:", self.parado 
              )
        
#HERENCIA MÚLTIPLE
class B_electrica(Vehículos, V_electricos):
    
    def estado(self): 
        print("Marca", self.marca,"Modelo", self.modelo) 

    def cilindrada(self): 
        self.cilindrada=3000 

    def estado(self): 
        print("Marca", self.marca,
           "Modelo", self.modelo,
             "Cilindrada", self.cilindrada)

#SUPER()
class Persona(): 

    def __init__(self, nombre, edad, lugar): 
        self.nombre=nombre 
        self.edad=edad 
        self.lugar=lugar 

    def descripcion(self): 
        print("El nombre es ", self.nombre,
               ", tiene ", self.edad,
                 "años", " y es de ", self.lugar) 

class Empleado(Persona): 
    def __init__(self, salario, antiguedad, nombre_emp, edad_emp, lugar_epm):
        super().__init__(nombre_emp, edad_emp, lugar_epm) 
        self.salario=salario 
        self.antiguedad=antiguedad 
         
    def descripcion(self): 
        super().descripcion() 
        print("Salario: ", self.salario, 
        ", antiguedad: ", self.antiguedad) 
         
Angel=Persona("Angel", 43, "Malaga") 
Angel.descripcion() 
 
Empleado1=Empleado(2000, 2017, "Manolo", 
33, "Madrid") 
Empleado1.descripcion()

#SIN SUPER
class Padre(): #Creamos la clase Padre 
    def __init__(self, ojos, cejas): 
#Definimos los Atributos en el constructor de la clase 
        self.ojos = ojos 
        self.cejas = cejas 
 
class Hijo(Padre): #Creamos clase hija que hereda de Padre 
    def __init__(self, ojos, cejas, cara): #Definimos los atributos en el 
        #constructor 
        self.ojos = ojos #Sobreescribimos cada atributo 
        self.cejas = cejas 
        self.cara = cara #Especificamos el nuevo atributo para Hijo 
         
Tomas = Hijo('Marrones', 'Negras', 'Larga') #Instanciamos 
print (Tomas.ojos, Tomas.cejas, Tomas.cara) #Imprimimos los atributos del objeto 

class Padre(object): #Creamos la clase Padre 
    def __init__(self, ojos, cejas): 
#Definimos los Atributos 
        self.ojos = ojos 
        self.cejas = cejas 
         
class Hijo(Padre): #Creamos clase hija que hereda de Padre 
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la 
        #clase especificando atributos 
        super().__init__(ojos, cejas)#Solicitamos a super llamar de la 
        #clase padre esos atributos 
        self.cara = cara #Especificamos el nuevo atributo para Hijo 

Tomas = Hijo('Marrones', 'Negras', 'Larga') 
print (Tomas.ojos, Tomas.cejas, Tomas.cara)

#EN PYTHON TODO ES PUBLICO, SE DIFERENCIA POR NOMENCLATURA CON UN _ O DOS __
class Ejemplo: 
    __atributo_privado = "Soy un atributo inalcanzable desde fuera." 
 
    def __metodo_privado(self): 
        print("Soy un método inalcanzable desde fuera.") 
 
    def atributo_publico(self): 
        return self.__atributo_privado 
 
    def metodo_publico(self): 
        return self.__metodo_privado() 
 
e = Ejemplo() 
print(e.atributo_publico()) 
e.metodo_publico() 

class Coche: 
    # Método constructor 
    def __init__(self): 
        self.__largo = 250 
        self.__ancho = 120 
        self.__ruedas = 4 
        self.__peso = 900 
        self.__color = "rojo" 
        self.__is_enMarcha = False 
 
    # Declaración de métodos 
    def arrancar(self):  # self hace referencia a la instancia de clase. 
        self.is_enMarcha = True  # Es como si pusiésemos miCoche.is_enMarcha = True 
 
    def estado(self): 
        if (self.is_enMarcha == True): 
            return "El coche está arrancado" 
        else: 
            return "El coche está parado" 
 
        # Declaración de una instancia de 
        # clase, objeto de clase o ejemplar de clase. 
 
miCoche = Coche() 
 
miCoche.__ruedas = 9 
print("Mi coche tiene", miCoche.__ruedas, "ruedas.") 

