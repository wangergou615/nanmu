from src.agents.agent import Agent


def test_agent_creation():
    agent = Agent("test-agent")
    assert agent.name == "test-agent"


def test_agent_run():
    agent = Agent("test-agent")
    result = agent.run("hello")
    assert result is not None
