import uuid
import logging
from datetime import datetime
from typing import Dict, Any

from pydantic import BaseModel

from app.memory.redis_memory import RedisMemory

logger = logging.getLogger(__name__)
memory = RedisMemory()


class BaseAgent:
    """
    ADK-style Agent:
    - has a role
    - receives a task
    - produces an output
    - persists memory
    """

    def __init__(self, role: str, agent_id: str | None = None):
        self.role = role
        self.agent_id = agent_id or str(uuid.uuid4())
        self.state = memory.get_state(self.agent_id) or {}

        self._log_event("agent_initialized", {"role": self.role})

    # ---- memory ----
    def save_state(self):
        memory.set_state(self.agent_id, self.state)

    def events(self, limit=50):
        return memory.get_events(self.agent_id, limit)

    # ---- observability ----
    def _log_event(self, event_type: str, payload: Dict[str, Any] | Any):
        """
        Store events in Redis in a JSON-safe way
        """

        # ✅ Make payload JSON-serializable
        if isinstance(payload, BaseModel):
            payload = payload.model_dump()
        elif isinstance(payload, dict):
            payload = {
                k: (v.model_dump() if isinstance(v, BaseModel) else v)
                for k, v in payload.items()
            }

        event = {
            "type": event_type,
            "payload": payload,
            "timestamp": datetime.utcnow().isoformat(),
        }

        memory.append_event(self.agent_id, event)
        logger.info(f"[{self.role}] {event_type}")

    # ---- ADK execution ----
    def run(self, task: Dict[str, Any]):
        """
        ADK-style execution:
        task → reasoning → output
        """
        self._log_event("task_received", task)

        try:
            output = self.execute(task)
            self._log_event("task_completed", output)
            self.save_state()
            return output
        except Exception as e:
            self._log_event("task_failed", {"error": str(e)})
            raise

    def execute(self, task: Dict[str, Any]):
        raise NotImplementedError