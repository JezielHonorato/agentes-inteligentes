from environment_01 import *
from table_agent import TableDrivenVacuumAgent
from reflex_agent import ReflexVacuumAgent, ReflexTriVacuumAgent
from model_based_agent import ModelBasedVacuumAgent, ModelBasedTriVacuumAgent


def run_simulation(agent_factory, environment, start_location, steps=10):
    agent = TraceAgent(agent_factory())
    environment.add_thing(agent, start_location)

    print("\n==============================")
    print(f"Agente: {agent_factory.__name__}")
    print(f"Ambiente: {environment.__class__.__name__}")
    print("==============================\n")

    for step in range(steps):
        print(f"Passo {step + 1}")
        environment.step()

        print(
            "Estado:",
            environment.status,
            "| posição:",
            agent.location,
            "| desempenho:",
            agent.performance,
        )
        print()

    return agent.performance


def main():

    agent_factory = ModelBasedTriVacuumAgent
    # agent_factory = ReflexTriVacuumAgent
    # agent_factory = TableDrivenVacuumAgent
    # agent_factory = ReflexVacuumAgent
    # agent_factory = ModelBasedVacuumAgent

    if "Tri" in agent_factory.__name__:
        env = TriVacuumEnvironment()
        env.status = {
            loc_A: "Dirty",
            loc_B: "Dirty",
            loc_C: "Dirty",
        }
        start = loc_A
    else:
        env = TrivialVacuumEnvironment()
        env.status = {
            loc_A: "Dirty",
            loc_B: "Dirty",
        }
        start = loc_A

    run_simulation(agent_factory, env, start, steps=10)


if __name__ == "__main__":
    main()
