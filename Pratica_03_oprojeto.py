import os
os.system("cls")

arquivoLivros = "teste.csv"
arquivoCategorias = "Categorias.csv"
arquivoListaDesejo = "ListaDesejos.csv"
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

#Alinhamentos
linha0 = "| {:<30} | {:^22} | {:^20} | {:^10}" # sem favorito
linha1 = "| {:<30} | {:^9} | {:^22} | {:^20} | {:^10}"  #com favorito
linha2 = "| {:<30} | {:^9} | {:^22} | {:^20} | R${:>9,.2f}" #com favorito e valor
linha3 = "| {:<30} | {:^22} | {:^20} | R${:>9,.2f}" # sem favorito e com valor

# Formatação dos Menus
separador = ("=-="*8)
menuMain = "{:<3}{}".format("",f"{azul} MENU PRINCIPAL {fimCor}")
menuMeusLivros = "{:<6}{}".format("",f"{azul}MEUS LIVROS{fimCor}")
menuNovoLivro = "{:<6}{}".format("",f"{azul}NOVO LIVRO{fimCor}")
menuListaCat = "{:<6}{}".format("",f"{azul}LISTA CATEGORIA{fimCor}")
menuListaAutor = "{:<6}{}".format("",f"{azul}LISTA AUTOR{fimCor}")
menuListaFav = "{:<6}{}".format("",f"{azul}LISTA FAVORITOS{fimCor}")
menuListaComp = "{:<6}{}".format("",f"{azul}LISTA COMPLETA{fimCor}")
menuListaDj = "{:<4}{}".format("",f"{azul}LISTA DE DESEJOS{fimCor}")

#Terminado
def principalMenu():
    print(f"{separador}\n{menuMain}\n{separador}")
    
    print(f"1- Meus Livros\n2- Lista de Desejos\n0- Encerrar")
    print("=-="*8)
    opMenuMain= input("Opção: ")
    os.system("cls")
    
    if opMenuMain == "1":
        os.system("cls")
        meusLivros()
    elif opMenuMain == "2":
        os.system("cls")
        listaDesejos()        
    elif opMenuMain == "0": # Fazer tratramento de erro para (Caracter e Str)
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
    print(f"{separador}\n{menuMeusLivros}\n{separador}")
    
    print(f"1- Novo Livro\n2- Lista por Categoria\n3- Lista por Autor\n4- Lista por Favoritos\n5- Alterar Livros\n0- Voltar")
    print("=-="*8)    
    opMeusLivros = input("Opção: ")
    
    if opMeusLivros == "1":
        os.system("cls")
        novoLivro()
    elif opMeusLivros == "2":
        os.system("cls")
        listaCategoria()
    elif opMeusLivros == "3":
        os.system("cls")
        listaAutor()
    elif opMeusLivros == "4":
        os.system("cls")
        listaFavoritos()
    elif opMeusLivros == "5":
        os.system("cls")
        alterar()
    elif opMeusLivros == "0":
        os.system("cls")
        principalMenu()
    else:
        print(f"{vermelho}Opção não valida !{fimCor}\nPressione {vermelho}(Enter){fimCor}.")
        retorno1 = input()
        if (retorno1 != enter):
            os.system("cls")
            meusLivros()
        
#Terminado
def novoLivro():
    print(f"{separador}\n{menuNovoLivro}\n{separador}")
    
    with open(arquivoLivros, "a", encoding="utf-8") as biblioteca:
        
        nomeLivro = input("Nome do Livro: ").capitalize().strip()
        os.system("cls")
        
        print(f"{separador}\n{menuNovoLivro}\n{separador}")
        print(f"É um livro {amarelo}Favorito{fimCor} ?")
        print("1- Sim\n2- Não")
        print("=-="*8)
        favoritar = int(input("Opção: ")) #Tratar erro ao receber uma Str em vem de Int
        if favoritar == 1:
            favorito = "★"
        elif favoritar == 2:
            favorito ="~"
        else:
            print(f"Está é uma opção invalida.\n{vermelho}(ENTER){fimCor} para voltar")
            voltar = input()
            if voltar != startar:
                os.system("cls")
                meusLivros()
        os.system("cls")
        
        print(f"{separador}\n{menuNovoLivro}\n{separador}")
        with open(arquivoCategorias, "rt+", encoding="utf-8") as categorias:
            linhas = categorias.readlines()
            
            for i,categoria in enumerate(linhas):
                catFormat = categoria.upper().strip()
                print(f"- {catFormat}")
            print(f"\n## {amarelo}Você pode adicionar uma nova categoria{fimCor} ##\n")
            
            categoriaOp = input("Categoria do livro: ").capitalize().strip()
            if categoriaOp in [linha.strip().capitalize() for linha in linhas]:
                os.system("cls")
            else:
                categorias.write(f"{categoriaOp}\n")
                categorias.close()
                os.system("cls")
        
        print(f"{separador}\n{menuNovoLivro}\n{separador}")
        autor = input("Nome do autor: ").capitalize().strip()
        os.system("cls")
        
        print(f"{separador}\n{menuNovoLivro}\n{separador}")
        valor = float(input("Valor do livro: "))
        valor2F = float(f"{valor:.2f}")
        os.system("cls")
        
        print(f"{separador}\n{menuNovoLivro}\n{separador}")    
        biblioteca.write(f"{nomeLivro},{favorito},{categoriaOp},{autor},{valor2F}\n")
        biblioteca.close()
        
        print(f"\nLivro adicionado com sucesso!\nPressione {vermelho}(Enter){fimCor}")
        voltar = input("")
        if voltar != enter:
            os.system("cls")
            meusLivros()


