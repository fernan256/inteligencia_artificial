# Inteligencia Artificial

## Trabajo Practico numero 1

### Resolver el 8-puzzle
#### 1. Partiendo de el estado objetivo, hacer 50 movimientos validos para desordenar
#### 2. Una vez desordenado, buscar una solucion aplicando movimientos RANDOM y medir cuantos intentos lleva.
#### 3. Buscar solucion usando busqueda en anchura
#### 4. Buscar solucion usando Busqueda bidireccional

### Uso

#### Desordenar tablero
```
python main.py -c 3 -r 3
```

#### Resolver metodo random
```
python main.py -c 3 -r 3 -n 50 -ra
```

#### Resolver con metodo busqueda en anchura
```
python main.py -c 3 -r 3 -n 50 -ba
```

#### Resolver con metodo busqueda bidireccional
```
python main.py -c 3 -r 3 -n 50 -bd
```