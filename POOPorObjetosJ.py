#SOLO COMO EJEMPLO DE POLIMOFISMO
#EJEMPLO 1

def rebajar_producto(producto, rebaja): 
    producto.pvp = producto.pvp - (producto.pvp/100 * rebaja)

print(alimento, "\n") 
rebajar_producto(alimento, 10)


#EJEMPLO 2
class Cuadrado(Poligono): 
    def __init__(self, lado, color=None): 
        Poligono.__init__(self,4,color) 
        self.lado = lado 

    def show(self): 
        super().show() 
        print('lado:', self.lado) 

c1 = Cuadrado(2, 'verde')   #Declaramos un cuadrado 
poligonos = t1, t2, c1      

#Tupla con dos Trinagulo y un Cuadrado 
for poligono in poligonos: 
    poligono.show() 
    print()

#EJEMPLO 3
class Empleado: 
    def __init__(self, nombre, sueldo): 
        self.nombre = nombre 
        self.sueldo = sueldo 
    def __str__(self): 
        return f'Empleado: [Nombre: 
            {self.nombre}, Sueldo: {self.sueldo}]' 
    def mostrar_detalles(self): 
        return self.__str__() 
class Gerente(Empleado): 
    def __init__(self, nombre, sueldo, 
        departamento): 
        super().__init__(nombre, sueldo) 
        self.departamento = departamento 
    def __str__(self): 
        return f'Gerente [Departamento: 
        {self.departamento}] {super().__str__()}' 
# def mostrar_detalles(self): 
# return self.__str__() 
    def imprimir_detalles(objeto): 
# print(objeto) 
        print(type(objeto)) 
        print(objeto.mostrar_detalles()) 

empleado = Empleado('Juan', 5000) 
imprimir_detalles(empleado) 
gerente = Gerente('Karla', 6000, 'Sistemas') 
imprimir_detalles(gerente)
