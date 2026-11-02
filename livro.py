class Livro:
    def __init__(self, titulo: str, autor: str) -> None:
        self.titulo: str = titulo
        self.autor: str = autor
        self.disponivel: bool = True


    def __str__(self) -> str:
        return f"{self.titulo} | {self.autor}"


    def exibir_dados(self) -> str:
        return str(self)


    def emprestar_livro(self) -> None:
        self.disponivel = False


    def devolver_livro(self) -> None:
        self.disponivel = True


    def para_dict(self) -> dict:
        return {
            "titulo": self.titulo,
            "autor" : self.autor,
            "disponivel": self.disponivel
        }

    # Aqui recebo uma classe, com os dados do livro que está em json, e retorno um objeto do tipo Livro, convertendo os dados dicionario criado anteriormente, para um livro novamente.
    @classmethod 
    def de_dict(cls, dados: dict) -> Livro:
        livro = cls(
            dados["titulo"],
            dados["autor"]
        )

        livro.disponivel = dados["disponivel"]

        return livro