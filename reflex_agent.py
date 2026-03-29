import random
from environment_01 import Agent, loc_A, loc_B, loc_C

# Os agentes não possuem memória

def ReflexVacuumAgent():
    def program(percept):
        location, status = percept

        if status == "Dirty":
            return "Suck"
        elif location == loc_A:
            return "Right"
        elif location == loc_B:
            return "Left"

    return Agent(program)


def ReflexTriVacuumAgent():
    def program(percept):
        location, status = percept

        if status == "Dirty":
            return "Suck"
        elif location == loc_A:
            return "Right"
        elif location == loc_B:
            return random.choice(["Left", "Right"])
        elif location == loc_C:
            return "Left"

    return Agent(program)
