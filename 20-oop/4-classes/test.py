# Testing
#-----------------------------------------------

class Vehiculo:
    
    def __init__(self, tipoVehiculo: str, ruedas: int, puertas: int):
        self.greeting:     str = 'Soy un vehiculo!'
        
        
        self.tipoVehiculo: str = tipoVehiculo
        self.ruedas:       int = ruedas
        self.puertas:      int = puertas
    
    def __str__(self) -> str:
        introduccion: str = f"Hola! Soy un  {self.tipoVehiculo}, tengo {self.ruedas} ruedas"
    
        if self.puertas > 0:
            closing: str = f"y tengo {self.puertas} puertas!"
    
        return f"{introduccion}\n{closing}"
                
class Coche(Vehiculo):
    
    def __init__(self, tipoVehiculo: str, ruedas: int, puertas: int, marca: str):
        super().__init__(tipoVehiculo, ruedas, puertas)
        self.tipoVehiculo: str  = "Coche"
        self.ruedas:       int  = 4
        self.volante:      bool = True 
        
        self.marca:        str  = marca
        
    @classmethod
    def alter_constr(cls, ruedas: int, puertas: int, marca: str):
        
        result: cls
        
        result = cls("Coche Familiar", ruedas, puertas , marca)
        
        return result
    
def show_attributes(something) -> None:

    keys:   list = sorted(something.__dict__.keys())
    values: list = [something.__dict__[key] for key in keys]

    for key, value in zip(keys, values):
        print(f'{key}: {value}')

    print()

if __name__ == "__main__":
    
    vehiculo: Vehiculo = Vehiculo("Vehiculo", 10, 10)
    coche:    Coche    = Coche("coche", 3, 5, "Toyota")

    coche_familiar: Coche = Coche.alter_constr(4, 7, "Seat")
    show_attributes(coche_familiar)

    print(coche, vehiculo, sep="\n\n")

