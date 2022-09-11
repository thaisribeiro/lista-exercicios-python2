# 1. Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma
# classe onde teremos o retorno do documento, o retorno do nome e
# verificação de tipo de pessoa, onde um método irá receber como
# parâmetro “F” ou “N” para trazer fumante ou não fumante.
# Feito isso, crie uma instância e retorne esses valores.

# Nome, idade, CPF, tipo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
            
    def smoke(self):
         return f"Fumante: F"
        
    def dont_smoke(self):
         return f"Fumante: N"
        
    def info(self):
        return f"- DADOS PESSOAIS:\nNome: {self.nome} \nIdade: {self.idade}"
        
# 2. Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método
# exclusivo para a classe e acesse-o

class PessoaFisica(Pessoa):
     def __init__(self, nome, idade, cpf):
         super().__init__(nome, idade)
         self.cpf = cpf
         
         
     def info(self):
         return f"- PESSOA FÍSICA:\nNome: {self.nome} \nIdade: {self.idade} \nCPF: {self.cpf}"
     
# 3. Escreva uma classe “PessoaJurica” e herde Pessoa, agora
# modificando o comportamento, retorne o cnpj. Crie uma instância e
# acesse os dados.
class PessoaJuridica(Pessoa):
     def __init__(self, nome, idade, cnpj):
         super().__init__(nome, idade)
         self.cnpj = cnpj
         
     def info(self):
         return f"- PESSOA JURÍDICA:\nNome: {self.nome} \nIdade: {self.idade} \nCNPJ: {self.cnpj}"
     
pessoa = Pessoa("Hozania", 32)
pessoafisica1 = PessoaFisica("Maria", 25, 65984536595)
pessoajuridica1 = PessoaJuridica("José", 35, 58468665984536595)

# pessoa.info()
print(pessoa.info())
print(pessoa.dont_smoke())
pessoa.dont_smoke()
print(pessoafisica1.info())
print(pessoajuridica1.info())