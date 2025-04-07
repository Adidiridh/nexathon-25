from uagents import Agent, Context, Model

agent = Agent()

AI_AGENT_ADDRESS = "agent1qdv2qgxucvqatam6nv28qp202f3pw8xqpfm8man6zyegztuzd2t6yem9evl"


class FinanceQA(Model):
    question: str


class Response(Model):
    text: str


question = FinanceQA(question="What is a stock?")


@agent.on_event("startup")
async def handle_startup(ctx: Context):
    """Send the prompt to the AI agent on startup."""
    await ctx.send(AI_AGENT_ADDRESS, question)
    ctx.logger.info(f"Sent question to Finance QA agent: {question.question}")


@agent.on_message(Response)
async def handle_response(ctx: Context, sender: str, msg: Response):
    """Do something with the response."""
    ctx.logger.info(f"Received response from: {sender}: {msg.text}")


if __name__ == "__main__":
    agent.run()
