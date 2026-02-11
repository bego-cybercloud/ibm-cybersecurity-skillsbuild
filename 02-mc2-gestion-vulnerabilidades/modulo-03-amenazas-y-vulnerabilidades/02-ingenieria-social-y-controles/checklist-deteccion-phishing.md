# 🎣 Checklist de Detección de Ingeniería Social y Phishing

**Propósito:** Guía de verificación para empleados y equipo de seguridad para identificar intentos de compromiso mediante manipulación psicológica.

## 1. Análisis de Correos Electrónicos (Phishing / Spear Phishing)
Para cada correo sospechoso, verificar los siguientes indicadores de compromiso (IoC):

- [ ] **Remitente Incongruente:** ¿El nombre dice "Soporte IT" pero el correo es `usuario123@gmail.com`?
- [ ] **Urgencia Fabricada:** ¿El asunto exige acción inmediata ("Su cuenta será borrada en 24h")?
- [ ] **Enlaces Enmascarados:** Al pasar el ratón por encima del link (sin hacer clic), ¿la URL coincide con el destino real?
- [ ] **Solicitud de Credenciales:** ¿Pide usuario y contraseña en un formulario externo? (Nunca legítimo).
- [ ] **Adjuntos Peligrosos:** ¿Contiene archivos `.exe`, `.scr`, `.vbs` o `.docm` (con macros)?

## 2. Prevención de Spear Phishing (Ataques Dirigidos)
- [ ] **Datos Personales:** ¿El correo menciona datos específicos (cargo, nombre del jefe) que podrían haberse obtenido de redes sociales (OSINT)?
- [ ] **Verificación Out-of-Band:** Si un directivo pide una transferencia urgente por email, ¿se ha confirmado por llamada telefónica antes de actuar?

## 3. Seguridad Física y Humana (Tailgating)
- [ ] **Control de Acceso:** ¿Se ha verificado que nadie entre "aprovechando la puerta abierta" detrás de un empleado autorizado?
- [ ] **Política de Escritorio Limpio:** ¿Hay contraseñas escritas en post-its visibles a visitas externas?

---
*Documento de referencia interna basado en vectores de ataque de ingeniería social.*
