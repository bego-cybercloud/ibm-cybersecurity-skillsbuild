#!/bin/bash

# ==========================================
# Script de Aprovisionamiento Seguro - Capital Ink
# Autor: Begoña Ortiz (Security Analyst)
# Descripción: Crea la estructura de directorios segura y asigna permisos
# basados en roles (Simulación de prácticas RHCSA).
# ==========================================

echo "⚙️  Iniciando configuración de estructura de servidores..."

# 1. Definir rutas base para la simulación
BASE_DIR="./capital_ink_server"
WEB_DIR="$BASE_DIR/var/www/html"
LOG_DIR="$BASE_DIR/var/log/security"
CONFIDENTIAL_DIR="$BASE_DIR/opt/datos_privados"

# 2. Crear directorios (simulando un servidor real)
echo "📂 Creando directorios corporativos..."
mkdir -p "$WEB_DIR"
mkdir -p "$LOG_DIR"
mkdir -p "$CONFIDENTIAL_DIR"

# 3. Crear archivos de prueba
touch "$WEB_DIR/index.html"
touch "$LOG_DIR/access.log"
touch "$CONFIDENTIAL_DIR/nominas.db"

# 4. Asignación de Permisos (Hardening)
# La parte más crítica de la administración de sistemas Linux

echo "🔒 Aplicando políticas de permisos (Principio de Mínimo Privilegio)..."

# A. Directorio Web: 755 (Dueño: RWX, Grupo: RX, Otros: RX)
# Permite que el servidor lea los archivos, pero solo el admin los modifique.
chmod 755 "$WEB_DIR"
echo "   [OK] Permisos Web establecidos a 755 (Público Lectura/Ejecución)."

# B. Directorio de Logs: 740 (Dueño: RWX, Grupo: R, Otros: Nada)
# Solo el sistema escribe, los auditores leen, nadie más entra.
chmod 740 "$LOG_DIR"
echo "   [OK] Permisos Logs establecidos a 740 (Restringido)."

# C. Datos Confidenciales: 700 (Dueño: RWX, Grupo: Nada, Otros: Nada)
# EXCLUSIVO para el dueño (root/admin). Nadie más puede ver que existe.
chmod 700 "$CONFIDENTIAL_DIR"
echo "   [OK] Permisos Confidenciales establecidos a 700 (TOTALMENTE PRIVADO)."

echo "✅ Aprovisionamiento completado exitosamente."
echo "   Estructura creada en: $BASE_DIR"
