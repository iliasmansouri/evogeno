from abc import ABC, abstractmethod
from math import exp


class Neuron(ABC):
    def __init__(self, weight, bias) -> None:
        self.weight = weight
        self.bias = bias

    def activate(self, neural_input):
        return self.weight * neural_input + self.bias

    def transfer(self, activation):
        return 1.0 / (1.0 + exp(-activation))

    def feed_forward(self, neural_input):
        activation = self.activate(neural_input)
        neural_transfer = self.transfer(activation)
        return neural_transfer

    @classmethod
    def create(cls, weight, bias):
        return cls(weight, bias)


class HiddenNeuron(Neuron):
    def __init__(self, weight, bias) -> None:
        self.neuron_output = 0
        super().__init__(weight, bias)
        self.neuron_output = None

    def get_neuron_output(self):
        return self.neuron_output

    def feed_forward(self, neural_input):
        self.neuron_output = super().feed_forward(neural_input)
        return self.neuron_output

    def __repr__(self) -> str:
        return "hidden_neuron"


class SensoryNeuron(Neuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)
        self.input_state = None

    @abstractmethod
    def get_sensor_input(self):
        pass

    def get_neuron_output(self):
        return self.get_sensor_input()

    @property
    def input_state(self):
        return self.__input_state

    @input_state.setter
    def input_state(self, state):
        self.__input_state = state


class ActionNeuron(Neuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)
        self.neuron_output = 0

    def get_neuron_output(self):
        return self.neuron_output

    def feed_forward(self, neural_input):
        self.neuron_output = super().feed_forward(neural_input)
        return self.neuron_output
