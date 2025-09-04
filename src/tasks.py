# tasks.py
from crewai import Task
from agents import ResearchAgents

class ResearchTasks:
    """
    A class to define the tasks for the research crew.
    """
    def research_task(self, agent, topic):
        """
        Task to research a given topic.
        """
        return Task(
            description=f"Identify the latest trends and breakthroughs in {topic}. "
                        f"Focus on finding key research papers and articles.",
            expected_output=f"A list of 5-10 relevant research papers and articles on {topic} with their URLs.",
            agent=agent,
        )

    def analysis_task(self, agent, topic, context):
        """
        Task to analyze the research findings.
        """
        return Task(
            description=f"Analyze the provided research context on {topic}. "
                        f"Summarize the key findings, identify major trends, "
                        f"and create a structured analysis.",
            expected_output=f"A detailed analysis report on {topic}, including key findings and trends."
                           f"The report should be well-structured and easy to read.",
            agent=agent,
            context=context
        )

    def writing_task(self, agent, topic, context):
        """
        Task to write the final report.
        """
        return Task(
            description=f"Write a comprehensive research report on {topic} based on the provided analysis."
                        f"The report should be in markdown format and include a comparison table of different technologies or approaches if applicable.",
            expected_output=f"A final research report in markdown format on {topic}, including an introduction,"
                           f" key findings, a comparison table, and a conclusion.",
            agent=agent,
            context=context
        )
