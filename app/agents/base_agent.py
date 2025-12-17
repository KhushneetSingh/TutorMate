import uuid
import logging
from datetime import datetime
from typing import Dict, Any

from app.memory.redis_memory import RedisMemory

logger = logging.getLogger(__name__)
memory = RedisMemory()


class BaseAgent:
    """
    Base class for all agents.
    Provides:
    - identity
    - persistent state
    - event logging
    - safe execution wrapper
    """

    def __init__(self, agent_id: str | None = None):
        self.agent_id = agent_id or str(uuid.uuid4())
        self.state: Dict[str, Any] = memory.get_state(self.agent_id) or {}
        self.started_at = datetime.utcnow().isoformat()

        self._log_event("agent_started", {"state": self.state})

    # -------- Memory --------
    def save_state(self):
        memory.set_state(self.agent_id, self.state)

    def get_events(self, limit: int = 50):
        return memory.get_events(self.agent_id, limit)

    # -------- Logging --------
    def _log_event(self, event_type: str, payload: Dict[str, Any]):
        event = {
            "type": event_type,
            "payload": payload,
            "timestamp": datetime.utcnow().isoformat(),
        }
        memory.append_event(self.agent_id, event)
        logger.info(f"[{self.__class__.__name__}] {event_type}: {payload}")

    # -------- Execution --------
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Public execution entrypoint.
        Wraps agent logic with logging and failure safety.
        """
        self._log_event("input_received", input_data)

        try:
            result = self._execute(input_data)
            self._log_event("execution_success", result)
            self.save_state()
            return result

        except Exception as e:
            self._log_event("execution_failed", {"error": str(e)})
            raise

    def _execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Implement this in child agents.
        """
        raise NotImplementedError