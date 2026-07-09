from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from services.criar_professor_service import CriarProfessorService
from services.listar_professores_service import ListarProfessoresService
from services.buscar_professor_por_id_service import BuscarProfessorPorIdService
from services.atualizar_professor_service import AtualizarProfessorService
from services.deletar_professor_service import DeletarProfessorService
from services.buscar_professores_por_disciplina_service import BuscarProfessoresPorDisciplinaService
from models.database import db

professor_controller = Blueprint("professor_controller", __name__)


@professor_controller.post("/professores")
def criar_professor():
    try:
        dados = request.get_json() or {}
        service = CriarProfessorService()
        professor = service.executar(dados)
        return jsonify(professor), 201

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"erro": "Erro ao salvar professor no banco de dados."}), 500


@professor_controller.get("/professores")
def listar_professores():
    service = ListarProfessoresService()
    professores = service.executar()
    return jsonify(professores), 200


@professor_controller.get("/professores/por-disciplina")
def buscar_professores_por_disciplina():
    try:
        disciplina = request.args.get("disciplina")
        service = BuscarProfessoresPorDisciplinaService()
        professores = service.executar(disciplina)
        return jsonify(professores), 200

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"erro": "Erro ao buscar professores por disciplina."}), 500


@professor_controller.get("/professores/<int:professor_id>")
def buscar_professor_por_id(professor_id):
    service = BuscarProfessorPorIdService()
    professor = service.executar(professor_id)

    if professor is None:
        return jsonify({"erro": "Professor não encontrado."}), 404

    return jsonify(professor), 200


@professor_controller.put("/professores/<int:professor_id>")
def atualizar_professor(professor_id):
    try:
        dados = request.get_json() or {}
        service = AtualizarProfessorService()
        professor = service.executar(professor_id, dados)

        if professor is None:
            return jsonify({"erro": "Professor não encontrado."}), 404

        return jsonify(professor), 200

    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"erro": "Erro ao atualizar professor no banco de dados."}), 500


@professor_controller.delete("/professores/<int:professor_id>")
def deletar_professor(professor_id):
    try:
        service = DeletarProfessorService()
        professor_deletado = service.executar(professor_id)

        if professor_deletado is False:
            return jsonify({"erro": "Professor não encontrado."}), 404

        return "", 204

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"erro": "Erro ao deletar professor no banco de dados."}), 500
