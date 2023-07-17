def buscaSequencial (dados, buscado):
    achou = 0
    i = 0
    for i in range (0, len(dados)):
      if (dados[i] == buscado):
        achou = achou + 1
      else:
        achou + 1
    if (achou != 0):
        return achou
    else:
      return -1

# programa principal
dados = [23, 4, 67, 54, 90, 21, 54, 5, 29, 54]
print(dados)
buscado = int(input('Digite o valor que deseja buscar: '))
achou = buscaSequencial(dados, buscado)
if (achou == -1):
    print('Valor não encontrado.')
else:
    print('Valor encontrado {}x'.format(achou))