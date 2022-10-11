import math
import numpy

#### Basicamente oque o código faz é pegar os valores de entrada (x',y',z',angulo) para cada operação
#### Vai substituir o valor da operação na fórmula, e após isso vai inserir essa formula com os valores
#### e vai inserir em um array chamado matriz_composta. 
#### Para calcular a matriz composta apenas iterei sobre o array matriz_composta multiplicando cada matriz
#### e ao final retorna a matriz resultante dessas multiplicações.

#### Para o resultado final apenas multipliquei a matriz de entrada pela matriz composta.


#### ps: Para testar, altere as matrizes relativas ao [[x],[y],[z]] na funç



###############
#FUNÇÕES DE TRANSLAÇÃO
###############

def translacao(dim):
    valorx = float(input(f'Escolha o valor de x: '))
    valory = float(input(f'Escolha o valor de y: '))
    return translacao_2d(valorx, valory) if (dim == 2) else translacao_3d(valorx, valory)


def translacao_2d(tx, ty):
    matrix = [[1,0,tx],
	  [0,1,ty],
	  [0,0,1]]

    return matrix


def translacao_3d(tx, ty):
    tz = float(input(f'Escolha o valor de z: '))
    matrix = [
            [1,0,0,tx],
            [0,1,0,ty],
            [0,0,1,tz],
            [0,0,0,1],
    ]
    return matrix

############
#FUNÇÕES DE TRANSLAÇÃO INVERSA
############

def translacao_inversa(dim):
    valorx = float(input(f'Escolha o valor de x: '))
    valory = float(input(f'Escolha o valor de y: '))
    return translacao_inversa_2d(valorx, valory)  if (dim == 2) else translacao_inversa_3d(valorx, valory)


def translacao_inversa_2d(tx, ty):
    matrix = [[1,0,-tx],
	  [0,1,-ty],
	  [0,0,1]]

    return matrix


def translacao_inversa_3d(tx, ty):
    tz = float(input(f'Escolha o valor de z: '))
    matrix = [
            [1,0,0,-tx],
            [0,1,0,-ty],
            [0,0,1,-tz],
            [0,0,0,1],
    ]
    return matrix

##############
#FUNÇÕES DE ROTAÇÃO
##############

def rotacao(dim):
    angulo = int(input(f'Escolha o angulo da rotação: '))
    return rotacao_2d(angulo)  if (dim == 2) else rotacao_3d(angulo)


def rotacao_2d(x):
    matrix = [[math.cos(x), -math.sin(x), 0],
	  [math.sin(x), math.cos(x), 0],
	  [0	,0	,1]]

    return matrix


def rotacao_3d(x):
    eixo = str(input(f'Escolha um eixo (x, y, z): ')).lower()

    if eixo == 'x':
        matrix = [
        [1,0,0,0],
        [0,math.cos(x),-math.sin(x),0],
        [0,math.sin(x),math.cos(x),0],
        [0,0,0,1]
        ]
        return matrix

    elif eixo == 'y':
        matrix = [
        [math.cos(x),0,math.sin(x),0],
        [0,1,0,0],
        [-math.sin(x),0,math.cos(x),0],
        [0,0,0,1]
        ]
        return matrix
    
    else:
        matrix = [
        [math.cos(x),math.sin(x),0,0],
        [math.sin(x),math.cos(x),0,0],
        [0,0,1,0],
        [0,0,0,1]
        ]
        return matrix
    

##############
#FUNÇÕES DE ROTAÇÃO INVERSA
##############

def rotacao_inversa(dim):
    angulo = int(input(f'Escolha o angulo da rotação: '))
    return rotacao_inversa_2d(angulo)  if (dim == 2) else rotacao_inversa_3d(angulo)


def rotacao_inversa_2d(x):
    matrix = [[math.cos(x), math.sin(x), 0],
	  [-math.sin(x), math.cos(x), 0],
	  [0	,0	,1]]

    return matrix


