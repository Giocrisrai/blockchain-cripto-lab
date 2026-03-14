# Observaciones: Tabla Comparativa AES-256 vs DES

**1. ¿Por qué el cyphertext de DES es diferente al de AES?**
**Respuesta:** Porque utilizan estructuras matemáticas y algoritmos criptográficos diferentes. DES usa una red de Feistel clásica con bloques de 8 bytes, mientras que AES emplea una red de sustitución-permutación (SPN) con bloques de 16 bytes. Además, el vector de inicialización (IV) generado es de distinto tamaño, lo que produce una dispersión de bits y resultados completamente distintos incluso con el mismo texto original.

**2. ¿Qué relación hay entre el tamaño de bloque y el padding?**
**Respuesta:** Los algoritmos de cifrado simétrico por bloques (como AES y DES) dividen la información en pedazos fijos (16 bytes o 8 bytes respectivamente). El padding (o relleno) se encarga de añadir los bytes faltantes al último pedazo del mensaje original para que su longitud total sea un múltiplo exacto del tamaño de bloque del algoritmo, permitiendo así cifrar el último bloque correctamente.

**3. ¿Por qué DES se considera inseguro hoy en día?**
**Respuesta:** La debilidad principal de DES es la longitud de su clave: solo 56 bits efectivos (8 bits son descartados como bits de paridad). Con el poder computacional actual, un ataque de fuerza bruta que pruebe todas las posibles claves ($2^{56}$) se puede realizar en cuestión de horas o días usando hardware especializado, por lo que ya no garantiza la seguridad de los datos.

**4. ¿Cuál algoritmo elegirías para una blockchain y por qué?**
**Respuesta:** AES-256, sin duda. Posee un nivel de seguridad mucho mayor gracias a su llave de 256 bits, lo cual es matemáticamente inviable de romper mediante fuerza bruta incluso utilizando supercomputadoras modernas. Además, está profundamente optimizado (aceleración por hardware AES-NI) por lo que ofrece un gran rendimiento, siendo el estándar de oro actual para confidencialidad.
