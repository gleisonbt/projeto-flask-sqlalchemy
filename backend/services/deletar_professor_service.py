from models.professor_model import Professor


class DeletarProfessorService:
    def executar(self, professor_id):
        professor = Professor.buscar_por_id(professor_id)

        if professor is None:
            return False

        professor.deletar()
        return True
