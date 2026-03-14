# Reflexion - Actividad 1.1

**1. ¿Que pasa si cambias un solo bit de la llave?**
El algoritmo usaria una clave completamente distinta y el descifrado produciria basura o un error de padding. Ningun dato original podria recuperarse, garantizando que solo quien posea la llave exacta pueda revelar el mensaje.

**2. ¿Por que es vital que el IV cambie en cada operacion?**
Porque si ciframos el mismo mensaje exacto dos veces con la misma llave y el mismo IV, el texto cifrado resultante seria identico. Un atacante podria deducir patrones (saber que se envio el mismo mensaje). Cambiar el IV asegura que el criptograma siempre sea unico.

**3. ¿Para que sirve el padding en algoritmos de bloque como AES?**
Algoritmos como AES particionan la informacion en bloques de tamano exacto (16 bytes). Como los textos cifrados raras veces son multiplos exactos de 16, el padding rellena los bytes faltantes del ultimo bloque para que AES pueda procesarlo con exito matematicamente.
