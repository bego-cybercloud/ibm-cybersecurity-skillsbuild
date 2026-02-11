# ============================================================
# Herramienta: Verificador de Integridad de Firmware (FIV)
# Cliente: Capital Ink 
# Autor:   Begoña Ortiz | Rol: Security Analyst @ BlueCore
# Descripción: Compara el Hash SHA-256 para evitar malware.
# ============================================================

import hashlib

def verificar_integridad(nombre_archivo, hash_oficial):
    print(f"🔍 Analizando archivo: {nombre_archivo}...")
    
    # Simulamos el contenido del archivo (En entirno real se leería el binario)
    contenido_simulado = f"Datos del firmware {nombre_archivo}".encode()
    
    # Calculamos el hash
    hash_calculado = hashlib.sha256(contenido_simulado).hexdigest()
    
    print(f"   > Hash Calculado: {hash_calculado}")
    print(f"   > Hash Oficial:   {hash_oficial}")
    
    if hash_calculado == hash_oficial:
        print("✅ EL FIRMWARE ES SEGURO. Proceder con instalación.")
    else:
        print("❌ ALERTA: Los hashes no coinciden. Archivo corrupto.")

# --- Ejecución ---
if __name__ == "__main__":
    # Hash ficticio del fabricante
    hash_bueno = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
    
    print("--- Auditoría BlueCore: Inicio ---")
    verificar_integridad("router_v2.bin", hash_bueno)
    print("--- Auditoría Finalizada ---")
