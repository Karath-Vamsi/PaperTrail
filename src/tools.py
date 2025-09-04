# tools.py
from crewai_tools import tool
from langchain_community.tools import ArxivQueryRun, DuckDuckGoSearchRun

@tool('DuckDuckGoSearch')
def DuckDuckGoSearchTool():
    """
    A tool for searching the web using DuckDuckGo.
    """
    return DuckDuckGoSearchRun()

@tool('ArxivSearch')
def ArxivSearchTool():
    """
    A tool for searching for academic papers on Arxiv.
    """
    return ArxivQueryRun()
