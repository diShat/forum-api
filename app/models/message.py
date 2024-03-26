from app.database import db
from datetime import datetime


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id", ondelete="CASCADE"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # also backref maybe probably??

    def __init__(self, content, creator_id, topic_id):
        self.content = content
        self.creator_id = creator_id
        self.topic_id = topic_id


    def create_message(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def update_message(cls, message_id, content):
        message = cls.query.filter_by(id=message_id).first()
        if message:
            message.title = message
            db.session.commit()
            return True
        return False

    @classmethod
    def delete_message(cls, message_id):
        message = cls.query.filter_by(id=message_id).first()
        if message:
            db.session.delete(message)
            db.session.commit()
            return True
        return False

    @classmethod
    def get_message(cls, message_id):
        return cls.query.filter_by(id=message_id).first()

    @classmethod
    def get_messages_by_topic(cls, topic_id):
        return cls.query.filter_by(topic_id=topic_id).all()
    

    def __repr__(self):
        return f"Message content: {self.content}\nby {self.creator_id}, {self.created_at}"