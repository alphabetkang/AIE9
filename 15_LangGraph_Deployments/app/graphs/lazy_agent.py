"""An agent that only performs the user's request if it feels like it

The graph:
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.prompots import ChatPromptTemplate

from app.models import get_chat_model
from app.state import MessagesState
from app.tools import get_tool_belt


class AgentMood(BaseModel):
    feels_like_working: bool = Field(description="Whether the agent feels like doing its job")

def _build_model_with_tools():
    """Return a chat model instance bound to the current tool belt."""
    model = get_chat_model()
    return model.bind_tools(get_tool_belt())


def call_model(state: MessagesState) -> dict:
    """Invoke the model with the accumulated messages and append its response."""
    model = _build_model_with_tools()
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}

def route_to_action_or_mood_reflection(state: MessagesState):
    """Decide whether to execute tools or run the mood reflection."""
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return "action"
    return "mood_reflection"

def mood_reflection(state: MessageState):
    """Decide whether you want to complete the user's request."""

_mood_prompt = ChatPromptTemplate.from_template(
    "Given an initial query and a final response, determine if the agent feels like doing its job"
)


def build_graph():
    """Build an agent graph that interleaves model and tool execution."""
    graph = StateGraph(MessagesState)
    tool_node = ToolNode(get_tool_belt())
    graph.add_node("agent", call_model)
    graph.add_node("action", tool_node)
    graph.add_node("think_about_mood", think_about_mood)
    graph.add_edge(START, "agent")
    graph.add_conditional_edges("agent", think_about_mood, {"continue": "action", END: END})
    graph.add_conditional_edges("action", tools_condition, {"tools": "action", END: END})
    graph.add_edge("action", "agent")
    return graph


# Export compiled graph for LangGraph
graph = build_graph().compile()