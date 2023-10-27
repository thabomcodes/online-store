from flask_jwt_extended import get_current_user
from sqlalchemy import func
from app.models import db


class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    type = db.Column(db.String(16), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    user_id = db.Column(
        db.ForeignKey("users.id"), default=lambda: get_current_user().id, nullable=False
    )
