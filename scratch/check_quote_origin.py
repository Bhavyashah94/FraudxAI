import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Users\bhavy\.gemini\antigravity\brain\bb46deb3-54dc-4cb9-a946-6206c822c9a5\.system_generated\logs\transcript_full.jsonl"

with open(path, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        if 275 <= idx <= 285:
            data = json.loads(line)
            content = str(data.get("content", ""))
            print(f"=== Line {idx} (Step {data.get('step_index')}) ===")
            if "Banks use complex AI models" in content:
                print("FOUND IN LINE", idx)
                # print lines around it
                for cl in content.split('\n'):
                    if any(w in cl for w in ["Banks use", "Goal", "Title", "Right Side", "SHAP", "What They Did"]):
                        print("  ", cl)
