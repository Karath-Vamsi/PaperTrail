# crew.py
from crewai import Crew, Process
from agents import ResearchAgents
from tasks import ResearchTasks

class ResearchCrew:
    """
    A class to create and manage the research crew.
    """
    def __init__(self, topic):
        self.topic = topic
        self.agents = ResearchAgents()
        self.tasks = ResearchTasks()

    def run(self):
        """
        Method to run the research crew.
        """
        # Create agents
        researcher = self.agents.researcher_agent()
        analyst = self.agents.analyst_agent()
        writer = self.agents.writer_agent()

        # Create tasks
        research_task = self.tasks.research_task(researcher, self.topic)
        analysis_task = self.tasks.analysis_task(analyst, self.topic, [research_task])
        writing_task = self.tasks.writing_task(writer, self.topic, [analysis_task])

        # Create the crew
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential,
            verbose=True
        )

        # Run the crew
        result = crew.kickoff()
        return result
