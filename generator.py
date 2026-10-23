import random
import time
from datetime import datetime, timezone

def generate_sensor_frame(machine_id="CNC-01"):
    return {
        "machine_id": machine_id,
        "temperature": round(60.0 + random.gauss(0, 3.0), 2),
        "vibration_rms": round(1.5 + abs(random.gauss(0, 0.4)), 3),
        "pressure_psi": round(100.0 + random.gauss(0, 5.0), 2),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

if __name__ == "__main__":
    for _ in range(5):
        print(generate_sensor_frame())
        time.sleep(0.1)
