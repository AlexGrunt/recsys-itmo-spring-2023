from enum import Enum

import mmh3


class Treatment(Enum):
    C = 0
    T1 = 1
    T2 = 2
    T3 = 3
    T4 = 4
    T5 = 5
    T6 = 6


class Split(Enum):
    HALF_HALF = 2
    FOUR_WAY = 4
    FIVE_WAY = 5
    SEVEN_WAY = 7


class Experiment:
    """
    Represents a single A/B experiment. Assigns
    any user to one of the treatments based on
    experiment name and user ID.

    An example usage::

        experiment = Experiments.AA
        if experiment.assign(user) == Treatment.C:
            # do control actions
            ...
        elif experiment.assign(user) == Treatment.T1:
            # do treatment actions
            ...

    """

    def __init__(self, name: str, split: Split):
        self.name = name
        self.split = split
        self.hash = mmh3.hash(self.name)

    def assign(self, user: int) -> Treatment:
        user_hash = mmh3.hash(str(user), self.hash, False)
        return Treatment(user_hash % self.split.value)

    def __repr__(self):
        return f"{self.name}:{self.split}"


class Experiments:
    """
    A static container for all the existing experiments.
    """

    # TODO Seminar 6 step 5: Configure RECOMMENDERS A/B experiment

    AA = Experiment("AA", Split.HALF_HALF)
    STICKY_ARTIST = Experiment("STICKY_ARTIST", Split.HALF_HALF)
    TOP_POP = Experiment("TOP_POP", Split.FOUR_WAY)
    USER_BASED = Experiment("USER_BASED", Split.HALF_HALF)
    PERSONALIZED = Experiment("PERSONALIZED", Split.HALF_HALF)
    CONTEXTUAL = Experiment("CONTEXTUAL", Split.HALF_HALF)
    RECOMMENDERS = Experiment("RECOMMENDERS", Split.HALF_HALF)

    def __init__(self):
        self.experiments = [Experiments.RECOMMENDERS]
