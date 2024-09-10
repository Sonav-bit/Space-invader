import pygame
screen_width=800
screen_height=500
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speedx=4
enemy_speedy=40
bullet_speed=10
collision_distance=27

pygame.init()

screen=pygame.display.set_mode((screen_width,screen_height))
background=pygame.image.load('space.jpeg')
pygame.display.set_caption('Space Invader')
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
