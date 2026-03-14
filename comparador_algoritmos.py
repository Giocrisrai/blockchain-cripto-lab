"""
comparador_algoritmos.py — Comparación AES-256 vs DES
======================================================
BCY0010 · Fundamentos de Blockchain
EA1 · Act 1.1 · Trabajo Autónomo
IL1.2

Descripción:
    Cifra el mismo archivo con AES-256 y DES, comparando tamaños
    de llaves, cyphertext y tiempos de ejecución. Genera una tabla
    comparativa como evidencia para la Evaluación Formativa 2.

Uso:
    python comparador_algoritmos.py <archivo.txt>

Autor: Sebastián Tralma
Fecha: 14/03/2026
"""

from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import time
import sys
import os


# ──────────────────────────────────────────────────────────────
# CONSTANTES
# ──────────────────────────────────────────────────────────────
TAMANIO_MAX = 1024  # 1 KB

# Configuración de cada algoritmo
ALGORITMOS = {
    "AES-256": {
        "cipher_class": AES,
        "key_size": 32,       # 256 bits
        "block_size": 16,     # 128 bits
        "mode": AES.MODE_CBC,
    },
    "DES": {
        "cipher_class": DES,
        "key_size": 8,        # 56 bits efectivos (64 con paridad)
        "block_size": 8,      # 64 bits
        "mode": DES.MODE_CBC,
    },
}


# ──────────────────────────────────────────────────────────────
# FUNCIONES
# ──────────────────────────────────────────────────────────────

def cifrar_con_algoritmo(plaintext_bytes, nombre_algoritmo):
    """
    Cifra un texto usando el algoritmo especificado.

    Args:
        plaintext_bytes (bytes): Texto plano en bytes.
        nombre_algoritmo (str): "AES-256" o "DES".

    Returns:
        dict: Resultados del cifrado con métricas.

    Nota: Esta función ya está implementada para ambos algoritmos
          (AES-256 y DES). Ejecútala y analiza los resultados.
    """
    config = ALGORITMOS[nombre_algoritmo]

    # Generar llave del tamaño correcto
    key = get_random_bytes(config["key_size"])

    # Medir tiempo de cifrado
    inicio = time.perf_counter()

    # Crear cifrador
    cipher = config["cipher_class"].new(key, config["mode"])

    # Aplicar padding al tamaño de bloque del algoritmo
    padded = pad(plaintext_bytes, config["block_size"])

    # Cifrar
    cyphertext = cipher.encrypt(padded)
    iv = cipher.iv

    fin = time.perf_counter()
    tiempo_cifrado_ms = (fin - inicio) * 1000

    # Medir tiempo de descifrado
    inicio_dec = time.perf_counter()

    decipher = config["cipher_class"].new(key, config["mode"], iv=iv)
    padded_dec = decipher.decrypt(cyphertext)
    plaintext_dec = unpad(padded_dec, config["block_size"])

    fin_dec = time.perf_counter()
    tiempo_descifrado_ms = (fin_dec - inicio_dec) * 1000

    # Verificar integridad
    integridad = plaintext_bytes == plaintext_dec

    return {
        "algoritmo": nombre_algoritmo,
        "key_size_bytes": config["key_size"],
        "key_size_bits": config["key_size"] * 8,
        "block_size_bytes": config["block_size"],
        "plaintext_size": len(plaintext_bytes),
        "padded_size": len(padded),
        "cyphertext_size": len(cyphertext),
        "iv_size": len(iv),
        "tiempo_cifrado_ms": tiempo_cifrado_ms,
        "tiempo_descifrado_ms": tiempo_descifrado_ms,
        "integridad": integridad,
    }


