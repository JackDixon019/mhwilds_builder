from init import db, ma


# ApprovedBird allows connecting of birds with two users:
# One is the submitting user - directly connected
# The other is the approving admin - connected via ApprovedBird
class ArmourSkills(db.Model):
    __tablename__ = "armour_skills"

    armour_id = db.Column(db.ForeignKey("armour_pieces.id"), primary_key=True)
    skill_id = db.Column(db.ForeignKey("skills.id"), primary_key=True)

    armour = db.relationship("Armour", back_populates="skills")
    skill = db.relationship("Skill", back_populates="innate_armours")



class ArmourSkillSchema(ma.Schema):
    class Meta:
        fields = ("armour_id", "skill_id")


armour_skill_schema = ArmourSkillSchema()
armour_skills_schema = ArmourSkillSchema(many=True)