def rotacao_inversa_3d(x):
    eixo = str(input(f'Escolha um eixo (x, y, z): ')).lower()

    if eixo == 'x':
        matrix = [
        [1,0,0,0],
        [0,math.cos(-x),-math.sin(-x),0],
        [0,math.sin(-x),math.cos(-x),0],
        [0,0,0,1]
        ]
        return matrix

    elif eixo == 'y':
        matrix = [
        [math.cos(-x),0,math.sin(-x),0],
        [0,1,0,0],
        [-math.sin(-x),0,math.cos(-x),0],
        [0,0,0,1]
        ]
        return matrix
    
    else:
        matrix = [
        [math.cos(-x),math.sin(-x),0,0],
        [math.sin(-x),math.cos(-x),0,0],
        [0,0,1,0],
        [0,0,0,1]
        ]
        return matrix

##############
#FUNÇÕES DE ESCALA
##############

def escala(matriz, dim):
    valorx = float(input(f'Escolha o valor de x: '))
    valory = float(input(f'Escolha o valor de y: '))
    return escala_2d(valorx, valory)  if (dim == 2) else escala_3d(valorx, valory, matriz)


def escala_2d(sx, sy):
    matrix = [
			  [sx,0,0],
			  [0,sy,0],
			  [0,0,1]
	  ]

    return matrix


def escala_3d(sx, sy, matriz):
    sz = float(input(f'Escolha o valor de z: '))
    matrix = [
      [sx,0,0,(1 - sx)*matriz[0][0]],
      [0,sy,0,(1 - sy)*matriz[1][0]],
      [0,0,sz,(1 - sz)*matriz[2][0]],
      [0,0,0,1]
    ]

    return matrix

##############
#FUNÇÕES DE ESCALA INVERSA
##############

def escala_inversa(matriz, dim):
    valorx = float(input(f'Escolha o valor de x: '))
    valory = float(input(f'Escolha o valor de y: '))
    return escala_inversa_2d(valorx, valory)  if (dim == 2) else escala_inversa_3d(valorx, valory, matriz)


def escala_inversa_2d(sx, sy):
    matrix = [
			[(1/sx),0,0],
			[0,(1/sy),0],
			[0,0,1]
	  ]

    return matrix


def escala_inversa_3d(sx, sy, matriz):
    sz = float(input(f'Escolha o valor de z: '))
    matrix = [
      [(1/sx),0,0,(1-(1/sx))*matriz[0][0]],
      [0,(1/sy),0,(1-(1/sy))*matriz[1][0]],
      [0,0,(1/sz),(1-(1/sz))*matriz[2][0]],
      [0,0,0,1]
    ]
    return matrix

##############
#EXECUÇÃO DO CÓDIGO
##############

def execucao(matriz):

    #MENU
    matriz_composta = []
    dimensao = int(input(f'Você deseja realizar transformações 2d ou 3d? '))

    while True:

        print(f'\n-=- OPÇÕES -=-')
        print(f'1 - Translação\n2 - Rotação\n3 - Escala\n4 - Translação inversa\n5 - Rotação inversa\n6 - Escala inversa\n7 - Sair')
        opcao = int(input(f'O que você deseja fazer? '))

        while ((opcao < 1) or (opcao > 7)):
            print(f'Por favor, escolha uma opção válida')
            opcao = int(input(f'O que você deseja fazer?'))

        if (opcao == 7):
            break

        elif (opcao == 1):
            matriz_composta.append(translacao(dimensao))
        
        elif (opcao == 2):
            matriz_composta.append(rotacao(dimensao))

        elif (opcao == 3):
            matriz_composta.append(escala(matriz, dimensao))

        elif (opcao == 4):
            matriz_composta.append(translacao_inversa(dimensao))

        elif (opcao == 5):
            matriz_composta.append(rotacao_inversa(dimensao))

        elif (opcao == 6):
            matriz_composta.append(escala_inversa(matriz, dimensao))

    #RESULTADO
    print(f'\n-=- Resultado -=-\n')
    resultado = matriz_composta[0]
    for i in range (1, len(matriz_composta)):
        resultado = numpy.matmul(resultado, matriz_composta[i])
    
    return numpy.matmul(resultado, matriz)




def main():
    
    matriz2d = [[12], [4], [1]] #MATRIZ DE PONTO 2D PARA TESTE
    matriz3d = [[12], [4], [8], [1]] #MATRIZ DE PONTO 3D PARA TESTE
    print(execucao(matriz3d))



main()
