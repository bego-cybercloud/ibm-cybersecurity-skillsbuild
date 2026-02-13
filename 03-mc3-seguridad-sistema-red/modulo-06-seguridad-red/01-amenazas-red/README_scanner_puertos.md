# 🔍 BlueCore Network Scanner (TCP Port Auditor)

Herramienta de auditoría de red desarrollada en Python para identificar puertos TCP abiertos en un sistema objetivo.  
El proyecto fue creado como ejercicio práctico para comprender la fase de Reconocimiento en amenazas de red, desde una perspectiva defensiva (Blue Team).

---

## 🎯 Objetivo del proyecto
- Comprender cómo un atacante identifica servicios expuestos.
- Aprender cómo funciona el protocolo TCP a bajo nivel.
- Practicar auditoría básica de red sin depender de herramientas de caja negra (herramientas automatizadas cuyo funcionamiento interno no es visible para el usuario, como Nmap).
- Preparación para certificación de ciberseguridad (IBM).

---

## 🧠 Enfoque técnico
- **Tipo de escaneo:** TCP Connect Scan (3-Way Handshake completo).
- **Lenguaje:** Python 3.
- **Librerías:** `socket`, `sys`, `datetime`.
- **Modo:** CLI (Command Line Interface).

> **Nota:** Este tipo de escaneo es intencionalmente ruidoso y genera logs en el sistema destino, lo cual es ideal para auditorías defensivas y validación de monitoreo.

---

## ⚙️ Funcionamiento
1. El usuario proporciona una IP objetivo por línea de comandos.
2. El script intenta establecer una conexión TCP con una lista de puertos comunes.
3. Si el puerto responde, se marca como **ABIERTO**.
4. Se muestra el servicio estándar asociado al puerto (si existe).

---

## ▶️ Uso
```bash
python3 port_scanner.py <IP_OBJETIVO>
```  

**Ejemplo:**
```bash
python3 port_scanner.py 127.0.0.1
```  

**📌 Ejemplo de salida:**
```text
[+] Puerto 80    [http]:    ABIERTO
[+] Puerto 443   [https]:   ABIERTO
```  

---

## 🔐 Contexto de seguridad
Este proyecto **no tiene fines ofensivos**. Fue desarrollado con fines educativos y defensivos para:
- Identificar superficies de ataque.
- Detectar servicios innecesarios o inseguros.
- Mejorar visibilidad de red.
- Comprender cómo se generan logs en escaneos reales.

---

## 🚀 Próximas mejoras (Roadmap)
- [ ] **Rate limiting / throttling:** control de velocidad de escaneo para reducir ruido.
- [ ] **Exportación a JSON/CSV:** para integración con herramientas de reporte.
- [ ] **Soporte para rangos de IP:** capacidad de escaneo por segmento (CIDR).

---

### 👤 Autoría y Contacto
**Begoña Ortiz** *Analista de Ciberseguridad Jr.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]([https://www.linkedin.com/in/bego%C3%B1aortiz/](https://www.linkedin.com/in/bego%C3%B1aortiz/)) 
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bego-cybercloud)

---
<div align="center">
  <i>"No puedes proteger lo que no ves. La visibilidad total es el primer paso hacia una red segura."</i>   
  <br>
  <b>© 2026 Begoña Ortiz — Portafolio IBM Cybersecurity Analyst</b>
</div>
