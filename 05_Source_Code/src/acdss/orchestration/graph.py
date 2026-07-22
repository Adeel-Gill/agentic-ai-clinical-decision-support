"""LangGraph state graph (Layer 4 — Orchestration).

Wires the agents into a directed state graph with:
  * a coordinator/router entry node,
  * specialist agent nodes,
  * a **conflict-resolution** node that reconciles disagreeing agent outputs, and
  * a **verification gate** that must pass before the decision engine is reached.

The graph operates over :class:`AssessmentState`, a shared, additively-updated
state dict that every node reads from and writes to.
"""

from __future__ import annotations

from typing import Annotated, Any, TypedDict

from acdss.agents.base import AgentOutput
from acdss.llm.base import LLMClient
from acdss.memory.clinical_context import ClinicalContext


def _merge(existing: dict[str, Any], update: dict[str, Any]) -> dict[str, Any]:
    """Reducer for the ``outputs`` channel: merge agent outputs by name."""
    return {**existing, **update}


class AssessmentState(TypedDict, total=False):
    """Shared state threaded through the graph."""

    patient_id: str
    context: ClinicalContext
    plan: list[str]
    outputs: Annotated[dict[str, AgentOutput], _merge]
    conflicts: list[str]
    verified: bool
    requires_human_review: bool


def build_graph(llm: LLMClient) -> Any:
    """Construct and compile the LangGraph ``StateGraph``.

    Node/edge outline (to implement with ``langgraph.graph.StateGraph``):

        graph = StateGraph(AssessmentState)
        graph.add_node("coordinator", coordinator_node)
        graph.add_node("data_retrieval", ...)
        graph.add_node("monitoring", ...)
        graph.add_node("diagnosis", ...)
        graph.add_node("risk", ...)
        graph.add_node("treatment", ...)
        graph.add_node("explanation", ...)
        graph.add_node("conflict_resolution", conflict_resolution_node)
        graph.add_node("verification", verification_node)      # gate
        graph.set_entry_point("coordinator")
        # ... edges: coordinator -> specialists -> conflict_resolution
        #     -> verification -> (END if passed else back to coordinator/human)
        graph.add_conditional_edges("verification", _gate_router,
                                    {"pass": END, "revise": "coordinator"})
        return graph.compile()

    Args:
        llm: Injected LLM client shared by the agent nodes.
    """
    # TODO: build nodes (each wraps an Agent.run), add edges, compile.
    raise NotImplementedError


def conflict_resolution_node(state: AssessmentState) -> AssessmentState:
    """Reconcile disagreements between agent outputs.

    TODO: detect contradictions (e.g. treatment vs. differential vs. interaction
    warnings), record them in ``state['conflicts']``, and either resolve via an
    arbitration LLM call or flag for human review.
    """
    raise NotImplementedError


def verification_node(state: AssessmentState) -> AssessmentState:
    """Verification gate — runs the VerificationAgent and sets ``verified``.

    TODO: invoke VerificationAgent; set ``state['verified']`` and
    ``state['requires_human_review']``. Downstream edges block the decision
    engine unless ``verified`` is True.
    """
    raise NotImplementedError
