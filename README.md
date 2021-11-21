<div id="top"></div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Based on the paper [Evolving Neural Networks through
Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf), this project sets out to experiments some of the concepts mentioned in the paper.

It's still very much a WiP.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- Python 3.9.7
- PyGame

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

In your Python environment:

```sh
pip install -r requirements.txt
```

### Installation

<!-- USAGE EXAMPLES -->

## Usage

For now, only 1 simulation is available where agents learn to migrate on the correct side of the world.

```sh
  python simulator.py
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] First Refactoring
  - [x] Separation of responsibility
  - [x] Type hinting
  - [x] Dedicated neuron folders
- [x] First version of a Graph based brain construction
- [x] Proper neural interaction with:
  - [x] activations
  - [x] propagations
- [x] Add first "proper" neurons:
  - [x] 4 cardinal movement neurons
  - [x] Location xy-location sensory neuron
- [ ] Test simple migration simulation with new graph based Brain
- [ ] Find a way to abstract the simulation to ease the creation of different simulation runs
- [ ] Find elegant solution to pass an agent's state to the Brain class
- [ ] Add more complex neurons:
  - [ ] Pheromone neurons
  - [ ] Kill neurons
  - [ ] Age neurons
  - [ ] Clock neurons
- [ ] Implement cost based actions dependent of calories

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

[Ilias Mansouri](https://www.linkedin.com/in/ilias-mansouri/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

<p align="right">(<a href="#top">back to top</a>)</p>
