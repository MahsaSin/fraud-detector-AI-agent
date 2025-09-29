import os, json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from conf import SYSTEM_PROMPT, MODEL_VERSION
from schema import FraudGuardResult
from uuid import uuid4


from tools import pattern_check, search_tool 

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Build agent
def build_agent_executor() -> AgentExecutor:
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])
    llm = ChatOpenAI(model=MODEL_VERSION, temperature=0, api_key=OPENAI_API_KEY)
    tools = [pattern_check, search_tool]
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=False)

# Run agent
def run_fraud_agent(query: str) -> dict:
    agent = build_agent_executor()
    raw = agent.invoke({"input": query})
    output = raw.get("output", raw)
    try:
        data = json.loads(output) if isinstance(output, str) else output
    except Exception:
        data = {"rating": "UNKNOWN", "score": 0, "reasons": [], "evidence": [], "disclaimer": str(output)}
    return {
        "rating": data.get("rating", "UNKNOWN"),
        "score": int(data.get("score", 0) or 0),
        "reasons": list(data.get("reasons", []) or []),
        "evidence": list(data.get("evidence", []) or []),
        "disclaimer": data.get("disclaimer", "Educational triage only. Not investment advice."),
    }


# def pretty_print(result: FraudGuardResult):
#     print("\n=== FraudGuard Result ===")
#     print(f"Risk rating : {result.rating}  (score: {result.score})")
#     print("\nReasons:")
#     for r in result.reasons:
#         print(f" - {r}")
#     if result.evidence:
#         print("\nEvidence:")
#         for e in result.evidence:
#             print(f" - {e.title}: {e.url}")
#     print(f"\nDisclaimer: {result.disclaimer}")
#     print("=========================\n")

# if __name__ == "__main__":
#     query = "Offer: Guaranteed 25% monthly returns via crypto bot. Company: AlphaYield Capital."
#     result = run_fraud_agent(query)
#     pretty_print(result)