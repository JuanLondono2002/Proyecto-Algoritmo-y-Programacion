import API
from Clase import Departamento, Obra_Museo

class Museo:

    def __init__(self):
        self.nacionalidades=[]
        archivo=open("Nacionalidad_Autor.txt", "r")
        for nacionalidad in archivo:
            nacionalidades_autores=nacionalidad.strip()
            self.nacionalidades.append(nacionalidades_autores)
        archivo.close()

    def empezar_programa(self):
        while True:
            opcion = input("""\nBienvenido a MetroArt: Seleccione una opción del menú:

1- Ver departamentos de MetroArte

2- Buscar obras por nacionalidad del autor

3- Buscar obras por nombre del autor

4- Salir del programa

--> """)

            if opcion == '1':
                self.ver_departamentos()
            elif opcion == '2':
                self.buscar_nacionalidades()
            elif opcion == '3':
                self.buscar_por_nombre_autor()
            elif opcion == '4':
                print("Gracias por visitar MetroArt")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")

    def buscar_nacionalidades(self):
        pagina = 0
        elementos_por_pagina = 25
        total_paginas = (len(self.nacionalidades) + elementos_por_pagina - 1) // elementos_por_pagina

        while True:
            inicio = pagina * elementos_por_pagina
            fin = inicio + elementos_por_pagina
            nacionalidades_pagina = self.nacionalidades[inicio:fin]

            print("\n--- Nacionalidades Disponibles ---")
            for i, nacionalidad in enumerate(nacionalidades_pagina,start=1):
                print(f"{i} - {nacionalidad}")

            print("\nSeleccione una opcion del menu:")
            print(f"1- Seleccionar una nacionalidad de la lista (1-{len(nacionalidades_pagina)})")
            if pagina < total_paginas - 1:
                print("2- Ver más nacionalidades")
            print("3- Volver al menú principal")

            opcion = input("--> ")

            if opcion == '1':
                selec_nacionalidad = input(f"\nIngrese el número de nacionalidad de la lista (1-{len(nacionalidades_pagina)}): ")
                if selec_nacionalidad.isdigit():
                    selec_nacionalidad = int(selec_nacionalidad)
                    if 1 <= selec_nacionalidad <= len(nacionalidades_pagina):
                        nacionalidad_seleccionada = nacionalidades_pagina[selec_nacionalidad-1]
                        self.obras_por_nacionalidad(nacionalidad_seleccionada)
                        break
                    else:
                        print("\nNúmero fuera de rango. Intente nuevamente.")
                else:
                    print("\nOpcion invalida. Debe ingresar un número.")

            elif opcion == '2' and pagina < total_paginas - 1:
                pagina += 1
                print(f"Mostrando página {pagina + 1} de {total_paginas}")

            elif opcion == '3':
                break

            else:
                print("Opción no válida. Intente nuevamente.")

    def obras_por_nacionalidad(self, nacionalidad):
        print(f"Buscando obras de la nacionalidad: {nacionalidad}")
        ids_obras = API.buscar_obras_por_nacionalidad(nacionalidad)

        print(f"\nObras encontradas:")
        for obra_id in ids_obras[:25]:
            detalles_obra = API.obtener_detalles_obra(obra_id)
            if detalles_obra is not None:
                obra = Obra_Museo(id=detalles_obra.get('objectID'),
                    titulo=detalles_obra.get('title', 'Título no disponible'),
                    nombre_artista=detalles_obra.get('artistDisplayName', 'Anónimo'),
                    nacionalidad=detalles_obra.get('artistNationality', 'No disponible'),
                    fecha_nacimiento=detalles_obra.get('artistBeginDate', 'No disponible'),
                    fecha_muerte=detalles_obra.get('artistEndDate', 'No disponible'),
                    tipo=detalles_obra.get('classification', 'No disponible'),
                    fecha_creacion=detalles_obra.get('objectDate', 'No disponible'),
                    url_imagen=detalles_obra.get('primaryImageSmall', 'No disponible'))
                print(f"ID: {obra_id} - Título: {obra.titulo} - Autor: {obra.nombre_artista}")

        opcion=input("""Seleccione una opcion del menu:

1- Ver detalles de una obra de la lista
2- Volver al menu principal
--> """)

        if opcion=="1":
            id_obra=input("\nIngrese el ID de la obra para ver sus detalles: ")
            self.ver_detalles_obra(id_obra)

        elif opcion=="2":
            self.empezar_programa()

        else:
            print("\nOpcion Invalidad. Seleccione una opcion del menu")

    def ver_departamentos(self):
        departamentos_dic = API.obtener_departamentos()
        departamentos_obj = []
        for departamento in departamentos_dic:
            departamentos_obj.append(Departamento(departamento["departmentId"],departamento["displayName"]))

        print("\nDepartamentos de MetroArt")
        for departamento in departamentos_obj:
            departamento.show()

        id_departamento = input("\nEscribe el ID del departamento del cual quieres ver sus obras: ")
        ids_obras = API.obtener_obras_por_departamento(id_departamento)

        print(f"\nBuscando obras del departamento seleccionado:")
        for id_obra in ids_obras[:25]:
            detalles_obra = API.obtener_detalles_obra(id_obra)
            if detalles_obra is not None:
                obra = Obra_Museo(
                    id=detalles_obra.get('objectID'),
                    titulo=detalles_obra.get('title', 'Título no disponible'),
                    nombre_artista=detalles_obra.get('artistDisplayName', 'Anónimo'),
                    nacionalidad=detalles_obra.get('artistNationality', 'No disponible'),
                    fecha_nacimiento=detalles_obra.get('artistBeginDate', 'No disponible'),
                    fecha_muerte=detalles_obra.get('artistEndDate', 'No disponible'),
                    tipo=detalles_obra.get('classification', 'No disponible'),
                    fecha_creacion=detalles_obra.get('objectDate', 'No disponible'),
                    url_imagen=detalles_obra.get('primaryImageSmall', 'No disponible'))
                print(f"ID: {id_obra} - Título: {obra.titulo} - Autor: {obra.nombre_artista}")

        
        opcion=input("""\nSeleccione una opcion del menu:

1- Ver detalle de una obra de la lista
2- Volver al menu principal
--> """)

        if opcion=="1":
            id_obra=input("\nIngrese el ID de la obra para ver sus detalles: ")
            self.ver_detalles_obra(id_obra)

        elif opcion=="2":
            self.empezar_programa()

        else:
            print("\nOpcion Invalidad. Seleccione una opcion del menu")

    def buscar_por_nombre_autor(self):
        nombre_autor = input("\nIngrese el nombre del autor que deseas buscar (ej: Vincent van Gogh): ")
        ids_obras = API.buscar_obras_por_autor(nombre_autor)

        if len(ids_obras) == 0:
            print("\nNo se encontraron obras para este autor.")
            return

        print(f"\nBuscando obras de: {nombre_autor}")
        for obra_id in ids_obras[:25]:
            detalles_obra = API.obtener_detalles_obra(obra_id)
            if detalles_obra is not None:
                obra = Obra_Museo(
                    id=detalles_obra.get('objectID'),
                    titulo=detalles_obra.get('title', 'Título no disponible'),
                    nombre_artista=detalles_obra.get('artistDisplayName', 'Anónimo'),
                    nacionalidad=detalles_obra.get('artistNationality', 'No disponible'),
                    fecha_nacimiento=detalles_obra.get('artistBeginDate', 'No disponible'),
                    fecha_muerte=detalles_obra.get('artistEndDate', 'No disponible'),
                    tipo=detalles_obra.get('classification', 'No disponible'),
                    fecha_creacion=detalles_obra.get('objectDate', 'No disponible'),
                    url_imagen=detalles_obra.get('primaryImageSmall', 'No disponible'))
                print(f"ID: {obra_id} - Título: {obra.titulo} - Autor: {obra.nombre_artista}")

        opcion=input("""\nSeleccione una opcion del menu:

1- Ver detalle de una obra de la lista
2- Volver al menu principal
--> """)
        
        if opcion=="1":
            id_obra=input("\nIngrese el ID de la obra para ver sus detalles: ")
            self.ver_detalles_obra(id_obra)

        elif opcion=="2":
            self.empezar_programa()

        else:
            print("\nOpcion Invalidad. Seleccione una opcion del menu")

    def ver_detalles_obra(self, id_obra):
        datos_obra_dict = API.obtener_detalles_obra(id_obra)
        if datos_obra_dict is not None:
            obra_obj = Obra_Museo(
                id=datos_obra_dict.get('objectID'),
                titulo=datos_obra_dict.get('title', 'Título no disponible'),
                nombre_artista=datos_obra_dict.get('artistDisplayName', 'Anónimo'),
                nacionalidad=datos_obra_dict.get('artistNationality', 'No disponible'),
                fecha_nacimiento=datos_obra_dict.get('artistBeginDate', 'No disponible'),
                fecha_muerte=datos_obra_dict.get('artistEndDate', 'No disponible'),
                tipo=datos_obra_dict.get('classification', 'No disponible'),
                fecha_creacion=datos_obra_dict.get('objectDate', 'No disponible'),
                url_imagen=datos_obra_dict.get('primaryImageSmall', 'No disponible')
            )
            obra_obj.show()

            opcion_imagen = input("""\n¿Desea ver la imagen de la obra?
-1 Si
-2 No. Volver al menu principal
--> """)
            if opcion_imagen == '1':
                obra_obj.mostrar_imagen()

            elif opcion_imagen=="2":
                self.empezar_programa()
        else:
            print("\nNo se pudieron obtener los detalles de la obra.")
