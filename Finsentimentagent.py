from uagents import Agent, Context, Model


class FinancialSentimentRequest(Model):
    text: str


class FinancialSentimentResponse(Model):
    positive: float
    neutral: float
    negative: float


agent = Agent()

AI_AGENT_ADDRESS = "agent1qtfz9zr5sh7jx55uvcvnf4ehsk6z2m5udesueyqr927q6rvznsjlc4npmp0"

prompt = (
    "Apple has launched its iphone 16 and the sales are half the times of iphone 15."
)


@agent.on_event("startup")
async def handle_startup(ctx: Context):
    """Send the prompt to the AI agent on startup."""
    await ctx.send(AI_AGENT_ADDRESS, FinancialSentimentRequest(text=prompt))
    ctx.logger.info(f"Sent prompt to AI agent: {prompt}")


@agent.on_message(FinancialSentimentResponse)
async def handle_response(ctx: Context, sender: str, msg: FinancialSentimentResponse):
    """Do something with the response."""
    ctx.logger.info(f"Received response from: {sender}: {msg}")


if __name__ == "__main__":
    agent.run()
