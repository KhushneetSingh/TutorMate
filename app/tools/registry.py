# app/tools/registry.py
from typing import Callable, Dict, Any
import json

Tool = Callable[..., Any]

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Tool] = {}

    def register(self, name: str, fn: Tool):
        self._tools[name] = fn

    def call(self, name: str, *args, **kwargs):
        if name not in self._tools:
            raise KeyError(f"Tool '{name}' not registered")
        return self._tools[name](*args, **kwargs)

    def list_tools(self):
        return list(self._tools.keys())

registry = ToolRegistry()