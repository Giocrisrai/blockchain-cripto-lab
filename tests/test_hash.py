"""
test_hash.py — Tests para verificador_hash.py
"""

import sys
import os
import hashlib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from verificador_hash import calcular_hash
    FUNCIONES_DISPONIBLES = True
except ImportError:
    FUNCIONES_DISPONIBLES = False


def test_hash_consistente():
    """El mismo archivo debe producir siempre el mismo hash."""
    if not FUNCIONES_DISPONIBLES:
        print("SKIP: No se pudo importar verificador_hash.py")
        return

    with open("test_h.txt", "w") as f:
        f.write("Contenido de prueba")

    h1 = calcular_hash("test_h.txt")
    h2 = calcular_hash("test_h.txt")

    if h1 is None:
        print("FAIL: calcular_hash() retornó None — completa los TODO")
        return

    assert h1 == h2, "El hash debe ser consistente"
    assert len(h1) == 64, f"SHA-256 debe tener 64 caracteres hex, tiene {len(h1)}"
    print("PASS: Hash consistente y longitud correcta (64 chars)")
    os.remove("test_h.txt")


def test_hash_diferente_contenido():
    """Archivos diferentes deben producir hashes diferentes."""
    if not FUNCIONES_DISPONIBLES:
        print("SKIP")
        return

    with open("test_h1.txt", "w") as f:
        f.write("Archivo A")
    with open("test_h2.txt", "w") as f:
        f.write("Archivo B")

    h1 = calcular_hash("test_h1.txt")
    h2 = calcular_hash("test_h2.txt")

    if h1 is None:
        print("FAIL: calcular_hash() retornó None")
        return

    assert h1 != h2, "Contenidos diferentes deben dar hashes diferentes"
    print("PASS: Contenidos diferentes producen hashes diferentes")
    os.remove("test_h1.txt")
    os.remove("test_h2.txt")


def test_hash_mismo_contenido():
    """Archivos con el mismo contenido deben tener el mismo hash."""
    if not FUNCIONES_DISPONIBLES:
        print("SKIP")
        return

    contenido = "Contenido idéntico para verificar"
    with open("test_h3.txt", "w") as f:
        f.write(contenido)
    with open("test_h4.txt", "w") as f:
        f.write(contenido)

    h1 = calcular_hash("test_h3.txt")
    h2 = calcular_hash("test_h4.txt")

    if h1 is None:
        print("FAIL: calcular_hash() retornó None")
        return

    assert h1 == h2, "Mismo contenido debe producir mismo hash"
    print("PASS: Mismo contenido produce mismo hash (integridad)")
    os.remove("test_h3.txt")
    os.remove("test_h4.txt")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  Tests del Verificador Hash — BCY0010")
    print("=" * 60 + "\n")

    test_hash_consistente()
    print()
    test_hash_diferente_contenido()
    print()
    test_hash_mismo_contenido()

    print("\n" + "=" * 60 + "\n")
