def multiplicacao(n1, n2):
  return n1 * n2

def divisao(n1, n2):
  return n1/n2

def soma(n1, n2):
  return n1 + n2

def subtracao(n1, n2):
  return n1 - n2

numeros = []

for cont in range(2):
  ok = False
  while not ok:
      try:
          n = float(input(f'Digite o {cont + 1}º número: '))
          numeros.append(n)
          ok = True
      except:
        print('Número inválido, digite novamente')

n1 = numeros[0]
n2 = numeros[1]

ok = False
while not ok:
  try:
    print('''
    ESCOLHA O TIPO DE CÁLCULO

    (+) - SOMA
    (-) - SUBTRAÇÃO
    () - MULTIPLICAÇÃO
    (/) - DIVISÃO''')
    conta = input()
    if conta != '+' and conta != '-' and conta != '' and conta !='/':
      print('Digite uma forma válida')
    else:
      ok = True
  except:
    print('Digite uma forma válida')