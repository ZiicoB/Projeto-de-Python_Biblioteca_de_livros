import os
os.system("cls")

arquivoLivros = "Arquivos/Livros.csv"
arquivoCategorias = "Arquivos/Categorias.csv"
arquivoListaDesejo = "Arquivos/ListaDesejos.csv"
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
separador = (f"{azul}=-={fimCor}"*8)
menuStarte = "{:<2}{}".format("",f"{vermelho}(ENTER){fimCor} Para iniciar")
menuMain = "{:<5}{}".format("",f"MENU PRINCIPAL")
menuMeusLivros = "{:<6}{}".format("",f"MEUS LIVROS")
menuNovoLivro = "{:<6}{}".format("",f"NOVO LIVRO")
menuListaCat = "{:<6}{}".format("",f"LISTA CATEGORIA")
menuListaAutor = "{:<6}{}".format("",f"LISTA AUTOR")
menuListaFav = "{:<6}{}".format("",f"LISTA FAVORITOS")
menuListaDj = "{:<4}{}".format("",f"LISTA DE DESEJOS")


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
    elif opMenuMain == "0":
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
    
    print(f"1- Novo Livro\n2- Lista Completa\n3- Lista por Categoria\n4- Lista por Autor\n5- Lista por Favoritos\n0- Voltar")
    print("=-="*8)    
    opMeusLivros = input("Opção: ")
    
    if opMeusLivros == "1":
        os.system("cls")
        novoLivro()
    elif opMeusLivros == "2":
        os.system("cls")
        alterar()
    elif opMeusLivros == "3":
        os.system("cls")
        listaCategoria()
    elif opMeusLivros == "4":
        os.system("cls")
        listaAutor()
    elif opMeusLivros == "5":
        os.system("cls")
        listaFavoritos()
    elif opMeusLivros == "0":
        os.system("cls")
        principalMenu()
    else:
        print(f"{vermelho}Opção não valida !{fimCor}\nPressione {vermelho}(Enter){fimCor}.")
        retorno1 = input()
        if (retorno1 != enter):
            os.system("cls")
            meusLivros()
        

def novoLivro():
    print(f"{separador}\n{menuNovoLivro}\n{separador}")
    
    with open(arquivoLivros, "a", encoding="utf-8") as biblioteca:
        
        nomeLivro = input("Nome do Livro: ").capitalize().strip()
        os.system("cls")
        
        print(f"É um livro {amarelo}Favorito{fimCor} ?")
        print("1- Sim\n2- Não")
        print("=-="*8)
        favoritar = (input("Opção: "))
        if favoritar == "1":
            favorito = "★"
        elif favoritar == "2":
            favorito ="~"
        else:
            print(f"Está é uma opção invalida.\n{vermelho}(ENTER){fimCor} para voltar")
            voltar = input()
            if voltar != startar:
                os.system("cls")
                meusLivros()
        os.system("cls")
        
        with open(arquivoCategorias, "rt+", encoding="utf-8") as categorias:
            linhas = categorias.readlines()
            
            for i,categoria in enumerate(linhas):
                catFormat = categoria.upper().strip()
                print(f"- {catFormat}")
            print(f"\n## {amarelo}Você pode adicionar uma nova categoria{fimCor} ##\n")
            
            categoriaOp = input("Categoria do livro: ").capitalize().strip()
            if categoriaOp in [linha.strip().capitalize() for linha in linhas]:
                categorias.close()
                os.system("cls")
            else:
                categorias.write(f"{categoriaOp}\n")
                categorias.close()
                os.system("cls")
        
        autor = input("Nome do autor: ").capitalize().strip()
        os.system("cls")
        try:
            valor = float(input("Valor do livro: "))
            valor2F = float(f"{valor:.2f}")
            os.system("cls")
        except ValueError:
            print(f"Informação invalida!\nPressione {vermelho}(Enter){fimCor}")
            voltar = input("")
            if voltar != enter:
                os.system("cls")
                meusLivros()
            
        print(f"{separador}\n{menuNovoLivro}\n{separador}")    
        biblioteca.write(f"{nomeLivro},{favorito},{categoriaOp},{autor},{valor2F}\n")
        biblioteca.close()
        
        print(f"\nLivro adicionado com sucesso!\nPressione {vermelho}(Enter){fimCor}")
        voltar = input("")
        if voltar != enter:
            os.system("cls")
            meusLivros()


