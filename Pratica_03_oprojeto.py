import os
os.system("cls")

#Generos existentes para verificação e adição de novos generos (ja que não pode ser dividido em mais de 1 arquivo)
generos = ["Romance","Biografia","Fantasia","Infantil","Ficção","Aventura","Policial","Terror"]

#comandos retorno
enter = "x5s8e2"
#Teste de envio
#cores 
vermelho = "\033[91m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
azulClaro = "\033[94m"
fimCor = "\033[m"

# menu principal
menuMain = "{:<3}{}".format("",f"{azul} MENU PRINCIPAL {fimCor}")

menu = "{} {}".format("\t","R$")

def principalMenu(): #Terminado
    print("=-="*8)
    print(f"{menuMain}")
    print("=-="*8)
    
    print(f"{verde}1) Meus Livros\n2) Quero Comprar{fimCor}\n{vermelho}0) Sair{fimCor}")
    opMenuMain= int(input("Opção: "))
    os.system("cls")
    
    if opMenuMain == 1:
        os.system("cls")
        meusLivros()
    elif opMenuMain == 2:
        os.system("cls")
        queroComprar()        
    elif opMenuMain == 0:
        os.system("cls")
        print(f"{vermelho}PROGRAMA FINALIZADO!{fimCor}")
        return
    else:
        print(f"{vermelho}Opção não valida !\n(Enter) para retornar.{fimCor}")
        retorno1 = input()
        if (retorno1 != enter):
            os.system("cls")
            principalMenu()



def meusLivros():
    print("=-="*8)
    print("{:<5}{}".format("",f"{azul}MEUS LIVROS{fimCor}"))
    print("=-="*8)

    with open("teste.csv", "r", encoding="utf-8") as biblioteca: #"r" leitura "rt+"
        linhas = biblioteca.readlines()
        #read() => le todo o arquivo como uma so informação
        #readlines() => le cada linha separada do arquivo
        #write() =>adicionar uma informação na linha usanro "W" "A"
        linha  = "| {:<30} | {:^9} | {:^22} | {:^20} | {:^10} "
        linha2 = "| {:<30} | {:^9} | {:^22} | {:^20} | R${:^10} "
        cabecalho = linha.format("Título do Livro","Favorito","Autor","Categoria","Valor")
        
        print(cabecalho)
        print("=" * len(cabecalho))

        somatotal = 0
        for informacao in linhas:
            info = informacao.strip().split(",") #retira espaçamentos e le velores apos a virgula
            nome = info[0]
            favorito = info[1]
            categoria = info[2]
            altor = info[3]
            valor = float(info[4])

            print(linha2.format(nome,favorito,categoria,altor,valor))
            somatotal += valor
        print("=" * len(cabecalho))
        print(f"Valor total da coleção: R$ {somatotal}\n")

    
        


def queroComprar():
    print("=-="*8)
    print("{:<5}{}".format("",f"{azul}QUERO COMPRAR{fimCor}"))
    print("=-="*8)



def startar():
    print("=-="*8)
    print("{:<2}{}".format("",f"{vermelho}(ENTER){fimCor} Para iniciar"))
    print("=-="*8)
    start = input("")
    if start != enter:
        os.system("cls")
        principalMenu()
startar()