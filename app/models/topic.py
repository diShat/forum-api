from app.database import db
from datetime import datetime


class Topic(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    theme_id = db.Column(db.Integer, db.ForeignKey("themes.id", ondelete="CASCADE"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # concidering adding the backref relationships to themes and users table
    

    def __init__(self, title, body, creator_id, theme_id):
        self.title = title
        self.body = body
        self.creator_id = creator_id
        self.theme_id = theme_id


    def create_topic(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def update_topic(cls, topic_id, title=None, body=None):
        topic = cls.query.filter_by(id=topic_id).first()
        if topic:
            was_updated = False
            if title:
                topic.title = title
                was_updated = True
            if body:
                topic.body = body
                was_updated = True

            if was_updated:
                db.session.commit()

            return was_updated
        return False

    @classmethod
    def delete_topic(cls, topic_id):
        topic = cls.query.filter_by(id=topic_id).first()
        if topic:
            db.session.delete(topic)
            db.session.commit()
            return True
        return False
    

    @classmethod
    def get_topic(cls, topic_id):
        return cls.query.filter_by(id=topic_id).first()

    @classmethod
    def get_topics_by_theme(cls, theme_id):
        return cls.query.filter_by(theme_id=theme_id).all()


    def __repr__(self):
        return f"Topic title: {self.title}\nBody: {self.body}\n by {self.creator_id}, {self.created_at}"