#Ejercicio con Destructor

class Book(): 

#Clase para trabajar con libros 

    def __init__(self, title, author = "", electronic = False): 
        self.title = title 
        self.author = author 
        self.is_electronic = electronic 
        '''print(self.title)
        print(self.author)
        print(self.is_electronic)'''

    def __del__(self): 
        '''print(self.title)
        print(self.author)
        print(self.is_electronic)'''
        print("Acabas de llamar al método destructor. El objeto acaba de ser eliminado")

book = Book("Lazarillo de Tormes") 
book.title 
print(book.title)
print(book.author)
print(book.is_electronic)   
del book 

#Da error al haber sido eliminado el objeto 'book' de la clase 'Book'
'''print(book.title)
print(book.author)
print(book.is_electronic)'''
