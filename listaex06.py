# Crie um arquivo main.py, importe a classe “Quadrado”, crie uma nova
# instância e acesse seus métodos.
from listaex05 import Quadrado



quad = Quadrado(float(input("Insira a médida do lado do quadrado:")))
print(30*"=")
print(f"Resultado: \nÁrea = {quad.area_of_square()} \nPerímetro = {quad.perimeter_of_square()}")
print(30*"=")
