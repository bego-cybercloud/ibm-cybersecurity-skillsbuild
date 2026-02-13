# 🛡️ SUITE DE AUDITORÍA DE RED Y SIMULACIÓN DE AMENAZAS

**Versión:** 1.3 (Enterprise Ready)  
**Analista:** Begoña Ortiz | Junior Cybersecurity Analyst  
**Certificación:** IBM Cybersecurity Analyst Professional Certificate 

---

## 📋 Resumen Ejecutivo

Esta suite es un conjunto de herramientas desarrolladas en Python para gestionar la seguridad de una red empresarial en dos fases críticas:

- **Reconocimiento:** Identificación de puertos abiertos que podrían ser explotados.
- **Simulación:** Evaluación de la resiliencia ante 12 tipos de ataques reales y definición de sus mitigaciones.

---

## 🚀 Herramienta 1: Sistema de Simulación de Amenazas

### 🔎 ¿Qué es?

Simulador diseñado para entrenar personal y validar protocolos de seguridad sin riesgo real.  
Recrea el comportamiento de 12 ataques comunes (ej. Man-in-the-Middle, exfiltración Bluetooth, DoS).

### 💡 Guía de uso (Paso a paso)

1. **Arranque**
   ```bash
   python3 simulador_amenazas.py
   ```

- Interfaz: Menú interactivo con 12 escenarios numerados.
- Ejecución: Seleccionar el número del ataque (ej. 3 para Man-in-the-Middle).
- Resultado: Explicación técnica del ataque y mitigación basada en estándares internacionales (NIST / ISO 27001).
- Evidencia: Se genera automáticamente simulador_amenazas.log
- Visualización del informe: cat simulador_amenazas.log

## 🔍 Herramienta 2: BlueCore Network Scanner


### 🔎 ¿Qué es?


Escáner de puertos diseñado para identificar servicios expuestos antes de que lo haga un atacante.

### 💡 Guía de uso (Paso a paso)

1. **Arranque**
   ```bash
   python3 port_scanner.py 127.0.0.1
   ```
    Funcionamiento

        Detecta puertos abiertos.

        Informa servicios potencialmente expuestos.

    Valor Empresarial

        Permite reducir superficie de ataque.

        Mejora postura de seguridad preventiva.


###  📂 Inventario de Archivos

| Archivo | Descripción |
|----------|-------------|
| `simulador_amenazas.py` | Motor principal de simulación |
| `simulador_amenazas.log` | Registro de auditorías |
| `port_scanner.py` | Escáner de puertos |
| `README.md` | Manual principal |
| `README_scanner_puertos.md` | Manual técnico detallado |

## 👤 Autoría y Contacto

**Begoña Ortiz**  
Analista de Ciberseguridad Junior  


> "La resiliencia de una red no reside en la ausencia de ataques, sino en la capacidad técnica para detectarlos y la rapidez para mitigarlos.  
> La visibilidad total es el primer paso hacia una defensa infranqueable."

© 2026 Begoña Ortiz
Portafolio – IBM Cybersecurity Analyst
Especialización: Auditoría de Redes y Respuesta ante Incidentes
