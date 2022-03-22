from robot import Robot
class Fleet:
  def __init__(self):
    self.robots = []
    pass

  def create_fleet(self):
    create_fleet = self.robots.append(Robot(input('Pick a name for your Robot: ')))
    while len(self.robots) <= 3:
      robots = self.robots.append(create_fleet)
      print(f'You have name a dinosuar! please name a total of 3 to complete the herd')
      return robots
    else:
      print(f'you have filled out your team {self.robots}')
      
