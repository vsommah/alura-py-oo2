# testando a modificação de atributos de classe

class Pessoa:
    tamanho_cpf = 11


p = Pessoa()

# o python aqui buscou o atributo da classe, já que ele não existia na instância

print(p.tamanho_cpf)

# ao modificar o atributo, estamos apenas alterando o da instância e não o da classe

p.tamanho_cpf = 12

print(p.tamanho_cpf)

print(Pessoa.tamanho_cpf)
