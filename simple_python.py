#basically this checks if the together ai API is working or not
# if it is working then it will print "Hello, world!" in the console
# if it is not working then it will print an error message

import os
import openai

client = openai.OpenAI(
  api_key="tgp_v1_Y0LTi2p7Saow_0Us38sNK44bzZsvV0XpaxUgtwQg7rM",
  base_url="https://api.together.xyz/v1",
)

response = client.chat.completions.create(
  model="deepseek-ai/DeepSeek-R1",
  messages=[{"role": "user", "content": "Hello, world!"}],
)
print(response.choices[0].message.content)