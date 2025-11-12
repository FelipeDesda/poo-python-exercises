class Aluno:
    def __init__(self,nome,matricula,curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

class Disciplina:
    def __init__(self,nome,codigo,carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria

if __name__=="__main__":
    a1 = Aluno("João Silva", "2023001", "Engenharia de SOftware")
    a2 = Aluno("Maria Santos", "2023002", "ADS")
    d1 = Disciplina("Progamação Orientada a Objetos", "POO001", "60")
    d2 = Disciplina("IOT", "IOT001", "80")

print(f"Aluno: {a1.nome}, Matrícula: {a1.matricula}, Curso: {a1.curso}")
print(f"Disciplina: {d1.nome}, Código: {d1.codigo}, Carga Horária: {d1.carga_horaria}h")
print(f"Aluno: {a2.nome}, Matrícula: {a2.matricula}, Curso: {a2.curso}")
print(f"Disciplina: {d2.nome}, Código: {d2.codigo}, Carga Horária: {d2.carga_horaria}h")

