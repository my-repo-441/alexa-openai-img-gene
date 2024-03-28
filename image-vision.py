from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-6ctCbGpXizEe2iVIO0X6AiO3/user-34JYIi4w60JwZ0pf4FRH5vZJ/img-zYWUGkmAQchaCXw6FP1GKicz.png?st=2024-03-25T23%3A26%3A51Z&se=2024-03-26T01%3A26%3A51Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-25T21%3A02%3A28Z&ske=2024-03-26T21%3A02%3A28Z&sks=b&skv=2021-08-06&sig=kI0mjWz8pIQMumw7N6eEWZ8t8M8ntrM15qXuyordchk%3D",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

# 結果の 'content' のみを出力
print(f"content = {response.choices[0].message.content}")
