from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    uname = StringField(label="用户名",validators=[DataRequired(message="姓名不能为空！")])
    upwd = StringField(label="密码", validators=[DataRequired(message="密码不能为空！")])
    submit = SubmitField(label="点击提交")