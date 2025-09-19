# tools.py
import os
from dotenv import load_dotenv
from crewai_tools import ArxivPaperTool, TavilySearchTool

# Load environment variables at the top of the file
load_dotenv()

# Instantiate the tools directly
TavilyTool = TavilySearchTool()
ArxivSearchTool = ArxivPaperTool()