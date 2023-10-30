import os
os.system("cls")

amarelo = "\033[33m"
azul = "\033[34m"
azulClaro = "\033[94m"
fimCor = "\033[m"

cabecalhos = ["Título do Livro", "Favorito", "Autor", "Categoria", "Valor"]
livro1 = ["Círculo de Fogo", "★", "Nora Robertis", "Ficção", "253.25"]
livro2 = ["Senhos dos Anéis: A Nova Era", "-", "André Boarte Silvaas", "Comédia Romântica", "73.53"]

linha = "| {:<30} | {:^9} | {:^22} | {:^20} | {:^10} "
# Imprimir encabezados de la tabla
cabecalho = linha.format(cabecalhos[0], cabecalhos[1], cabecalhos[2], cabecalhos[3], cabecalhos[4])

# Imprimir información de los libros
#linha1 = linha.format(livro1[0], livro1[1], livro1[2], livro1[3], livro1[4])
#linha2 = linha.format(livro2[0], livro2[1], livro2[2], livro2[3], livro2[4])

favorito = amarelo + livro1[1] + fimCor
print(cabecalho)
print("=" * len(cabecalho))
if livro1[1] == "★":
    print(linha.format(livro1[0], livro1[1], livro1[2], livro1[3], livro1[4]))
else:
    print(linha.format(livro1[0], livro1[1], livro1[2], livro1[3], livro1[4]))

if livro2[1] == "★":
    print(linha.format(livro2[0], amarelo + livro2[1] + fimCor, livro2[2], livro2[3], livro2[4]))
else:
    print(linha.format(livro2[0], livro2[1], livro2[2], livro2[3], livro2[4]))

#print(linha2)
print("-" * len(cabecalho))
