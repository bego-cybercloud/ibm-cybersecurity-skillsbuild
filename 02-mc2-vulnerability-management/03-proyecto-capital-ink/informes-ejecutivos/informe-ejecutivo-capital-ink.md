# 📊 Informe Ejecutivo de Ciberseguridad: Proyecto Capital Ink

**Para:** Junta Directiva / CISO de Capital Ink Publishing
**De:** Begoña Ortiz, Analista de Seguridad (Consultor Externo)
**Fecha:** 05 de Febrero de 2026
**Asunto:** Resultados de la Auditoría de Vulnerabilidades Web y Plan de Mitigación

---

## 1. Resumen Ejecutivo
A petición de la dirección de **Capital Ink**, se ha realizado una evaluación de seguridad integral sobre la infraestructura web de la editorial. El objetivo principal ha sido identificar brechas que pudieran comprometer la propiedad intelectual de las publicaciones y los datos de los suscriptores.

**Conclusión General:** La postura de seguridad actual presenta un **Riesgo ALTO**. Se han detectado vulnerabilidades críticas que permitirían a un atacante externo robar la base de datos completa o alterar el contenido del sitio web sin autorización.

## 2. Metodología Utilizada
Para esta auditoría se siguieron estándares internacionales de industria:
* **Escaneo Dinámico (DAST):** Uso de **OWASP ZAP** para simular ataques reales contra la aplicación web.
* **Puntuación de Riesgo:** Aplicación del estándar **CVSS v3.1** para priorizar los hallazgos según su gravedad matemática.
* **Marco de Referencia:** Alineación con controles **GDPR** (Protección de Datos) y **OWASP Top 10**.

## 3. Hallazgos Críticos y Análisis de Impacto
Se identificaron 3 vulnerabilidades principales que requieren acción inmediata:

### A. Inyección SQL (SQLi) - *Criticidad: CRÍTICA (CVSS 9.8)*
* **El Problema:** El formulario de acceso permite manipular la base de datos.
* **Impacto de Negocio:** Robo masivo de credenciales de clientes y posible eliminación de archivos literarios (Ransomware/Sabotaje).
* **Consecuencia Legal:** Multas severas por incumplimiento del GDPR (fuga de datos personales).

### B. Cross-Site Scripting (XSS) - *Criticidad: ALTA (CVSS 7.2)*
* **El Problema:** Los atacantes pueden inyectar scripts en los comentarios del blog.
* **Impacto de Negocio:** Redirección de usuarios a sitios de phishing, dañando la reputación de marca de Capital Ink.

### C. Ausencia de Cifrado (HTTP) - *Criticidad: MEDIA (CVSS 5.4)*
* **El Problema:** Los datos viajan en texto plano.
* **Impacto de Negocio:** Intercepción de contraseñas en redes Wi-Fi públicas.

## 4. Recomendaciones Estratégicas
Se solicita la aprobación inmediata de los siguientes recursos para mitigar los riesgos:

1.  **Corrección de Código (Inmediato):** Asignar al equipo de desarrollo la implementación de "Consultas Preparadas" para cerrar la brecha de SQL Injection.
2.  **Certificación de Seguridad (Corto Plazo):** Adquisición e implementación de certificados SSL/TLS para cifrar todas las comunicaciones (HTTPS).
3.  **Cultura de Seguridad (Continuo):** Iniciar campaña de concienciación contra Phishing para empleados administrativos.

---
*Fin del Informe. Documento generado bajo simulación de auditoría profesional.*
