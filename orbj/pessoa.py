class Pessoa:
    # Criando um método 'cumprimentar'
    def cumprimentar(self):
        return f'Ola {id(self)}'
if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    # Passando o objeto 'p' como parametro
    print(id(p))
    print(p.cumprimentar())

