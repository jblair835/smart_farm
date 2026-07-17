# agents/reviewer_agent.py
class ReviewerAgent:
    """
    Ivy reviews decisions for contradictions or missing logic.
    """

    def run(self, decisions):
        issues = []

        # --- Safety: ensure decisions structure is valid ---
        if not decisions or not isinstance(decisions, dict):
            return {"issues": ["Decision data missing or invalid."]}

        pesticide = decisions.get("pesticide", {})
        fertilizer = decisions.get("fertilizer", {})

        # --- Contradictions ---
        if pesticide.get("should_spray") and not pesticide.get("timing"):
            issues.append("Pesticide spraying approved but no timing provided.")

        if fertilizer.get("should_apply") and not fertilizer.get("timing"):
            issues.append("Fertilizer application approved but no timing provided.")

        # --- Risk alignment ---
        reason = pesticide.get("reason", "").lower()
        if pesticide.get("should_spray") and "wind" in reason:
            issues.append("Pesticide spraying approved despite wind risk.")

        return {"issues": issues}

    def speak(self, issues):
        if not issues:
            return "Inspector Ivy reporting — everything checks out."

        return "Inspector Ivy reporting — issues detected:\n" + "\n".join(
            f"• {i}" for i in issues
        )
