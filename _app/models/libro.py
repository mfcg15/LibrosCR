from _app.config.connection import connectToMySQL

class Libro:
    def __init__( self , data ):
        self.id = data['id']
        self.titulo = data['titulo']
        self.numero_paginas = data['numero_paginas']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO libros (titulo,numero_paginas,created_at,updated_at) VALUES (%(titulo)s,%(numero_paginas)s,NOW(),NOW());"
        return connectToMySQL('esquema_libros').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM libros;"
        results = connectToMySQL('esquema_libros').query_db(query)
        libros = []
        for libro in results:
            libros.append(libro)
        return libros

    @classmethod
    def get_libro(cls,data):
        query = "SELECT * FROM libros where id = %(id)s;"
        results = connectToMySQL('esquema_libros').query_db(query,data)
        libro = []
        for i in results:
            libro.append(i)
        return libro
    
    @classmethod
    def get_libro_autor(cls,data):
        query = "SELECT nombre FROM libros inner join favoritos on libros.id = favoritos.libro_id inner join autores on autores.id = favoritos.autor_id where libro_id = %(id)s;"
        results = connectToMySQL('esquema_libros').query_db(query,data)
        librosautor = []
        for i in results:
            librosautor.append(i)
        return librosautor
    
    @classmethod
    def get_lack_libro(cls,data):
        query = "SELECT * FROM libros where libros.id not in (select favoritos.libro_id from favoritos where favoritos.autor_id = %(id)s);"
        results = connectToMySQL('esquema_libros').query_db(query,data)
        lacklibros = []
        for i in results:
            lacklibros.append(i)
        return lacklibros
