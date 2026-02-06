import hashlib
import sys

def verificar_hash_firmware(ruta_archivo, hash_esperado):
    """
    Simula la verificación de integridad de un archivo de firmware
    comparando su hash SHA-256 real con el oficial del fabricante.
    """
    print(f"🔍 Analizando firmware: {ruta_archivo}...")
    
    # En un caso real, aquí leeríamos el archivo binario.
    # Para la simulación, usaremos un string dummy.
    sha256_hash = hashlib.sha256()
    
    # Simulamos que leemos el archivo
    contenido_simulado = b"Firmware-Capital-Ink-v2.0" 
    sha256_hash.update(contenido_simulado)
    
    hash_calculado = sha256_hash.hexdigest()
    
    print(f"🧮 Hash Calculado: {hash_calculado}")
    print(f"📝 Hash Esperado:  {hash_esperado}")
    
    if hash_calculado == hash_esperado:
        print("\n✅ INTEGRIDAD VERIFICADA: El firmware es seguro para instalar.")
    else:
        print("\n❌ ALERTA DE SEGURIDAD: El hash no coincide. El archivo podría estar corrupto o infectado.")

# Ejemplo de uso (Simulación)
if __name__ == "__main__":
    # Hash SHA-256 de "Firmware-Capital-Ink-v2.0"
    hash_oficial = "0a501e5b9875883842c867252069818823184518d8440263f69e63a18e00192e"
    # Ejecutamos con un hash incorrecto para probar la alerta
    verificar_hash_firmware("update_router_v2.bin", "99999999999999999999999999999999")
