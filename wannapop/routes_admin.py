from flask import Blueprint, render_template, flash, abort, redirect, url_for
from .models import User, BlockedUser
from .helper_role import Role, role_required
from .forms import DeleteForm
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
    block = db.session.query(BlockedUser).join(User)
    return render_template('admin/users_list.html', users=users, block=block)

#Rutas para la Moderacion

@admin_bp.route('/admin/bloc')
@role_required(Role.admin)
def bad_users():
    users = db.session.query(User).all()
    block = db.session.query(BlockedUser).all()
    return render_template('admin/blocked_users_list.html', users=users, block=block)

# Bloqueo de usuario
@admin_bp.route('/users/<user_id>/block', methods=['POST'])
@role_required(Role.admin)
def block_user(user_id):
    # Lógica para bloquear al usuario
    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        abort(404)
    form = BlockedUser()
    if form.validate_on_submit(): # si s'ha fet submit al formulari
        # insert!
        db.session.add()
        db.session.commit()
        flash("Usuario bloqueado", "success")
        return redirect(url_for('/admin/users'))
    else: # GET
        return render_template('admin/users_list.html', form = form)

# Desbloqueo de usuario
@admin_bp.route('/users/<user_id>/unblock', methods=['POST'])
@role_required(Role.admin)
def unblock_user(user_id):
    # Lógica para desbloquear al usuario
    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        abort(404)
    form = BlockedUser()
    if form.validate_on_submit(): # si s'ha fet submit al formulari
        # insert!
        db.session.add()
        db.session.commit()
        flash("Usuario desbloqueado", "success")
        return redirect(url_for('/admin/users'))
    else: # GET
        return render_template('admin/users_list.html', form = form)


