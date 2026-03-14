"""
ejemplo_aes.py — Ejemplo RESUELTO de cifrado AES-256
=====================================================
Este archivo es de REFERENCIA. Consulta este código si necesitas
ayuda para completar los TODO en encriptador.py.

No copies y pegues: entiende cada línea antes de implementarla.
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def demo_cifrado_aes():
    """Demostración completa del proceso de cifrado y descifrado AES-256."""

    print("=" * 60)
    print("  DEMO: Cifrado simétrico AES-256-CBC con PyCryptodome")
    print("=" * 60)

    # ── 1. Texto plano ──
    mensaje = "Hola Blockchain! Este mensaje será cifrado con AES-256."
    plaintext_bytes = mensaje.encode("utf-8")
    print(f"\n1. Texto plano:     '{mensaje}'")
    print(f"   Tamaño:          {len(plaintext_bytes)} bytes")

    # ── 2. Generar llave ──
    key = get_random_bytes(32)  # 32 bytes = 256 bits
    print(f"\n2. Llave generada:  {key.hex()}")
    print(f"   Tamaño llave:    {len(key)} bytes ({len(key) * 8} bits)")

    # ── 3. Cifrar ──
    cipher_enc = AES.new(key, AES.MODE_CBC)
    iv = cipher_enc.iv
    padded = pad(plaintext_bytes, AES.block_size)
    cyphertext = cipher_enc.encrypt(padded)

    print(f"\n3. Cifrado:")
    print(f"   IV:              {iv.hex()}")
    print(f"   IV tamaño:       {len(iv)} bytes")
    print(f"   Padding:         {len(plaintext_bytes)} → {len(padded)} bytes")
    print(f"   Cyphertext:      {cyphertext.hex()}")
    print(f"   Cyphertext tam:  {len(cyphertext)} bytes")

    # ── 4. Descifrar ──
    cipher_dec = AES.new(key, AES.MODE_CBC, iv=iv)
    padded_dec = cipher_dec.decrypt(cyphertext)
    plaintext_dec = unpad(padded_dec, AES.block_size)
    mensaje_dec = plaintext_dec.decode("utf-8")

    print(f"\n4. Descifrado:      '{mensaje_dec}'")

    # ── 5. Verificar ──
    assert mensaje == mensaje_dec, "ERROR: Los mensajes no coinciden!"
    print(f"\n5. Verificación:    ✅ El mensaje descifrado es idéntico al original.")

    # ── 6. Demostrar efecto avalancha ──
    print(f"\n{'=' * 60}")
    print("  DEMO: Efecto avalancha (cambiar 1 byte cambia todo)")
    print("=" * 60)

    # Modificar un solo byte del cyphertext
    cyphertext_mod = bytearray(cyphertext)
    cyphertext_mod[0] ^= 0x01  # Cambiar solo 1 bit del primer byte
    cyphertext_mod = bytes(cyphertext_mod)

    print(f"\n   Original:  {cyphertext.hex()[:40]}...")
    print(f"   Modificado:{cyphertext_mod.hex()[:40]}...")

    try:
        cipher_dec2 = AES.new(key, AES.MODE_CBC, iv=iv)
        resultado = cipher_dec2.decrypt(cyphertext_mod)
        resultado = unpad(resultado, AES.block_size)
        print(f"   Resultado: '{resultado.decode('utf-8', errors='replace')}'")
        print(f"   ⚠️ El descifrado produjo basura — la integridad está comprometida.")
    except ValueError as e:
        print(f"   ❌ Error de padding: {e}")
        print(f"   El descifrado falló porque el cyphertext fue alterado.")


if __name__ == "__main__":
    demo_cifrado_aes()
