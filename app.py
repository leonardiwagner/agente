from email.mime import message

import chainlit as cl
import boto3
from mypy_boto3_bedrock_runtime.client import BedrockRuntimeClient
from mypy_boto3_bedrock_runtime import type_defs as bedrock_types


client: BedrockRuntimeClient = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)  

@cl.on_chat_start
async def start_chat():
    cl.user_session.set("messages", [])

@cl.on_message
async def on_message(message: cl.Message):
    print(message.__dict__)

    messages = cl.user_session.get("messages")
    print(type(messages))
    messages.append({"role": "user", "content": [{"text": message.content}]})
    print(type(messages))
    print(messages)

    response: bedrock_types.ConverseResponse = client.converse(
        modelId="us.anthropic.claude-haiku-4-5-20251001-v1:0", 
        messages=messages
    )  

    print(response)

   # tokens_input = response["usage"]["inputTokens"]
   # tokens_output = response["usage"]["outputTokens"]

    print("Log - cache input: " + str(response["usage"]["cacheReadInputTokens"]) + ", write: " + str(response["usage"]["cacheWriteInputTokens"]))

    assitant_message = response["output"]["message"]["content"][0]["text"]
    messages.append({"role": "assistant", "content": [{"text": assitant_message}]})
    cl.user_session.set("messages", messages)


    await cl.Message(
        content=assitant_message
    ).send()
