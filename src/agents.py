# agents.py
from crewai import Agent
from langchain_openai import ChatOpenAI
from tools import ArxivSearchTool, DuckDuckGoSearchTool
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the language model
llm = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        model="openai/gpt-4.1-nano", # this is not free, make limited calls per day
        temperature=0.5,
        max_tokens=750
    )

class ResearchAgents:
    """
    A class to define the research agents.
    """
    def researcher_agent(self):
        """
        Agent responsible for gathering research papers and articles.
        """
        return Agent(
            role='Senior Researcher',
            goal='Uncover groundbreaking technologies and research papers in {topic}',
            backstory=(
                "As a seasoned researcher, you have a knack for finding the most relevant"
                " and impactful research papers and articles from various online sources."
                " You are an expert in using search tools to find information."
            ),
            tools=[DuckDuckGoSearchTool(), ArxivSearchTool()],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def analyst_agent(self):
        """
        Agent responsible for analyzing the gathered research.
        """
        return Agent(
            role='Principal Analyst',
            goal='Analyze the gathered research and create a detailed report on {topic}',
            backstory=(
                "With a sharp eye for detail and a deep understanding of technology,"
                " you analyze research findings to identify key trends, breakthroughs,"
                " and potential implications. You are an expert at creating structured reports."
            ),
            tools=[],
            llm=llm,
            verbose=True,
            allow_delegation=True
        )

    def writer_agent(self):
        """
        Agent responsible for writing the final research report.
        """
        return Agent(
            role='Professional Writer',
            goal='Write a clear, concise, and engaging research report on {topic}',
            backstory=(
                "You are a skilled writer who can transform complex technical information"
                " into an easy-to-understand and engaging report. You specialize in creating"
                " markdown reports and comparison tables."
            ),
            tools=[],
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
