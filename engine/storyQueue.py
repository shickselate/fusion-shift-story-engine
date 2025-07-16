from eventGenerator import generate_event
from narrativeBuilder import format_narrative
from datetime import datetime
from collections import deque
import time
import random

# Simulated queue for incoming game events
class StoryQueue:
    def __init__(self):
        self.queue = deque()

    def add_event(self, event):
        event["timestamp"] = datetime.utcnow().isoformat()
        self.queue.append(event)

    def process_next(self, tone="neutral"):
        if self.queue:
            event = self.queue.popleft()
            story = format_narrative(event["main_actor"], 
                                     event["type"],
                                     tone=tone,
                                     outcome=event.get("outcome"))
            return {
                "event": event,
                "story": story
            }
        return None

    def process_all(self, tone="neutral"):
        results = []
        while self.queue:
            results.append(self.process_next(tone))
        return results

# Example: demo flow
if __name__ == "__main__":
    q = StoryQueue()

    print("⏳ Generating sample events...")
    for _ in range(3):
        e = generate_event()
        q.add_event(e)
        time.sleep(random.uniform(0.3, 1.0))  # Simulate staggered arrival

    print("\n📜 Narratives from the queue:")
    for result in q.process_all(tone="cinematic"):
        print("\n---")
        print(result["story"])
