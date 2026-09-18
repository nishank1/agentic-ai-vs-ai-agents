# Overall architecture

```text
01 LLM
User → LLM → Response

02 AI Agent
User → Agent
          ├─→ Tool
          └─→ Response

03 Agentic Workflow
Input → Step 1 → Step 2 → Step 3 → Output

04 Multi-Agent
Input → Researcher → Writer → Reviewer → Output

05 Real-World Demo
Topic → Planner → Researcher → Editor → Content Brief
```
