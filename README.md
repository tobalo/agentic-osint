# Pub/Sub to Agentic Swarm POC

This is a POC for a system that ingests data from Pub/Sub, processes it using a Agentic Swarm model

Primarily in the use-case of intelligence research for targeted topics, including financial market analysis and open-source intelligence (OSINT) at scale.

Example outputs can be found in the `example_reports` folder.

## Setup
```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
Ensure nats-server is running and create environment variables for NATS_URL and openai api key.

```sh
nats-server # visit https://nats.io
```

```sh
export NATS_URL="nats://localhost:4222"
export OPENAI_API_KEY="sk-proj-..."
```

## Run swarm worker
```sh
python3 swarm.py
```

## Publish message to NATS as subject `swarm.*`
If you'd like to change the queue, you can do so by editing the `SWARM_BASE_QUEUE` variable in `pkg/shared.py`.
```sh
nats pub swarm.texas "what is going on in with nuclear and data centers in Texas?"
nats pub swarm.california "what is going on in with nuclear and data centers in California?"
nats pub swarm.switzerland "what is going on in with nuclear and data centers in Switzerland?"
```
