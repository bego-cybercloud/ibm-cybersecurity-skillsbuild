🛡️ SUITE DE AUDITORÍA DE RED Y SIMULACIÓN DE AMENAZAS

Versión: 1.3 (Enterprise Ready)
Analista: Begoña Ortiz | Junior Cybersecurity Analyst

Certificación: IBM Cybersecurity Analyst Professional Certificate

📋 Resumen Ejecutivo

Esta "Suite" es un conjunto de herramientas programadas en Python que permiten gestionar la seguridad de una red empresarial en dos fases críticas:

1. Reconocimiento: Identificar "puertas abiertas" (puertos) por donde podría entrar un atacante.
2. Simulación: Probar la resistencia de la empresa ante 12 tipos de ataques reales y definir cómo detenerlos.

🚀 Herramienta 1: Sistema de Simulación de Amenazas

¿Qué es? Es un simulador que permite a una empresa entrenar a su personal o probar sus protocolos sin ponerse en riesgo real. Recrea el comportamiento de 12 ataques (como el robo de datos por Bluetooth o la caída de servidores por exceso de tráfico).

💡 Guía de uso para no técnicos (Paso a paso):

- Arranque: En la terminal, escribimos python3 simulador_amenazas.py.
- Interfaz: Aparecerá un menú profesional con 12 opciones numeradas.
- Ejecución: Si eliges una opción (ej. el número 3 para "Man-in-the-Middle"), verás cómo el sistema explica qué está haciendo el atacante.
- Resultado: El programa no solo "ataca", sino que entrega una solución técnica (Mitigación) basada en estándares internacionales (NIST/ISO).
- Evidencia: Al terminar, el sistema guarda un informe automático llamado simulador_amenazas.log que sirve como prueba de la auditoría realizada.
- Visualización del Informe: Para leer los resultados de la auditoría en pantalla, simplemente escribe: cat simulador_amenazas.log
  (Esto abrirá el "cuaderno de bitácora" donde se detalla cada prueba realizada con su fecha y hora exacta).

🔍 Herramienta 2: BlueCore Network Scanner

¿Qué es? Es un "auditor de puertas". Antes de que un atacante intente entrar, esta herramienta revisa qué servicios de la empresa están expuestos a internet.

💡 Guía de uso para no técnicos (Paso a paso):

- Arranque: Se usa escribiendo python3 port_scanner.py seguido de la dirección IP que queremos revisar (ej: 127.0.0.1).
- Funcionamiento: El programa toca a la "puerta" de cada servicio. Si alguien responde, el programa nos avisa que ese puerto está ABIERTO.
- Valor para la empresa: Permite cerrar servicios innecesarios antes de que un hacker los encuentre.

📂 Inventario de Archivos (Estructura del Proyecto)

- simulador_amenazas.py: El motor inteligente de la suite.
- simulador_amenazas.log: El historial de seguridad (muy importante para cumplimiento legal).
- port_scanner.py: La herramienta de escaneo y visibilidad.
- README.md: Este manual de uso (Portada principal).
- README_scanner_puertos.md: Manual técnico detallado del escáner.

👤 Autoría y Contacto

Begoña Ortiz — Analista de Ciberseguridad Junior

<div align="center">
<i>"La resiliencia de una red no reside en la ausencia de ataques, sino en la capacidad técnica para detectarlos y la rapidez para mitigarlos. La visibilidad total es el primer paso hacia una defensa infranqueable."</i>
<b>© 2026 Begoña Ortiz — Portafolio IBM Cybersecurity Analyst</b>
<span>Especialización: Auditoría de Redes y Respuesta ante Incidentes</span>
</div>
