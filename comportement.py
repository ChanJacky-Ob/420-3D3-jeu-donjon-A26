from abc import ABC, abstractmethod


class Comportement(ABC):

    @abstractmethod
    ##besoin info du enemi donc ajout (self,ennemi) 
    #on peut utiliser hp et maxhp pour reduire les données utiliser
    def agir(self, ennemi) -> str:
        """Décide l'action de l'ennemi pour ce tour.

        Args:
            ennemi : l'ennemi qui agit (pour accéder à ses HP, etc.)

        Returns:
            "attaque" ou "defend"
        """
        pass