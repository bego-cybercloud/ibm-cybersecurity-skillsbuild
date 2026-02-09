# ============================================================
# Herramienta: Configuración de Servidor Seguro
# Cliente: Capital Ink 
# Autor:   Begoña Ortiz | Rol: Security Analyst @ BlueCore
# Descripción: Crea carpetas y define permisos (Mínimo Privilegio).
# ============================================================

import os

def crear_carpeta(ruta, permiso, descripcion):
    print(f"📂 Procesando: {descripcion}...")
    
    # Crear la carpeta si no existe
    if not os.path.exists(ruta):
        try:
            os.makedirs(ruta)
            print(f"   > Carpeta creada: {ruta}")
        except OSError:
            print(f"   > Error creando carpeta")
    
    # En un servidor real, aquí usaríamos os.chmod(ruta, permiso)
    # Como es una simulación en el propio PC, solo imprimimos la acción de seguridad.
    permiso_octal = oct(permiso)[-3:]
    print(f"   🔒 Permisos aplicados: {permiso_octal} (Simulado)")

# --- Ejecución ---
if __name__ == "__main__":
    raiz = "capital_ink_server"
    
    print("--- BlueCore: Iniciando Aprovisionamiento ---")
    
    # 1. Carpeta Pública (Web) - 755 (Todos leen, solo dueño escribe)
    crear_carpeta(f"{raiz}/public_html", 0o755, "Servidor Web Público")
    
    # 2. Carpeta Logs - 740 (Dueño todo, Grupo lee, Otros nada)
    crear_carpeta(f"{raiz}/logs", 0o740, "Registros de Auditoría")
    
    # 3. Carpeta Privada - 700 (Solo el dueño entra)
    crear_carpeta(f"{raiz}/privado", 0o700, "Base de Datos Confidencial")
    
    print("--- Estructura creada exitosamente ---")
