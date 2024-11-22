# HeartPole

## The Why

*HeartPole* is a simple Gymnasium for benchmarking Reinforcement Learning algorithms. Think CartPole for healthcare. It is meant as a first test for reinforcement learning techniques aimed at the Healthcare domain, before moving on to actual clinical data like [MIMIC III](https://mimic.physionet.org) 

This project includes a [tutorial on creating your own Gymnasium environment](HeartPole.ipynb), using HeartPole as an example, as well as a [writeup of experimental results](HeartPole_abstract.pdf), submitted to HEALTHINF conference. 

## The What

You are a developer working on an important project.
You want to maximize your productivity, but not at the expense of health - any serious health issue will negate all the effects of increased productivity.

Action space is discrete with 4 possible actions:

```
[do_nothing, drink_coffee, drink_beer, sleep]
```

Observation space is continious, with 6 dimensions:

```
['alertness', 'hypertension', 'intoxication',
 'time_since_slept', 'time_elapsed', 'work_done']
```

Your productivity mainly depends on alertness, you get a reward of 1 for every unit of work done and a reward of -100 if you suffer a heart attack.

## The How

Install with

```
pip install heartpole
```

Create an environment with

```
from heartpole import HeartPole
env = HeartPole()
```

and use your favourite reinforcement learning algorithm, for example, from [keras-rl](https://github.com/keras-rl/keras-rl)