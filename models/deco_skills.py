from init import db, ma


# ApprovedBird allows connecting of birds with two users:
# One is the submitting user - directly connected
# The other is the approving admin - connected via ApprovedBird
class DecoSkills(db.Model):
    __tablename__ = "deco_skills"

    deco_id = db.Column(db.ForeignKey("decos.id"), primary_key=True)
    skill_id = db.Column(db.ForeignKey("skills.id"), primary_key=True)

    deco = db.relationship("Deco", back_populates="skills")
    skill = db.relationship("Skill", back_populates="decos")



class DecoSkillSchema(ma.Schema):
    class Meta:
        fields = ("deco_id", "skill_id")


deco_skill_schema = DecoSkillSchema()
deco_skills_schema = DecoSkillSchema(many=True)