# Referencia rápida — Conceptos criptográficos

## Cifrado simétrico

En el cifrado simétrico, **una única llave secreta** se usa tanto para cifrar como para descifrar.

```
          LLAVE                LLAVE
            │                    │
            ▼                    ▼
Plaintext ──→ [CIFRADO] ──→ Cyphertext ──→ [DESCIFRADO] ──→ Plaintext
```

### Ventajas
- Rápido y eficiente para grandes volúmenes de datos.
- Bajo costo computacional.

### Desventajas
- Problema de distribución de llaves: ¿cómo compartir la llave de forma segura?
- Si la llave se compromete, toda la comunicación está expuesta.

---

## AES (Advanced Encryption Standard)

Estándar del NIST desde 2001. Reemplazó a DES.

| Variante | Tamaño llave | Rondas | Uso |
|----------|-------------|--------|-----|
| AES-128  | 128 bits    | 10     | Seguro para la mayoría de usos |
| AES-192  | 192 bits    | 12     | Mayor seguridad |
| AES-256  | 256 bits    | 14     | Máxima seguridad (usado en blockchain) |

### Modo CBC (Cipher Block Chaining)

Cada bloque de texto plano se combina (XOR) con el bloque cifrado anterior antes de cifrarse. El primer bloque usa el **IV** (Vector de Inicialización).

```
Plaintext:  [Bloque 1] [Bloque 2] [Bloque 3]
                │           │           │
IV ──→ XOR     │    ┌──→ XOR     ┌──→ XOR
        │       │    │      │     │      │
        ▼       │    │      ▼     │      ▼
    [AES-ENC]   │    │  [AES-ENC] │  [AES-ENC]
        │       │    │      │     │      │
        ▼       │    │      ▼     │      ▼
   Cyphertext 1 ┘    │ Cyphertext 2    Cyphertext 3
                      │
```

---

## DES (Data Encryption Standard)

Estándar desde 1977. **OBSOLETO** desde 1999.

| Aspecto | DES | AES-256 |
|---------|-----|---------|
| Tamaño llave | 56 bits | 256 bits |
| Tamaño bloque | 64 bits | 128 bits |
| Seguridad | Vulnerable a fuerza bruta | Seguro |
| Velocidad | Más lento | Más rápido (aceleración por hardware) |

**¿Por qué DES es inseguro?** Con solo 56 bits de llave, existen 2^56 ≈ 7.2 × 10^16 combinaciones posibles. En 1999, la máquina *Deep Crack* rompió DES en menos de 24 horas.

---

## Funciones hash

Una función hash toma un input de **cualquier tamaño** y produce un output de **tamaño fijo**.

```
"Hola"           → SHA-256 → 3d5a1688...  (64 hex = 256 bits)
"Hola Mundo"     → SHA-256 → ca70bde1...  (64 hex = 256 bits)
(archivo de 1GB) → SHA-256 → 8f2e9bc4...  (64 hex = 256 bits)
```

### Propiedades fundamentales

1. **Determinista**: Mismo input → mismo output, siempre.
2. **Efecto avalancha**: Cambiar 1 bit del input cambia ~50% del hash.
3. **Unidireccional**: Imposible reconstruir el input desde el hash.
4. **Resistente a colisiones**: Extremadamente improbable que dos inputs distintos produzcan el mismo hash.

### Uso en blockchain

- **Integridad de bloques**: Cada bloque contiene el hash del bloque anterior.
- **Merkle Trees**: Estructura de hashes para verificar transacciones eficientemente.
- **Proof of Work**: Los mineros buscan un nonce que produzca un hash con N ceros iniciales.

---

## Padding

AES cifra en bloques de 16 bytes. Si el texto no es múltiplo de 16, se agrega **padding**.

```
Texto:   "Hola" (4 bytes)
Padding: "Hola" + 12 bytes de relleno = 16 bytes (1 bloque)

Texto:   "Mensaje largo..." (20 bytes)  
Padding: 20 bytes + 12 bytes de relleno = 32 bytes (2 bloques)
```

PyCryptodome usa **PKCS7**: cada byte de relleno indica cuántos bytes de padding hay.

---

## Vector de Inicialización (IV)

Valor aleatorio que se usa como "semilla" del cifrado. Garantiza que cifrar el **mismo texto con la misma llave** produzca **resultados diferentes** cada vez.

- El IV **no es secreto** — se envía junto al cyphertext.
- El IV **debe ser único** para cada cifrado.
- En AES-CBC, el IV tiene 16 bytes (tamaño del bloque).

---

## Glosario rápido

| Término | Definición |
|---------|-----------|
| **Plaintext** | Texto original sin cifrar |
| **Cyphertext** | Texto cifrado (ilegible) |
| **Key (llave)** | Secreto que controla el cifrado |
| **IV** | Valor aleatorio para iniciar el cifrado |
| **Padding** | Relleno para completar el último bloque |
| **CSPRNG** | Generador de números aleatorios criptográficamente seguro |
| **Hash** | Huella digital de tamaño fijo de cualquier contenido |
| **SHA-256** | Función hash estándar que produce 256 bits |
| **CBC** | Modo de cifrado por bloques encadenados |
