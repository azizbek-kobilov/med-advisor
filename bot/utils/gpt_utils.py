from decouple import config
from openai import OpenAI


client = OpenAI(
    api_key=config('CHATGPT_API_KEY')
)


def comp(PROMPT, max_tokens=50, outputs=3):
    try:
        completion = client.completions.create(
            model="text-davinci-003",
            prompt=PROMPT,
            max_tokens=max_tokens,
            n=outputs
        )
    except:
        return ['Что-то пошло не так... GPT не отвечает']

    output = list()
    for k in completion.choices:
        output.append(k.text)

    return output


async def get_drug_info_from_chatgpt(drug_name):
    result = comp("Предоставьте подробную информацию о лекарстве " + drug_name, max_tokens=100, outputs=1)
    return result[0]
