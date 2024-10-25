class Coche: 

# Declaración del constructor con parámetros 

    def __init__(self, largo, ancho, ruedas, peso, color, is_enMarcha):  

        self.largo = largo
        self.ancho = ancho 
        self.ruedas = ruedas 
        self.peso = peso 
        self.color = color 
        self.is_enMarcha = is_enMarcha 
        print(self.largo)
        print(self.ancho)
        print(self.peso)
        print(self.color)
        print(self.is_enMarcha)

# Declaración de dos instancias de clase pasándoles 
# los parámetros requeridos en el constructor. 

coche_1 = Coche(400, 160, 4, 1200, "amarillo", True) 

coche_2 = Coche(420, 150, 4, 1500, "verde", False)

# Da error al faltar el último parámetro
# coche_3 = Coche(420, 150, 4, 1500, "verde")

# Da el mismo error si falta cualquier otro, dice que le falta el último
# al ir los parámetros en orden de forma obligatoria
# coche_2 = Coche(420, 150, 4, 1500, False)
