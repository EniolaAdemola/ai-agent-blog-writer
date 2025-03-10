import os
from crewai import Agent
from tools.tools import yt_tool
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"


# Create a advance blog content researcher
blog_researcher = Agent(
    role = "Blog Researcher from YouTube Videos",
    goal = "get the relevant video transcription for the topic: {topic} from the provided youtube channel",
    tools = [yt_tool],
    verbose = True, # get the detailed information
    memory = True, # to remember the previous conversation
    allow_delegation = True, # allow the agent to delegate the task to other agents
    backstory = (
        "Expert in understanding videos in AI, Data Science, Machine Learning and GEN AI and providing suggestion"
    ) # to provide the background of the agent
)

# Create a advance blog content writer
blog_writer = Agent(
    role = "Blog Writer",
    goal = "Narrate nice tech stories about the video: {topic} from Youtube Video",
    tools = [yt_tool],
    verbose = True, # get the detailed information
    memory= True, # to remember the previous conversation
    allow_delegation = False, 
    backstory = (
        "Expert in writing blogs on AI, Data Science, Machine Learning and GEN AI"
    ) # to provide the background of the agent 
)