from init import db
from flask import Blueprint

from models.deco import Deco
from models.deco_skills import DecoSkills
from models.skill import Skill
from models.armour import Armour
from models.armour_skills import ArmourSkills
from models.weapon import Weapon
from models.weapon_skills import WeaponSkills


db_commands = Blueprint('db', __name__)

# Creates CLI command create: run w -$ flask db create
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("And on the first day...")

@db_commands.cli.command('yeet')
def drop_db():
    db.drop_all()
    print("Let the fires of Hell consume them...")

@db_commands.cli.command('seed')
def seed_db():
    # Creates first card object
    skill1 = Skill(
        name="testAttackBoost",
        effect="Raises Attack",
        details = "Raises Attack by +3 raw"
    )
    # Adds this object to the table
    db.session.add(skill1)

    # create the second card object
    skill2 = Skill(
        name = "Crit Boost",
        effect = "Increases Critical damage",
        details = "Increases Critical damage form 25% -> 30/35/40%"
    )
    # Add the object as a new row to the table
    db.session.add(skill2)

    db.session.commit()

    # create new deco
    deco1 = Deco(
        name = "Attack",
        sizes = [1, 2, 3]
    )
    # add deco to db
    db.session.add(deco1)
    db.session.commit()

    deco_skill1 = DecoSkills(
        deco = deco1,
        skill = skill1
    )
    db.session.add(deco_skill1)
    # commit the changes
    db.session.commit()
    print("May you reap what you have sown...")
