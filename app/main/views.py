from app.request import get_quotes
from . import main
from flask import render_template,redirect,url_for
from .forms import CreateBLog

@main.route('/')
def index():
   quote =get_quotes()
   
   return render_template('index.html', quote =quote)

@main.route('/create_new', methods = ['POST','GET'])
def new_blog():
    form =CreateBLog()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
        
    return render_template('blog.html', form = form)


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

