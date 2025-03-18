from init import db, ma


# ApprovedBird allows connecting of birds with two users:
# One is the submitting user - directly connected
# The other is the approving admin - connected via ApprovedBird
class WeaponSkills(db.Model):
    __tablename__ = "weapon_skills"

    weapon_id = db.Column(db.ForeignKey("weapons.id"), primary_key=True)
    skill_id = db.Column(db.ForeignKey("skills.id"), primary_key=True)

    weapon = db.relationship("Weapon", back_populates="skills")
    skill = db.relationship("Skill", back_populates="innate_weapons")



class WeaponSkillSchema(ma.Schema):
    class Meta:
        fields = ("weapon_id", "skill_id")


weapon_skill_schema = WeaponSkillSchema()
weapon_skills_schema = WeaponSkillSchema(many=True)