from models.professor_model import Professor


class BuscarProfessorPorIdService:
    def executar(self, professor_id):
        professor = Professor.buscar_por_id(professor_id)

        if professor is None:
            return None

        return professor.to_dict()
