import os
from dotenv import load_dotenv
load_dotenv()

from src.researcher_crew.crew import TownHallInnovationCrew

def run():
    inputs = {
        'townhall': 'Lugo'
    }
    TownHallInnovationCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
