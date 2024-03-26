from app.database import db
from datetime import datetime


class Theme(db.Model):
    __tablename__ = 'themes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())


    def __init__(self, title):
        self.title = title


    def create_theme(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def update_theme(cls, theme_id, title):
        theme = cls.query.filter_by(id=theme_id).first()
        if theme:
            theme.title = title
            db.session.commit()
            return True
        return False

    @classmethod
    def delete_theme(cls, theme_id):
        theme = cls.query.filter_by(id=theme_id)
        if theme:
            db.session.delete(theme)
            db.session.commit()
            return True
        return False

    @classmethod
    def get_theme(cls, theme_id):
        return cls.query.filter_by(id=theme_id).first()
    
    @classmethod
    def get_themes(cls):
        return cls.query.all()


    def __repr__(self):
        return f"Theme title: {self.title}"