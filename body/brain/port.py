from neuron import Neuron
class Port:
  neuron : Neuron = None
  activation : float = None

  is_sensor : bool = None
  is_actor : bool = None
