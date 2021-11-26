from .abstract import ActionNeuron


class ActionMux:
    def __init__(self) -> None:
        self.mux = {0: MoveLeft, 1: MoveRight, 2: MoveBack, 3: MoveForward}

    def select_neuron(self, neuron_idx):
        return self.mux.get(neuron_idx)


class MoveLeft(ActionNeuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)

    def __repr__(self) -> str:
        return "move_left"


class MoveRight(ActionNeuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)

    def __repr__(self) -> str:
        return "move_right"


class MoveBack(ActionNeuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)

    def __repr__(self) -> str:
        return "move_back"


class MoveForward(ActionNeuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)

    def __repr__(self) -> str:
        return "move_forward"
