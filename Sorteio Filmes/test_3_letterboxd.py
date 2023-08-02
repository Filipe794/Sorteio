import random
import tkinter as tk
from tkinter import messagebox
import webbrowser
from unidecode import unidecode  # Importar a função unidecode

def realizar_sorteio():
    global filmes

    if not filmes:
        messagebox.showinfo("Lista Vazia", "A lista de filmes está vazia. Adicione filmes antes de fazer o sorteio.")
        return

    filme_sorteado = random.choice(filmes)
    filmes.remove(filme_sorteado)

    # Remover os acentos da palavra sorteada
    filme_sorteado_sem_acentos = unidecode(filme_sorteado)

    lbl_resultado.config(text=f"O filme sorteado é: {filme_sorteado}")
    salvar_filmes_em_arquivo()

    pesquisa = filme_sorteado_sem_acentos.replace(" ", "+")  # Substituir espaços por '+'
    url_google = f"https://www.google.com/search?q={pesquisa}"
    webbrowser.open(url_google)

    url_letterboxd = f"https://letterboxd.com/search/{pesquisa}/"
    webbrowser.open_new_tab(url_letterboxd)

def adicionar_filmes():
    global filmes

    entrada_filmes = ent_filmes.get()

    novos_filmes = entrada_filmes.split(',')

    novos_filmes = [filme.strip() for filme in novos_filmes]

    filmes.extend(novos_filmes)
    salvar_filmes_em_arquivo()

    ent_filmes.delete(0, tk.END)
    messagebox.showinfo("Filmes Adicionados", "Filmes adicionados com sucesso!")

def salvar_filmes_em_arquivo():
    global filmes

    with open("lista_de_filmes.txt", 'w') as arquivo:
        for filme in filmes:
            arquivo.write(filme + '\n')

def ler_filmes_do_arquivo():
    try:
        with open("lista_de_filmes.txt", 'r') as arquivo:
            filmes = [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        filmes = []
    return filmes

def main():
    global filmes, ent_filmes, lbl_resultado

    root = tk.Tk()
    root.title("Sorteio de Filmes")
    root.geometry("400x300")

    filmes = ler_filmes_do_arquivo()

    lbl_instrucao = tk.Label(root, text="Digite os nomes dos filmes, separados por vírgula:")
    lbl_instrucao.pack(pady=10)

    ent_filmes = tk.Entry(root, width=50)
    ent_filmes.pack(pady=5)

    btn_adicionar = tk.Button(root, text="Adicionar Filmes", command=adicionar_filmes)
    btn_adicionar.pack(pady=5)

    lbl_resultado = tk.Label(root, text="")
    lbl_resultado.pack(pady=20)

    btn_sorteio = tk.Button(root, text="Realizar Sorteio", command=realizar_sorteio)
    btn_sorteio.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
