# Escreva uma classe “Quadrado”, crie dois métodos que retornem a
# área do quadrado e o perímetro, não crie a instância nesse exercício.
class Quadrado:
    def __init__(self, side):
        self.side = side
        
    def area_of_square(self):
        return self.side**2
    
    def perimeter_of_square(self):
        return 4 * self.side
    
# quad = Quadrado(2)
# print(f"TESTE: àrea = {quad.area_of_square()} e perímetro = {quad.perimeter_of_square()}")