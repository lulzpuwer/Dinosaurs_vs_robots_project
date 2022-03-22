from Dinosaurs_vs_robots_project.dinosuar import Dinosaur
from Dinosaurs_vs_robots_project.weapon import Weapon
from fleet import Fleet
from herd import Herd

class Battle_field:
  def __init__(self):
      self.fleet = Fleet()
      self.herd = Herd()
      self.current_faction = ''
      pass
  
  def run_game(self):
    print(Battle_field.display_welcome(self))

  def display_welcome(self):
    print('WELCOME TO DINOSAURS VS ROBOTS!')
    choose_faction = print(input('Would you like to play "dinosuars" or "robots": '))
    if choose_faction == 'dinosuars':
      self.current_faction = self.herd
      self.fleet = self.fleet.robots.append(('Megatron', 100, Weapon), ('iron man', 100, Weapon), ('Mecha Godzilla', 100, Weapon))
    elif choose_faction == 'robots':
      self.current_faction = self.fleet
      self.herd = self.herd.dinosaurs.append(('Godzilla', 100, Weapon), ('Mega Moth', 100, Weapon), ('Boar God of the Moutain', 100, Weapon))
    return self.current_faction

  def battle(self):
    pass

  def dino_turn(self, dinosaur):
    pass

  def robo_turn(self, robot):
    pass

  def show_dino_opponent_options(self):
    pass

  def show_robo_opponent_options(self):
    pass

  def display_winner(self):
    pass
