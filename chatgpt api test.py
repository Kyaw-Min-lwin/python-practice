import openai

openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages = [{"role":"user", "content":prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == '__main__':
    while True:
        user_input = input('You : ')
        if user_input.lower() in ['quit', 'exit']:
            break

        response = chat_with_gpt(user_input)
        print(response)