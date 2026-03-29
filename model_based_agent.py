from environment_01 import Agent, loc_A, loc_B, loc_C


def ModelBasedVacuumAgent():
    model = {loc_A: None, loc_B: None}

    def program(percept):
        location, status = percept
        model[location] = status

        if model[loc_A] == model[loc_B] == "Clean":
            return "NoOp"
        elif status == "Dirty":
            return "Suck"
        elif location == loc_A:
            return "Right"
        else:
            return "Left"

    return Agent(program)


def ModelBasedTriVacuumAgent():
    model = {loc_A: None, loc_B: None, loc_C: None}

    def program(percept):
        location, status = percept
        model[location] = status

        if model[loc_A] == model[loc_B] == model[loc_C] == "Clean":
            return "NoOp"
        elif status == "Dirty":
            return "Suck"
        elif location == loc_A:
            return "Right"
        elif location == loc_B:
            if model[loc_A] == "Clean":
                return "Right"
            else:
                return "Left"
        else:
            return "Left"

    return Agent(program)
