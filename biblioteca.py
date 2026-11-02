from livro import Livro
import json

class Biblioteca:
    def __init__(self) -> None:
        self.livros: list[Livro] = []


    def adicionar_livro(self, livro: Livro) -> None:
        self.livros.append(livro)


    def listar_livros(self) -> None:
        for livro in self.livros:
            print(livro)


    def buscar_livro(self, titulo: str) -> Livro | None:
        if not titulo:
            raise ValueError("Título vazio!")

        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None


    def emprestar_livro(self, titulo: str) -> None:        
        livro = self.buscar_livro(titulo)

        if livro is None:
            raise ValueError("Livro não encontrado!")
        
        livro.emprestar_livro()


    def devolver_livro(self, titulo: str) -> None:
        livro = self.buscar_livro(titulo)

        if livro is None:
            raise ValueError("Livro não encontrado!")
        
        livro.devolver_livro()


    def salvar_em_json(self) -> None:
        livros_para_salvar = []

        for livro in self.livros:
            livros_para_salvar.append(livro.para_dict())

        with open(
            "biblioteca.json",
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                livros_para_salvar,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

    def carregar_json(self) -> None:
        with open(
            "biblioteca.json",
            "r",
            encoding="utf-8"
        ) as arquivo:

            dados = json.load(arquivo)

            self.livros = []

            for livro_dict in dados:
                livro = Livro.de_dict(livro_dict)
                self.livros.append(livro)