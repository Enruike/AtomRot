Con este código es posible leer los archivs .vasp para realizar rotaciones y traslaciones en clústeres de átomos.
No hace falta poner "Sí/No" o "Traslación/Rotación" completamente. Basta con poner la inicial (s/n) o (t/r)
La traslación es la única que puede generar una serie de archivos que se multiplica a través de $N \cdot \Delta n$,
donde $n = x, y, z$ y $N = 1, 2, 3, ...$

Los archivos generados a través de la traslación contienen el siguiente formato
POSCAR - tras - $N \cdot \Delta x$ - $N \cdot \Delta y$ - $N \cdot \Delta z$.vasp
