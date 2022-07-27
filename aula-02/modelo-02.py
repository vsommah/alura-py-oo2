# trabalhando com herança para evitar repetição

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)     # chamando construtor da classe mãe para evitar repetição
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 3)
atlanta.dar_like()
atlanta.dar_like()
print(f'{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}')

