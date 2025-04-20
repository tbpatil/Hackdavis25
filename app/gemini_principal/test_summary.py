import sys
import os

# Add the grandparent directory to the Python path (so "knowledge" becomes importable)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gemini.summary_generator import generate_short_summary, generate_detailed_summary

def test_summaries(stage, confidence):
    print("=== Short Summary ===")
    short_text, short_tokens = generate_short_summary(stage, confidence)
    print(short_text)
    print(f"Tokens used: {short_tokens}")

    print("\n=== Detailed Summary ===")
    detailed_text, detailed_tokens = generate_detailed_summary(stage, confidence)
    print(detailed_text)
    print(f"Tokens used: {detailed_tokens}")

if __name__ == "__main__":
    test_summaries(stage=4, confidence=0.91)