def listaCategoria():
    print()

#Formatação de texto com letras maiusculas e menusculas. >> add nas outras litas
def listaAutor():
    print(f"{separador}\n{menuListaAutor}\n{separador}\n")
    
    with open (arquivoLivros, "r+", encoding="utf-8") as biblioteca:
        linhas = biblioteca.readlines()
        
        nomeAutor = input("Nome do Autor: ").capitalize().strip()
        
        cabecalho = linha1.format("Título do Livro","Favoritos","Categoria","Autor","Valor")
        print(cabecalho)
        print("="* (len(cabecalho)+4))
        
        somaTotal = 0
        for informacao in linhas:
            info = informacao.strip().split(",") #retira espaçamentos e le velores apos a virgula
            nome = info[0]
            favoritos = info[1]
            categoria = info[2]
            autor = info[3]
            valor = float(info[4])
            favorito =  "{:^17}".format(amarelo+favoritos+fimCor)
            
            if autor == nomeAutor and favoritos == "~" :
                print(linha2.format(nome,favoritos,categoria,autor,valor))
                somaTotal += valor
            elif autor == nomeAutor and favoritos == "★":
                print(linha2.format(nome,favorito,categoria,autor,valor))
                somaTotal += valor
            else:
                print(end ="")
        print("="* (len(cabecalho)+4))
        print(f"Valor total da lista: R$ {somaTotal:,.2f}\n")
        print(f"Pressione {vermelho}(Enter){fimCor}")
        voltar = input("")
        if voltar != enter:
            os.system("cls")
            meusLivros()


#Terminado OK
def listaFavoritos():
    print(f"{separador}\n{menuListaFav}\n{separador}\n")
    
    with open (arquivoLivros, "r+", encoding="utf-8") as biblioteca:
        linhas = biblioteca.readlines()
        
        cabecalho = linha1.format("Título do Livro","Favoritos","Categoria","Autor","Valor")
        print(cabecalho)
        print("="* (len(cabecalho)+4))
        
        somaTotal = 0
        for informacao in linhas:
            info = informacao.strip().split(",") #retira espaçamentos e le velores apos a virgula
            nome = info[0]
            favoritos = info[1]
            categoria = info[2]
            autor = info[3]
            valor = float(info[4])
            favorito =  "{:^17}".format(amarelo+favoritos+fimCor)
            
            if favoritos == "★":
                print(linha2.format(nome,favorito,categoria,autor,valor))
                somaTotal += valor
            else:
                print(end ="")
        print("="* (len(cabecalho)+4))
        print(f"Valor total da lista: R$ {somaTotal:,.2f}\n")
        print(f"Pressione {vermelho}(Enter){fimCor}")
        voltar = input("")
        if voltar != enter:
            os.system("cls")
            meusLivros()



