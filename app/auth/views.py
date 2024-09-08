from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Creator, db
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import auth_blueprint

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        creator = Creator.query.filter_by(name=form.name.data).first()
        if creator:
            flash('Username already exists.', 'danger')
        else:
            creator = Creator(name=form.name.data)
            creator.set_password(form.password.data)
            db.session.add(creator)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        creator = Creator.query.filter_by(name=form.name.data).first()
        if creator and creator.check_password(form.password.data):
            login_user(creator)
            flash('Login successful!', 'success')
            return redirect(url_for('posts.index'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')
    return render_template('auth/login.html', form=form)

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('posts.index'))
