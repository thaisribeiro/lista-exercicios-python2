#=====================================================================
#               Gravity Falls: Um Verão de Mistérios
#=====================================================================

class Personagens:
    def __init__(self, nome, aniversario, caracteristica):
        self.nome = nome
        self.aniversario = aniversario
        self.caracteristica = caracteristica
       
    def get_nome(self):
        return f"O nome do Personagem é: {self.nome}"
    
    def get_aniversario(self):
        return f"Ele(a) faz aniversário em {self.aniversario}"
    
    def get_caracteristica(self):
        return f"Suas características são: {self.caracteristica}"
    
 #=======================================================================   
class Mabel(Personagens):
    def __init__(self, nome, aniversario, caracteristica, sonhos):
      self.sonhos = sonhos
      
      super().__init__(nome, aniversario,caracteristica)
      
    
    def sobre_mabel(self):
        return f'Esta é {self.nome}.\n Ela faz aniversario em {self.aniversario}.\n Características de Mabel: {self.caracteristica}'
    
    def get_sonhos(self):
        if self.sonhos == 'S':
            return f"Bons sonhos fazem Mabel dormir tranquila"
        
        if self.sonhos == 'P':
            return f"Sempre que Mabel tem pesadelos, ela mia e volta a dormir."
        
        return f"Está acordada."
    
#============================================================================
mabel_pines = Mabel('Mabel', '31 de Agosto ', 'Otimista, energética, se apaixona facilmente e é viciada em açúcar', 'P')
print(18*"=====","\n",mabel_pines.sobre_mabel(),"\n", mabel_pines.get_sonhos(),"\n",18*"=====")
