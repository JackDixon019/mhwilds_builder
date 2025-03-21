from init import db, ma


# ApprovedBird allows connecting of birds with two users:
# One is the submitting user - directly connected
# The other is the approving admin - connected via ApprovedBird
class ArmourSkills(db.Model):
    __tablename__ = "armour_skills"

    id = db.Column(db.Integer(), primary_key=True)

    armour_id = db.Column(db.Integer(), db.ForeignKey("armour_pieces.id"), primary_key=True, nullable=False)
    armour = db.relationship("Armour", back_populates="skills")

    skill_id = db.Column(db.Integer(), db.ForeignKey("skills.id"), primary_key=True, nullable=False)
    skill = db.relationship("Skill", back_populates="innate_armours")



class ArmourSkillSchema(ma.Schema):
    class Meta:
        fields = ("armour", "skill")


armour_skill_schema = ArmourSkillSchema()
armour_skills_schema = ArmourSkillSchema(many=True)