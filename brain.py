from dataclasses import dataclass

from genes import Genome
from neurons.factory import NeuronFactory
from collections import defaultdict
from neurons.abstract import SensoryNeuron, ActionNeuron


@dataclass
class Brain:
    genome: Genome
    _directed: bool = True

    def __post_init__(self):
        self._graph = defaultdict(set)
        self.neuron_factory = NeuronFactory()
        self.neurons = list()
        self.construct()

    def execute(self, state) -> dict:
        decisions = dict()
        for source_neuron in self.get_graph():
            if isinstance(source_neuron, SensoryNeuron):
                source_neuron.input_state = state
            for connected_neuron in self.get_connected_neurons(source_neuron):
                if isinstance(connected_neuron, ActionNeuron):
                    decisions[connected_neuron] = connected_neuron.feed_forward(
                        source_neuron.get_neuron_output()
                    )
        return decisions

    def construct(self):
        genes = self.genome.genes

        for gene in genes:
            neuron_pairs = self.neuron_factory.create_neurons(gene)
            if None not in neuron_pairs:
                self.add_connections([neuron_pairs])

    def add_connections(self, connections):
        """Add connections (list of tuple pairs) to graph"""
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """Add connection between node1 and node2"""
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """Remove all references to node"""
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
        """Is node1 directly connected to node2"""
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """Find any path between node1 and node2 (may not be shortest)"""
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
        return "{}({})".format(self.__class__.__name__, self.get_graph())

    def get_graph(self) -> dict:
        return dict(self._graph)

    def get_connected_neurons(self, neuron):
        return self._graph[neuron]
