from models.comportement import Comportement
from models.actions.action_attaque import ActionAttaque
from models.actions.action_defense import ActionDefense
from models.actions.action_double import ActionAttaqueDouble

class ComportementBoss(Comportement):

    def agir(self, ennemi) -> str:
        if ennemi.hp > ennemi.hp_max * 0.6:
            return ActionDefense()
        elif ennemi.hp > ennemi.hp_max * 0.3 and ennemi.hp < ennemi.hp_max * 0.6 :
            return ActionAttaque()
        else:
            return ActionAttaqueDouble()
    
    

    def __str__(self):
        return"ComportementBoss"