def listaCategoria():
    print(separador)
    with open (arquivoLivros, "r+", encoding="utf-8") as biblioteca:
        linhas = biblioteca.readlines()
        
        print(separador)
        with open(arquivoCategorias, "r", encoding="utf-8") as categorias:
            linhasCat = categorias.readlines()
            
            
            for i,categoria in enumerate(linhasCat):
                catFormat = categoria.upper().strip()
                print(f"- {catFormat}")
            categorias.close()
            
            print(separador)
            print(f"{vermelho}Voltar{fimCor} => 0")
            nomeCateg = input("Categoria desejada: ").capitalize().strip()
            os.system("cls")

            if nomeCateg in [linha.strip().capitalize() for linha in linhasCat]:
                cabecalhoC = linha1.format("Título do Livro","Favoritos","Categoria","Autor","Valor")
                print(cabecalhoC)
                print(f"{azul}={fimCor}"*  (len(cabecalhoC)+6))
                
                somaTotal = 0
                for informacao in linhas:
                    info = informacao.strip().split(",")
                    nome = info[0]
                    favoritos = info[1]
                    categoria = info[2]
                    autor = info[3]
                    valor = float(info[4])
                    favorito =  "{:^17}".format(amarelo+favoritos+fimCor)
                    
                    if categoria == nomeCateg and favoritos == "~" :
                        print(linha2.format(nome,favoritos,categoria,autor,valor))
                        somaTotal += valor
                    elif categoria == nomeCateg and favoritos == "★":
                        print(linha2.format(nome,favorito,categoria,autor,valor))
                        somaTotal += valor
                    else:
                        print(end ="")
                        
                print(f"{azul}={fimCor}"* (len(cabecalhoC)+6))
                print(f"Valor total: R$ {amarelo}{somaTotal:,.2f}{fimCor} | {vermelho}(Enter){fimCor} Para voltar.")
                voltar = input("")
                if voltar != enter:
                    os.system("cls")
                    meusLivros()
                    
            elif nomeCateg == "0":
                os.system("cls")
                meusLivros()   
            else:
                print(f"Esssa Categoria não existe.\nPressione {vermelho}(Enter){fimCor}")
                voltar = input("")
                if voltar != enter:
                    os.system("cls")
                    listaCategoria()


def listaAutor():
    print(f"{separador}\n{menuListaAutor}\n{separador}\n")
    
    with open (arquivoLivros, "r+", encoding="utf-8") as biblioteca:
        linhas = biblioteca.readlines()
        
        nomeAutor = input("Nome do Autor: ").capitalize().strip()
        os.system("cls")
        print(f"{separador}\n{menuListaAutor}\n{separador}\n")
        cabecalho = linha1.format("Título do Livro","Favoritos","Categoria","Autor","Valor")
        print(cabecalho)
        print(f"{azul}={fimCor}"* (len(cabecalho)+6))
        
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
        print(f"{azul}={fimCor}"* (len(cabecalho)+6))
        print(f"Valor total: R$ {amarelo}{somaTotal:,.2f}{fimCor} | {vermelho}(Enter){fimCor} Para voltar.")
        voltar = input("")
        if voltar != enter:
            os.system("cls")
            meusLivros()


def listaFavoritos():
    print(f"{separador}\n{menuListaFav}\n{separador}\n")
    
    with open (arquivoLivros, "r+", encoding="utf-8") as biblioteca:
        linhas = biblioteca.readlines()
        
        cabecalho = linha1.format("Título do Livro","Favoritos","Categoria","Autor","Valor")
        print(cabecalho)
        print(f"{azul}={fimCor}"* (len(cabecalho)+6))
        
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
        print(f"{azul}={fimCor}"* (len(cabecalho)+6))
        print(f"Valor total: R$ {amarelo}{somaTotal:,.2f}{fimCor} | {vermelho}(Enter){fimCor} Para voltar.")
        voltar = input("")
        if voltar != enter:
            os.system("cls")
            meusLivros()


