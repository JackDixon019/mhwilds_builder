from init import db, ma

class Weapon(db.Model):
    __tablename__ = "weapons"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    slots = db.Column(db.ARRAY(db.Integer()))
    weapon_type = db.Column(db.String())
    max_value = db.Column(db.Integer())

    skills = db.relationship("WeaponSkills", back_populates="weapon", cascade="all, delete")
