import os
os.system("cls")

cabecalhos = ["Título do Livro", "Favorito", "Autor", "Categoria", "Valor"]
livro1 = ["Círculo de Fogo", "★", "Nora Sobertis", "Ficção", "253.25"]
livro2 = ["Senhos dos Anéis: A Nova Era", "-", "André Boarte Silvaas", "Comédia Romântica", "73.53"]

# Imprimir encabezados de la tabla
print("{:<30} {:<14} {:<23} {:<22} {:^10}".format(cabecalhos[0], cabecalhos[1], cabecalhos[2], cabecalhos[3], cabecalhos[4]))
print("=-=" * 35)

# Imprimir información de los libros
print("{:<33} {:<11} {:<23} {:<24} R${:^8}".format(livro1[0], livro1[1], livro1[2], livro1[3], livro1[4]))
print("{:<33} {:<11} {:<23} {:<24} R${:^8}".format(livro2[0], livro2[1], livro2[2], livro2[3], livro2[4]))