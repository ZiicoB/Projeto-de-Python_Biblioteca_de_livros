import os
os.system("cls")

#Categorias existentes para verificação e adição de novas Categorias (ja que não pode ser dividido em mais de 1 arquivo)
categorias = ["Romance","Biografia","Fantasia","Infantil","Ficção","Aventura","Policial","Terror"]

#comandos retorno
enter = "x5s8e2"

#cores 
vermelho = "\033[91m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
azulClaro = "\033[94m"
fimCor = "\033[m"

# menu principal
menuMain = "{:<3}{}".format("",f"{azul} MENU PRINCIPAL {fimCor}")

def principalMenu(): #Terminado
    print("=-="*8)
    print(f"{menuMain}")
    print("=-="*8)
    
    print(f"1- Meus Livros\n2- Lista de Desejos\n0- Encerrar")
    print("=-="*8)
    opMenuMain= int(input("Opção: "))
    os.system("cls")
    
    if opMenuMain == 1:
        os.system("cls")
        meusLivros()
    elif opMenuMain == 2:
        os.system("cls")
        listaDesejos()        
    elif opMenuMain == 0: # Fazer tratramento de erro para (Caracter e Str)
        os.system("cls")
        print(f"{vermelho}PROGRAMA FINALIZADO!{fimCor}\n")
        return
    else:
        print(f"{vermelho}Opção não valida !{fimCor}\nPressione {vermelho}(Enter){fimCor}.")
        retorno1 = input()
        if (retorno1 != enter):
            os.system("cls")
            principalMenu()


def meusLivros():
    print("=-="*8)
    print("{:<6}{}".format("",f"{azul}MEUS LIVROS{fimCor}"))
    print("=-="*8)
    
    print(f"1- Novo Livro\n2- Lista por Categoria\n3- Lista por Altor\n4- Alterar Livro\n0- Voltar")
    print("=-="*8)
    opMeusLivros= int(input("Opção: "))
    os.system("cls")


def listaDesejos():
    print("=-="*8)
    print("{:<4}{}".format("",f"{azul}LISTA DE DESEJOS{fimCor}"))
    print("=-="*8)

    print(f"1- Novo Livro\n2- Alterar Livro\n0- Voltar")
    print("=-="*8)
    opMeusLivros= int(input("Opção: "))
    os.system("cls")


def startar():
    print("=-="*8)
    print("{:<2}{}".format("",f"{vermelho}(ENTER){fimCor} Para iniciar"))
    print("=-="*8)
    start = input("")
    if start != enter:
        os.system("cls")
        principalMenu()
startar()