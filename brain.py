from dataclasses import dataclass

from genes import Genome
from neurons.factory import NeuronFactory
from collections import defaultdict

# Source Neuron Structure
#   if bit at index 0
#       0: select Sensory Neuron as input
#       1: select Hidden Neuron as input
#   bits at index 1 -> 4:
#       select neuron type

# Sink Neuron Structure
#   if bit at index 5
#       0: select Action Neuron as output
#       1: select Hidden Neuron as output
#   bits at index 6 -> 10:
#       select neuron type

# Weights
# Take last 5 bits and convert it into -1 to 1 range
# which encodes strength of source neuron to sink neuron


@dataclass
class Brain:
    genome: Genome
    directed: bool = True

    def __post_init__(self):
        self._graph = defaultdict(set)
        self.neuron_factory = NeuronFactory()
        self.neurons = list()
        self.construct()

    def execute(self, state):
        coord = state["coord"]
        for neuron in self.neurons:
            return neuron.execute(coord)

    def construct(self):
        genes = self.genome.genes

        for gene in genes:
            # print(gene)
            self.neurons.append(self.neuron_factory.create_neuron(gene))

        # print(self.neurons)
