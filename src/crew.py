import os
from typing import Dict
from dotenv import load_dotenv
from crewai.process import Process
from crewai import Crew
from langchain_openai import AzureChatOpenAI
from src.agents import MyAgents
from src.tasks import MyTasks

load_dotenv()


class MyCrew:
    def __init__(self) -> None:
        self.llm = self._create_llm()
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _create_llm(self) -> AzureChatOpenAI:
        return AzureChatOpenAI(
            openai_api_type="azure",
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            openai_api_version=os.getenv("AZURE_OPENAI_VERSION"),
            api_key=os.getenv("OPENAI_API_KEY"),
            azure_endpoint=os.getenv("OPENAI_ENDPOINT"),
            temperature=0.75,
        )

    def _create_agents(self) -> MyAgents:
        return MyAgents(self.llm)

    def _create_tasks(self) -> MyTasks:
        return MyTasks(self.llm)

    def _create_crew(self) -> Crew:
        return Crew(
            agents=[
                self.agents.phd_researcher(),
                self.agents.academic_writer(),
                self.agents.reviewer_supervisor(),
            ],
            process=Process.sequential,
            verbose=0,
        )

    def run(self, inputs: Dict) -> str:
        self.crew.tasks = [
            self.tasks.research(),
            self.tasks.writing(),
            self.tasks.reviewing_and_final_draft(),
        ]
        response = self.crew.kickoff(inputs=inputs)
        return response
