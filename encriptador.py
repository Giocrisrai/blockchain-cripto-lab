"""
encriptador.py — Cifrado simétrico AES-256 con PyCryptodome
============================================================
BCY0010 · Fundamentos de Blockchain
EA1 · Act 1.1 · Encriptador simple y compraventa
IL1.1 · IL1.2

Descripción:
    Programa de línea de comandos que cifra y descifra archivos
    de texto plano (máximo 1 KB) utilizando AES-256 en modo CBC.

Uso:
    python encriptador.py cifrar <archivo.txt>
    python encriptador.py descifrar <archivo.enc>

Autor: Sebastián Tralma
Fecha: 14/03/2026
"""

# ──────────────────────────────────────────────────────────────
# IMPORTACIONES
# ──────────────────────────────────────────────────────────────
# Módulos de PyCryptodome para cifrado simétrico
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Módulos estándar de Python
import os
import sys

# Constantes
TAMANIO_LLAVE = 32          # 32 bytes = 256 bits (AES-256)
TAMANIO_BLOQUE = AES.block_size  # 16 bytes
TAMANIO_MAX_ARCHIVO = 1024  # 1 KB máximo
ARCHIVO_LLAVE = "secret.key"


# ──────────────────────────────────────────────────────────────
# FUNCIONES
# ──────────────────────────────────────────────────────────────

def generar_llave():
    """
    Genera una llave AES-256 criptográficamente segura y la guarda
    en un archivo. Si el archivo ya existe, carga la llave existente.

    Returns:
        bytes: Llave AES de 32 bytes.

    Conceptos clave:
        - get_random_bytes() usa el CSPRNG del sistema operativo.
        - Nunca uses random.randint() para generar llaves criptográficas.
        - La llave debe tener exactamente 32 bytes para AES-256.
    """
    if os.path.exists(ARCHIVO_LLAVE):
        with open(ARCHIVO_LLAVE, "rb") as f:
            key = f.read()
        print("  Llave cargada desde 'secret.key'")
        return key
    else:
        key = get_random_bytes(TAMANIO_LLAVE)
        with open(ARCHIVO_LLAVE, "wb") as f:
            f.write(key)
        print("  Nueva llave generada y guardada")
        return key


def cifrar_archivo(ruta_archivo, key):
    """
    Cifra un archivo de texto plano usando AES-256 en modo CBC.

    Args:
        ruta_archivo (str): Ruta al archivo de texto plano.
        key (bytes): Llave AES de 32 bytes.

    Returns:
        tuple: (iv, cyphertext)
            - iv (bytes): Vector de inicialización de 16 bytes.
            - cyphertext (bytes): Texto cifrado.

    Raises:
        ValueError: Si el archivo excede 1 KB.
        FileNotFoundError: Si el archivo no existe.

    Proceso:
        1. Leer el archivo de texto plano.
        2. Validar que no exceda 1 KB.
        3. Convertir el texto a bytes (UTF-8).
        4. Crear un cifrador AES en modo CBC (genera IV automáticamente).
        5. Aplicar padding al texto (múltiplo de 16 bytes).
        6. Cifrar el texto con padding.
        7. Retornar el IV y el cyphertext.
    """
    # Paso 1: Leer el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        plaintext = f.read()

    # Paso 2: Validar tamaño
    if len(plaintext.encode("utf-8")) > TAMANIO_MAX_ARCHIVO:
        raise ValueError(f"El archivo excede el tamaño máximo de {TAMANIO_MAX_ARCHIVO} bytes (1 KB)")

    # Paso 3: Convertir a bytes
    plaintext_bytes = plaintext.encode("utf-8")

    # Paso 4: Crear el cifrador AES en modo CBC
    cipher = AES.new(key, AES.MODE_CBC)

    # Paso 5: Aplicar padding
    padded_data = pad(plaintext_bytes, TAMANIO_BLOQUE)

    # Paso 6: Cifrar
    cyphertext = cipher.encrypt(padded_data)

    # Paso 7: Obtener el IV y retornar
    if cipher is None or cyphertext is None:
        print(" No se pudo cifrar. Completa los TODO en cifrar_archivo().")
        return None, None

    iv = cipher.iv

    # Información para el usuario
    print(f"  Texto original:  {len(plaintext)} caracteres")
    print(f"  IV ({len(iv)} bytes):     {iv.hex()}")
    print(f"  Cyphertext:      {len(cyphertext)} bytes")
    print(f"  Cyphertext (hex): {cyphertext.hex()[:64]}...")

    return iv, cyphertext


