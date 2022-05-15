from app.request import get_quotes
from . import main
from flask import render_template,redirect,url_for
from flask_login import current_user
from .forms import CreateBLog
from ..models import User,Blog,Comment

@main.route('/')
def index():
   return render_template('index.html')

@main.route('/random_quotes')
def random():
   quote = get_quotes()
   return render_template('random.html',quote = quote)


@main.route('/create_new', methods = ['POST','GET'])
def new_blog():
    form =CreateBLog()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        name = form.name.data
        new_pitch_object = Blog(username=name,blog=blog,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.blog'))
        
    return render_template('blog.html', form = form)

@main.route('/blog')
def blog():
    blog = Blog.query.all()
    return render_template('new_blog.html', blog = blog)


# @main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
# def comment(pitch_id):
#     form = CommentForm()
#     pitch = Pitch.query.get(pitch_id)
#     all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
#     if form.validate_on_submit():
#         comment = form.comment.data 
#         pitch_id = pitch_id
#         user_id = current_user._get_current_object().id
#         new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
#         new_comment.save_c()
#         return redirect(url_for('.comment', pitch_id = pitch_id))
#     return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)

