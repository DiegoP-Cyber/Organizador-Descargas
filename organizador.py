import os
import shutil

# 1. Configuración de rutas
descargas = os.path.join(os.path.expanduser("~"), "Downloads")

# 2. Diccionario de categorías (Fácil de expandir)
CATEGORIAS = {
    "Instaladores": [".exe", ".msi"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
}

print(f"--- EJECUTANDO ORGANIZADOR PRO ---")

for archivo in os.listdir(descargas):
    ruta_archivo = os.path.join(descargas, archivo)
    
    # Solo procesamos archivos, ignoramos carpetas
    if os.path.isfile(ruta_archivo):
        nombre, extension = os.path.splitext(archivo)
        ext = extension.lower()
        
        movido = False
        for categoria, extensiones in CATEGORIAS.items():
            if ext in extensiones:
                # Crear la carpeta de la categoría si no existe
                ruta_destino = os.path.join(descargas, categoria)
                if not os.path.exists(ruta_destino):
                    os.makedirs(ruta_destino)
                
                # Mover el archivo
                shutil.move(ruta_archivo, os.path.join(ruta_destino, archivo))
                print(f"[OK] {archivo} -> {categoria}")
                movido = True
                break
        
        if not movido:
            print(f"[OMITIDO] {archivo} (Sin categoría)")

print("-" * 30)
print("SISTEMA ORGANIZADO.")