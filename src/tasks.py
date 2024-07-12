from dotenv import load_dotenv
from crewai import Task
from crewai.project import task
from src.agents import MyAgents

load_dotenv()


class MyTasks(MyAgents):
    @task
    def research(self) -> Task:
        return Task(
            config=self.tasks_config["research"],
            agent=self.phd_researcher(),
        )

    @task
    def writing(self) -> Task:
        return Task(
            config=self.tasks_config["writing"],
            agent=self.academic_writer(),
            context=[self.research()],
        )

    @task
    def reviewing_and_final_draft(self) -> Task:
        return Task(
            config=self.tasks_config["reviewing_and_final_draft"],
            agent=self.reviewer_supervisor(),
            context=[
                self.research(),
                self.writing(),
            ],
            output_file="results.md",
        )
