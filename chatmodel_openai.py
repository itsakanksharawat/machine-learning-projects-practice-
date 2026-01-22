from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

result = model.invoke("What is the capital of India?")
print(result.content)
