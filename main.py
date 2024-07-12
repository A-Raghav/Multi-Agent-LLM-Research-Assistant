from dotenv import load_dotenv
from src.crew import MyCrew


load_dotenv()

if __name__ == "__main__":
    crew = MyCrew(
        llm_name="llama3_70b",
        temperature=0.75,
    )
    inputs = {
        "research_topic": """ "Environmental Life Cycle Assessment (LCA) of Bioactives (such as fucoidan, alginate, etc.) from seaweed (especially brown seaweed) at laboratory scale and pilot scale" """,
        "research_paper_section": "Introduction",
    }
    response = crew.run(inputs=inputs)
    print(response)
