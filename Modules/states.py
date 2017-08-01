class AbstractState(object):
  def switch(self, next_state):
    self.__class__ = next_state

  def name(self):
    return self.__class__.__name__

class AbstractStateController(object):
    def __init__(self, default_state, allowed_states):
      self.state = default_state
      self.allowed_states = allowed_states

    def move(self, next_state):
        print next_state
        print self.allowed_states
        print next_state == self.allowed_states[0]
        if next_state not in self.allowed_states:
            raise NameError
        self.state.switch(next_state)

    def __str__(self):
        return self.state.name()

    def eql(self, other_state):
        return self.state.name() == other_state.name()

# for binary systems i.e. error
class On(AbstractState): pass
class Off(AbstractState): pass

class ErrorStateController(AbstractStateController, object):
    default_state = Off()
    allowed_states = [On(), Off()]

    def __init__(self):
        super(
            ErrorStateController,
            self
        ).__init__(
            ErrorStateController.default_state,
            ErrorStateController.allowed_states
        )

esc = ErrorStateController()
print esc
print esc.move(On())
