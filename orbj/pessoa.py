class Pessoa:
    olhos = 2 # Atributo default ou de Classe
    # Método __init__, passando parâmetros
    def __init__(self, *filhos, nome=None, idade=45):
        # Criando os abtributos
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    # Criando um método 'cumprimentar'
    def cumprimentar(self):
        return f'Ola {id(self)}'

    # Método Estático de Classe; Decorator
    @staticmethod
    def metodo_estatico():
        return 42
    # outro método de Classe: classmethod
    def nome_e_atributos_de_classe(cls):
        return(f'{cls} - olhos {cls.olhos}')

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
    carlos.olhos = 1
    del carlos.olhos # Apaga o atributo do objeto
    print(eduardo.__dict__)
    print(carlos.__dict__)
    Pessoa.olhos = 3
    print(f'Olhos: {Pessoa.olhos}')
    print(f'Olhos Carlos: {carlos.olhos}')
    print(f'Olhos Eduardo: {eduardo.olhos}')
    print(id(Pessoa.olhos), id(carlos.olhos), id(eduardo.olhos))
    print(Pessoa.metodo_estatico(), eduardo.metodo_estatico())
    # executando pela Classe
    print(Pessoa.nome_e_atributos_de_classe())
    # executando diretamente através do objeto
    print(carlos.nome_e_atributos_de_classe())