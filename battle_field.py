from fleet import Fleet
from herd import Herd

class Battle_field:
  def __init__(self):
      self.fleet = Fleet()
      self.herd = Herd()
      pass
  
  def run_game(self):
    print(Battle_field.display_welcome(self))

  def display_welcome(self):
    print('WELCOME TO DINOSAURS VS ROBOTS!')
    choose_faction = print(input('Would you like to play "dinosuars" or "robots": '))
    if choose_faction == 'dinosuars':
      current_faction = self.herd
    else:
      current_faction = self.fleet
    return current_faction


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
