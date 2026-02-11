# ============================================================
# Herramienta: BlueCore Network Scanner v2.0
# Autor: Begoña Ortiz (Analista de Seguridad)
# Uso: python3 port_scanner.py <IP_OBJETIVO>
# ============================================================

import socket
import sys
from datetime import datetime

def obtener_servicio(puerto):
    """Intenta adivinar qué servicio corre en ese puerto (Ej: 80 -> http)"""
    try:
        return socket.getservbyport(puerto)
    except:
        return "Desconocido"

def escanear_puertos(objetivo_ip, lista_puertos):
    print("-" * 60)
    print(f"🔍 [BLUECORE] Iniciando escaneo en: {objetivo_ip}")
    print(f"🕒 Hora de inicio: {datetime.now()}")
    print("-" * 60)

    try:
        for puerto in lista_puertos:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            
            resultado = sock.connect_ex((objetivo_ip, puerto))
            
            if resultado == 0:
                # ¡Mejora! Ahora obtenemos el nombre del servicio
                nombre_servicio = obtener_servicio(puerto)
                print(f"   [+] Puerto {puerto:<5} [{nombre_servicio}]: \t ABIERTO 🚨")
            
            sock.close()

    except KeyboardInterrupt:
        print("\n🛑 Escaneo detenido por el usuario.")
        sys.exit()
    except socket.gaierror:
        print("\n❌ Error: No se pudo resolver el nombre del host.")
        sys.exit()
    except socket.error:
        print("\n❌ Error: No se pudo conectar al servidor.")
        sys.exit()

    print("-" * 60)
    print("✅ Escaneo finalizado.")

# --- Ejecución Principal ---
if __name__ == "__main__":
    # ¡MEJORA! Leemos la IP desde la terminal (sys.argv)
    # sys.argv[0] es el nombre del script
    # sys.argv[1] es el primer argumento (la IP)
    
    if len(sys.argv) == 2:
        target = sys.argv[1] # Capturo la IP objetivo directamente desde los argumentos de la consola
        
        # Puertos comunes (Top ports)
        puertos = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
        
        # Validamos que la IP tenga formato correcto 
        try:
            socket.inet_aton(target)
            escanear_puertos(target, puertos)
        except socket.error:
            print("❌ Error: La dirección IP no es válida.")
            
    else:
        # Si no proporciono argumentos, muestro la ayuda automática
        print("\n⚠️  [ERROR] Debes especificar una IP objetivo.")
        print(f"Uso correcto: python3 {sys.argv[0]} <IP_OBJETIVO>")
        print(f"Ejemplo:      python3 {sys.argv[0]} 127.0.0.1\n")
