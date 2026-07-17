# agents/report_agent.py
class ReportAgent:
    """
    Produces final structured farm report.
    Sage provides persona-rich summary.
    """

    def run(
        self,
        weather_output,
        risk_output,
        data_output,
        advisor_output,
        reviewer_output,
        weather_voice,
        risk_voice,
        data_voice,
        advisor_voice,
        reviewer_voice
    ):
        # Fallbacks to prevent None from breaking formatting
        weather_voice = weather_voice or "Weather data unavailable."
        risk_voice = risk_voice or "No risk data available."
        data_voice = data_voice or "(No USDA data provided.)"
        advisor_voice = advisor_voice or "No recommendations available."
        reviewer_voice = reviewer_voice or "No review notes available."

        formatted = f"""
Sage reporting — here’s your real-time farm intelligence:

### 🌦 Weather Summary
{weather_voice}

### ⚠️ Risk Assessment
{risk_voice}

### 📊 Data Summary
{data_voice}

### 🧑‍🌾 Recommendations
{advisor_voice}

### 🔍 Review Notes
{reviewer_voice}
"""

        return {"formatted": formatted}

    def speak(self, formatted):
        return formatted
