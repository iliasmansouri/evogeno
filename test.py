import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from dataclasses import dataclass
from abc import ABC, abstractmethod
from math import exp

class Neuron(ABC):
    def __init__(self,weight,bias) -> None:
        self.weight = weight
        self.bias = bias
        
    def activate(self,neural_input):
        return self.weight * neural_input + self.bias
    
    def transfer(self,activation):
        return 1.0 / (1.0 + exp(-activation))

    def feed_forward(self,neural_input):
        activation = self.activate(neural_input)
        neural_transfer = self.transfer(activation)
        return neural_transfer

class HiddenNeuron(Neuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)
        self.neuron_output = None
    def get_neuron_output(self):
        return self.neuron_output
    def feed_forward(self,neural_input):
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
        

class Neuron1(ActionNeuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)
    
    def __repr__(self) -> str:
        return "n1"

    
class Neuron2(SensoryNeuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)
    def __repr__(self) -> str:
        return "n2"
    def get_sensor_input(self):
        return 0.5
class Neuron3(ActionNeuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)
    def __repr__(self) -> str:
        return "n3"

class Neuron4(HiddenNeuron):
    def __init__(self, weight, bias) -> None:
        super().__init__(weight, bias)



    def __repr__(self) -> str:
        return "n4"



class Graph:
    def __init__(self, directed=True):
        self._graph = defaultdict(set)
        self._directed = directed

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """
        for n, cxns in self._graph.items():  
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self.get_graph())

    def get_graph(self) -> dict:
        return dict(self._graph)  

    def get_connected_neurons(self,neuron):
        return self._graph[neuron]

    def execute(self):
        for s in g.get_graph():
            print(s)
            print('----------')
            for connected_neuron in g.get_connected_neurons(s):
                print("\t", connected_neuron)
                print(connected_neuron.feed_forward(s.get_neuron_output()))

n1 = Neuron1(1,0)
n2 = Neuron2(2,0)
n3 = Neuron3(3,0)
n4 = Neuron4(2,1)


connections = [(n2,n1), (n2,n4),(n4,n1) ,(n2, n3)]

g = Graph()
g.add_connections(connections)
g.execute()


