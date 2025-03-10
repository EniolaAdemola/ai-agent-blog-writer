from crewai import Crew, Process
from agent.agent import blog_researcher, blog_writer
from tasks.tasks import research_task, write_task

# forming the crew with the agents and tasks
crew = Crew(
    agents = [blog_researcher, blog_writer],
    tasks = [research_task, write_task],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100, # maximum requests per minute
    share_crew = True # share the crew with other users
)

# run the crew
result = crew.kickoff(inputs={
    "topic": "AI VS ML VS DL vs Data Science"
})

print(result)