def alterar():
    with open (arquivoLivros, "r+", encoding="utf-8") as biblioteca:
        linhasL = biblioteca.readlines()

        cabecalho = linha1.format("Título do Livro","Favoritos","Categoria","Autor","Valor")
        print("\n ",cabecalho)
        print(f"{azul}={fimCor}"* (len(cabecalho)+6))

        somaTotal = 0
        for i , livro in enumerate(linhasL):
            infoLivro = livro.strip().split(',')
            
            nome = infoLivro[0]
            favorito = infoLivro[1]
            categoria = infoLivro[2]
            autor = infoLivro[3]
            valor = float(infoLivro[4])

            favoritoS =  "{:^17}".format(amarelo+favorito+fimCor)            
            planilhaM1 = linha2.format(nome,favoritoS,categoria,autor,valor)
            planilhaM2 = linha2.format(nome,favorito,categoria,autor,valor)

            if favorito == "~":
                print(i+1, planilhaM2)
                somaTotal += valor
            else:
                print(i+1, planilhaM1)
                somaTotal += valor

        print(f"{azul}={fimCor}"* (len(cabecalho)+6))
        print(f"Valor total: R$ {amarelo}{somaTotal:,.2f}{fimCor} | {vermelho}(Enter){fimCor} Para voltar.\n")

        print(f"Linhas editaveis [{amarelo}1{fimCor}] até [{amarelo}{i+1}{fimCor}].")
        editarLivro = input("Numero da linha => ")

        if editarLivro.isdigit():
            editarLivros = int(editarLivro) -1

            if editarLivros >= 0 and editarLivros < len(linhasL):
                numeroLinha = linhasL[editarLivros]
                infoLivro = numeroLinha.strip().split(',')
                os.system("cls")
                
                numLinFormat = "| {:<20} | {:^6} | {:^18} | {:^18} | R${:>9}".format(*infoLivro)
                print(f"{azul}={fimCor}"* (len(numLinFormat)+6))
                print(numLinFormat)
                print(f"{azul}={fimCor}"* (len(numLinFormat)+6))
                
                print("\n1- Alterar \n2- Deletar \n0- Voltar\n")
                opAlterar = input("Opção: ")
                
                if opAlterar == '1':
                    os.system("cls")
                    print(separador)
                    novoNome = input("\nNome do Livro: ").capitalize().strip()
                    os.system("cls")
                    
                    print(f"É um livro {amarelo}Favorito{fimCor} ?")
                    print("1- Sim\n2- Não")
                    print(f"{azul}={fimCor}"*8)
                    
                    novoFav = int(input("Opção: ")) #Tratar erro ao receber uma Str em vem de Int
                    if novoFav == 1:
                        novoFavorito = "★"
                    elif novoFav == 2:
                        novoFavorito ="~"
                    else:
                        print(f"Está é uma opção invalida.\nPresione {vermelho}(enter){fimCor}.")
                        voltar = input()
                        if voltar != enter:
                            os.system("cls")
                            alterar()
                    
                    with open(arquivoCategorias, "r", encoding="utf-8") as categorias:
                        linhascat = categorias.readlines()
                        os.system("cls")
                        
                        print(separador)
                        for x,categoria in enumerate(linhascat):
                            catFormat = categoria.upper().strip()
                            print(f"- {catFormat}")
                        print(separador)
                        novaCat = input("Categoria do livro: ").capitalize().strip()
                        if novaCat not in [linha.strip().capitalize() for linha in linhascat]:
                            os.system("cls")
                            print(f"Essa Categoria não existe!\nPressione {vermelho}(Enter){fimCor}")
                            voltar = input()
                            if voltar != enter:
                                os.system("cls")
                                exibirEditar()
                    categorias.close()
                    os.system("cls")

                    novoAutor = input("Nome do autor: ").capitalize().strip()
                    os.system("cls")
                    try:
                        novoValor = float(input("Valor do livro: "))
                        os.system("cls")
                    except ValueError:
                        print(f"Informação invalida!\nPressione {vermelho}(Enter){fimCor}")
                        voltar = input("")
                        if voltar != enter:
                            os.system("cls")
                            meusLivros()

                    infoLivro[0] = novoNome
                    infoLivro[1] = novoFavorito
                    infoLivro[2] = novaCat
                    infoLivro[3] = novoAutor
                    infoLivro[4] = novoValor
                    linhasL[editarLivros] =",".join(map(str, infoLivro)) + "\n"
                    print("\n",linhasL[editarLivros])
                    #Vai atualizar a linha
                    with open(arquivoLivros, "w", encoding="utf-8") as biblioteca:
                        biblioteca.writelines(linhasL)
                        biblioteca.close()
                    os.system("cls")
                    print(f"Livro Atualizado!\nPressione {vermelho}(Enter){fimCor}")
                    voltar = input()
                    if voltar != enter:
                        os.system("cls")
                        alterar()

                elif opAlterar == '2':
                    del linhasL[editarLivros]
                    with open(arquivoLivros, "w", encoding="utf-8") as biblioteca:
                        biblioteca.writelines(linhasL)
                        biblioteca.close()
                    os.system("cls")
                    print(f"Livro deletado !\nPressione {vermelho}(Enter){fimCor}")
                    voltar = input()
                    if voltar != enter:
                        os.system("cls")
                        alterar()

                elif opAlterar == '0':
                    biblioteca.close()
                    os.system("cls")
                    meusLivros()

                else:
                    voltar = input(f"Opção invalida\nPresione {vermelho}enter{fimCor}.")
                    if voltar != enter:
                        os.system("cls")
                        alterar()
            else:
                os.system("cls")
                meusLivros()
        else:
            os.system("cls")
            meusLivros()
            
