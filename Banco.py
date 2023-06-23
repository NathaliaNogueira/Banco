NOME_ARQUIVO = "texto.txt"
#contas = [[1, "Ana", 20], [2, "Felipe", 100], [3, "Maria", 200]]
contas = []

def linha():
    print("-"*30)

def menuprincipal():
    print("-"*30)
    print("{:^30}".format("MENU"))
    print("-"*30)
    print("(1) Inclusão de conta"
 "\n(2) Alteração de saldo"
 "\n(3) Exclusão de conta"
 "\n(4) Relatórios gerenciais"
 "\n(5) Sair do programa")
    print("-"*30)

def grava_conta(contas):
    with open(NOME_ARQUIVO, "w") as arq:
        for conta in contas:
            arq.write(str(conta[0]) + ";" + (conta[1]) + ";" + str(conta[2]) + "\n")
    print("Arquivo gravado")     

def le_contas(contas):
    with open(NOME_ARQUIVO, "r") as arq:
        conta = arq.readline()
        while (conta != ""):
            conta = conta.strip("\n")
            conta = conta.split(";")
            conta[0], conta[2] = int(conta[0]), float(conta[2])
            contas.append(conta)
            conta = arq.readline()
    return contas

def ler_int():
    ok = False
    while not ok:
        try:
            num = int(input("Digite a opção desejada: "))
            ok = True
        except ValueError:
            print("Dígito inválido. Digite novamente.")
    return num

def ler_conta():
    ok = False
    while not ok:
        try:
            num = int(input("Digite o número da conta: "))
            ok = True
        except ValueError:
            print("Dígito inválido. Digite novamente.")
    return num

def pesquisaconta(contas, num):
    while True:
        achou = False
        if num in (i[0] for i in contas):
            print("Erro, número de conta já existe. Digite novamente.")
            achou = True
            num = int(input("Digite o número da conta: "))
        else:
            break
    return achou 

def ler_float():
    ok = False
    while not ok:
        try:
            saldo = float(input("Digite o saldo: "))
            ok = True
        except ValueError:
            print("Dígito inválido. Digite novamente.")
    return saldo

def valida_nome():
    while True:
        nome = input("Digite o nome: ")
        if nome.isdigit():
            print("Erro. Digite novamente.")
        else:
            sobrenome = input("Digite o sobrenome: ")
            if sobrenome.isdigit():
                print("Erro. Digite novamente.")
            else:
                nome = nome + " " + sobrenome
                break
    return nome

def inclusão(contas):
    num = int(input("Digite o número da conta: "))
    linha()
    opcao = pesquisaconta(contas, num) 
    if (opcao == False):
        nome = valida_nome() #função para ler nomes
        linha()
        saldo = ler_float()  #função para ler float
        if (saldo >= 0): 
            lista = [num, nome, saldo]
            contas.append(lista)
            print(contas)
    return num

def menu_cred_deb():
    print("Digite a operação a ser realizada: "
    "\n(1) Crédito"
    "\n(2) Débito")

def pesquisaconta2(contas): #pesquisa conta para função cred/deb e exclusão
    while True:
        try:
            num = int(input("Digite o número da conta: "))
            achou = False
            if num in (i[0] for i in contas):
                achou = True
                break
            else:
                print("Número de conta inválido.")
        except ValueError:
            print("Número de conta inválido.")
    return num

def credito():
    opcao = pesquisaconta2(contas)
    perg_cred = ler_float()
    for j in range(len(contas)):
        if opcao == contas[j][0]:
            pos = j
            contas[pos][2] += perg_cred
            print("Crédito em conta adicionado com sucesso.")
            break
            
def debito():
    opcao = pesquisaconta2(contas)
    perg_deb = ler_float()
    for j in range(len(contas)):
        if opcao == contas[j][0]:
            pos = j
            contas[pos][2] -= perg_deb
            print("Débito realizado com sucesso.")
            break
            
def altera_saldo():
    while True:
        menu_cred_deb()
        pergunta_altera = ler_int()
        if (pergunta_altera == 1): 
            credito()     #função para cred
            print(contas)
            break
        elif (pergunta_altera == 2):
            debito()     #função para deb
            print(contas)
            break
        else:
            print("Opção inválida. Digite novamente.")
    
def exclusão(contas):
    while True:
        exc = pesquisaconta2(contas)
        for i in contas:
            if exc == i[0]:
                pos = i
                contas.remove(pos)
                print(contas)
                break
        return contas 

def saldo_negativo(contas):
    for i in contas:
        pos = i
        if i[2] < 0:
            print(pos)
      
def saldo_acima(contas):
    saldo_acima = ler_float()
    for i in contas:
        pos = i
        if i[2] >= saldo_acima:
            print(pos)

def menu_relatorio():
    print("(1) Lista clientes com saldo negativo"
 "\n(2) Lista de clientes com saldo acima de um valor específico"
 "\n(3) Listar todas as contas"
 "\n(4) Sair do relatório")
    linha()

def relatorio(contas):
    menu_relatorio()
    perg_relatorio = ler_int()
    while True:
        if (perg_relatorio == 1):
            saldo_negativo(contas)
            break
        elif (perg_relatorio == 2):
            saldo_acima(contas)
            break
        elif (perg_relatorio == 3):
            print(contas)
            break
        elif (perg_relatorio == 4):
            print("Fim do relatório")
            linha()
            break
        else:
            print("Dígito inválido. Digite novamente.")
        perg_relatorio = ler_int()


def main():
    menuprincipal()
    escolha = ler_int()
    while True:
        if (escolha == 1): 
            inclusão(contas)
        elif (escolha == 2):
            altera_saldo()
        elif (escolha == 3):
            exclusão(contas)
        elif (escolha == 4):
            relatorio(contas)
        elif (escolha == 5):
            print("Fim do programa")
            break    
        else:
            print("Dígito inválido. Digite novamente.")
        escolha = ler_int()


le_contas(contas) 
main()
print(contas)
grava_conta(contas)
