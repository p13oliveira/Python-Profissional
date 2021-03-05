# Classe descreve um determinado objeto, abstrata onde nunca vai ser estanciada
class Pokemon:
    # Método construtor, usado para construir um objeto (Sempre executado quando inicializar)
    # nome=None --> Quer dizer que não é obrigatório definir uma valor para nome
    def __init__(self, especie, level=1, nome=None):
        # self.alguma_coisa é quando nos referimos aos atributos desse objeto
        self.especie = especie
        self.level = level
        if nome:
            self.nome = nome
        else:
            self.nome = especie

    # Quando printamos um objeto, é isso que ele nos retorna de informação
    def __str__(self):
        return f"{self.nome}(Nv.{self.level})"

    def atacar(self, pokemon):
        print(f"{self} atacou {pokemon}!")

