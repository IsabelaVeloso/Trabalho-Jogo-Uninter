from code.entity import Entity
from code.enemy import Enemy
from code.player import Player

class EntityMediator:

    survival_time = 0

    @staticmethod
    def __verify_collision_window(ent: Entity):  
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:  # quando sai da tela, zerar a vida
                ent.health = 0 
        pass

    @staticmethod
    def __verify_collision_entity(ent1, ent2):  # se jogador encostar no inimigo
        valid_interaction = False
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True

        if valid_interaction:  # mesma coisa de: if valid_interaction == True
            if (ent1.rect.right >= ent2.rect.left and 
                    ent1.rect.left <= ent2.rect.right and 
                    ent1.rect.bottom >= ent2.rect.top and 
                    ent1.rect.top <= ent2.rect.bottom): 
                ent1.health -= ent2.damage

    @staticmethod
    def give_score():  # Atualizar score com base no tempo de sobrevivência
        return EntityMediator.survival_time  # Retorna o tempo de sobrevivência como score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):  # colisões
        for i in range(len(entity_list)):
            entity1 = entity_list[i]  # verificar colisões entre todos, eliminando os repetidos
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)  # Destruir entidade
