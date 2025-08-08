import Imagen

class Departamento:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def show(self):
        print(f"ID: {self.id} - Nombre: {self.nombre}")

class Obra_Museo:
    def __init__(self, id, titulo, nombre_artista, nacionalidad, fecha_nacimiento, fecha_muerte, tipo, fecha_creacion, url_imagen):
        self.id = id
        self.titulo = titulo
        self.nombre_artista = nombre_artista
        self.nacionalidad_artista = nacionalidad
        self.fecha_nacimiento_artista = fecha_nacimiento
        self.fecha_muerte_artista = fecha_muerte
        self.tipo = tipo
        self.fecha_creacion = fecha_creacion
        self.url_imagen = url_imagen

    def resumen(self):
        print(f"ID: {self.id} - Título: {self.titulo} - Artista: {self.nombre_artista}")

    def show(self):
        print("\nDetalles de la obra seleccionada")
        print(f"Título: {self.titulo}")
        print(f"Artista: {self.nombre_artista}")
        print(f"Nacionalidad del artista: {self.nacionalidad_artista}")
        print(f"Periodo del Artista: {self.fecha_nacimiento_artista} - {self.fecha_muerte_artista}")
        print(f"Tipo de obra: {self.tipo}")
        print(f"Año de creación: {self.fecha_creacion}")
        print(f"URL de la imagen: {self.url_imagen}")
    
    def mostrar_imagen(self):
        if self.url_imagen and self.url_imagen.lower() != 'no disponible':
            print(f"\nMostrando imagen de la obra: {self.titulo}")
            Imagen.mostrar_imagen_desde_url(self.url_imagen)
        else:
            print("La obra no tiene una imagen disponible.")