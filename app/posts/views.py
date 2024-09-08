from app.models import Post, db, Creator
from flask import render_template, request, redirect, url_for
from app.posts import  post_blueprint
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

@post_blueprint.route("", endpoint="index") 
def index():
    posts = Post.query.all()
    return render_template("posts/index.html", posts=posts)


@post_blueprint.route("<int:post_id>", endpoint="details")
def details(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("posts/details.html", post=post)

from app.posts.forms import postForm

@post_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
@login_required
def create():
    form = postForm()
    if request.method == "POST" and form.validate_on_submit():
        image_name=None
        if request.files.get('image'):
             image= form.image.data
             image_name =secure_filename(image.filename)
             image.save(os.path.join('app/static/blog/images/', image_name))
        post = Post(name=request.form["name"], description=request.form["description"], 
          image=image_name, creator_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(post.show_url)
    return render_template("posts/create.html", form=form)


@post_blueprint.route("<int:post_id>/delete", endpoint="delete", methods=['POST'])
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.creator_id != current_user.id:
        return redirect(url_for('posts.index'))
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.index'))

@post_blueprint.route("/<int:post>/edit", endpoint="edit", methods=["GET", "POST"])
@login_required
def edit(post):
    post = Post.query.get_or_404(post)
    if post.creator_id != current_user.id:
        return redirect(url_for('posts.index'))
    form = postForm(obj=post)
    if request.method == "POST" and form.validate_on_submit():
        post.name = form.name.data
        post.description = form.description.data
        post.creator_id = form.creator_id.data
        if request.files.get('image'):
            image= form.image.data
            image_name =secure_filename(image.filename)
            image.save(os.path.join('app/static/blog/images/', image_name))
            post.image = image_name
        db.session.commit()
        return redirect(post.show_url)
    return render_template("posts/edit.html", form=form, post=post)