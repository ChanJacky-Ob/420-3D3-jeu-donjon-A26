from models.comportement import Comportement

class Ennemi:        #facilite lecture seulement
    def __init__(self, nom:str, hp:int, attaque:int, comportement:Comportement):
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self._comportement = comportement  # Objet de type qui hérite de Comprotement
                                          # Objet de type comportement
       
        # avant 
        #mon_dragon =Ennemi("Dragon",60,10,"agressif")
        
        # apres 
        #mon_dragon =Ennemi("Dragon",60,10,ComportementAleatoire())
    

    def agir(self):
        return self._comportement.agir(self)

    def set_comportement(self,nouveau_comportement):
        self._comportement = nouveau_comportement

    def get_comportement(self):
        return self._comportement
    
        
            

    def recevoir_degats(self, degats):
        self.hp = max(0, self.hp - degats)

    def est_vivant(self):
        return self.hp > 0

    ##O — Open/Closed Principle (OCP)
    ##code mal conçu peut ajouter sans entraver au code