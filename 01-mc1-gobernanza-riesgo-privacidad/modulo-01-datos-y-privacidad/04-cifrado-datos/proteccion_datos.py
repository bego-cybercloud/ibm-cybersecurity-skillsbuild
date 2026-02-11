import hashlib

# ==========================================
# SIMULADOR DE PROTECCIÓN DE DATOS (Módulo 1)
# Autor: Begoña (Analista de Ciberseguridad en formación)
# Objetivo: Demostrar técnicas básicas de protección de PII y Credenciales
# ==========================================

def generar_hash_contrasena(contrasena_texto_plano):
    """
    Simula el almacenamiento seguro de contraseñas.
    En lugar de guardar el texto real, guardamos una 'huella digital' (Hash).
    Algoritmo usado: SHA-256 (Estándar de la industria).
    """
    # Convertimos el texto a bytes (necesario para el algoritmo)
    bytes_contrasena = contrasena_texto_plano.encode('utf-8')
    # Generamos el hash
    hash_objeto = hashlib.sha256(bytes_contrasena)
    # Devolvemos el resultado en formato hexadecimal (legible)
    return hash_objeto.hexdigest()

def enmascarar_email(email):
    """
    Técnica de 'Data Masking' para proteger PII en logs o reportes.
    Muestra solo los primeros caracteres y oculta el resto.
    """
    try:
        nombre, dominio = email.split('@')
        if len(nombre) > 2:
            # Muestra las 2 primeras letras y oculta el resto con asteriscos
            nombre_oculto = nombre[:2] + "****"
        else:
            nombre_oculto = nombre + "****"
        return f"{nombre_oculto}@{dominio}"
    except ValueError:
        return "Email inválido"

# --- EJECUCIÓN DE LA PRUEBA ---
if __name__ == "__main__":
    print("--- INICIO DE AUDITORÍA DE SEGURIDAD ---\n")

    # 1. Datos sensibles simulados (INPUT)
    usuario_id = "user_001"
    email_real = "cliente.vip@empresa-ejemplo.com"
    password_real = "SuperSecreto2024!"

    print(f"[DATOS ENTRADA] Usuario: {usuario_id}")
    print(f"[RIESGO] Contraseña en texto plano: {password_real}")
    print(f"[RIESGO] Email expuesto: {email_real}")
    
    print("\n... APLICANDO CONTROLES DE CIBERSEGURIDAD ...\n")

    # 2. Aplicación de Controles (PROCESO)
    password_protegida = generar_hash_contrasena(password_real)
    email_protegido = enmascarar_email(email_real)

    # 3. Resultado Seguro (OUTPUT)
    print(f"[SECURE] Contraseña almacenada (SHA-256): {password_protegida}")
    print("Comentario: Si un hacker roba la BD, solo verá este código, no la clave real.")
    
    print(f"\n[PRIVACY] Email para reportes: {email_protegido}")
    print("Comentario: Se protege la identidad (PII) cumpliendo normativas de privacidad.")
    
    print("\n--- FIN DE LA SIMULACIÓN ---")
