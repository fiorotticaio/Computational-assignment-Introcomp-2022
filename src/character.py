class Character:
  # Commum atributes of allies and enemies
  life_points = 0
  attack = 0
  defense = 0
  speed = 0

  def __init__(self, life_points, attack, defense, speed):
    self.life_points = life_points
    self.attack = attack
    self.defense = defense
    self.speed = speed

  def get_life_points(self):
    return self.life_points
  
  def set_life_points(self, life_points):
    self.life_points = life_points
  
  def get_attack(self):
    return self.attack
  
  def set_attack(self, attack):
    self.attack = attack
  
  def get_defense(self):
    return self.defense
  
  def set_defense(self, defense):
    self.defense = defense
  
  def get_speed(self):
    return self.speed
  
  def set_speed(self, speed):
    self.speed = speed
  
  def character_died(self):
    return self.life_points <= 0