__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from crew import ResearchCrew
from dotenv import load_dotenv

load_dotenv()

def main():
    """
    Main function to create and run the Streamlit UI.
    """
    st.set_page_config(page_title="Research Automation Crew", layout="wide")
    st.title(" 🤖 Research Automation Crew")

    with st.sidebar:
        st.header("About This Project")
        st.markdown(
            "This application uses a multi-agent system built with **CrewAI** to automate research on various topics. "
            "It leverages **LangChain** and **LLMs** to: "
            "1. **Gather** information from public sources and academic APIs (ArXiv, DuckDuckGo). "
            "2. **Analyze** the findings to identify key trends and breakthroughs. "
            "3. **Generate** a structured markdown report, including a comparison table."
        )
        st.info("💡 **How to Use:**\n"
                "1. Enter a research topic in the text box.\n"
                "2. Click the 'Start Research' button.\n"
                "3. Wait for the crew to complete the tasks.\n"
                "4. The final report will appear below.")

    st.header("Enter Your Research Topic")
    topic = st.text_input("Topic:", placeholder="e.g., 'Quantum Computing breakthroughs'", key="topic_input")

    if st.button("Start Research", type="primary"):
        if topic:
            st.write(f"### Starting research on: **{topic}**")
            st.info("The crew is working... This may take a few minutes. Please wait.")
            
            with st.spinner('Research in progress...'):
                try:
                    research_crew = ResearchCrew(topic)
                    result = research_crew.run()

                    st.success("Research completed!")
                    st.balloons()
                    st.subheader("Final Research Report")
                    st.markdown(result, unsafe_allow_html=True)
                
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.warning("Please check your API keys and internet connection.")
        else:
            st.warning("Please enter a research topic to begin.")

if __name__ == "__main__":
    main()