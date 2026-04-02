import os
import time
from datetime import datetime, timezone


def main() -> None:
    interval_seconds = int(os.getenv("INTERVAL_SECONDS", "5"))
    print("worker started; polling loop active")
    while True:
        now = datetime.now(tz=timezone.utc).isoformat()
        print(f"[{now}] worker heartbeat")
        time.sleep(interval_seconds)


if __name__ == "__main__":
    main()
