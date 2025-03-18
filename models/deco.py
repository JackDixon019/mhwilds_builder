from init import db, ma

class Deco(db.Model):
    __tablename__ = "decos"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    base_value = db.Column(db.Integer())
    effect = db.Column(db.String())
    details = db.Column(db.String())

    skills = db.relationship("DecoSkills", back_populates="deco")
