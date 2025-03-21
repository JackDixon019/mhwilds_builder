from init import db, ma
from marshmallow import fields


# ApprovedBird allows connecting of birds with two users:
# One is the submitting user - directly connected
# The other is the approving admin - connected via ApprovedBird
class DecoSkills(db.Model):
    __tablename__ = "deco_skills"

    id = db.Column(db.Integer(), primary_key=True)

    deco_id = db.Column(db.Integer(), db.ForeignKey("decos.id"))
    deco = db.relationship("Deco", back_populates="skills")

    skill_id = db.Column(db.Integer(), db.ForeignKey("skills.id"))
    skill = db.relationship("Skill", back_populates="decos")



class DecoSkillSchema(ma.Schema):
    class Meta:
        fields = ("id", "deco", "skill")


deco_skill_schema = DecoSkillSchema()
deco_skills_schema = DecoSkillSchema(many=True)