def alterar():
    print(f"{separador}\n{menuListaComp}\n{separador}")
    
    with open(arquivoLivros, "r+", encoding="utf-8") as biblioteca:
        linhas= biblioteca.readlines()
        
        cabecalho = linha1.format("Título do Livro","Favoritos","Categoria","Autor","Valor")
        print("\n ",cabecalho)
        print("="* (len(cabecalho)+4))
        
        somaTotal = 0
        for i, informacao in enumerate(linhas):
            info = informacao.strip().split(",")
            nome = info[0]
            favoritos = info[1]
            categoria = info[2]
            autor = info[3]
            valor = float(info[4])
            favorito =  "{:^17}".format(amarelo+favoritos+fimCor)
            
            planilhaM1 = linha2.format(nome,favorito,categoria,autor,valor)
            planilhaM2 = linha2.format(nome,favoritos,categoria,autor,valor)
            if favoritos == "~":
                print(i+1, planilhaM2)
                somaTotal += valor
            else:
                print(i+1, planilhaM1)
                somaTotal += valor
                print(end ="")
                
        print("="* (len(cabecalho)+4))
        print(f"Valor total da lista: R$ {somaTotal:,.2f}\n")
        
        print("1- Alterar\n2- Deletar\n0- Voltar")
        print("=-="*8)
        opAlterar = input("Opção: ")
        
        if opAlterar == "1":
            print("=-="*8)
            editLivro = int(input(f"Numero da linha [1] até [{i+1}]: ")) -1
            
            if editLivro >=0 and editLivro <= len(linhas):
                numLinha = linhas[editLivro]
                info = numLinha.strip().split(",")
                
                novoNome = input("\nNome do Livro: ").capitalize().strip()
                
                print(f"\nÉ um livro {amarelo}Favorito{fimCor} ?")
                print("1- Sim\n2- Não")
                novoFav = input("Opção: ")
                if novoFav == "1":
                    favorito = "★"
                    os.system("cls")
                elif novoFav == "2":
                    favorito ="~"
                    os.system("cls")
                else:
                    print(f"Está é uma opção invalida.\n{vermelho}(ENTER){fimCor} para voltar")
                    voltar = input()
                    if voltar != startar:
                        os.system("cls")
                        alterar()
                
                with open(arquivoCategorias, "rt+", encoding="utf-8") as categorias:
                    linhas = categorias.readlines()
                    
                    for i,categoria in enumerate(linhas):
                        catFormat = categoria.upper().strip()
                        print(f"- {catFormat}")
                    print(f"\n## {amarelo}Você pode adicionar uma nova categoria{fimCor} ##\n")
                    
                    novaCat = input("Categoria do livro: ").capitalize().strip()
                    if novaCat in [linha.strip().capitalize() for linha in linhas]:
                        os.system("cls")
                    else:
                        categorias.write(f"{novaCat}\n")
                        categorias.close()
                        os.system("cls")
                
                novoAutor = input("Nome do autor: ").capitalize().strip()
                os.system("cls")
                
                novoValor = float(input("Valor do livro: "))
                os.system("cls")
                
                info[0] = novoNome
                info[1] = novoFav
                info[2] = novaCat
                info[3] = novoAutor
                info[4] = novoValor
                linhas[editLivro] = ",".join(map(str, info)) + "\n"
                biblioteca.close()
                
                print(f"Livro Atualizado!\nPressione {vermelho}(Enter){fimCor}")
                voltar = input("")
                if voltar != enter:
                    os.system("cls")
                    meusLivros()

        elif opAlterar == "2": 
            del linhas[editLivro]
            print("Linha deletada com sucesso!\nPressione {vermelho}(Enter){fimCor}")
            voltar = input("")
            if voltar != enter:
                os.system("cls")
                meusLivros()
                
        elif opAlterar == "0":
            os.system("cls")
            principalMenu()
        else:
            print("Opação invalida!\nPressione {vermelho}(Enter){fimCor}")
            voltar = input("")
            if voltar != enter:
                os.system("cls")
                meusLivros()

    
            
###################################################################

# Tratamento de erro
def listaDesejos():
    print(f"{separador}\n{menuListaDj}\n{separador}")

    print(f"1- Novo Livro\n2- Exibir e Editar\n0- Voltar")
    print("=-="*8)
    opMeusLivros= input("Opção: ")
    
    if opMeusLivros == "1":
        os.system("cls")
        livroDesejados()
    elif opMeusLivros == "2":
        os.system("cls")
        exibirEditar()
    elif opMeusLivros == "0":
        os.system("cls")
        principalMenu()

