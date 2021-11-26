from dataclasses import dataclass
import os, binascii
from random import random, randint


@dataclass
class Gene:
    n_bits = 16

    def __post_init__(self):
        self.bit_seq = "".join([str(randint(0, 1)) for n in range(self.n_bits)])

    def mutate(self, mutation_proability) -> None:
        new_seq = list()
        for b in self.bit_seq:
            if random() < mutation_proability:
                new_seq.append("0" if b == "1" else "1")
            else:
                new_seq.append(b)

        self.bit_seq = new_seq


@dataclass
class Genome:
    gene_length: int = 1

    def __post_init__(self):
        self.genes = [Gene() for _ in range(self.gene_length)]
