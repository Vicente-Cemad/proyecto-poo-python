#SOLO COMO EJEMPLO DE POLIMOFISMO
#EJEMPLO 1
'''
def rebajar_producto(producto, rebaja): 
    producto.pvp = producto.pvp - (producto.pvp/100 * rebaja)

print(alimento, "\n") 
rebajar_producto(alimento, 10)
'''

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
