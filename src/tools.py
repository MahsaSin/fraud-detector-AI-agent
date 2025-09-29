import re
import os

from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

from conf import PATTERNS, THRESHOLDS

# Load keys
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# Tool 1: regex-based scam checker
@tool
def pattern_check(offer_text: str) -> dict:
    """Check text for scam patterns. Returns rating, score, and reasons."""
    text = offer_text.lower()
    score, reasons = 0, []
    for pat, (w, msg) in PATTERNS.items():
        if re.search(pat, text):
            score += w
            reasons.append(msg)

    if score >= THRESHOLDS["RED"]:
        rating = "RED"
    elif score >= THRESHOLDS["AMBER"]:
        rating = "AMBER"
    else:
        rating = "GREEN"

    return {"rating": rating, "score": score, "reasons": reasons}

# Tool 2: built-in Tavily search
search_tool = TavilySearchResults(max_results=3, tavily_api_key=TAVILY_API_KEY)
