import os
os.system("cls")

amarelo = "\033[33m"
azul = "\033[34m"
azulClaro = "\033[94m"
fimCor = "\033[m"

with open("teste.csv", "r", encoding="utf-8") as biblioteca: #"r" leitura "rt+"
    linhas = biblioteca.readlines()
    #read() => le todo o arquivo como uma so informação
    #readlines() => le cada linha separada do arquivo
    #write() =>adicionar uma informação na linha usanro "W" "A"
    linha1  = "| {:<30} | {:^9} | {:^22} | {:^20} | {:^10} "
    linha2 = "| {:<30} | {:^9} | {:^22} | {:^20} | R${:^10,.2f} "
    cabecalho = linha1.format("Título do Livro","Favorito","Categoria","Autor","Valor")
    
    
    print(cabecalho)
    print("=" * len(cabecalho))

    somatotal = 0
    for informacao in linhas:
        info = informacao.strip().split(",")
        nome = info[0]
        favoritos = info[1]
        categoria = info[2]
        autor = info[3]
        valor = float(info[4])
        favorito =  "{:^17}".format(amarelo+favoritos+fimCor)
        
        if favoritos == "★":
            print(linha2.format(nome,favorito,categoria,autor,valor))
        else:
            print(linha2.format(nome,favoritos,categoria,autor,valor))
        somatotal += valor
    print("=" * len(cabecalho))
    print(f"Valor total da coleção: R$ {somatotal}\n")
