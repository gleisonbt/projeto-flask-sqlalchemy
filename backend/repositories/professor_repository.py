from sqlalchemy import text

from models.database import db
from models.professor_model import Professor


class ProfessorRepository:
    """
    Repository usado para consultas que vão além do CRUD básico da Model.

    Neste exemplo, o caso de uso é buscar professores ativos por disciplina.
    Quando o projeto está usando MySQL, o Repository encapsula o CALL da
    stored procedure sp_professores_por_disciplina.
    """

    @staticmethod
    def buscar_por_disciplina(disciplina):
        banco = db.session.get_bind().dialect.name

        if banco == "mysql":
            sql = text("CALL sp_professores_por_disciplina(:disciplina)")
            resultado = db.session.execute(sql, {"disciplina": disciplina})
            linhas = resultado.mappings().all()
            resultado.close()

            return [Professor(**dict(linha)) for linha in linhas]

        # Fallback apenas para facilitar os testes locais com SQLite em sala.
        # No MySQL, a consulta fica na procedure e o CALL fica neste Repository.
        return (
            Professor.query
            .filter(Professor.disciplina == disciplina)
            .filter(Professor.ativo.is_(True))
            .order_by(Professor.nome.asc())
            .all()
        )
