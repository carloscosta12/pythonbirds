class Pessoa:
    # Mótodo __init__, passando parâmetros
    def __init__(self, *filhos, nome=None, idade=45):
        # Criando os abtributos
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    # Criando um método 'cumprimentar'
    def cumprimentar(self):
        return f'Ola {id(self)}'
if __name__ == '__main__':
    carlos = Pessoa(nome='Carlos')
    eduardo = Pessoa(carlos, nome='Eduardo')
    print(Pessoa.cumprimentar(eduardo))
    print(id(eduardo))
    print(eduardo.cumprimentar())
    print(eduardo.nome)
    print(eduardo.idade)
    for filho in eduardo.filhos:
        print(filho.nome)
    eduardo.sobrenome = 'Santos'
    # Usando o método Dunder __dict))
    del eduardo.filhos # removendo o atribudo eduardo.filhos
    print(eduardo.__dict__)
    print(carlos.__dict__)

