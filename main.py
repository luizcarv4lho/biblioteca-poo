from livro import Livro
from biblioteca import Biblioteca

def exibir_menu() -> str:
    return f"""
    ===Biblioteca===
    
    1 - Cadastrar Livro
    2 - Listar Livros
    3 - Buscar Livro
    4 - Emprestar Livro
    5 - Devolver Livro
    6 - Salvar
    7 - Sair
    """


biblioteca = Biblioteca()

try:
    biblioteca.carregar_json()
except FileNotFoundError:
    pass


while True:
    print(exibir_menu())

    opcao = input("Escolha uma opção: ")

    if opcao == "7":

        biblioteca.salvar_em_json()

        print(
            "Dados salvos."
        )
        
        break
    elif opcao == "1":
        titulo = input(
            "Digite o título: "
        )

        autor = input(
            "Digite o autor: "
        )

        livro = Livro(
            titulo,
            autor
        )

        biblioteca.adicionar_livro(
            livro
        )

        print("Livro cadastrado com sucesso!")
    elif opcao == "2":
        biblioteca.listar_livros()
    elif opcao == "3":
        titulo = input(
            "Digite o título: "
        )

        livro = biblioteca.buscar_livro(
            titulo
        )

        if livro is None:
            print("Livro não encontrado! ")
        else:
            print(livro)
    elif opcao == "4":
        titulo = input(
            "Digite o título do livro: "
        )

        try:
            biblioteca.emprestar_livro(titulo)

            print(
                "Livro emprestado com sucesso!"
            )
        except ValueError as erro:
            print(erro)        
    elif opcao == "5":
        titulo = input(
            "Digite o título do livro: "
        )

        try:
            biblioteca.devolver_livro(titulo)

            print("Livro devolvido com sucesso!")
        except ValueError as erro:
            print(erro)
    elif opcao == "6":
        biblioteca.salvar_em_json()

        print(
            "Biblioteca salva com sucesso!"
        )
    else:
        print("Digite uma opção valida do menu!")