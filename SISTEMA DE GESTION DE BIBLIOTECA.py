class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}')"

    def añadir_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"El libro {libro.titulo} no está en la lista de libros prestados.")


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()

    def añadir_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} ha sido eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn} en la biblioteca.")

    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} ya está registrado.")
        else:
            self.usuarios_registrados.add(Usuario(nombre, id_usuario))
            print(f"Usuario '{nombre}' registrado con ID {id_usuario}.")

    def dar_baja_usuario(self, id_usuario):
        usuario = next((u for u in self.usuarios_registrados if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios_registrados.remove(usuario)
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} no está disponible en la biblioteca.")
            return

        libro = self.libros_disponibles[isbn]
        usuario = next((u for u in self.usuarios_registrados if u.id_usuario == id_usuario), None)

        if usuario is None:
            print(f"Usuario con ID {id_usuario} no está registrado.")
            return

        usuario.añadir_libro(libro)
        del self.libros_disponibles[isbn]
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, isbn, id_usuario):
        usuario = next((u for u in self.usuarios_registrados if u.id_usuario == id_usuario), None)

        if usuario is None:
            print(f"Usuario con ID {id_usuario} no está registrado.")
            return

        libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)

        if libro is None:
            print(f"El libro con ISBN {isbn} no está en los libros prestados por {usuario.nombre}.")
            return

        usuario.devolver_libro(libro)
        self.libros_disponibles[isbn] = libro
        print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if (criterio == 'titulo' and libro.titulo.lower() == valor.lower()) or \
                    (criterio == 'autor' and libro.autor.lower() == valor.lower()) or \
                    (criterio == 'categoria' and libro.categoria.lower() == valor.lower()):
                resultados.append(libro)

        if resultados:
            return resultados
        else:
            print(f"No se encontraron libros con {criterio} '{valor}'.")

    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios_registrados if u.id_usuario == id_usuario), None)

        if usuario is None:
            print(f"Usuario con ID {id_usuario} no está registrado.")
            return

        if usuario.libros_prestados:
            return usuario.libros_prestados
        else:
            print(f"El usuario con ID {id_usuario} no tiene libros prestados.")


# Ejemplo de uso
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", categoria="Novela", isbn="1234567890")
libro2 = Libro(titulo="Don Quijote de la Mancha", autor="Miguel de Cervantes", categoria="Novela", isbn="0987654321")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario(nombre="Ana Pérez", id_usuario="user1")
biblioteca.registrar_usuario(nombre="Luis Gómez", id_usuario="user2")

# Prestar libros
biblioteca.prestar_libro(isbn="1234567890", id_usuario="user1")

# Buscar libros
print(biblioteca.buscar_libro('titulo', 'Cien años de soledad'))

# Listar libros prestados
print(biblioteca.listar_libros_prestados('user1'))

# Devolver libros
biblioteca.devolver_libro(isbn="1234567890", id_usuario="user1")

# Quitar libros
biblioteca.quitar_libro(isbn="0987654321")