def descifrar(iv, cyphertext, key):
    """
    Descifra un texto cifrado usando AES-256 en modo CBC.

    Args:
        iv (bytes): Vector de inicialización (16 bytes).
        cyphertext (bytes): Texto cifrado.
        key (bytes): Llave AES de 32 bytes (la misma usada para cifrar).

    Returns:
        str: Texto plano descifrado.

    Proceso:
        1. Crear un descifrador AES con la misma llave e IV.
        2. Descifrar el cyphertext.
        3. Remover el padding.
        4. Convertir de bytes a string (UTF-8).
    """
    # TODO: Paso 1 — Crear descifrador usando AES.new(key, AES.MODE_CBC, iv=iv)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # TODO: Paso 2 — Descifrar usando cipher.decrypt(cyphertext)
    padded_plaintext = cipher.decrypt(cyphertext)

    # TODO: Paso 3 — Remover padding usando unpad(padded_plaintext, TAMANIO_BLOQUE)
    plaintext_bytes = unpad(padded_plaintext, TAMANIO_BLOQUE)

    # TODO: Paso 4 — Decodificar de bytes a string con .decode("utf-8")
    plaintext = plaintext_bytes.decode("utf-8")

    if plaintext is None:
        print("  ❌ No se pudo descifrar. Completa los TODO en descifrar().")
        return None

    print(f"  Texto descifrado: {len(plaintext)} caracteres")

    return plaintext


def guardar_cifrado(archivo_salida, iv, cyphertext):
    """
    Guarda el IV y el cyphertext en un solo archivo binario.

    Formato del archivo: [IV (16 bytes)] + [cyphertext (N bytes)]

    Args:
        archivo_salida (str): Ruta del archivo de salida.
        iv (bytes): Vector de inicialización.
        cyphertext (bytes): Texto cifrado.
    """
    with open(archivo_salida, "wb") as f:
        f.write(iv + cyphertext)
    print(f"  Archivo cifrado guardado en: '{archivo_salida}'")


def cargar_cifrado(archivo_cifrado):
    """
    Lee un archivo cifrado y separa el IV del cyphertext.

    Args:
        archivo_cifrado (str): Ruta del archivo .enc

    Returns:
        tuple: (iv, cyphertext)
    """
    with open(archivo_cifrado, "rb") as f:
        data = f.read()

    iv = data[:TAMANIO_BLOQUE]       # Primeros 16 bytes = IV
    cyphertext = data[TAMANIO_BLOQUE:]  # El resto = cyphertext

    print(f"  IV leído:        {iv.hex()}")
    print(f"  Cyphertext:      {len(cyphertext)} bytes")

    return iv, cyphertext


# ──────────────────────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ──────────────────────────────────────────────────────────────

def main():
    """
    Punto de entrada del programa.

    Uso:
        python encriptador.py cifrar <archivo.txt>
        python encriptador.py descifrar <archivo.enc>
    """
    if len(sys.argv) < 3:
        print("╔══════════════════════════════════════════════════════════╗")
        print("║  Encriptador AES-256 · BCY0010 · Act 1.1               ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║  Uso:                                                   ║")
        print("║    python encriptador.py cifrar   <archivo.txt>         ║")
        print("║    python encriptador.py descifrar <archivo.enc>        ║")
        print("╚══════════════════════════════════════════════════════════╝")
        sys.exit(1)

    accion = sys.argv[1].lower()
    archivo = sys.argv[2]

    if accion == "cifrar":
        print(f"\n Cifrando '{archivo}'...")
        print("─" * 40)

        # Generar o cargar llave
        key = generar_llave()
        if key is None:
            print("Error: La función generar_llave() retornó None.")
            print("   Completa los TODO en la función generar_llave().")
            sys.exit(1)

        # Cifrar el archivo
        try:
            iv, cyphertext = cifrar_archivo(archivo, key)
        except Exception as e:
            print(f"Error al cifrar: {e}")
            sys.exit(1)

        if cyphertext is None:
            print("Error: La función cifrar_archivo() retornó None.")
            print("   Completa los TODO en la función cifrar_archivo().")
            sys.exit(1)

        # Guardar archivo cifrado
        archivo_salida = archivo + ".enc"
        guardar_cifrado(archivo_salida, iv, cyphertext)
        print("─" * 40)
        print("Cifrado completado exitosamente.\n")

    elif accion == "descifrar":
        print(f"\n Descifrando '{archivo}'...")
        print("─" * 40)

        # Cargar llave
        if not os.path.exists(ARCHIVO_LLAVE):
            print(f"Error: No se encontró el archivo de llave '{ARCHIVO_LLAVE}'.")
            print("   Necesitas la misma llave usada para cifrar.")
            sys.exit(1)

        key = generar_llave()

        # Leer archivo cifrado
        iv, cyphertext = cargar_cifrado(archivo)

        # Descifrar
        try:
            texto = descifrar(iv, cyphertext, key)
        except Exception as e:
            print(f"Error al descifrar: {e}")
            sys.exit(1)

        if texto is None:
            print("Error: La función descifrar() retornó None.")
            print("   Completa los TODO en la función descifrar().")
            sys.exit(1)

        # Guardar texto descifrado
        archivo_salida = archivo.replace(".enc", ".dec.txt")
        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"  Archivo descifrado guardado en: '{archivo_salida}'")
        print("─" * 40)
        print("Descifrado completado exitosamente.\n")

    else:
        print(f"Acción '{accion}' no reconocida.")
        print("   Usa 'cifrar' o 'descifrar'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
