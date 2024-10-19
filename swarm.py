### AUTHOR: Tobalo Torres-Valderas
### DATE: 2024-10-16
### PURPOSE: Create a swarm of agents that can be used to perform targeted intelligence research
import os
import asyncio
import nats
import json
import logging

from pkg.agents import swarm
from pkg.shared import SWARM_BASE_QUEUE, OUTPUT_DIR
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

async def main():
    logging.info("Starting Swarm")
    nc = await nats.connect(os.getenv("NATS_URL"))
    logging.info(f"NATS connected to {nc.connected_url}")
    async def message_handler(msg):
        data = json.loads(msg.data.decode())
        question = data["question"]
        swarm_sub_queue = msg.subject.split(".")[-1]
        logging.info(f"Received message on: {swarm_sub_queue} with question: {question}")
        await swarm.arun(question)
    await nc.subscribe(f"{SWARM_BASE_QUEUE}.*", cb=message_handler)
    logging.info(f"Subscribed to {SWARM_BASE_QUEUE}.*")
    # Keep the program running to listen for incoming messages
    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        logging.info("Shutting down Swarm Consumer")
        await nc.close()

        
if __name__ == "__main__":
   if not os.path.exists(OUTPUT_DIR):
       os.makedirs(OUTPUT_DIR)
   asyncio.run(main())