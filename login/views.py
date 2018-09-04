from flask import render_template, Blueprint,  redirect, url_for, flash,jsonify,request
from login.forms import UserForm

blue = Blueprint("blue",__name__)

@blue.route('/login',methods=['GET','POST'])
def login():
    form = UserForm()  # 表单实例化对象
    if form.validate_on_submit():
        if form.uname.data =='tom' and form.upwd.data=='123' :
            return redirect(url_for('blue.welcome'))
        else:
            flash('用户名或密码错误！')
            return redirect(url_for('blue.login'))

    return render_template('login.html',form=form)

@blue.route('/ajax',methods=['GET','POST'])
def ajax():
    name = request.args.get('uputin')
    print(name)
    if name == 'fruit':
        return jsonify({'name':'草莓','price':12})
    else:
        return jsonify({'name':'篮球','price':12})


@blue.route('/welcome',methods=['GET','POST'])
def welcome():
    return render_template('welcome.html')

