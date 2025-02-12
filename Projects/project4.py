# Section 1 - setup

import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
player = codesters.Sprite("")
stage.set_background("flowerfield")
object_speed = 10
lives = 0

# section 2 - objects
def falling_object() :
     global object_speed,lives

     if lives>0:
          x=0
          y=0
          object = codesers.Sprite("star", x, y)
          object.set_size(5)
          object.set_x_speed(object_speed)
stage.event_interval (falling_object, 3)

   
    
# # section 3 -collision
# def collision(player/object):
#     global 0

#     if object.get_image_name() == "Unicon":
#          stage.remove_sprite(object)
#          t=3
#          if lives == 0:
#               player.say(f"You lose!",5)
#             else:
#               player.say(f"{lives} lives", 0.5)
# player.event_collision(collision) 

# # section 4 -controls

# # right key
# def go_right():
#      player.move_right(10)

# player.event_key("right", go_right)

# # left key
# def go_left():
#      player.move_left(10)

# player.event_key("left", go_left)

# # down key
# def go_down():
#      player.move_down(10)

# player.event_key("down", go_down)

# # up key
# def go_up():
#      player.move_up(10)

# player.event_key("up", go_up)



