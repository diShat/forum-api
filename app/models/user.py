from app.database import db
import bcrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    passwd_hash = db.Column(db.String(128), nullable=False)     # will include hash as the bcrypt lib is used
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    last_login = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    role = db.Column(db.String(), default="author")

    __table_args__ = (
        db.CheckConstraint(role.in_(['author', 'admin']), name='role_types'),
    )

    
    def __init__(self, username, email, passwd):
        self.username = username
        self.email = email
        self.set_password(passwd)


    def set_password(self, passwd):
        self.passwd_hash = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


    def verify_password(self, passwd):
        return bcrypt.checkpw(passwd.encode('utf-8'), self.passwd_hash.encode('utf-8'))


    def create_user(self):
        user = User.query.filter_by(id=self.id).first()
        if user:
            db.session.add(self)
            db.session.commit()
            return True
        return False

    
    @classmethod
    def update_last_login(cls, user_id):
        user = cls.query.filter_by(id=user_id).first()
        if user:
            user.last_login = db.func.current_timestamp()
            db.session.commit()
            return True
        return False


    @classmethod
    def update_password(cls, user_id, old_passwd, new_passwd):
        pass


    @classmethod
    def update_role(cls, user_id, role=None):
        user = cls.query.filter_by(id=user_id).first()
        if user:
            if role:
                user.role = role
                db.session.commit()
                return True
        return False

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @classmethod    
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


    def __repr__(self):
        return f"User: {self.username}, {self.role}\nLast login: {self.last_login}"