# Multi-Agent-LLM-Research-Assistant
Multi-Agent LLM Framework for a research assistant for PhD scholars

### About
This repository includes implementation of a multi-agent based LLM framework for assisting researchers in writing well-structured and coherent sections of their research on a topic of their choosing. We have used `crewai` python library to build the agentic workflow, which uses Azure-OpenAI in the backend, but can be re-configured to use other LLMs as well with minor tweaks to the original codebase.

### Getting Started
Make sure you have python>=3.10 installed on your kernel. First, install the dependencies -<br>
```pip install -r requirements.txt```

Add the required environment variables for LLM in the `.env` in root - 
* AZURE_OPENAI_DEPLOYMENT
* AZURE_OPENAI_VERSION
* OPENAI_API_KEY
* OPENAI_ENDPOINT

Then, in `main.py`, change the `research_topic` and `research_paper_section` as per your requirement, then run `main.py` - <br>
```python main.py```

Once the agent execution is completed (usually takes ~1 min), the results are populated in the `results.md` file.

### Author
[Aseem Raghav](raghavaseem@gmail.com)
