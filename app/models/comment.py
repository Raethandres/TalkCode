from ..database import db, Model , Column, relationship

from sqlalchemy_utils import Timestamp


class Comment(Model, Timestamp):
    __tablename__ = 'comment_snippet'
    id          = Column(db.Integer, primary_key=True)
    id_user     = Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    id_snippet  = Column(db.Integer, db.ForeignKey('snippet.id'), nullable=False)
    text        = Column(db.String(156), nullable=False)
    # Relationships
    user        = relationship("User", back_populates="comments")


    def __init__(self, id_user, id_snippet, text):
        self.id_user     = id_user
        self.id_snippet  = id_snippet
        self.text        = unicode(text)