from ice.recipe import recipe
from ice.agents.openai import OpenAIAgent


def make_qa_prompt(question: str) -> str:
    return f"""Answer the following question:

Question: "{question}"
Answer: "
""".strip()


async def answer(question: str = "Write hello world in python"):
    prompt = make_qa_prompt(question)

    answer = await OpenAIAgent(model='code-davinci-002').complete(prompt=prompt, stop='"')
    return answer


if __name__ == '__main__':
    recipe.main(answer)
