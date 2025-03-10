from crewai import Task
from tools.tools import yt_tool
from agent.agent import blog_researcher, blog_writer

# Research Task
research_task = Task(
    description = (
        "Identify the video {topic}"
        "Get detailed information about the video from the channel video"
    ),
    expected_output = "A comprehensive report based on the {topic} of the video content.",
    tools = [yt_tool],
    agent = blog_researcher
)

# Writing Task
write_task = Task(
    description = (
        "Get the information from the youtube channel on the topic {topic}"
    ),
    expected_output = "Summarize the information from the youtube channel video on the topic {topic} and create the content for the blog post.",
    tools = [yt_tool],
    agent = blog_writer,
    async_execution = False,
    output_file = "blog-post.md" # save the output to the file
)