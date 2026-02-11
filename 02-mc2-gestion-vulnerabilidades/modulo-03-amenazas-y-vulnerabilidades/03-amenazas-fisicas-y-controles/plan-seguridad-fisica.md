# 🏢 Plan de Control de Seguridad Física (Defensa en Profundidad)

**Objetivo:** Proteger la infraestructura crítica (Hardware) contra acceso no autorizado, robo y desastres ambientales.
**Estrategia:** Defensa en Profundidad (Múltiples capas de seguridad).

## 1. Capa Perimetral (Exterior)
* **Vigilancia:** Cámaras CCTV con detección de movimiento 24/7 cubriendo todas las entradas y salidas.
* **Iluminación:** Focos activados por movimiento en zonas de carga y descarga para disuadir intrusiones nocturnas.
* **Acceso:** Barreras físicas en el parking y registro obligatorio de matrículas.

## 2. Capa Interna (Edificio y Oficinas)
* **Control de Acceso:** Uso de tarjetas RFID personales. Política de "No Tailgating" (no dejar pasar a nadie detrás sin tarjeta).
* **Recepción:** Personal de seguridad para validación de visitas externas con libro de registro.
* **Estaciones de Trabajo:** Cables de seguridad (Kensington locks) para portátiles en zonas comunes.

## 3. Zona Crítica (Sala de Servidores / Data Center)
Esta zona requiere el nivel máximo de restricción.

### A. Controles de Acceso
* **Autenticación Multifactor (MFA):** Tarjeta inteligente + Pin o Biometría (Huella dactilar) para abrir la puerta del rack.
* **Registro (Logging):** Auditoría automática de quién entra y sale con marca de tiempo.

### B. Controles Ambientales (Protección de Hardware)
* **Climatización (HVAC):** Control de temperatura y humedad constante para evitar sobrecalentamiento de servidores.
* **Supresión de Incendios:** Sistema de gas inerte (FM-200) que apaga el fuego sin dañar los equipos electrónicos (no usar aspersores de agua).
* **Energía:** UPS (Sistema de Alimentación Ininterrumpida) y generador diésel para mantener la disponibilidad ante cortes de luz.

---
*Este plan mitiga riesgos de la Lección 3: Amenazas Físicas y Controles Ambientales.*
