class Coche:
    def __init__(selt, gasolina):
        selt.gasolina = gasolina
        print("Tenenemos", gasolina, "Litros")
    
    def arrancar(selt):
        if selt.gasolina > 0:
            print("Arranca")
        else:
            print("No arranca")
            
    def conducir(selt):
      if selt.gasolina > 0:
          selt.gasolina -= 1
          print("Quedan", selt.gasolina, "Litros")
      else:
          print("No se mueve")

mi_coche = Coche(3)

class Instrumento:
    def __init__(selt, precio):
        selt.precio = precio
    
    def tocar(selt):
        print("Estamos tocando musica")
    
    def romper(selt):
        print("Eso lo pagas tu")
        print("Son", selt.precio, "$$$")  
        
class Bateria(Instrumento):
    pass
class Guitarra(Instrumento):
    pass