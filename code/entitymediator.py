from code.entity import Entity
from code.enemy import Enemy

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity): # metodo que so funciona nessa classe, caso __
        if isinstance(ent, Enemy):
           if ent.rect.right < 0: # quando sai da tela zerar a vida
               ent.health = 0 
        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            pass
           # test_entity = entity_list
            #Entity.__verify_collision_window(test_entity)
            
        
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent) # Destruir 