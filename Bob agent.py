import requests
from typing import Optional
from uagents import Agent, Context, Field, Model, Protocol

QUESTION = "Write the Javascript code to give me the sum from 1 to 10"

class AIRequest(Model):
    question: str = Field(
        description="The question that the user wants to have an answer for."
    )
class AIResponse(Model):
    answer: str = Field(
        description="The answer from AI agent to the user agent"
    )

@agent.on_event("startup")
async def ask_question(ctx: Context):
    ctx.logger.info(
        f"Asking AI agent to answer {QUESTION}"
    )
    await ctx.send(
        'agent1q2jz799u38llhjkzrftuqfyxaxpr8klfrpt45vkrtu5hj7lhwnkcxyyzsq7', AIRequest(question=QUESTION)
    )

@agent.on_message(model=AIResponse)
async def handle_data(ctx: Context, sender: str, data: AIResponse):
    ctx.logger.info(f"Got response from AI agent: {data.answer}")
