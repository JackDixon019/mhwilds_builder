from init import db, ma
from marshmallow import fields

from models.skill import SkillSchema

class Deco(db.Model):
    __tablename__ = "decos"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    base_value = db.Column(db.Integer())
    sizes = db.Column(db.ARRAY(db.Integer()))

    skills = db.relationship("DecoSkills", back_populates="deco", cascade="all, delete")

class DecoSchema(ma.Schema):
    skills = fields.List(fields.Nested(SkillSchema(only=["name"])))
    class Meta:
        fields = ("id", "name", "base_value", "skills", "sizes")
