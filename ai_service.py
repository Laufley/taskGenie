import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
    if not client.api_key:
        return ["Error: OpenAI API not configured"]
    try:
        prompt = f"""Break down the following task in a list of 3 to 5 simple and actionable subtasks.
        
        Task: {description}
        Format of the answer:
        - Subtask 1:
        - Subtask 2:
        - Subtask 3:
        - etc.

        Reply only with the list of subtasks, one per line, starting each linea with a hyphen """

        params = {
            "model" : "gpt-5",
            "messages" : [
                {"role": "system", "content": "you are a tasks management expert assistant who helps breaking down complex tasks into smaller steps that are simple and actionable"},
                {"role": "user", "content": prompt}
                ],
                "max_completion_tokens": 300,
                "verbosity": "medium",
                "reasoning_effort": "minimal"
        }

        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: Subtasks could not be generated."]

    except Exception as e:
        return [f"Error:{e}"]