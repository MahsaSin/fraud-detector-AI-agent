# Scam pattern
PATTERNS = {
    r"\bguarantee(?:d|s)?\b": (20, "Uses 'guaranteed'"),
    r"\brisk[-\s]?free\b": (10, "Claims 'risk-free'"),
    r"\b\d{2,}%\s*(daily|weekly|monthly|per\s*month|per\s*week)?\b": (
        15,
        "Unrealistic % returns",
    ),
}

THRESHOLDS = {"RED": 30, "AMBER": 15}

# Prompt for agent
SYSTEM_PROMPT = (
    "You are FraudGuard, a cautious triage bot for dubious investment offers.\n"
    "Tools:\n"
    "- pattern_check: detect scammy language\n"
    "- tavily_search_results_json: check web/regulators\n\n"
    # NOTE: escape the braces around title/url with double braces:
    "Return JSON with keys: rating (RED/AMBER/GREEN), score, reasons, "
    "evidence (list of objects with '{{title}}' and '{{url}}'), disclaimer.\n"
    "Keep it brief and neutral."
)

MODEL_VERSION = "gpt-5-mini"
