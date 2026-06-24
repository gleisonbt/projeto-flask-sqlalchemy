from models.professor_model import Professor


class ListarProfessoresService:
    def executar(self):
        professores = Professor.listar_todos()
        return [professor.to_dict() for professor in professores]
