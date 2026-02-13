import time
import logging
import sys
from dataclasses import dataclass

# --- CONFIGURACIÓN DE AUDITORÍA (LOGS) ---
logging.basicConfig(
    filename="simulador_amenazas.log",
    level=logging.INFO,
    format="%(asctime)s | [AUDITORÍA] | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def print_banner():
    # Diseño corporativo
    print("\n")
    print("="*70)
    print(f"{'CERTIFICACIÓN DE CIBERSEGURIDAD IBM - SISTEMA DE SIMULACIÓN DE AMENAZAS':^70}")
    print("="*70)
    print(f"{'Módulo: Seguridad en la Red (Full Coverage)':^70}")
    print(f"{'Solo Personal Autorizado | System v1.3':^70}")
    print("-" * 70)
    print(f"{'Creado por Begoña Ortiz | Analista de Ciberseguridad Junior':^70}")
    print("-" * 70)
    print("\n")

@dataclass
class Amenaza:
    id: str
    nombre: str
    tipo: str
    descripcion: str
    impacto: str
    defensa: str

    def ejecutar_simulacion(self):
        print("\n" + "-"*70)
        print(f" >> INICIANDO PROTOCOLO DE SIMULACIÓN: {self.nombre}")
        print(f" >> Categoría: {self.tipo}")
        print("-" * 70)
        
        print("\n[+] Cargando vector de ataque...")
        time.sleep(1)
        print(f"[+] Ejecutando: {self.descripcion}")
        time.sleep(1.5)
        print(f"[!] ALERTA DE SEGURIDAD: {self.impacto}")
        time.sleep(1)
        
        print("\n" + "="*70)
        print(f"🛡️  ACCIÓN DE REMEDIACIÓN RECOMENDADA (Mejores Prácticas):")
        print(f"    {self.defensa}")
        print("=" * 70 + "\n")
        
        logging.info(f"Simulacion finalizada: {self.nombre} | Resultado: Mitigacion propuesta")
        input("Presiona ENTER para regresar al panel de control...")

class SistemaSimulacion:
    def __init__(self):
        self.catalogo = [
            # 📌 Ataques a aplicaciones y servicios
            Amenaza("1", "DoS (Denegación de Servicio)", "Disponibilidad", "Inundación de tráfico desde una única fuente.", "Interrupción temporal del servicio.", "Rate Limiting y Firewalls."),
            Amenaza("2", "DDoS (Denegación Distribuida)", "Disponibilidad", "Ataque coordinado desde múltiples botnets.", "Colapso total de la infraestructura.", "Protección Anti-DDoS en la nube (Cloudflare/AWS Shield)."),
            Amenaza("3", "Man-in-the-Middle (MitM)", "Intercepción", "Intercepción activa de comunicaciones.", "Robo de credenciales y datos confidenciales.", "Cifrado TLS/SSL forzado y VPN."),
            Amenaza("4", "Desbordamiento de Búfer", "Aplicación", "Escritura de datos fuera de los límites de memoria.", "Ejecución de código arbitrario o crash del sistema.", "Validación de inputs y protección de memoria (ASLR)."),
            Amenaza("5", "Día Cero (Zero-Day)", "Vulnerabilidad", "Explotación de fallo desconocido por el fabricante.", "Compromiso crítico sin parche disponible.", "Defensa en profundidad y detección de anomalías."),
            
            # 📌 Suplantación e Integridad
            Amenaza("6", "Suplantación de IP (IP Spoofing)", "Autenticación", "Falsificación de la IP de origen en paquetes.", "Evasión de reglas de firewall basadas en IP.", "Filtrado de ingreso/egreso (Ingress/Egress Filtering)."),
            Amenaza("7", "Envenenamiento DNS", "Integridad", "Corrupción de la caché del servidor DNS.", "Redirección de usuarios a sitios maliciosos.", "Implementación de DNSSEC."),
            Amenaza("8", "Suplantación MAC (MAC Spoofing)", "Acceso", "Clonado de dirección física de tarjeta de red.", "Acceso no autorizado a redes filtradas por MAC.", "Seguridad de puertos (Port Security) y NAC."),
            
            # 📌 Ataques inalámbricos
            Amenaza("9", "Gemelo Malvado (Evil Twin)", "Wireless", "Punto de acceso falso con mismo nombre (SSID).", "Robo de credenciales wifi.", "Autenticación robusta (WPA3/802.1X)."),
            Amenaza("10", "Punto de Acceso No Autorizado (Rogue AP)", "Wireless", "Router conectado ilegalmente a la red física.", "Puerta trasera (Backdoor) a la intranet.", "Escaneo de red y bloqueo de puertos de switch."),
            Amenaza("11", "Jamming (Inhibición)", "Disponibilidad", "Interferencia de radiofrecuencia.", "Bloqueo total de la señal Wi-Fi.", "Monitoreo de espectro y sensores WIPS."),
            Amenaza("12", "Bluesnarfing", "Wireless", "Robo de información vía Bluetooth.", "Exfiltración de contactos y mensajes.", "Desactivar visibilidad Bluetooth y emparejamiento seguro.")
        ]

    def ejecutar(self):
        while True:
            print_banner()
            print("SELECCIONE EL VECTOR DE ANÁLISIS (Temario IBM):\n")
            
            print("--- APLICACIONES Y SERVICIOS ---")
            for a in self.catalogo[:5]: print(f" [{a.id}] {a.nombre}")
            
            print("\n--- SUPLANTACIÓN E INTEGRIDAD ---")
            for a in self.catalogo[5:8]: print(f" [{a.id}] {a.nombre}")
            
            print("\n--- ATAQUES INALÁMBRICOS ---")
            for a in self.catalogo[8:]: print(f" [{a.id}] {a.nombre}")
            
            print("\n [0] Cerrar Sesión y Generar Reporte")
            
            opcion = input("\n>> Seleccione opción: ")
            if opcion == "0":
                print("\n[INFO] Sesión finalizada. Registro de auditoría guardado en 'simulador_amenazas.log'.")
                sys.exit()
            
            amenaza = next((a for a in self.catalogo if a.id == opcion), None)
            if amenaza:
                amenaza.ejecutar_simulacion()
            else:
                print("\n[ERROR] Selección no válida.")
                time.sleep(1)

if __name__ == "__main__":
    sim = SistemaSimulacion()
    sim.ejecutar()
