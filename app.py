from flask import Flask, url_for, request, render_template, current_app, send_from_directory,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,current_user,UserMixin,login_required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_uploads import UploadSet, configure_uploads, IMAGES

import datetime,os,re
from upload import save_image
from Config import Common,users

app = Flask(__name__,static_url_path='')
app.config.from_object(Common)
app.jinja_env.auto_reload = True
db = SQLAlchemy(app)
login = LoginManager(app)
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


@login.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    for user in users:
        if user_id == user['id']:
            user = User()
            user.id = user_id
            return user  # 返回用户对象

login.login_view = 'login'



#用户认证
class User(UserMixin):
    pass

# 照片表单
class NewAlbumForm(FlaskForm):
    title = StringField(u'标题')
    about = TextAreaField(u'介绍', render_kw={'rows': 8})
    photo = FileField(u'图片', validators=[
        FileRequired(u'你还没有选择图片！'),
        FileAllowed(photos, u'只能上传图片！')])
    submit = SubmitField(u'上传')

# 照片数据库
class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(64))  # 原图url
    url_t = db.Column(db.String(64))  # 缩略图url
    timestamp = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())

# 首页
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():

    return render_template('login.html')
# 图片上传
@app.route('/upload/', methods=['GET', 'POST'])
# @login_required
def new_photo():
    imgs = Photo.query.all()
    form = NewAlbumForm()
    if form.validate_on_submit():
        if request.method == 'POST' or 'photo' in request.files.getlist("photo"):
            images = save_image(request.files.getlist("photo"),photos=photos)
            # 作用域
        title = form.title.data
        # 这里把上传的第一张图片作为封面的初始值

        for url in images:
            photo = Photo(url=url[0],url_t=url[1])
            db.session.add(photo)
        db.session.commit()
        flash(u'上传完成', 'success')
        # 跳转到批量编辑页面
        return redirect(url_for('new_photo'))

    return render_template('upload.html', form=form,imgs=imgs[:50])

# 缩略图路径
@app.route('/uploads/thumb/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOADED_PHOTOS_DEST'],'thumb/'+filename)

#照片编辑页面
@app.route('/edit/<string:name>',methods=['GET','POST'])
def edit(name):
    img = Photo.query.get(int(name))
    if request.method == 'POST':
        #删除图片，同时删除数据库
        de_img = Photo.query.get(int(name))
        filename = re.search("/photos/(.*)",de_img.url,re.S).group(1)
        os.remove(photos.path(filename))
        db.session.delete(de_img)
        db.session.commit()

        return redirect(url_for('new_photo'))

    return render_template('edit.html',img=img)



if __name__ == '__main__':
    app.run()
