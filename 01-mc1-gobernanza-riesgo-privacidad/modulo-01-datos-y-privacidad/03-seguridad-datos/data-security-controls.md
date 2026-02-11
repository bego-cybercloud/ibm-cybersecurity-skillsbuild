# Controles de Seguridad de Datos (Data Security Controls) – Módulo 1

## 1. Objetivo
Definir controles mínimos para proteger datos corporativos, con especial foco en datos **Restringidos (PII)**, garantizando la **Confidencialidad, Integridad y Disponibilidad (CIA)**.

## 2. Controles de Acceso
- **Principio de mínimo privilegio (PoLP):** acceso estrictamente necesario.
- **RBAC (Role-Based Access Control):** permisos por rol (no por “personas”).
- **MFA:** obligatorio para accesos administrativos y acceso remoto.
- **Revisión de accesos:** revisión periódica (trimestral) y revocación al salir de la empresa.

## 3. Protección de Datos en Aplicaciones y Sistemas
- **Hardening básico:** deshabilitar servicios innecesarios, aplicar configuraciones seguras.
- **Gestión de parches:** actualización regular de SO y aplicaciones.
- **Segmentación:** separar sistemas críticos / bases de datos / usuarios finales.
- **Endpoint protection:** AV/EDR (concepto) y control de ejecución.

## 4. Registro y Auditoría (Logging)
- Registrar accesos a PII y cambios relevantes:
  - Quién accede (usuario/rol)
  - Cuándo (fecha/hora)
  - Qué acción (lectura/escritura/borrado)
  - Resultado (éxito/fallo)
- Los logs deben estar protegidos contra manipulación y con retención definida.

## 5. Minimización y Retención
- **Minimización:** recopilar solo los datos necesarios.
- **Retención:** definir plazos; eliminar datos cuando ya no sean necesarios.
- **Pseudonimización / enmascaramiento:** para reportes y entornos no productivos.

## 6. Resultado esperado
La organización reduce el riesgo de fuga de datos, accesos no autorizados y manipulación, alineándose con buenas prácticas y cumplimiento.
