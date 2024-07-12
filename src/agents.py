import yaml
from pathlib import Path
from dotenv import load_dotenv
from crewai import Agent
from langchain_openai import AzureChatOpenAI
from crewai.project import agent

load_dotenv()

root = Path().absolute()
config_dir = root / "src/config"


class MyAgents:
    def __init__(self, llm: AzureChatOpenAI) -> None:
        self.agents_config = yaml.safe_load(open(config_dir / "agents.yaml"))
        self.tasks_config = yaml.safe_load(open(config_dir / "tasks.yaml"))
        self.llm = llm

    @agent
    def phd_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["phd_researcher"],
            llm=self.llm,
        )

    @agent
    def academic_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["academic_writer"],
            llm=self.llm,
        )

    @agent
    def reviewer_supervisor(self) -> Agent:
        return Agent(
            config=self.agents_config["reviewer_supervisor"],
            llm=self.llm,
        )
