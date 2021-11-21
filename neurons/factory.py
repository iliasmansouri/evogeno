from abstract import Neuron, HiddenNeuron
from sensory import SensoryMux
from action import ActionMux


class MoveLeft:
    def execute(self, coord):
        x = coord[0]
        y = coord[1]
        if x > 0:
            x -= 1
        return (x, y)


class MoveRight:
    def execute(self, coord):
        x = coord[0]
        y = coord[1]
        if x < 128:
            x += 1
        return (x, y)

class SourceDecoding:
    def __init__(self) -> None:
        self.index = 0
        self.type_indices = (1,3)
        self.weight_indices = (4,7)
        self.bias_index = 8

class SinkDecoding:
    def __init__(self) -> None:  
        self.index = 9
        self.type_indices = (10,11)
        self.weight_indices = (12,13)
        self.bias_index = 14

class NeuronFactory:
    def __init__(self) -> None:
        self.sensor_mux = SensoryMux()
        self.action_mux = ActionMux()
        
        self.source_decoding = SourceDecoding()
        self.sink_decoding = SinkDecoding()
        
    def create_neuron(self, gene):
        if self.check_nth_bit_set(gene, 0):
            return MoveLeft()
        else:
            return MoveRight()
    
    def create_neurons(self,gene) -> list:
        neurons = list()
        for code in [self.source_decoding,self.sink_decoding]:
            neurons.append(self.__get_neuron(gene,code))
        return neurons
    def __get_neuron(self, gene,code) -> Neuron:
        if self.check_nth_bit_set(gene, code.index):
            neuron_idx = self.__extract_sequence(gene, code.type_indices)
            neuron = self.sensor_mux.select_neuron(neuron_idx)
        else:
            neuron = HiddenNeuron
        weight = self.__extract_sequence(gene,code.weight_indices)
        bias = self.__extract_sequence(gene,code.bias_index)        
        return neuron(weight,bias)

    def __extract_sequence(self, gene, indices) -> int:
        start, end = indices
        code_seq = gene.get_binary()[start:end]
        return int(code_seq, 2)
    
    def create_connection(self, gene) -> tuple:
        source_neuron, sink_neuron = self.create_neurons(gene)
        return (source_neuron, sink_neuron)

    def check_nth_bit_set(self, gene, n) -> bool:
        return True if gene.get_list()[-(n+1)] == "1" else False

