from sys import argv

arq = []
transicao = []

def leArquivo(localArq):
    arquivo = open(localArq, "r")
    for linha in arquivo.readlines():
        arq.append(linha[:-1])   
    arquivo.close()

def separaArquivo():
    x=3 
    while x<len(arq):
        transicao.append(arq[x].split(" "))
        x+=1

def defineTransicao(est):
	if est == "":
		return -1
	else:
		return int(est)

def automato():
	k = 0
	estado = 0
	palavra = arq[0]
	while k < len(palavra):
		est=estado
		if palavra[k] == '0':
			estado = defineTransicao(transicao[estado][1][1:])
		else:
			estado = defineTransicao(transicao[estado][2][1:])
		if estado == -1:
			break
		print("Delta(q{},{})=q{}".format(est,palavra[k],estado))
		k+=1
	if estado == int(arq[2][1:]):
		print("A cadeia foi aceita")
	else:
		print("A cadeia foi rejeitada")

leArquivo(argv[1])

separaArquivo()

automato()