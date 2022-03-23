from robot import Robot
from weapon import Weapon

class Fleet:
  def __init__(self):
    self.robots = []
    pass

  def create_fleet(self):
    create_fleet = self.robots.append(Robot(input('Pick a name for your Robot: ')))
    while len(self.robots) <= 2:
      robots = self.robots.append(create_fleet)
      print(f'You have name a dinosuar! please name a total of 3 to complete the herd')
      return robots
    else:
      print(f'you have filled out your team {self.robots}')
      
  def generate_default_fleet(self):
    self.robots = [('Megatron', 100, Weapon('great sword', 20)), ('iron man', 100, Weapon('hand beam', 20)), ('Mecha Godzilla', 100, Weapon('eye laser', 20))]