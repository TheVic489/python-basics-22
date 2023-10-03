#! /usr/bin/env python3

import random

phrases: list = [
    "Hoy será un gran día.",
    "Hoy es mejor que juegues a la lotería.",
    "La respuesta del examen es 42.",
    "Hoy aprobarás programación, si no preguntas al profe.",
    "Symlinks: ln -snf <ruta>"
]

print(random.choice(phrases))
