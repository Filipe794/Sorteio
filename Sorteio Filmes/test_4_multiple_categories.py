import random
import tkinter as tk
from tkinter import messagebox
import webbrowser
from unidecode import unidecode

categorias = ["Ação", "Comédia", "Drama", "Romance", "Suspense", "Terror", "Ficção científica", "Documentário"]

ent_filme = None
lbl_resultado = None  # Criar a variável lbl_resultado no escopo global

def realizar_sorteio(categoria):
    global filmes, lbl_resultado  # Adicionar lbl_resultado no escopo global

    if not filmes[categoria]:
        messagebox.showinfo("Lista Vazia", f"A lista de filmes na categoria '{categoria}' está vazia. Adicione filmes antes de fazer o sorteio.")
        return

    filme_sorteado = random.choice(filmes[categoria])
    filmes[categoria].remove(filme_sorteado)

    # Remover os acentos da palavra sorteada
    filme_sorteado_sem_acentos = unidecode(filme_sorteado)

    lbl_resultado.config(text=f"O filme sorteado é: {filme_sorteado}")
    salvar_filmes_em_arquivo(categoria)

    pesquisa = filme_sorteado_sem_acentos.replace(" ", "+")  # Substituir espaços por '+'
    url_google = f"https://www.google.com/search?q={pesquisa}"
    webbrowser.open(url_google)

    url_letterboxd = f"https://letterboxd.com/search/{pesquisa}/"
    webbrowser.open_new_tab(url_letterboxd)

def adicionar_filme(categoria):
    global filmes, ent_filme

    filme = ent_filme.get()
    if filme:
        filmes[categoria].append(filme)
        salvar_filmes_em_arquivo(categoria)
        ent_filme.delete(0, tk.END)
        messagebox.showinfo("Filme Adicionado", f"O filme '{filme}' foi adicionado à categoria '{categoria}'.")
    else:
        messagebox.showwarning("Campo Vazio", "Digite o nome do filme antes de adicionar à categoria.")

def salvar_filmes_em_arquivo(categoria):
    with open(f"lista_de_filmes_{categoria}.txt", 'w') as arquivo:
        for filme in filmes[categoria]:
            arquivo.write(filme + '\n')

def ler_filmes_do_arquivo(categoria):
    try:
        with open(f"lista_de_filmes_{categoria}.txt", 'r') as arquivo:
            filmes_categoria = [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        filmes_categoria = []
    return filmes_categoria

def selecionar_categoria(categoria):
    global root, filmes, ent_filme, lbl_resultado  # Adicionar lbl_resultado no escopo global

    root.withdraw()  # Esconder a janela principal

    filmes[categoria] = ler_filmes_do_arquivo(categoria)

    categoria_window = tk.Toplevel(root)
    categoria_window.title(f"Selecionar Categoria - {categoria}")
    categoria_window.geometry("300x200")

    lbl_instrucao = tk.Label(categoria_window, text=f"Você selecionou a categoria: {categoria}")
    lbl_instrucao.pack(pady=10)

    ent_filme = tk.Entry(categoria_window, width=30)
    ent_filme.pack(pady=5)

    btn_adicionar = tk.Button(categoria_window, text="Adicionar Filme", command=lambda: adicionar_filme(categoria))
    btn_adicionar.pack(pady=5)

    btn_sorteio = tk.Button(categoria_window, text="Realizar Sorteio", command=lambda: realizar_sorteio(categoria))
    btn_sorteio.pack()

    btn_voltar = tk.Button(categoria_window, text="Voltar", command=lambda: [selecionar_categoria_principal(), categoria_window.destroy()])
    btn_voltar.pack()

    lbl_resultado = tk.Label(categoria_window, text="")
    lbl_resultado.pack(pady=20)  # Adicionar lbl_resultado à janela da categoria

def selecionar_categoria_principal():
    root.deiconify()  # Exibir a janela principal

def main():
    global filmes, root

    root = tk.Tk()
    root.title("Sorteio de Filmes")
    root.geometry("400x300")

    filmes = {categoria: [] for categoria in categorias}

    lbl_instrucao = tk.Label(root, text="Selecione uma categoria de filmes:")
    lbl_instrucao.pack(pady=10)

    for categoria in categorias:
        btn_categoria = tk.Button(root, text=categoria, command=lambda c=categoria: selecionar_categoria(c))
        btn_categoria.pack(pady=5)

    btn_sair = tk.Button(root, text="Sair", command=root.quit)
    btn_sair.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
