# Model - entidade Oficina.

from extensions import db


class Oficina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    instrutor = db.Column(db.String(120))
    vagas = db.Column(db.Integer)

    # O objeto se descreve como dicionario, para as rotas que respondem JSON.
    def para_dicionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "instrutor": self.instrutor,
            "vagas": self.vagas
        }
