import random
import webbrowser

def salvar_filmes_em_arquivo(filmes, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for filme in filmes:
            arquivo.write(filme + '\n')

def ler_filmes_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            filmes = [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        filmes = []
    return filmes

def realizar_sorteio(filmes):
    if not filmes:
        print("A lista de filmes está vazia. Adicione filmes antes de fazer o sorteio.")
        return None, None

    indice_sorteado = random.randrange(len(filmes))
    filme_sorteado = filmes[indice_sorteado]

    return filme_sorteado, indice_sorteado

def main():
    nome_arquivo = "lista_de_filmes.txt"

    filmes = ler_filmes_do_arquivo(nome_arquivo)

    print("Bem-vindo ao sorteio de filmes!")

    while True:
        print("\nOpções:")
        print("1 - Adicionar filme")
        print("2 - Realizar sorteio")
        print("3 - Sair")

        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == '1':
            entrada_filmes = input("Digite os nomes dos filmes, separados por vírgula: ")

            # Dividir a string de filmes em uma lista usando a vírgula como separador
            novos_filmes = entrada_filmes.split(',')

            # Remover espaços em branco no início e no final de cada nome de filme
            novos_filmes = [filme.strip() for filme in novos_filmes]

            # Adicionar os novos filmes à lista existente
            filmes.extend(novos_filmes)

            salvar_filmes_em_arquivo(filmes, nome_arquivo)

            print("Filmes adicionados com sucesso!")

        elif opcao == '2':
            filme_sorteado, indice_sorteado = realizar_sorteio(filmes)
            if filme_sorteado is not None:
                print(f"O filme sorteado é: {filme_sorteado}")

                # Remover o filme sorteado da lista
                filmes.pop(indice_sorteado)
                salvar_filmes_em_arquivo(filmes, nome_arquivo)

                # Perguntar ao usuário se deseja pesquisar sobre o filme
                resposta_pesquisa = input("Deseja pesquisar sobre o filme no Google? (S/N): ")
                if resposta_pesquisa.lower() == 's':
                    pesquisa = filme_sorteado.replace(" ", "+")  # Substituir espaços por '+'
                    url = f"https://www.google.com/search?q={pesquisa}"
                    webbrowser.open(url)

        elif opcao == '3':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Escolha uma opção válida (1/2/3).")

if __name__ == "__main__":
    main()
