class Pessoa:
    # Mótodo __init__, passando o parâmetro 'nome' = None
    def __init__(self, nome=None, idade=45):
        # Cria um abtributo 'nome' como None
        self.nome = nome
        self.idade = idade

    # Criando um método 'cumprimentar'
    def cumprimentar(self):
        return f'Ola {id(self)}'
if __name__ == '__main__':
    p = Pessoa('Carlos Costa')
    print(Pessoa.cumprimentar(p))
    # Passando o objeto 'p' como parametro
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    # alterando o valor do atributo
    p.nome = 'Carlos'
    print(p.nome)
    print(p.idade)
