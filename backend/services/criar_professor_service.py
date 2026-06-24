from models.professor_model import Professor


class CriarProfessorService:
    def executar(self, dados):
        campos_obrigatorios = ["nome", "email", "disciplina"]

        for campo in campos_obrigatorios:
            if not dados.get(campo):
                raise ValueError(f"O campo '{campo}' é obrigatório.")

        professor_existente = Professor.buscar_por_email(dados["email"])
        if professor_existente:
            raise ValueError("Já existe um professor cadastrado com este e-mail.")

        professor = Professor(
            nome=dados["nome"],
            email=dados["email"],
            disciplina=dados["disciplina"],
        )

        professor.salvar()
        return professor.to_dict()
