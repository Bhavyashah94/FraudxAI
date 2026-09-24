import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Users\bhavy\.gemini\antigravity\brain\bb46deb3-54dc-4cb9-a946-6206c822c9a5\.system_generated\logs\transcript_full.jsonl"

with open(path, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        if 270 <= idx <= 292:
            data = json.loads(line)
            src = data.get("source")
            st = data.get("type")
            content = str(data.get("content", ""))
            print(f"=== Line {idx} (Step {data.get('step_index')}, {src}, {st}) ===")
            print(content[:2500])
            print("\n" + "="*50)
