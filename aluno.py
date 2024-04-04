class Aluno:
    def __init__(self, nome: str, idade: int, curso: str, nota: float):
        self.matricula = 0
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def __repr__(self):
        return f"({self.nome}, {self.idade}, {self.curso}, {self.nota})"


if __name__ == "__main__":
    print(Aluno('Rodrigo', 21, 'Python', 8.5))
