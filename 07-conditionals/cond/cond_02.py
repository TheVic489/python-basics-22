
edad: int = 100 # Años

if (0 <= edad <= 1):
    print("Regalar pañales")
else:
    # edad > 1
    if (1 <= edad <= 6):
        print("Regalar pelota")
    else:
        # edad > 6
        if (6 <= edad <= 90):
            print("Regalar ropa")
        else:
            # edad > 90
            if (90 < edad):
                print("Regalar pañales")

