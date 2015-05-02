# tanki
# TODO:
-create menu interface(fill it with anything neccesary)
-new game option allows player/s to choose map, tanks, number of AI controlled tanks
-create display and control systems

# Gameplay implementation:
- Actor - base class for everything interactable on map(has method collide, draw, ... and coordinates, image_to_draw...)
- GameInstance - contains list of actors for using collide function also controls gameplay(like when game ends or when to spawn bonus...)
- Tank - implements Actor, can create bullets on attack, has its own atributes like hp, dmg, speed, and methods like is_alive(). Contains three lists of bonuses, for example when collide with bullet occurs that deals 100dmg, tank calculates dmg based on stats and then calculates dmg by using bonus methods from list
- Bullet - implements Actor, on colide gives damage to tanks and destoys powerups, has sppeed, dmg, max_travel, direction, current_travel
- Walls - implements Actor, on colide stops tanks and bounces bullets
- Bonus - implements Actor, on colide with tanks it gives tank bonus, with colide wit bullet it gets destroyed
