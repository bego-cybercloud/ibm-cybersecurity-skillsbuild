# 🛡️ Protocolo de Seguridad y Auditoría de Firmware

**Cliente:** Capital Ink Publishing
**Responsable:** Begoña Ortiz (Security Analyst)
**Alcance:** Dispositivos de Red, IoT y Periféricos Críticos.
**Versión:** 1.0

## 1. Inventario de Activos y Firmware
Identificación de dispositivos críticos que requieren gestión de firmware para reducir la superficie de ataque.

| Tipo de Dispositivo | Rol en la Red | Tipo de Firmware | Riesgo Asociado |
| :--- | :--- | :--- | :--- |
| **Router Perimetral** | Gateway de salida a Internet | Alto Nivel (OS) | Acceso no autorizado a la red interna, Man-in-the-Middle. |
| **Cámaras de Seguridad** | Vigilancia Física (IoT) | Subsistema / Embebido | Espionaje, Botnets (ej. Mirai), Inyección de video. |
| **Impresoras de Red** | Periféricos de oficina | Subsistema | Robo de documentos confidenciales, Pivoteo lateral. |
| **Servidores** | Infraestructura Core | UEFI / BIOS | Bootkits, Rootkits persistentes, Secure Boot deshabilitado. |

## 2. Matriz de Vulnerabilidades y Mitigación (OWASP Firmware)
Análisis de las debilidades comunes (CWE) detectadas en el entorno.

### 🚨 Vulnerabilidad A: Credenciales por Defecto
* **Descripción:** Dispositivos (especialmente Routers e IoT) que mantienen `admin/admin`.
* **Acción de Mitigación:**
    - [x] Cambiar contraseñas predeterminadas inmediatamente tras la instalación.
    - [x] Implementar frases de contraseña (Passphrases) de +16 caracteres.
    - [x] Deshabilitar acceso WAN al panel de administración.

### 🔓 Vulnerabilidad B: Falta de Cifrado en Tránsito
* **Descripción:** Paneles de administración que usan HTTP en lugar de HTTPS.
* **Acción de Mitigación:**
    - [x] Forzar conexión HTTPS/TLS v1.2 o superior.
    - [x] Deshabilitar servicios inseguros (Telnet, FTP) y usar alternativos (SSH, SFTP).
    - [x] En redes Wi-Fi, migrar de WPA2 a **WPA3** y desactivar **WPS** (riesgo de fuerza bruta).

### 🔄 Vulnerabilidad C: Actualizaciones No Verificadas
* **Descripción:** Riesgo de instalar firmware corrupto o malicioso (Inyección).
* **Acción de Mitigación:**
    - [x] Descargar firmware *solo* de la web oficial del fabricante.
    - [x] Verificar el **Hash (SHA-256)** del archivo antes de instalar.
    - [x] Establecer ciclo de revisión mensual (Primer lunes de cada mes).

## 3. Procedimiento de Actualización Segura
Pasos técnicos para aplicar parches sin comprometer la integridad.

1.  **Backup:** Realizar copia de seguridad de la configuración actual del dispositivo.
2.  **Verificación:** Comprobar versión actual vs. última versión del fabricante.
    * *Ejemplo Router:* Versión actual `1.0.4` -> Nueva `1.0.6` (Parche de seguridad crítico).
3.  **Integridad:** Validar firma digital del archivo `.bin` o `.zip`.
4.  **Despliegue:** Instalar actualización mediante conexión cableada (evitar Wi-Fi para prevenir cortes).
5.  **Hardening:** Tras actualizar, revisar que las configuraciones de seguridad no se hayan reseteado.

---
*Documento basado en las mejores prácticas de seguridad de firmware (NIST / OWASP).*
