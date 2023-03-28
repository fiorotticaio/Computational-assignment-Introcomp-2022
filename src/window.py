class Window:
  width = 0 
  height = 0
  color = (0, 0, 0)

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def get_width(self): 
    return self.width
  
  def set_width(self, width):
    self.width = width
  
  def get_height(self): 
    return self.height
  
  def set_height(self, height):
    self.height = height

  def get_color(self):
    return self.color
  
  def set_color(self, color):
    self.color = color