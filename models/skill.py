from init import db, ma
from marshmallow import fields

class Skill(db.Model):
    __tablename__ = "skills"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    effect = db.Column(db.String())
    details = db.Column(db.String())

    innate_armours = db.relationship("ArmourSkills", back_populates="skill")
    innate_weapons = db.relationship("WeaponSkills", back_populates="skill")
    decos = db.relationship("DecoSkills", back_populates="skill")
    base_value = db.relationship("DecoSkills", back_populates="skill", overlaps="decos")

class SkillSchema(ma.Schema):
    base_value = fields.Nested("deco_skill_schema", only=["base_value"])
    class Meta: fields = ("id", "name", "base_value", "effect", "details")
    ordered = True