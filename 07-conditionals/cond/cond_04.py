age: int = 121 # Años

is_baby:  bool = (0 <= age <= 1)
is_child: bool = (2 <= age <= 6)
is_adult: bool = (7 <= age <= 90)
is_elder: bool = (91<= age <= 120)

if is_baby:
    print("Regalar pañales")
elif is_child:
    print("Regalar pelota")
elif is_adult:
    print("Regalar ropa")
elif is_elder:
    print("Regalar pañales")
else:
    print("¡¡Felicítale!!")
