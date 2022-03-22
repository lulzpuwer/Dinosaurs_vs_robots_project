import random
from Dinosaurs_vs_robots_project.weapon import Weapon
from robot  import Robot
from weapon import weapon

class Dinosaur:
  def __init__(self, name):
    self.name = name
    self.atk_power = Weapon(input(' Pick your attack!: '), random.randrange(0, 35))
    self.health = 100
    pass

  def attak(self):
    opponent_health = Robot[0 or 1 or 2]
    if self.atk_power > 0:
      opponent_health -= self.atk_power
      print(f'You deal {self.atk_power}. Your opponenet is at {opponent_health} current HP')
    else:
      print(f'You dealt NO damage! Your opponenet is at {opponent_health} current HP')
