from pathlib import Path

# Use pathlib.Path for OUTPUT_DIR instead of os.path.join
OUTPUT_DIR = Path(__file__).parent.parent / "osint_reports"
# Queues for the swarm
SWARM_BASE_QUEUE = "swarm"
