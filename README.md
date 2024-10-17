# Pub/Sub to Agentic Swarm POC

This is a POC for a system that ingests data from Pub/Sub, processes it using a Agentic Swarm model
Primarily in the use-case of open-source intelligence (OSINT) and financial intelligence (FININT)

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
nats pub swarm.stocks "What is the stock price of AAPL?"
nats pub swarm.united-states '{"question":"what is going on in United States?"}'
nats pub swarm.china '{"question":"what is going on in China?"}'
nats pub swarm.india '{"question":"what is going on in India?"}'
nats pub swarm.japan '{"question":"what is going on in Japan?"}'
nats pub swarm.south-korea '{"question":"what is going on in South Korea?"}'
nats pub swarm.russia '{"question":"what is going on in Russia?"}'
nats pub swarm.brazil '{"question":"what is going on in Brazil?"}'
nats pub swarm.mexico '{"question":"what is going on in Mexico?"}'
nats pub swarm.argentina '{"question":"what is going on in Argentina?"}'
nats pub swarm.colombia '{"question":"what is going on in Colombia?"}'
nats pub swarm.united-kingdom '{"question":"what is going on in United Kingdom?"}'
nats pub swarm.canada '{"question":"what is going on in Canada?"}'
nats pub swarm.spain '{"question":"what is going on in Spain?"}'
nats pub swarm.france '{"question":"what is going on in France?"}'
nats pub swarm.germany '{"question":"what is going on in Germany?"}'
nats pub swarm.italy '{"question":"what is going on in Italy?"}'
nats pub swarm.portugal '{"question":"what is going on in Portugal?"}'
nats pub swarm.switzerland '{"question":"what is going on in Switzerland?"}'
nats pub swarm.austria '{"question":"what is going on in Austria?"}'
nats pub swarm.belgium '{"question":"what is going on in Belgium?"}'
nats pub swarm.netherlands '{"question":"what is going on in Netherlands?"}'
nats pub swarm.denmark '{"question":"what is going on in Denmark?"}'
```
