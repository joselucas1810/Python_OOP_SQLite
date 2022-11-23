#Importar o arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
jose = Pessoa(1,"José Lucas")
print (jose)

#Mostrar apenas o nome
print (jose.nome)