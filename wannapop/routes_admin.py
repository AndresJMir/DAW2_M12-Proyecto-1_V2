from flask import Blueprint, render_template, flash
from .models import User
from .helper_role import Role, role_required
from . import db_manager as db

# Blueprint
admin_bp = Blueprint("admin_bp", __name__)

@admin_bp.route('/admin')
@role_required(Role.admin, Role.moderator)
def admin_index():
    return render_template('admin/index.html')

@admin_bp.route('/admin/users')
@role_required(Role.admin)
def admin_users():
    users = db.session.query(User).all()
    return render_template('admin/users_list.html', users=users)

#Rutas para la Moderacion

@admin_bp.route('/users/<user_id>/block', methods=['POST'])
@role_required(Role.admin)
def block_user(user_id):
    # Lógica para bloquear al usuario
    flash("Usuari bloqueao")
    return "Usuario bloqueado"  # Puedes retornar un mensaje o código de estado apropiado

@admin_bp.route('/users/<user_id>/unblock', methods=['POST'])
@role_required(Role.admin)
def unblock_user(user_id):
    # Lógica para desbloquear al usuario
    flash("Usuari desbloqueao")
    return "Usuario desbloqueado"

