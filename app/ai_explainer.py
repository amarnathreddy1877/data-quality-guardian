"""
app/ai_explainer.py

This module uses OpenAI's GPT models to generate plain-English explanations
for data quality issues and suggests fixes in Pandas and SQL.

Designed to help analysts and stakeholders quickly understand dataset problems.
"""

import os
import openai

# ✅ Option 1: Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")  

def explain_issues(report: dict) -> str:
    """
    Generate AI-powered explanations for a data quality report.
    
    Parameters:
        report (dict): Dictionary containing data quality issues
    
    Returns:
        str: Human-readable explanation with suggested fixes
    """

    # Prompt to guide the AI
    prompt = f"""
You are a data quality expert. 
Explain the following dataset issues in simple, clear English, 
and provide suggestions on how to fix them using Pandas or SQL:

{report}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # high-quality, cost-efficient model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3        # less randomness, more precise suggestions
        )

        explanation = response['choices'][0]['message']['content']
        return explanation

    except Exception as e:
        # Handle errors gracefully
        return f"⚠️ Error generating AI explanation: {e}"
