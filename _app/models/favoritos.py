from _app.config.connection import connectToMySQL

class Favorito:
    def __init__( self , data ):
        self.id = data['id']
        self.autor_id = data['autor_id']
        self.libro_id = data['libro_id']


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO favoritos (autor_id , libro_id) VALUES (%(autor_id)s,%(libro_id)s);"
        return connectToMySQL('esquema_libros').query_db( query, data)