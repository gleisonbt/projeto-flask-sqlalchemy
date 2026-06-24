from models.professor_model import Professor


class AtualizarProfessorService:
    def executar(self, professor_id, dados):
        professor = Professor.buscar_por_id(professor_id)

        if professor is None:
            return None

        novo_email = dados.get("email")
        if novo_email:
            professor_com_email = Professor.buscar_por_email(novo_email)
            if professor_com_email and professor_com_email.id != professor.id:
                raise ValueError("Já existe outro professor cadastrado com este e-mail.")

        professor.atualizar(
            nome=dados.get("nome"),
            email=dados.get("email"),
            disciplina=dados.get("disciplina"),
        )

        return professor.to_dict()
