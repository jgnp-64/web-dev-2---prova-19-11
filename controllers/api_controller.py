# Controller da API - as rotas daqui respondem DADOS em JSON.
#
#   Metodo   Endereco                 O que faz       Sucesso   Recusas
#   GET      /api/oficinas            lista todos     200       401
#   GET      /api/oficinas/<id>       devolve um      200       401 404   <- ITEM 7
#   DELETE   /api/oficinas/<id>       remove          204       401 404   <- ITEM 9
#
# Toda recusa tem o mesmo formato: {"erro": "mensagem"}.

from flask import Blueprint, request, session, jsonify
from models.oficina import Oficina
from dao.oficina_dao import OficinaDAO

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.before_request
def exigir_login():
    if not session.get("usuario_id"):
        return jsonify({"erro": "Autenticacao necessaria."}), 401


@api_bp.route("/oficinas", methods=["GET"])
def listar():
    lista = []

    for oficina in OficinaDAO.listar():
        lista.append(oficina.para_dicionario())

    return jsonify(lista)


# ===== ITEM 7 ========================================================
# Escreva aqui a rota GET /api/oficinas/<id>, que devolve UM registro.
# Se o id nao existir, a resposta e 404 com {"erro": "Oficina nao encontrada."}.
# =====================================================================


# ===== ITEM 9 ========================================================
# Escreva aqui a rota DELETE /api/oficinas/<id>, que remove UM registro.
# Sucesso: 204, sem corpo. Se o id nao existir: 404 com
# {"erro": "Oficina nao encontrada."}.
# =====================================================================