# Tratamento de erro
def livroDesejados():
    print(f"{separador}\n{menuNovoLivro}\n{separador}")
    
    with open(arquivoListaDesejo, "a", encoding="utf-8") as ListaDesejos:
        
        nomeLivroDj = input("Nome do Livro: ").capitalize().strip()
        os.system("cls")
        
        print(f"{separador}\n{menuNovoLivro}\n{separador}")
        with open(arquivoCategorias, "rt+", encoding="utf-8") as categorias:
            linhas = categorias.readlines()
            
            for i,categoria in enumerate(linhas):
                catFormat = categoria.upper().strip()
                print(f"- {catFormat}")
            print(f"\n## {amarelo}Você pode adicionar uma nova categoria{fimCor} ##\n")
            
            categoriaOp = input("Categoria do livro: ").capitalize().strip()
            if categoriaOp in [linha.strip().capitalize() for linha in linhas]:
                os.system("cls")
            else:
                categorias.write(f"{categoriaOp}\n")
                categorias.close()
                os.system("cls")
        
        print(f"{separador}\n{menuNovoLivro}\n{separador}")
        autor = input("Nome do autor: ").capitalize().strip()
        os.system("cls")
        
        print(f"{separador}\n{menuNovoLivro}\n{separador}")
        valor = float(input("Valor do livro: "))
        valor2F = float(f"{valor:.2f}")
        os.system("cls")
        
        print(f"{separador}\n{menuNovoLivro}\n{separador}")    
        ListaDesejos.write(f"{nomeLivroDj},{categoriaOp},{autor},{valor2F}\n")
        ListaDesejos.close()
        
        print(f"\nLivro adicionado com sucesso!\nPressione {vermelho}(Enter){fimCor}")
        voltar = input("")
        if voltar != enter:
            os.system("cls")
            listaDesejos()

#Tratamento de erro // Add o Editar
def exibirEditar():
    print(f"{separador}\n{menuListaDj}\n{separador}\n")
    
    with open(arquivoListaDesejo, "a", encoding="utf-8") as ListaDesejos:
        linhas= ListaDesejos.readlines()
        
        cabecalho = linha0.format("Título do Livro","Categoria","Autor","Valor")
        print("\n ",cabecalho)
        print("="* (len(cabecalho)+4))
        
        somaTotal = 0
        for i, informacao in enumerate(linhas):
            info = informacao.strip().split(",")
            nome = info[0]
            categoria = info[1]
            autor = info[2]
            valor = float(info[3])
            
            planilhaM = linha3.format(nome,categoria,autor,valor)
            print(i+1, planilhaM)
            somaTotal += valor

                
        print("="* (len(cabecalho)+4))
        print(f"Valor total da lista: R$ {somaTotal:,.2f}\n")
        
        print("1- Alterar\n2- Deletar\n0- Voltar")
        opAlterar = input("Opção: ")
        
        if opAlterar == "1":
            
            editLivroDJ = int(input(f"Numero do Livro (1) a ({i+1}): ")) -1
            
            if editLivroDJ >=0 and editLivroDJ <= len(linhas):
                numLinha = linhas[editLivroDJ]
                info = numLinha.strip().split(",")
                
                novoNome = input("Nome do Livro: ").capitalize().strip()
                os.system("cls")
                
                with open(arquivoCategorias, "rt+", encoding="utf-8") as categorias:
                    linhas = categorias.readlines()
                    
                    for i,categoria in enumerate(linhas):
                        catFormat = categoria.upper().strip()
                        print(f"{i+1}- {catFormat}")
                    print(f"\n## {amarelo}Você pode adicionar uma nova categoria{fimCor} ##\n")
                    
                    novaCat = input("Categoria do livro: ").capitalize().strip()
                    if novaCat in [linha.strip().capitalize() for linha in linhas]:
                        os.system("cls")
                    else:
                        categorias.write(f"{novaCat}\n")
                        categorias.close()
                        os.system("cls")
                
                novoAutor = input("Nome do autor: ").capitalize().strip()
                os.system("cls")
                
                novoValor = float(input("Valor do livro: "))
                os.system("cls")
                
                info[0] = novoNome
                info[1] = novaCat
                info[2] = novoAutor
                info[3] = novoValor
                linhas[editLivroDJ] = ",".join(map(str,info)) +"\n"
                ListaDesejos.close()
                
                print("Livro Atualizado!\nPressione {vermelho}(Enter){fimCor}")
                voltar = input("")
                if voltar != enter:
                    os.system("cls")
                    meusLivros()

        elif opAlterar == "2": 
            del linhas[editLivroDJ]
            print("Linha deletada com sucesso!\nPressione {vermelho}(Enter){fimCor}")
            voltar = input("")
            if voltar != enter:
                os.system("cls")
                meusLivros()
        
        elif opAlterar == "0":
            os.system("cls")
            meusLivros()
        else:
            print("Opação invalida!\nPressione {vermelho}(Enter){fimCor}")
            voltar = input("")
            if voltar != enter:
                os.system("cls")
                meusLivros()
        
#Terminado ok
def startar():
    print("=-="*8)
    print("{:<2}{}".format("",f"{vermelho}(ENTER){fimCor} Para iniciar"))
    print("=-="*8)
    start = input("")
    if start != enter:
        os.system("cls")
        principalMenu()
startar()