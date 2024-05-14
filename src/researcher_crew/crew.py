from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool

# tools
search_tool = SerperDevTool()


@CrewBase
class TownHallInnovationCrew():
    """TownHallInnovationCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o")

    @agent
    def townhall_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['townhall_researcher'],
            llm=self.llm,
            tools=[search_tool]
        )

    @agent
    def innovation_center_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['innovation_center_analyst'],
            llm=self.llm
        )
    
    @task
    def research_townhall_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_innovation_center_task'],
            agent=self.townhall_researcher(),
            
        )

    @task
    def analyze_innovation_center_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_innovation_center_task'],
            agent=self.innovation_center_analyst()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2
        )