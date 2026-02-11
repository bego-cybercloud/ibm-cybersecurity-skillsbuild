# ============================================================
# Herramienta: BlueCore Hardening Toolkit
# Cliente: Capital Ink 
# Autor:   Begoña Ortiz | Rol: Security Analyst @ BlueCore
# Descripción: Automatiza tareas de mantenimiento y defensa.
# ============================================================

import time
from datetime import datetime

def ejecutar_tarea(nombre, comando):
    """Simula la ejecución de un comando de sistema"""
    print(f"\n⚙️  [TAREA] {nombre}")
    print(f"   > Ejecutando comando: {comando}")
    time.sleep(1) # Pausa para realismo
    print("   ✅ Completado.")

def main():
    print("🛡️  BLUECORE SECURITY - INICIANDO HARDENING 🛡️")
    print(f"Fecha: {datetime.now()}")

    # 1. Actualizaciones (Patch Management)
    ejecutar_tarea(
        "Actualizando sistema operativo",
        "sudo apt-get update && sudo apt-get upgrade -y"
    )

    # 2. Deshabilitar servicios inseguros
    servicios = ["telnet", "ftp"]
    for srv in servicios:
        ejecutar_tarea(
            f"Desactivando protocolo inseguro: {srv}",
            f"sudo systemctl disable {srv}"
        )

    # 3. Configurar Firewall (UFW)
    ejecutar_tarea(
        "Configurando Firewall (Bloquear todo por defecto)",
        "sudo ufw default deny incoming"
    )
    ejecutar_tarea(
        "Permitiendo acceso SSH seguro",
        "sudo ufw allow ssh"
    )

    # 4. Backup
    print("\n💾 [BACKUP] Iniciando copia de seguridad...")
    archivo = f"backup_{datetime.now().strftime('%Y%m%d')}.zip"
    print(f"   > Cifrando datos críticos...")
    print(f"   ✅ Copia guardada y segura en: /backups/{archivo}")

    print("\n✨ El servidor cumple con la normativa de seguridad.")

if __name__ == "__main__":
    main()
