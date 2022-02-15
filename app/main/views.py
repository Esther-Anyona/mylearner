from flask import render_template,request,redirect,url_for,abort, flash
from ..models import User, Post, Comment
from . import main
from flask_login import login_required, current_user
from .. import db, photos
from .forms import UpdateProfile, PostForm, CommentForm

@main.route('/')
def home():
    posts= Post.query.order_by(Post.date_posted.desc()).all()
    title="My Learning post"
    return render_template('home.html', title=title, posts=posts)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/post/new',methods= ['GET','POST'])
@login_required
def new_post():
    postform=PostForm()
    if postform.validate_on_submit():
        post = Post(title=postform.title.data, content=postform.content.data, user_id=current_user._get_current_object().id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.home'))
        flash('Your post has been posted!', 'success')

    return render_template('create_post.html',postform =postform)

@main.route('/comment/<int:post_id>', methods = ['POST','GET'])
@login_required
def comment(post_id):
    commentform = CommentForm()
    post = Post.query.get(post_id)
    comments = Comment.query.filter_by(post_id = post_id).all()
    if commentform.validate_on_submit():
        comment = commentform.comment.data 
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,post_id = post_id)
        new_comment.save_comment()
        return redirect(url_for('.comment', id = post_id))
    return render_template('comment.html', commentform =commentform, post = post, comments=comments)


@main.route('/post/<int:post_id>', methods = ['GET','POST'])
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post = post, title=post.title)



@main.route('/post/<post_id>/update', methods = ['GET','POST'])
@login_required
def updatepost(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        abort(403)
    updateform = PostForm()
    if updateform.validate_on_submit():
        post.title = updateform.title.data
        post.content = updateform.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('main.post',id = post.id)) 
    if request.method == 'GET':
        post.title = updateform.title.data
        post.content = updateform.content.data

    return render_template('create_post.html', updateform = updateform)

