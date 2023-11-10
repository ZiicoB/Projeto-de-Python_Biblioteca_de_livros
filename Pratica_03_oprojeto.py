import os
os.system("cls")

arquivoLivros = "teste.csv"
arquivoCategorias = "Categorias.csv"
# /\ Registro de novas categorias e verificação das ja registradas.

#comandos retorno
enter = "x5s8e2"

#cores 
vermelho = "\033[91m"
verde = "\033[32m"
amarelo = "\033[33m"
azul = "\033[34m"
azulClaro = "\033[94m"
fimCor = "\033[m"

# Formatação dos Menus
separador = "=-="*8
menuMain = "{:<3}{}".format("",f"{azul} MENU PRINCIPAL {fimCor}")
menMeusLivros = "{:<6}{}".format("",f"{azul}MEUS LIVROS{fimCor}")
menNovoLivro = "{:<6}{}".format("",f"{azul}NOVO LIVRO{fimCor}")


def principalMenu(): #Terminado
    print(f"{separador}\n{menuMain}\n{separador}")
    
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
    print(f"{separador}\n{menMeusLivros}\n{separador}")
    
    print(f"1- Novo Livro\n2- Lista por Categoria\n3- Lista por Altor\n4- Alterar Livro\n0- Voltar")
    print("=-="*8)    
    opMeusLivros = int(input("Opção: "))
    if opMeusLivros == 1:
        os.system("cls")
        novoLivro()
    elif opMeusLivros == 2:
        os.system("cls")
        listaCategoria()
        

def novoLivro():
    print(f"{separador}\n{menNovoLivro}\n{separador}")
    
    with open(arquivoLivros, "a", encoding="utf-8") as biblioteca:
        
        nomeLivro = input("Nome do Livro: ")
        os.system("cls")
        
        print(f"{separador}\n{menNovoLivro}\n{separador}")
        print(f"É um livro {amarelo}Favorito{fimCor} ?")
        print("1- Sim\n2- Não")
        print("=-="*8)
        favoritar = int(input("Opção: "))
        if favoritar == 1:
            favorito = "★"
        elif favoritar == 2:
            favorito ="~"
        else:
            print("Está é uma opção invalida.\n{vermelho}(ENTER){fimCor} para voltar")
            voltar = input()
            if voltar != startar:
                os.system("cls")
                meusLivros()
        os.system("cls")
        
        print(f"{separador}\n{menNovoLivro}\n{separador}")
        with open(arquivoLivros, "r", encoding="utf-8") as categorias:
            # Adicionar a leitura do arquivo
            for i ,linhas in range(categorias):
                print(f"{linhas}")
                
        categoria = input("Categoria do livro: ")
        os.system("cls")
        
        print(f"{separador}\n{menNovoLivro}\n{separador}")
        altor = input("Nome do autor: ")
        os.system("cls")
        
        print(f"{separador}\n{menNovoLivro}\n{separador}")
        valor = float(input("Valor do livro: "))
        
        os.system("cls")
        
        print(f"{separador}\n{menNovoLivro}\n{separador}")    
        biblioteca.write(f"{nomeLivro},{favorito},{categoria},{altor},{valor}\n")
        print("\nLivro adicionado com sucesso!\n")
        biblioteca.close()
        
                
           
        for i, catG in enumerate(listaCateg):
            print(f"{i + 1}- {catG}")
            
def listaCategoria():
    h
    
###################################################################
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