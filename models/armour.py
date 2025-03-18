from init import db, ma

class Armour(db.Model):
    __tablename__ = "armour_pieces"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    slots = db.Column(db.ARRAY(db.Integer()))
    armour_type = db.Column(db.String())
    max_value = db.Column(db.Integer())

    skills = db.relationship("ArmourSkills", back_populates="armour", cascade="all, delete")
