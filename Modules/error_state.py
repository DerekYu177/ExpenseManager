class AbstractState(object):
  def switch(self, next_state):
    self.__class__ = next_state

  def name(self):
    return self.__class__.__name__

class On(AbstractState): pass
class Off(AbstractState): pass

class State:
  def __init__(self):
    self.state = Off()

  def move(self, next_state):
    self.state.switch(next_state)

  def __str__(self):
    state = self.state.name()
    return state
