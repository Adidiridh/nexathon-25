from uagents import Agent, Model, Context

from ai_engine import UAgentResponse

agent = Agent()

MY_DATA = {"latitude": 47.198073, "longitude": 15.128294, "distance": 15} # example data, change for your use-case

OPEN_CHARGE_MAP_AGENT_ADDRESS = "agent1q2lxngcrx33qn3dsxp32ldwtly00s6dq5ha7srrfsk6kdye623gs2364men"

class EvRequest(Model):
    latitude: float
    longitude: float
    distance: float


@agent.on_event("startup")
async def get_ev_charger_data(ctx: Context):
    ctx.logger.info("Sending request for EV chargers...")
    await ctx.send(
        OPEN_CHARGE_MAP_AGENT_ADDRESS,
        EvRequest(
            latitude=MY_DATA["latitude"],
            longitude=MY_DATA["longitude"],
            distance=MY_DATA["distance"],
        ),
    )

@agent.on_message(model=UAgentResponse)
async def handle_open_charge_map_response(ctx: Context, sender: str, msg: UAgentResponse):
    ctx.logger.info(f"Got response from open charger map agent: {msg}")
    closest_charger = msg.options[0].value if msg.options else msg.message
    ctx.logger.info(f"Closest charger: {closest_charger}")

if __name__ == "__main__":
    agent.run()



    
