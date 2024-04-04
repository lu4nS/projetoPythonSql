import pymysql.cursors

from aluno import Aluno


class AlunoData:
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='escola',
                                       cursorclass=pymysql.cursors.DictCursor)

    def insert(self, aluno: Aluno):
        with self.conexao.cursor() as cursor:
            try:
                sql = "INSERT INTO alunos (nome, idade, curso, nota) VALUES" \
                      "(%s, %s, %s, %s)"
                cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso, aluno.nota))
                self.conexao.commit()
            except Exception as error:
                print(f'Erro ao inserir! {error}')

    def update(self, aluno: Aluno):
        with self.conexao.cursor() as cursor:
            try:
                sql = "UPDATE alunos SET nome = %s," \
                       "idade = %s, curso = %s, nota = %s WHERE matricula = %s"
                cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso,
                                     aluno.nota, aluno.matricula))
                self.conexao.commit()
            except Exception as error:
                print(f'erro ao atualizar {error}')

    def delete(self, matricula):
        with self.conexao.cursor() as cursor:
            try:
                sql = "DELETE from alunos WHERE matricula = %s"
                cursor.execute(sql, matricula)
                self.conexao.commit()
            except Exception as error:
                print(f'erro ao deletar aluno {error}')

    def deleteAll(self):
        with self.conexao.cursor() as cursor:
            try:
                sql = "DELETE * FROM alunos"
                cursor.execute(sql)
            except Exception as error:
                print(f"erro ao deletar tudo  {error}")

    def select(self):
        with self.conexao.cursor() as cursor:
            sql = 'SELECT * from alunos'
            cursor.execute(sql)
            alunos = cursor.fetchall()
            return alunos

if __name__ == '__main__':
    AlunoData()