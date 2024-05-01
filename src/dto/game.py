from dataclasses import dataclass

@dataclass
class Game:
  def __init__(self):
    self.release_date = ''
    self.developer = ''
    self.publisher = ''
    self.platform = ''
    self.required_age = 0
    self.category = ''
    self.genre = ''
