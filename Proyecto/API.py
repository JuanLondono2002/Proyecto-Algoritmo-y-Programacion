import requests

def obtener_departamentos():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('departments', [])
    else:
        print(f"Error en API: La solicitud de departamentos falló con código {response.status_code}")
        return None

def obtener_obras_por_departamento(id_depto):  
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={id_depto}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('total', 0) == 0:
            return []
        return data.get('objectIDs', [])
    else:
        print(f"Error en API: La solicitud de obras falló con código {response.status_code}")
        return []

def obtener_detalles_obra(id_obra):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_obra}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error en API: La solicitud del objeto falló con código {response.status_code}")
        return None
    
def buscar_obras_por_nacionalidad(nacionalidad):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('total', 0) > 0:
            return data.get('objectIDs', [])
    return []

def buscar_obras_por_autor(nombre_autor):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_autor}"
    response = requests.get(url)
    data = response.json()
    return data.get('objectIDs', [])