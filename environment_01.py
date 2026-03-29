import random

# ambiente disponibilizado pelo professor, com algumas modificações, com algumas modificações.


class Thing:
    """This represents any physical object that can appear in an Environment.
    You subclass Thing to get the things you want. Each thing can have a
    .__name__  slot (used for output only)."""

    def __repr__(self):
        return "<{}>".format(getattr(self, "__name__", self.__class__.__name__))

    def is_alive(self):
        """Things that are 'alive' should return true."""
        return hasattr(self, "alive") and self.alive

    def show_state(self):
        """Display the agent's internal state. Subclasses should override."""
        print("I don't know how to show_state.")

    def display(self, canvas, x, y, width, height):
        """Display an image of this Thing on the canvas."""
        pass


class Agent(Thing):
    def __init__(self, program=None):
        self.alive = True
        self.bump = False
        self.holding = []
        self.performance = 0
        # Use callable() for a more robust check
        if program is None or not callable(program):

            def program(percept):
                # This is the default interactive program if no valid program is provided
                return eval(input("Percept={}; action? ".format(percept)))

        self.program = program

    def can_grab(self, thing):
        return False


class Environment:

    def __init__(self):
        self.things = []
        self.agents = []

    def percept(self, agent):
        raise NotImplementedError

    def execute_action(self, agent, action):
        raise NotImplementedError

    def default_location(self, thing):
        return None

    def exogenous_change(self):
        pass

    def is_done(self):
        return not any(agent.is_alive() for agent in self.agents)

    def step(self):
        if not self.is_done():
            actions = []
            for agent in self.agents:
                if agent.alive:
                    actions.append(agent.program(self.percept(agent)))
                else:
                    actions.append("")
            for agent, action in zip(self.agents, actions):
                self.execute_action(agent, action)
            self.exogenous_change()

    def run(self, steps=1000):
        for step in range(steps):
            if self.is_done():
                return
            self.step()

    def add_thing(self, thing, location=None):
        if not isinstance(thing, Thing):
            thing = Agent(thing)
        if thing in self.things:
            print("Can't add the same thing twice")
        else:
            thing.location = (
                location if location is not None else self.default_location(thing)
            )
            self.things.append(thing)
            if isinstance(thing, Agent):
                thing.performance = 0
                self.agents.append(thing)


# Locais
loc_A, loc_B, loc_C = "A", "B", "C"


# Quem sofre as alterações é o ambiente, por isso, as definições de percept e execute_action estão dentro da classe do ambiente, e não do agente, como no caso do ambiente de vácuo tradicional. O agente é apenas um "motor" que recebe os perceptos e retorna as ações, sem saber o que cada ação faz ou o que cada percepto significa. O ambiente é quem tem o controle sobre as regras do jogo, e o agente é apenas um "motor" que recebe os perceptos e retorna as ações, sem saber o que cada ação faz ou o que cada percepto significa.


class TrivialVacuumEnvironment(Environment):
    def __init__(self):
        super().__init__()
        self.status = {
            loc_A: random.choice(["Clean", "Dirty"]),
            loc_B: random.choice(["Clean", "Dirty"]),
        }

    def percept(self, agent):
        return agent.location, self.status[agent.location]

    def execute_action(self, agent, action):
        if action == "Right":
            agent.location = loc_B
            agent.performance -= 1

        elif action == "Left":
            agent.location = loc_A
            agent.performance -= 1

        elif action == "Suck":
            if self.status[agent.location] == "Dirty":
                agent.performance += 10
            self.status[agent.location] = "Clean"

        elif action == "NoOp":
            pass


class TriVacuumEnvironment(Environment):
    def __init__(self):
        super().__init__()
        self.status = {
            loc_A: random.choice(["Clean", "Dirty"]),
            loc_B: random.choice(["Clean", "Dirty"]),
            loc_C: random.choice(["Clean", "Dirty"]),
        }

    def percept(self, agent):
        return agent.location, self.status[agent.location]

    def execute_action(self, agent, action):
        if agent.location == loc_B and action == "Right":
            agent.location = loc_C
            agent.performance -= 1

        elif agent.location == loc_C and action == "Left":
            agent.location = loc_B
            agent.performance -= 1

        elif action == "Right":
            agent.location = loc_B
            agent.performance -= 1

        elif action == "Left":
            agent.location = loc_A
            agent.performance -= 1

        elif action == "Suck":
            if self.status[agent.location] == "Dirty":
                agent.performance += 10
            self.status[agent.location] = "Clean"

        elif action == "NoOp":
            pass


def TraceAgent(agent):
    old_program = agent.program

    def new_program(percept):
        action = old_program(percept)
        print(f"{agent} percebe {percept} e faz {action}")
        return action

    agent.program = new_program
    return agent
