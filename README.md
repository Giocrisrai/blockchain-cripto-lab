# Blockchain Cripto Lab - BCY0010

**Repositorio de laboratorio para la Actividad 1.1: Encriptador simple**

| Campo       | Detalle                                                        |
| ----------- | -------------------------------------------------------------- |
| Asignatura  | **BCY0010 - Fundamentos de Blockchain**                        |
| Experiencia | EA1 - Herramientas criptograficas y sistemas distribuidos      |
| Indicadores | IL1.1 (fundamentos historicos) - IL1.2 (criptografia aplicada) |
| Duracion    | 3 horas pedagogicas (Semana 1)                                 |
| Escuela     | Informatica y Telecomunicaciones - Duoc UC                     |

---

## Descripcion

Este repositorio contiene el codigo base (boilerplate) para construir un programa de cifrado simetrico en Python utilizando **PyCryptodome**. Los archivos principales tienen secciones marcadas con `# TODO:` que debes completar durante la sesion.

Al completar esta actividad seras capaz de:

- Generar llaves criptograficas seguras (AES-256).
- Cifrar y descifrar archivos de texto plano.
- Verificar la integridad de archivos mediante funciones hash (SHA-256).
- Comparar algoritmos criptograficos (AES-256 vs DES).

---

## Requisitos previos

- **Python** 3.8 o superior
- **pip** (gestor de paquetes de Python)
- **Git** instalado
- Editor: **Visual Studio Code** (recomendado) o **Google Colab**

---

## Instalacion

### Opcion A: Local (VS Code / Terminal)

```bash
# 1. Clonar el repositorio
git clone https://github.com/<tu-usuario>/blockchain-cripto-lab.git
cd blockchain-cripto-lab

# 2. Crear entorno virtual (recomendado)
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Verificar instalacion
python -c "from Crypto.Cipher import AES; print('PyCryptodome instalado correctamente')"
```

### Opcion B: Google Colab

Si prefieres trabajar en la nube sin instalar nada local:

1. Sube los archivos del repositorio a tu Google Drive.
2. Abre un notebook nuevo en [Google Colab](https://colab.research.google.com/).
3. Ejecuta en la primera celda:

```python
!pip install pycryptodome
```

4. Monta tu Drive y navega a la carpeta:

```python
from google.colab import drive
drive.mount('/content/drive')
%cd /content/drive/MyDrive/blockchain-cripto-lab
```

5. Ejecuta los scripts con `!python encriptador.py cifrar examples/mensaje_prueba.txt`

---

## Estructura del proyecto

```
blockchain-cripto-lab/
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias (pycryptodome)
├── .gitignore                   # Excluye llaves, archivos cifrados, __pycache__
│
├── encriptador.py               # Programa principal — COMPLETAR los TODO
├── verificador_hash.py          # Verificacion SHA-256 — COMPLETAR los TODO
├── comparador_algoritmos.py     # Comparacion AES vs DES — YA FUNCIONAL (trabajo autonomo)
│
├── examples/
│   ├── ejemplo_aes.py           # Ejemplo resuelto de cifrado AES-256 (referencia)
│   ├── ejemplo_hash.py          # Ejemplo resuelto de SHA-256 (referencia)
│   └── mensaje_prueba.txt       # Archivo de texto para pruebas
│
├── tests/
│   ├── test_encriptador.py      # Tests automaticos para el encriptador
│   └── test_hash.py             # Tests para el verificador de hash
│
└── docs/
    └── CONCEPTOS.md             # Referencia rapida: AES, DES, CBC, hash, padding
```

---

## Instrucciones paso a paso

### Parte 1: Completar `encriptador.py` (en clase)

Este archivo tiene 4 funciones con secciones `# TODO:` que debes implementar:

1. **`generar_llave()`** - Generar y cargar una llave AES-256.
2. **`cifrar_archivo()`** - Cifrar un archivo de texto con AES-256-CBC.
3. **`descifrar()`** - Descifrar un cyphertext.
4. **`main()`** - Ya esta implementado, no necesitas modificarlo.

Consulta `examples/ejemplo_aes.py` si necesitas ayuda.

**Probar tu implementacion:**

```bash
# Cifrar
python encriptador.py cifrar examples/mensaje_prueba.txt

# Descifrar
python encriptador.py descifrar examples/mensaje_prueba.txt.enc
```

### Parte 2: Completar `verificador_hash.py` (en clase)

Implementa la funcion `calcular_hash()` que calcula el SHA-256 de un archivo.

Consulta `examples/ejemplo_hash.py` si necesitas ayuda.

**Probar tu implementacion:**

```bash
python verificador_hash.py examples/mensaje_prueba.txt examples/mensaje_prueba.txt.dec.txt
```

Si tu cifrado y descifrado funcionan correctamente, los hashes deben coincidir.

### Parte 3: Ejecutar `comparador_algoritmos.py` (trabajo autonomo)

Este script **ya esta funcional**. Ejecutalo, analiza la tabla comparativa que genera
y responde las preguntas de observacion que aparecen en pantalla.

```bash
python comparador_algoritmos.py examples/mensaje_prueba.txt
```

---

## Validar tu trabajo con tests

Ejecuta los tests automaticos para verificar que tu implementacion es correcta:

```bash
# Ejecutar todos los tests
python tests/test_encriptador.py
python tests/test_hash.py

# O con pytest (si lo tienes instalado)
python -m pytest tests/ -v
```

---

## Entregables

Para la evaluacion formativa debes entregar:

1. **Enlace a tu repositorio GitHub** con el codigo completo (TODOs resueltos).
2. **Captura de pantalla** del programa cifrando y descifrando exitosamente.
3. **Verificacion de integridad**: captura mostrando que el hash original coincide con el hash del archivo descifrado.
4. **Tabla comparativa AES-256 vs DES** generada por `comparador_algoritmos.py`, con tus observaciones respondidas.

---

## Orden sugerido de trabajo

| Paso | Archivo                    | Que hacer                                                                                    |
| ---- | -------------------------- | -------------------------------------------------------------------------------------------- |
| 1    | `examples/ejemplo_aes.py`  | Leer y ejecutar para entender AES-256                                                        |
| 2    | `encriptador.py`           | Completar los TODO                                                                           |
| 3    | Probar cifrado/descifrado  | `python encriptador.py cifrar examples/mensaje_prueba.txt`                                   |
| 4    | `examples/ejemplo_hash.py` | Leer y ejecutar para entender SHA-256                                                        |
| 5    | `verificador_hash.py`      | Completar los TODO                                                                           |
| 6    | Verificar integridad       | `python verificador_hash.py examples/mensaje_prueba.txt examples/mensaje_prueba.txt.dec.txt` |
| 7    | Ejecutar tests             | `python tests/test_encriptador.py && python tests/test_hash.py`                              |
| 8    | Comparador (autonomo)      | `python comparador_algoritmos.py examples/mensaje_prueba.txt`                                |

---

## Referencia rapida

Consulta `docs/CONCEPTOS.md` para una explicacion de:

- Cifrado simetrico (AES-256, DES)
- Modo CBC y Vector de Inicializacion (IV)
- Funciones hash (SHA-256)
- Padding (PKCS7)

---

## Bibliografia

- Arboledas Brihuega, D. (2017). _Criptografia sin secretos con Python_. RA-MA Editorial.
- [PyCryptodome Documentation](https://pycryptodome.readthedocs.io/)
- [Python hashlib](https://docs.python.org/3/library/hashlib.html)

---

**Escuela de Informatica y Telecomunicaciones - Duoc UC**
BCY0010 - Fundamentos de Blockchain - 2025
