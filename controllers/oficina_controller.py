# Controller de PAGINAS - todas as rotas daqui respondem HTML ou
# redirecionamento.

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import session
from models.oficina import Oficina
from dao.oficina_dao import OficinaDAO

oficina_bp = Blueprint("oficina", __name__)


# ===== ITEM 5 ========================================================
# Hoje qualquer pessoa abre as paginas deste Blueprint sem entrar no
# sistema. Escreva aqui a protecao, em um ponto so.
# =====================================================================


# Listagem (GET) e cadastro (POST) na mesma rota
@oficina_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        oficina = Oficina(
            titulo=request.form["titulo"],
            instrutor=request.form["instrutor"],
            vagas=request.form["vagas"]
        )
        OficinaDAO.salvar(oficina)
        flash("Oficina cadastrada.")
        return redirect(url_for("oficina.index"))

    # ===== ITEM 3 ====================================================
    # Conte aqui, na SESSAO, quantas vezes esta pessoa abriu a listagem.
    # A chave deve se chamar "consultas". O template ja exibe o valor.
    # =================================================================

    return render_template("index.html", oficinas=OficinaDAO.listar())


# Edicao - GET mostra o formulario preenchido
@oficina_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    oficina = OficinaDAO.buscar_por_id(id)

    # ===== ITEM 4 ====================================================
    # O formulario de edicao e enviado para esta rota por POST, mas nada
    # e gravado. Trate aqui o envio: grave a alteracao e volte a listagem.
    # =================================================================

    return render_template("editar.html", oficina=oficina)


# Exclusao
@oficina_bp.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    oficina = OficinaDAO.buscar_por_id(id)
    OficinaDAO.excluir(oficina)
    flash("Oficina excluida.")
    return redirect(url_for("oficina.index"))
