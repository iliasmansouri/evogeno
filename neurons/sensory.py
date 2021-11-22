from .abstract import SensoryNeuron


class SensoryMux:
    def __init__(self) -> None:
        self.mux = {0: XPos, 1: YPos}

    def select_neuron(self, neuron_idx):
        return self.mux.get(neuron_idx, lambda: "Invalid neuron index")


class XPos(SensoryNeuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)

    def __repr__(self) -> str:
        return "x_pos"

    def get_sensor_input(self):
        return 0.5


class YPos(SensoryNeuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)

    def __repr__(self) -> str:
        return "x_pos"

    def get_sensor_input(self):
        return 0.5
