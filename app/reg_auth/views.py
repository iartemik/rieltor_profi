from app import *
from . import bp_login
from .forms.Forms import LoginForm,RegisterForm,ValidationError

@login_manager.user_loader
def load_user(user_id):
    user = Client.query.get(int(user_id))
    if user is None:
        user = Rieltor.query.get(int(user_id))
    return user

@bp_login.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        if form.is_rieltor.data:
            user = Rieltor.query.filter_by(phone=form.phone.data).first()
        else:
            user = Client.query.filter_by(phone=form.phone.data).first()
        if user:
            login_user(user)
            return redirect(url_for('main.index'))
    form_login=LoginForm() 
    form_register=RegisterForm()
    return render_template('login.html',form_login=form_login,form_reg=form_register)

@bp_login.route('/register', methods=['POST'])
def register():
       form = RegisterForm()
       try:
            form.validate_email_phone(form.email.data,form.phone.data) 
            if form.is_rieltor.data: 
                form.validate_fields_by_rieltor()
                user = Rieltor(phone=form.phone.data,email=form.email.data,
                               info=form.info.data,username=form.username.data,
                               company=form.company.data,experience=form.experience.data)
            else:
                user = Client(phone=form.phone.data,email=form.email.data,username=form.username.data)
            db.session.add(user)
            db.session.commit()
            flash('Вы успешно зарегистрированы!',category='success')       
       except ValidationError as e:
             flash(str(e),category='warning')       
       return redirect(url_for('auth.login'))

@bp_login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
