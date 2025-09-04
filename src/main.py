# main.py
from crew import ResearchCrew
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def run():
    """
    Main function to run the research crew.
    """
    # Get the research topic from the user
    topic = input("Enter the research topic: ")

    # Initialize the ResearchCrew
    research_crew = ResearchCrew(topic)

    # Kick off the research process
    result = research_crew.run()

    # Print the final result
    print("\n\n########################")
    print("## Here is the Research Report")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    run()
