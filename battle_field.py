import math
import random
from dinosuar import Dinosaur
from robot import Robot
from fleet import Fleet
from herd import Herd

class Battle_field:
  def __init__(self):
      self.fleet = Fleet
      self.herd = Herd 
      self.current_faction = ''
      self.selected_robo = Robot
      self.selected_dino = Dinosaur
      self.selected_opponent_dino = Dinosaur
      self.selected_opponent_robo = Robot
      pass
  
  def run_game(self):
    Battle_field.display_welcome(self)
    print(self.current_faction)
    if self.current_faction == 'dinosaurs':
      self.dino_turn(self)
      self.robo_turn(self)
    elif self.current_faction == 'robots':
      self.robo_turn(self)
      self.dino_turn(self)


  def display_welcome(self):
    print('WELCOME TO DINOSAURS VS ROBOTS!')
    self.current_faction = input('Would you like to play "dinosaurs" or "robots": ')
    if self.current_faction == 'dinosaurs':
      self.herd.create_herd(self.herd)
      self.fleet.generate_default_fleet(self.fleet)
    elif self.current_faction == 'robots':
      self.fleet.create_fleet(self.fleet)
      self.herd.generate_default_herd(self.herd)
    return self.current_faction


  def dino_turn(self, dinosaur):
    if self.current_faction == 'dinosaurs':
      for dino in self.herd.dinosaurs:
        print(dino)
      self.selected_dino = self.herd.dinosaurs[(int(input('Pick the dinosaur you would like to attack with: 0, 1, or 2: ')))]
      self.show_dino_opponent_options(self)
    else:
      self.selected_dino = self.herd.dinosaurs[math.floor(random.randrange(0, 3))]
      self.show_dino_opponent_options(self)
      pass

  def robo_turn(self, robot):
    if self.current_faction == 'robots':
      for robo in self.fleet.robots:
        print(robo)
      self.selected_robo = self.fleet.robots[(int(input('Pick the Robot you would like to attack with: 0, 1, or 2: ')))]
      self.show_robo_opponent_options()
    else:
      self.selected_robo = self.fleet.robots[math.floor(random.randrange(0, 3))]
      self.show_robo_opponent_options()
    pass

  def show_dino_opponent_options(self):
    if self.current_faction == 'dinosaurs':
      for robo in self.fleet.robots:
        print(robo)
      self.selected_opponent_robo = self.fleet.robots[(int(input('Which Robot would you like to attack? 0, 1, or 2: ')))]
      self.selected_opponent_robo.damage_recieved(self.selected_dino.attack)
    else:
      self.selected_opponent_robo = self.fleet.robots[math.floor(random.randrange(0, 3))]
      self.selected_opponent_robo.damage_recieved(self.selected_dino.attack)
    pass

  def show_robo_opponent_options(self):
    if self.current_faction == 'robots':
      for dino in self.herd.dinosaurs:
        print(dino)
      self.selected_opponent_dino = self.herd.dinosaurs[(int(input('Which Dinosaur would you like to attack? 0, 1, or 2: ')))]
      self.selected_opponent_dino.damage_recieved(self.selected_robo.attak)
    else:
      self.selected_opponent_dino = self.herd.dinosaurs[math.floor(random.randrange(0, 3))]
      self.selected_opponent_dino.damage_recieved(self.selected_robo.attak)
    pass


  def battle(self):
    if self.current_faction == 'dinosaurs':
      self.dino_turn(self)
    elif self.current_faction == 'robots':
      print(self.fleet.robots)
      self.robo_turn(self)
    pass



  def display_winner(self):
    pass
