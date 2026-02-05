# Política de Copias de Seguridad (Backup Policy) – Módulo 1

## 1. Objetivo
Garantizar la disponibilidad y recuperación de datos ante incidentes (borrado accidental, ransomware, fallos de hardware).

## 2. Alcance
Aplica a:
- Datos corporativos
- Datos sensibles (PII)
- Configuraciones críticas (sistemas y aplicaciones)

## 3. Estrategia (Regla 3-2-1)
- **3 copias** de los datos (1 principal + 2 copias)
- **2 soportes** distintos (por ejemplo: disco local + almacenamiento externo)
- **1 copia** fuera de la ubicación principal (offsite) o inmutable (concepto)

## 4. Frecuencia y Retención (ejemplo corporativo)
- Copia **diaria incremental**
- Copia **semanal completa**
- Retención: **30 días** (ajustable según negocio y normativa)

## 5. Seguridad de Backups
- Backups **cifrados**
- Acceso restringido (solo roles autorizados)
- Registro de ejecuciones (logs de backup)
- Protección contra borrado (inmutabilidad / WORM, concepto)

## 6. Pruebas de restauración (lo que muchos olvidan)
- Realizar **prueba de restauración mensual** (mínimo):
  - Verificar integridad
  - Verificar tiempos de recuperación (RTO)
  - Documentar resultados

## 7. Resultado esperado
Se minimiza el impacto ante pérdida de datos y se garantiza continuidad operativa.
