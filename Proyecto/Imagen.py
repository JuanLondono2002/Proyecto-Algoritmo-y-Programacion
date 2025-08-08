import requests
from PIL import Image

def mostrar_imagen_desde_url(url):
    try:
        nombre_temp = "temp_image"
        response = requests.get(url, stream=True)
        response.raise_for_status()

        content_type = response.headers.get('Content-Type', '')
        extension = '.jpg'
        
        if 'image/png' in content_type:
            extension = '.png'
        elif 'image/jpeg' in content_type:
            extension = '.jpg'
        elif 'image/svg+xml' in content_type:
            extension = '.svg'
        
        nombre_archivo = f"{nombre_temp}{extension}"
        
        with open(nombre_archivo, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        img = Image.open(nombre_archivo)
        img.show()
        
        return True
    except Exception as e:
        print(f"Error al mostrar la imagen: {e}")
        return False