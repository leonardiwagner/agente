import chainlit as cl
from openai import AsyncOpenAI


client = AsyncOpenAI()


@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a concise, helpful assistant."},
            *cl.chat_context.to_openai(),
        ],
    )

    await cl.Message(content=response.choices[0].message.content or "").send()
