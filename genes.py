from dataclasses import dataclass
import os, binascii
from random import random


@dataclass
class Gene:
    # bit_seq = binascii.b2a_hex(os.urandom(2))

    def __post_init__(self):
        # self.bit_seq = randint(0,5000)
        self.bit_seq = binascii.b2a_hex(os.urandom(1))

    def get_binary(self) -> str:
        return bin(self.get_decimal())

    def get_decimal(self) -> int:
        return int.from_bytes(self.bit_seq, byteorder="big", signed=False)

    def get_list(self) -> list:
        return list(self.get_binary())[2:]

    def mutate(self, mutation_proability) -> None:
        gene_seq = self.get_list()

        for i in range(len(gene_seq)):
            if random() < mutation_proability:
                gene_seq[i] = "0" if gene_seq[i] == "1" else "1"

        s = "".join(gene_seq)

        self.bit_seq = self.bitstring_to_bytes(s)

    def bitstring_to_bytes(self, s) -> bytes:
        return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder="big")


@dataclass
class Genome:
    gene_length: int = 1

    def __post_init__(self):
        self.genes = [Gene() for _ in range(self.gene_length)]
