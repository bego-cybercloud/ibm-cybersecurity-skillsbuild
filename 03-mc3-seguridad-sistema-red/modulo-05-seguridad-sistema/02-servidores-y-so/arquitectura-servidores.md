# 🏗️ Arquitectura de Servidores y Sistema Operativo

**Cliente:** Capital Ink Publishing
**Proyecto:** Modernización de Infraestructura Segura
**Estándar:** Linux Hardening / RHCSA Best Practices

## 1. Selección del Sistema Operativo (SO)
Tras evaluar Windows Server y Linux, se ha seleccionado **Linux (Red Hat Enterprise / Ubuntu Server)** como base para la infraestructura crítica.

### 📝 Justificación Técnica:
1.  **Seguridad del Kernel:** Linux permite una gestión granular de permisos y módulos de seguridad (SELinux/AppArmor).
2.  **Gestión de Paquetes:** Actualizaciones centralizadas y auditoría de software más eficiente que en entornos Windows.
3.  **Eficiencia:** Ausencia de GUI (Interfaz Gráfica) en servidores de producción reduce la superficie de ataque y consumo de recursos.
4.  **Costes:** Reducción de licencias propietarias en favor de soluciones Open Source empresariales.

## 2. Roles de Servidores Definidos
[cite_start]Basado en el análisis de necesidades, se implementarán los siguientes tipos de servidores[cite: 57, 58, 63, 79]:

| Rol del Servidor | Función Crítica | Medida de Seguridad Clave |
| :--- | :--- | :--- |
| **Servidor Web (Nginx/Apache)** | Alojamiento del portal corporativo y e-commerce. | Deshabilitar banners de versión y módulos innecesarios. |
| **Servidor Proxy Inverso** | Intermediario entre Internet y la red interna. | Filtrado de tráfico y ocultación de la IP real de los servidores backend. |
| **Servidor de Base de Datos** | Almacenamiento de inventario y clientes. | Aislamiento en subred privada (sin acceso directo a Internet). |
| **Servidor de Monitoreo** | Centralización de Logs y Alertas (SIEM). | Auditoría de accesos y detección de anomalías en tiempo real. |

## 3. Política de Usuarios y Grupos (Estándar RHCSA)
Para cumplir con el principio de "Mínimo Privilegio", se define la siguiente estructura:

* **Usuario Root:** Acceso deshabilitado por SSH. Solo acceso vía consola física o `sudo`.
* **Grupo `sysadmin`:** Permisos de administración completos vía `sudo`.
* **Grupo `developers`:** Acceso limitado solo a directorios `/var/www/html` (Web).
* **Grupo `audit`:** Permisos de solo lectura en `/var/log` para revisión de incidentes.

---
*Documento aprobado por el equipo de Ciberseguridad de Capital Ink.*
