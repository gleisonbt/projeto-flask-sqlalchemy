from repositories.professor_repository import ProfessorRepository


class BuscarProfessoresPorDisciplinaService:
    def executar(self, disciplina):
        if not disciplina or not disciplina.strip():
            raise ValueError("O parâmetro 'disciplina' é obrigatório.")

        professores = ProfessorRepository.buscar_por_disciplina(disciplina.strip())
        return [professor.to_dict() for professor in professores]
