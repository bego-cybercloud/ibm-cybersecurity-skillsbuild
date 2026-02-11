# 🛠️ Matriz de Selección de Herramientas de Seguridad

**Contexto:** Guía técnica para la selección de herramientas de evaluación y defensa según el vector de ataque.

## 📊 Tabla Comparativa

| Herramienta | Categoría | Tipo de Análisis | Objetivo Principal | Fase del Ciclo |
| :--- | :--- | :--- | :--- | :--- |
| **OWASP ZAP** | DAST (Dynamic Application Security Testing) | Caja Negra (Black Box) | Encontrar fallos en Aplicaciones Web (SQLi, XSS) | Evaluación / Pentesting |
| **Malwarebytes** | EDR / Endpoint Security | Heurístico y Firmas | Detectar y poner en cuarentena Malware/Ransomware en dispositivos locales | Detección / Respuesta |
| **AdwCleaner** | Utilidad de Limpieza | Escaneo bajo demanda | Eliminar PUPs (Programas No Deseados) y Adware | Higiene / Mantenimiento |
| **IBM X-Force** | Threat Intelligence | OSINT / Feeds | Obtener reputación de IPs, Hashes y puntajes CVSS | Investigación / Inteligencia |

## 💡 Casos de Uso (Playbook)

### Caso A: "La web corporativa va lenta y muestra errores extraños"
* **Herramienta:** OWASP ZAP.
* **Acción:** Ejecutar un escaneo automatizado para detectar vulnerabilidades de inyección o configuración.

### Caso B: "El ordenador de Finanzas tiene pop-ups de publicidad"
* **Herramienta:** AdwCleaner + Malwarebytes.
* **Acción:** Limpieza profunda de Adware y verificación de troyanos residentes.

### Caso C: "Hemos detectado una IP sospechosa en los logs: 192.168.x.x"
* **Herramienta:** IBM X-Force Exchange.
* **Acción:** Consultar la reputación de la IP para ver si pertenece a una Botnet conocida.

---
*Matriz basada en el stack tecnológico del curso IBM Cybersecurity Analyst.*