def mostrar_tabla_comparativa(resultados):
    """
    Muestra una tabla comparativa entre los algoritmos.

    Args:
        resultados (list): Lista de diccionarios con resultados de cada algoritmo.
    """
    print("\n╔════════════════════════════════════════════════════════════════════╗")
    print("║           TABLA COMPARATIVA — Algoritmos Criptográficos          ║")
    print("╠════════════════════════════════════════════════════════════════════╣")
    print("║                                                                  ║")

    # Encabezado
    print(f"║  {'Aspecto':<30} ", end="")
    for r in resultados:
        print(f"│ {r['algoritmo']:>10} ", end="")
    print("║")
    print(f"║  {'─' * 30} ", end="")
    for _ in resultados:
        print(f"│ {'─' * 10} ", end="")
    print("║")

    # Filas de datos
    filas = [
        ("Tamaño llave (bytes)", "key_size_bytes"),
        ("Tamaño llave (bits)", "key_size_bits"),
        ("Tamaño bloque (bytes)", "block_size_bytes"),
        ("Tamaño plaintext (bytes)", "plaintext_size"),
        ("Tamaño con padding (bytes)", "padded_size"),
        ("Tamaño cyphertext (bytes)", "cyphertext_size"),
        ("Tamaño IV (bytes)", "iv_size"),
    ]

    for label, key in filas:
        print(f"║  {label:<30} ", end="")
        for r in resultados:
            print(f"│ {r[key]:>10} ", end="")
        print("║")

    # Tiempos con formato decimal
    print(f"║  {'Tiempo cifrado (ms)':<30} ", end="")
    for r in resultados:
        print(f"│ {r['tiempo_cifrado_ms']:>10.4f} ", end="")
    print("║")

    print(f"║  {'Tiempo descifrado (ms)':<30} ", end="")
    for r in resultados:
        print(f"│ {r['tiempo_descifrado_ms']:>10.4f} ", end="")
    print("║")

    print(f"║  {'Integridad verificada':<30} ", end="")
    for r in resultados:
        estado = "Si" if r["integridad"] else "[X] No"
        print(f"│ {estado:>10} ", end="")
    print("║")

    print("║                                                                  ║")
    print("╚════════════════════════════════════════════════════════════════════╝")


def mostrar_observaciones():
    """
    Muestra la sección de observaciones que el estudiante debe completar.
    """
    print("\n┌──────────────────────────────────────────────────────────────────┐")
    print("│  OBSERVACIONES                       │")
    print("├──────────────────────────────────────────────────────────────────┤")
    print("│                                                                  │")
    print("│  1. ¿Por qué el cyphertext de DES es diferente al de AES?       │")
    print("│     Respuesta: ________________________________________________ │")
    print("│                                                                  │")
    print("│  2. ¿Qué relación hay entre el tamaño de bloque y el padding?   │")
    print("│     Respuesta: ________________________________________________ │")
    print("│                                                                  │")
    print("│  3. ¿Por qué DES se considera inseguro hoy en día?              │")
    print("│     Respuesta: ________________________________________________ │")
    print("│                                                                  │")
    print("│  4. ¿Cuál algoritmo elegirías para una blockchain y por qué?    │")
    print("│     Respuesta: ________________________________________________ │")
    print("│                                                                  │")
    print("└──────────────────────────────────────────────────────────────────┘")


# ──────────────────────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ──────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("╔══════════════════════════════════════════════════════════╗")
        print("║  Comparador de Algoritmos · BCY0010 · Trabajo Autónomo  ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║  Uso:                                                   ║")
        print("║    python comparador_algoritmos.py <archivo.txt>        ║")
        print("╚══════════════════════════════════════════════════════════╝")
        sys.exit(1)

    archivo = sys.argv[1]

    if not os.path.exists(archivo):
        print(f"Error: No se encontró '{archivo}'")
        sys.exit(1)

    # Leer archivo
    with open(archivo, "r", encoding="utf-8") as f:
        plaintext = f.read()

    if len(plaintext.encode("utf-8")) > TAMANIO_MAX:
        print(f"Error: El archivo excede {TAMANIO_MAX} bytes")
        sys.exit(1)

    plaintext_bytes = plaintext.encode("utf-8")

    print(f"\nComparando algoritmos con '{archivo}' ({len(plaintext_bytes)} bytes)...")

    # Ejecutar cada algoritmo
    resultados = []
    for nombre in ALGORITMOS:
        print(f"  Probando {nombre}...")
        resultado = cifrar_con_algoritmo(plaintext_bytes, nombre)
        resultados.append(resultado)

    # Mostrar resultados
    mostrar_tabla_comparativa(resultados)
    mostrar_observaciones()

    print("\nTip: Captura esta pantalla como evidencia para tu entrega.\n")


if __name__ == "__main__":
    main()
