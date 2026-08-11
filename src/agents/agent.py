"""Basic agent abstraction for Nanmu AI Workspace."""


class Agent:
    """Minimal AI workflow agent prototype."""

    def __init__(self, name: str):
        self.name = name

    def run(self, task: str) -> str:
        return f"{self.name} executing task: {task}"