#===== Funções a adicionadas a parte =====#

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


def livroDesejados():
    print(f"{separador}\n{menuNovoLivro}\n{separador}")
    
    with open(arquivoListaDesejo, "a", encoding="utf-8") as ListaDesejos:
        
        nomeLivroDj = input("Nome do Livro: ").capitalize().strip()
        os.system("cls")
        
        with open(arquivoCategorias, "rt+", encoding="utf-8") as categorias:
            linhas = categorias.readlines()
            
            print(separador)
            for i,categoria in enumerate(linhas):
                catFormat = categoria.upper().strip()
                print(f"- {catFormat}")
            print(separador)
            print(f"# {amarelo}Você pode adicionar uma nova categoria{fimCor} #\n")
            
            categoriaOp = input("Categoria do livro: ").capitalize().strip()
            if categoriaOp in [linha.strip().capitalize() for linha in linhas]:
                os.system("cls")
            else:
                categorias.write(f"{categoriaOp}\n")
                categorias.close()
                os.system("cls")
        
        autor = input("Nome do autor: ").capitalize().strip()
        os.system("cls")
        try:
            valor = float(input("Valor do livro: "))
            valor2F = float(f"{valor:.2f}")
            os.system("cls")
        except ValueError:
            print(f"Informação invalida!\nPressione {vermelho}(Enter){fimCor}")
            voltar = input("")
            if voltar != enter:
                os.system("cls")
                meusLivros()
         
        ListaDesejos.write(f"{nomeLivroDj},{categoriaOp},{autor},{valor2F}\n")
        ListaDesejos.close()
        
        print(f"\nLivro adicionado com sucesso!\nPressione {vermelho}(Enter){fimCor}")
        voltar = input("")
        if voltar != enter:
            os.system("cls")
            listaDesejos()


