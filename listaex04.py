class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__salario = salario
              
    def info(self):
        if self.nome == "Maria José":
          return f"- DADOS PESSOAIS:\nNome: {self.nome} \nIdade: {self.idade} \nSalário: R${self.__salario}"
        
        return f"- DADOS PESSOAIS:\nNome: {self.nome} \nIdade: {self.idade} \nSalário: Acesso Negado."

professor1 = Professor("Carlos", 36,1500)
professor2 = Professor("Maria José", 45,2500)
print(professor1.info())
print(professor2.info())
