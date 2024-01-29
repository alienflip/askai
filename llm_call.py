import os, sys, time
from os.path import join, dirname
from dotenv import load_dotenv
from openai import OpenAI
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class LLM_api:
    def __init__(self) -> None:
        pass

    def q_chatGPT(self, message):
        client = OpenAI(api_key=os.environ.get("OPEN_API_KEY"))
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role":"user", "content":message}]
        )
        return completion.choices[0].message.content

    def q_mistral(self, message):
        api_key = os.environ["MISTRAL_KEY"]
        client = MistralClient(api_key=api_key)
        chat_response = client.chat(
            model="mistral-tiny",
            messages=[ChatMessage(role="user", content=message)],
        )
        return chat_response.choices[0].message.content

if __name__ == "__main__":
    llm_api = LLM_api()
    while 1:
        user_prompt = input("> ")
        output = llm_api.q_chatGPT(user_prompt)
        with open("askai/outputs/dummy.txt", "a") as f:
            f.write("> " + user_prompt +"\n")
            f.write(output + "\n\n")
        for char in output:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.025)
        print("")