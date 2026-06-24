from .database import db


class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    disciplina = db.Column(db.String(100), nullable=False)

    def salvar(self):
        """CREATE: salva um novo professor no banco."""
        db.session.add(self)
        db.session.commit()

    def atualizar(self, nome=None, email=None, disciplina=None):
        """UPDATE: altera apenas os campos informados."""
        if nome is not None:
            self.nome = nome
        if email is not None:
            self.email = email
        if disciplina is not None:
            self.disciplina = disciplina

        db.session.commit()

    def deletar(self):
        """DELETE: remove o professor do banco."""
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def listar_todos():
        """READ: retorna todos os professores."""
        return Professor.query.order_by(Professor.id.asc()).all()

    @staticmethod
    def buscar_por_id(id):
        """READ: busca um professor pelo id."""
        return Professor.query.get(id)

    @staticmethod
    def buscar_por_email(email):
        """READ auxiliar: busca um professor pelo e-mail."""
        return Professor.query.filter_by(email=email).first()

    def to_dict(self):
        """Converte o objeto Professor para dicionário/JSON."""
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "disciplina": self.disciplina,
        }
