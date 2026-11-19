# DAO - concentra o acesso aos dados de Oficina.

from extensions import db
from models.oficina import Oficina


class OficinaDAO:

    # CREATE
    @staticmethod
    def salvar(oficina):
        db.session.add(oficina)

    # READ (todos)
    @staticmethod
    def listar():
        return Oficina.query.all()

    # READ (um) - devolve o objeto ou None
    @staticmethod
    def buscar_por_id(id):
        return Oficina.query.get(id)

    # UPDATE
    @staticmethod
    def atualizar(oficina, titulo, instrutor, vagas):
        oficina.titulo = titulo
        oficina.instrutor = instrutor
        oficina.vagas = vagas
        db.session.commit()

    # DELETE
    @staticmethod
    def excluir(oficina):
        db.session.delete(oficina)
        db.session.commit()
