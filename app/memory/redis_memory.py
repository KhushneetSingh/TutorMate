import redis
import json
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


class RedisMemory:
    def __init__(self):
        self.client = redis.from_url(REDIS_URL, decode_responses=True)

    def _key(self, agent_id, suffix):
        return f"agent:{agent_id}:{suffix}"

    def set_state(self, agent_id, state):
        self.client.set(self._key(agent_id, "state"), json.dumps(state))

    def get_state(self, agent_id):
        value = self.client.get(self._key(agent_id, "state"))
        return json.loads(value) if value else {}

    def append_event(self, agent_id, event):
        self.client.rpush(self._key(agent_id, "events"), json.dumps(event))

    def get_events(self, agent_id, limit=50):
        raw = self.client.lrange(self._key(agent_id, "events"), -limit, -1)
        return [json.loads(x) for x in raw]