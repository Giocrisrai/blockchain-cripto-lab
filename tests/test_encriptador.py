"""
test_encriptador.py — Tests para verificar tu implementación
=============================================================
Ejecutar: python -m pytest tests/ -v
          o bien: python tests/test_encriptador.py
"""

import sys
import os

# Agregar directorio padre al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Importar funciones del encriptador
try:
    from encriptador import generar_llave, cifrar_archivo, descifrar
    FUNCIONES_DISPONIBLES = True
except ImportError:
    FUNCIONES_DISPONIBLES = False


def test_generar_llave():
    """Test: generar_llave() debe retornar 32 bytes."""
    if not FUNCIONES_DISPONIBLES:
        print(" SKIP: No se pudo importar encriptador.py")
        return

    # Limpiar archivo de llave si existe
    if os.path.exists("secret.key"):
        os.remove("secret.key")

    key = generar_llave()

    if key is None:
        print("FAIL: generar_llave() retornó None")
        print("   → Completa los TODO en la función generar_llave()")
        return

    assert isinstance(key, bytes), f"La llave debe ser bytes, no {type(key)}"
    assert len(key) == 32, f"La llave debe ser 32 bytes, tiene {len(key)}"
    print("PASS: generar_llave() genera 32 bytes correctamente")

    # Verificar que la llave se guardó
    assert os.path.exists("secret.key"), "No se guardó el archivo secret.key"
    print("PASS: La llave se guarda en archivo")

    # Verificar que cargar devuelve la misma llave
    key2 = generar_llave()
    assert key == key2, "La llave cargada no coincide con la generada"
    print("PASS: La llave se carga correctamente del archivo")

    # Limpiar
    os.remove("secret.key")


def test_cifrar_descifrar():
    """Test: cifrar y descifrar debe retornar el texto original."""
    if not FUNCIONES_DISPONIBLES:
        print("SKIP: No se pudo importar encriptador.py")
        return

    # Crear archivo de prueba
    mensaje = "Este es un mensaje de prueba para AES-256!"
    with open("test_msg.txt", "w", encoding="utf-8") as f:
        f.write(mensaje)

    key = get_random_bytes(32)

    # Cifrar
    try:
        resultado = cifrar_archivo("test_msg.txt", key)
    except Exception as e:
        print(f"FAIL: cifrar_archivo() lanzo excepcion: {e}")
        print("   → Completa los TODO en la funcion cifrar_archivo()")
        os.remove("test_msg.txt")
        return

    if resultado is None or resultado[1] is None:
        print("FAIL: cifrar_archivo() retornó None")
        print("   → Completa los TODO en la función cifrar_archivo()")
        return

    iv, cyphertext = resultado
    assert isinstance(iv, bytes) and len(iv) == 16, "IV debe ser 16 bytes"
    assert isinstance(cyphertext, bytes) and len(cyphertext) > 0, "Cyphertext no puede estar vacío"
    print("PASS: cifrar_archivo() genera IV y cyphertext correctos")

    # Descifrar
    try:
        texto = descifrar(iv, cyphertext, key)
    except Exception as e:
        print(f"FAIL: descifrar() lanzo excepcion: {e}")
        print("   → Completa los TODO en la funcion descifrar()")
        os.remove("test_msg.txt")
        return

    if texto is None:
        print("❌ FAIL: descifrar() retorno None")
        print("   → Completa los TODO en la funcion descifrar()")
        os.remove("test_msg.txt")
        return

    assert texto == mensaje, f"El descifrado no coincide:\n  Original:   '{mensaje}'\n  Descifrado: '{texto}'"
    print("PASS: descifrar() recupera el texto original")

    # Limpiar
    os.remove("test_msg.txt")


def test_tamano_maximo():
    """Test: archivos mayores a 1KB deben ser rechazados."""
    if not FUNCIONES_DISPONIBLES:
        print("SKIP: No se pudo importar encriptador.py")
        return

    # Crear archivo de 2KB
    with open("test_grande.txt", "w") as f:
        f.write("A" * 2048)

    key = get_random_bytes(32)

    try:
        resultado = cifrar_archivo("test_grande.txt", key)
        if resultado == (None, None) or resultado is None:
            print("SKIP: cifrar_archivo() no esta completo (completa los TODO)")
        else:
            print("FAIL: Deberia rechazar archivos mayores a 1KB")
    except ValueError:
        print("PASS: Rechaza correctamente archivos mayores a 1KB")
    finally:
        os.remove("test_grande.txt")


def test_iv_diferente_cada_vez():
    """Test: cifrar el mismo texto debe producir IV diferente cada vez."""
    if not FUNCIONES_DISPONIBLES:
        print("SKIP: No se pudo importar encriptador.py")
        return

    with open("test_iv.txt", "w") as f:
        f.write("Mismo texto para probar IV")

    key = get_random_bytes(32)

    try:
        r1 = cifrar_archivo("test_iv.txt", key)
        r2 = cifrar_archivo("test_iv.txt", key)
    except Exception as e:
        print(f"SKIP: cifrar_archivo() lanzo excepcion: {e}")
        os.remove("test_iv.txt")
        return

    if r1 is None or r2 is None or r1[0] is None or r2[0] is None:
        print("SKIP: cifrar_archivo() retorna None (completa los TODO)")
        os.remove("test_iv.txt")
        return

    iv1, ct1 = r1
    iv2, ct2 = r2

    assert iv1 != iv2, "Los IVs deberían ser diferentes cada vez"
    assert ct1 != ct2, "Los cyphertext deberían ser diferentes con IVs distintos"
    print("PASS: Cada cifrado genera un IV diferente (seguridad)")

    os.remove("test_iv.txt")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  Tests del Encriptador AES-256 — BCY0010")
    print("=" * 60 + "\n")

    test_generar_llave()
    print()
    test_cifrar_descifrar()
    print()
    test_tamano_maximo()
    print()
    test_iv_diferente_cada_vez()

    print("\n" + "=" * 60)
    print("  Tests completados")
    print("=" * 60 + "\n")
