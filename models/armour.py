from init import db, ma
from marshmallow import fields, validate

class Armour(db.Model):
    __tablename__ = "armour_pieces"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    slots = db.Column(db.ARRAY(db.Integer()))
    armour_type = db.Column(db.String())
    max_value = db.Column(db.Integer())

    skills = db.relationship("ArmourSkills", back_populates="armour", cascade="all, delete")

class ArmourSchema(ma.Schema):
    skills = fields.Nested("ArmourSkillSchema", only=["skill"])
    armour_type = fields.String(validate=validate.OneOf(["helmet","chest","arms","waist","legs","talisman"]))

armour_schema = ArmourSchema()
armour_schemas = ArmourSchema(many=True)