def exibirEditar():
    with open(arquivoListaDesejo, "r+", encoding="utf-8") as ListaDesejos:
        linhasF= ListaDesejos.readlines()
        
        cabecalho = linha0.format("Título do Livro","Categoria","Autor","Valor")
        print("\n ",cabecalho)
        print(f"{azul}={fimCor}"* (len(cabecalho)+6))
        
        somaTotal = 0
        for i, livro in enumerate(linhasF):
            info = livro.strip().split(",")

            nome = info[0]
            categoria = info[1]
            autor = info[2]
            valor = float(info[3])
            
            planilhaM = linha3.format(nome,categoria,autor,valor)
            print(i+1, planilhaM)
            somaTotal += valor

        print(f"{azul}={fimCor}"* (len(cabecalho)+6))
        print(f"Valor total: R$ {amarelo}{somaTotal:,.2f}{fimCor} | {vermelho}(Enter){fimCor} Para voltar.\n")

        print(f"Linhas editaveis [{amarelo}1{fimCor}] até [{amarelo}{i+1}{fimCor}].")
        editarLivro = input("Numero da linha => ")

        if editarLivro.isdigit():
            editarLivros = int(editarLivro) -1

            if editarLivros >= 0 and editarLivros < len(linhasF):
                numeroLinha = linhasF[editarLivros]
                info = numeroLinha.strip().split(',')
                os.system("cls")
                
                numLinFormatt = "| {:<20} | {:^18} | {:^18} | R${:>9}".format(*info)
                print(f"{azul}={fimCor}"* (len(numLinFormatt)+6))
                print(numLinFormatt)
                print(f"{azul}={fimCor}"* (len(numLinFormatt)+6))
                
                print("\n1- Alterar \n2- Deletar \n0- Voltar\n")
                opAlterar = input("Opção: ")

                if opAlterar == '1':
                    os.system("cls")
                    print(f"{azul}=-={fimCor}"*8)
                    
                    novoNome = input("Nome do Livro: ").capitalize().strip()
                    os.system("cls")
                    
                    with open(arquivoCategorias, "r", encoding="utf-8") as categorias:
                        linhascat = categorias.readlines()
                        os.system("cls")
                        
                        for x,categoria in enumerate(linhascat):
                            catFormat = categoria.upper().strip()
                            print(f"- {catFormat}")
                        
                        novaCat = input("Categoria do livro: ").capitalize().strip()
                        if novaCat not in [linha.strip().capitalize() for linha in linhascat]:
                            os.system("cls")
                            print(f"Essa Categoria não existe!\nPressione {vermelho}(Enter){fimCor}")
                            voltar = input()
                            if voltar != enter:
                                os.system("cls")
                                exibirEditar()
                    categorias.close()
                    os.system("cls")
                    
                    novoAutor = input("Nome do autor: ").capitalize().strip()
                    os.system("cls")
                    try:
                        novoValor = float(input("Valor do livro: "))
                        os.system("cls")
                    except ValueError:
                        print(f"Informação invalida!\nPressione {vermelho}(Enter){fimCor}")
                        voltar = input("")
                        if voltar != enter:
                            os.system("cls")
                            meusLivros()

                    info[0] = novoNome
                    info[1] = novaCat
                    info[2] = novoAutor
                    info[3] = novoValor
                    linhasF[editarLivros] =",".join(map(str, info)) + "\n"
                    #Vai atualizar a linha
                    with open(arquivoListaDesejo, "w", encoding="utf-8") as ListaDesejos:
                        ListaDesejos.writelines(linhasF)
                        ListaDesejos.close()
                    os.system("cls")
                    print(f"Livro Atualizado!\nPressione {vermelho}(Enter){fimCor}")
                    voltar = input()
                    if voltar != enter:
                        os.system("cls")
                        exibirEditar()

                elif opAlterar == '2':
                    del linhasF[editarLivros]
                    with open(arquivoListaDesejo, "w", encoding="utf-8") as ListaDesejos:
                        ListaDesejos.writelines(linhasF)
                        ListaDesejos.close()
                    os.system("cls")
                    print(f"Livro deletado !\nPressione {vermelho}(Enter){fimCor}")
                    voltar = input()
                    if voltar != enter:
                        os.system("cls")
                        exibirEditar()

                elif opAlterar == '0':
                    ListaDesejos.close()
                    os.system("cls")
                    listaDesejos()

                else:
                    os.system("cls")
                    voltar = input(f"Opção invalida\nPresione {vermelho}enter{fimCor}.")
                    if voltar != enter:
                        os.system("cls")
                        exibirEditar()
            else:
                os.system("cls")
                listaDesejos()
        else:
            os.system("cls")
            listaDesejos()
        

def startar():
    print(f"{separador}\n{menuStarte}\n{separador}")
    start = input("")
    if start != enter:
        os.system("cls")
        principalMenu()
startar()