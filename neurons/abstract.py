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
        super().__init__(weight, bias)
        self.neuron_output = None

    def get_neuron_output(self):
        return self.neuron_output

    def feed_forward(self, neural_input):
        self.neuron_output = super().feed_forward(neural_input)
        return self.neuron_output


class SensoryNeuron(Neuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)

    @abstractmethod
    def get_sensor_input(self):
        pass

    def get_neuron_output(self):
        return self.get_sensor_input()


class ActionNeuron(Neuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)
