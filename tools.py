from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


def save_to_txt(data: str, filename: str = "reasearch_output.txt"):
    """Saves the given data to a text file with a timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    full_filename = f"{filename.split('.')[0]}_{timestamp}.txt"
    with open(full_filename, "w", encoding="utf-8") as file:
        file.write(data)
    print(f"Data saved to {full_filename}")
   
save_tool = Tool(
       name="Save_text_to_file",
       func=save_to_txt,
       description="Saves structured research data to a text file.",
   )

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="useful for when you need to look up current events or search the web for specific information",
)
api_wrapper = WikipediaAPIWrapper(top_k_results=4, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
