from crewai import Crew,Process
from agent.agents import blog_researcher,blog_writer
from tasks.tasks import research_task,write_task


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100, # Optional: Maximum requests per minute for all agents
  share_crew=True # Optional: Share the crew with other users
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'AI VS ML VS DL vs Data Science'})
print(result)