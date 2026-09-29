from models.comportement import Comportement
from models.actions.action_attaque import ActionAttaque
from models.actions.action_defense import ActionDefense
from models.actions.action_double import ActionAttaqueDouble

class ComportementAgressif(Comportement):

    def agir(self, ennemi) -> str:
        return ActionAttaque()
    def __str__(self):
        return"ComportementAgressif"