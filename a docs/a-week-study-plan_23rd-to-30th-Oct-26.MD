# Agentic AI Learning Resources — Consolidated Guide

_Compiled for: BeCCA MCP Server / ADK / A2A enablement_
_Plan window: **Start Oct 23, 2026 (Fri) → End Oct 29, 2026 (Thu)** — 1 week_
_Last updated: October 23, 2026 — all 43 links validated same day_

---

## 0. One-Week Schedule (Start: Oct 23, 2026 → End: Oct 29, 2026) — Full Focused Days

Revised assuming full dedicated days (no distractions) rather than evening-only sessions. This removes the main risk from the earlier version (fatigue/fragmented time after a workday) and allows room for GCP setup friction, deploy debugging, and a genuine stretch goal each day without slipping the Friday target.

| Day | Date | Focus | Resource(s) | Est. Time                                                                                                             | Buffer built in |
|---|---|---|---|-----------------------------------------------------------------------------------------------------------------------|---|
| Day 1 | **Fri, Oct 23** | ADK path + enterprise DB agents + badge | Google Skills: [Develop Agents with Agent Development Kit (ADK)](https://www.skills.google/paths/3545) (learning path) + [Build AI Agents with Enterprise Databases](https://www.skills.google/paths/3273/course_templates/1436) (MCP Toolbox for Databases — secure DB tools, vector + structured queries) + [Engineer AI Agents with ADK](https://www.skills.google/course_templates/1596) (skill badge). Also: set up your own GCP project, billing, and APIs — Google Skills labs use temporary credentials, but the Day 3+ Codelabs need your own project. | ~6–7 hrs                                                                                                              | ~1 hr for GCP project setup snags |
| Day 2 | **Sat, Oct 24** | Complete Day 1 content | Finish whatever remains of Day 1's three items — the ADK path is multi-course and the badge requires a challenge lab, so a full finish in one day is unlikely. Priority if short on time: badge challenge lab last. | ~3–4 hrs                                                                                                              | Spare time absorbs Day 1 overrun |
| Day 3 | **Sun, Oct 25** | MCP + A2A hands-on core | Codelabs: [Getting Started with MCP & A2A with ADK](https://codelabs.developers.google.com/getting-started-mcp-a2a-adk) (full build: MCP server → A2A agent → travel agent → Cloud Run deploy) | ~3–4 hrs                                                                                                              | ~45–60 min for first Cloud Run deploy troubleshooting |
| Day 4 | **Mon, Oct 26** | Multi-agent orchestration patterns | Codelabs: [Google's Agent Stack in Action: ADK, A2A, MCP](https://codelabs.developers.google.com/instavibe-adk-multi-agents/instructions) (InstaVibe workshop — core orchestration + A2A Inspector). **Stretch goal (optional):** Spanner graph-DB portion. | ~3–4 hrs core, +1–1.5 hrs stretch                                                                                     | Spanner/graph-DB section explicitly optional — skip without consequence if short on time |
| Day 5 | **Tue, Oct 27** | Governance-oriented multi-agent patterns | Codelabs: [Build a Multi-Agent Creative Studio](https://codelabs.developers.google.com/ai-creative-studio-adk-a2a) (critic/revision loop, context compaction, 6-agent A2A system) | ~3–4 hrs                                                                                                              | ~30–45 min for multi-service Cloud Run wiring |
| Day 6 | **Wed, Oct 28** | Agentic RAG (core to BeCCA data access) | Codelabs: [Building Agents with RAG](https://codelabs.developers.google.com/codelabs/production-ready-ai-with-gc/7-advanced-agent-capabilities/building-agents-with-retrieval-augmented-generation) (Vertex AI Search + custom tool) + [Database as a Tool: Agentic RAG with ADK, MCP Toolbox, and Cloud SQL](https://codelabs.developers.google.com/agentic-rag-toolbox-cloudsql) | ~4–5 hrs                                                                                                              | ~45 min for Cloud SQL provisioning wait time (setup script runs 10–15 min in background) |
| Day 7 | **Thu, Oct 29** | **Floating buffer** | Absorb any carryover from Days 1–6. If on schedule, review your Day 3–6 builds and note patterns to reuse for the BeCCA MCP server. | ~2–3 hrs if on track; full day if absorbing slippage                                                                  | Entire day is the buffer — nothing new is scheduled here |
| After plan | **Fri, Oct 30 →** | **Optional refresher** (not part of the 1-week window) | [ADK: From Zero to Hero](https://mauripsale.github.io/doc-adk-training/docs/) — community course; BeCCA-relevant modules listed in Section 7 | ~9 hrs focused set (full course ~29.5 hrs)  https://mauripsale.github.io/doc-adk-training/docs/timetable-self-service | Day 7 buffer takes priority; start only once Days 1–6 are done |

**Note on "by next Friday":** the plan ends Thu, Oct 29 (Day 7), which is itself a buffer day, so your Friday, Oct 30 deadline has a second day of slack behind it. The most likely slip points are Day 1–2 (path length and GCP setup), the Day 3 and 5 Cloud Run deploys, and Day 6 Cloud SQL provisioning.

**Deferred past this week regardless:** Agent Runtime deployment codelabs (Section 4, "Create multi-agent system... Agent Runtime" and "Agents at Scale"), LinkedIn Learning MCP courses, Educative courses (Section 6, optional). These add depth but aren't blocking for a first working MCP/ADK/A2A/RAG prototype — revisit the following week.

---

## 1. Framework & Protocol Reference

### Tier 0 — Interop/Protocol Layer (foundational)

| Item | Official Link | Docs / GitHub |
|---|---|---|
| Model Context Protocol (MCP) | [modelcontextprotocol.io](https://modelcontextprotocol.io/) | [Spec repo](https://github.com/modelcontextprotocol/modelcontextprotocol) · [GitHub org](https://github.com/modelcontextprotocol) |
| Agent2Agent Protocol (A2A) | [a2a-protocol.org](https://a2a-protocol.org/latest/) | [GitHub](https://github.com/a2aproject/A2A) |

### Tier 1 — Primary Agent Orchestration Framework

| Framework | Official Link | Docs / GitHub |
|---|---|---|
| Google ADK | [google.github.io/adk-docs](https://google.github.io/adk-docs/) (also [adk.dev](https://adk.dev/)) | [Docs](https://google.github.io/adk-docs/) · [GitHub](https://github.com/google/adk-python) |

_Scope narrowed to Google ADK, A2A, and the Google Cloud agent stack (Vertex AI, Agent Runtime, MCP Toolbox). Third-party frameworks (LangChain, LangGraph, LlamaIndex, Haystack, n8n, Semantic Kernel) removed from this guide._

---

## 2. RAG (Retrieval-Augmented Generation) — Reference & Resources

### RAG Architecture Options on Google Cloud (reference)

| Option | Best for | Docs |
|---|---|---|
| Vertex AI RAG Engine | Managed orchestration — DIY-to-production middle ground; handles ingestion, chunking, retrieval, re-ranking | [RAG Engine overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview) |
| Vertex AI Search (Agent Builder) | Out-of-the-box, Google-quality semantic + keyword search; enterprise connectors (GCS, Drive, Jira, Slack); fine-grained access controls | [Builder APIs](https://docs.cloud.google.com/generative-ai-app-builder/docs/builder-apis) |
| Fully DIY RAG (component APIs) | Full control — custom embedding, chunking, vector store, ranking | [Intro blog post](https://cloud.google.com/blog/products/ai-machine-learning/introducing-vertex-ai-rag-engine) |
| MCP Toolbox for Databases | Expose SQL + pgvector semantic search as MCP tools via YAML — no DB code in the agent | [GitHub](https://github.com/googleapis/mcp-toolbox) |

### Google Skills — RAG

| Course / Lab | Link | Est. Time | Notes |
|---|---|---|---|
| Multimodal Retrieval Augmented Generation (RAG) using the Gemini API in Agent Platform | [Google Skills](https://www.skills.google/focuses/85643?parent=catalog) | 5 min setup + 60 min access | Hands-on notebook: text + image metadata, text/image search, multimodal RAG |

### Google Codelabs — RAG / Agentic RAG

| Codelab | Link | Est. Time | Priority | What it builds |
|---|---|---|---|---|
| Building Agents with Retrieval-Augmented Generation | [Codelab](https://codelabs.developers.google.com/codelabs/production-ready-ai-with-gc/7-advanced-agent-capabilities/building-agents-with-retrieval-augmented-generation) | ~60 min | **Start here** | Financial analysis agent combining Vertex AI Search (unstructured SEC filings) + custom tool (structured stock data) via ADK multi-tool agent; core Agentic RAG concepts |
| Database as a Tool: Agentic RAG with ADK, MCP Toolbox, and Cloud SQL | [Codelab](https://codelabs.developers.google.com/agentic-rag-toolbox-cloudsql) | ~60–90 min | **High value** — directly relevant to BeCCA-style structured data access | Cloud SQL PostgreSQL + pgvector exposed as MCP tools via YAML (MCP Toolbox for Databases); ADK "Restaurant Concierge" agent; deployed to Cloud Run. Prerequisite for several downstream A2A/multi-agent codelabs. |
| AlloyDB Agentic RAG Application with MCP Toolbox | [Codelab](https://codelabs.developers.google.com/genai-db-retrieval-app) | ~60–90 min | Optional — alternative DB backend | Same MCP Toolbox pattern using AlloyDB instead of Cloud SQL; includes OAuth-gated booking flow |
| Building a Google-quality Search System with Vertex AI | [Codelab](https://codelabs.developers.google.com/build-google-quality-rag) | ~45–60 min | Optional — out-of-the-box RAG | Vertex AI Search/Agent Builder end-to-end: upload corpus → grounded, cited answers with minimal setup |

---

## 3. Google Skills (skills.google)

| Path / Course | Link | Est. Time | Priority | Notes |
|---|---|---|---|---|
| Agentic AI on Google Cloud (learning path) | [Google Skills](https://www.skills.google/paths/3273) | Multi-course path, several hrs | **Start here** | Umbrella path — principles, Gemini Enterprise intro, multi-agent architecture basics |
| Develop Agents with Agent Development Kit (ADK) (GEAR path) | [Google Skills](https://www.skills.google/paths/3545) | Multi-course path, several hrs | **Primary** | Production-ready, secure agents; MCP integrated into curriculum |
| Welcome: Develop Agents with ADK | [Google Skills](https://www.skills.google/paths/3545/course_templates/1778) | ~15–30 min | Intro module | Path orientation |
| Build Your First Agent with ADK | [Google Skills](https://www.skills.google/paths/3545/course_templates/1563) | ~1–2 hrs | Do for YAML config-driven path | Covers config-driven (not just code-first) agent definition |
| Get Started with Agent Development Kit (ADK) | [Google Skills](https://www.skills.google/focuses/125064?parent=catalog) | ~90 min lab | Refresher only | Architecture: agents/tools/sessions, custom tools, structured output |
| Engineer AI Agents with ADK | [Google Skills](https://www.skills.google/course_templates/1596) | Skill badge course, ~2–4 hrs | Do for badge + intermediate content | Multi-agent hierarchies, tool integration patterns |
| Build AI Agents with Enterprise Databases | [Google Skills](https://www.skills.google/paths/3273/course_templates/1436) | ~2–3 hrs | **Day 1** | MCP Toolbox for Databases — secure database tools, vector-embedding + structured queries; directly relevant to BeCCA data access |
| Build intelligent agents with ADK | [Google Skills](https://www.skills.google/course_templates/1382) | ~1–2 hrs | Supplementary | |

---

## 4. Google Codelabs (codelabs.developers.google.com)

| Codelab | Link | Est. Time | Priority | What it builds |
|---|---|---|---|---|
| Getting Started with MCP & A2A with ADK | [Codelab](https://codelabs.developers.google.com/getting-started-mcp-a2a-adk) | ~45–60 min | **Start here** | Currency MCP server → A2A-exposed currency agent → travel agent consuming it remotely; deployed to Cloud Run |
| Getting Started with MCP, ADK and A2A (earlier/simpler version) | [Codelab](https://codelabs.developers.google.com/codelabs/currency-agent) | ~30–45 min | Optional (largely superseded by above) | Remote MCP server + ADK agent + A2A exposure |
| Google's Agent Stack in Action: ADK, A2A, MCP on Google Cloud | [Codelab](https://codelabs.developers.google.com/instavibe-adk-multi-agents/instructions) | ~90–120 min | **High value** | Full workshop: orchestration patterns (sequential/parallel/conditional), sub-agents, Spanner as graph DB, A2A Inspector debugging |
| Build a Multi-Agent Creative Studio: ADK, A2A, MCP | [Codelab](https://codelabs.developers.google.com/ai-creative-studio-adk-a2a) | ~90–120 min | **High value for governance** | ADK Skills (SkillToolset), context compaction, critic/revision quality-control loop, 6+ agent roles over A2A |
| Create multi-agent system with ADK, deploy in Agent Runtime, A2A | [Codelab](https://codelabs.developers.google.com/codelabs/create-multi-agents-adk-a2a) | ~60–90 min | Do when ready for deployment target | Agent Runtime deployment, short/long-term memory (Sessions + Memory Bank) |
| Agents at Scale: Multi-Agent Architecture with A2A on Agent Runtime | [Codelab](https://codelabs.developers.google.com/adk-a2a-agent-runtime) | ~60–90 min (has prerequisite codelab) | Good testing-methodology reference | Reservation Agent + MCP Toolbox + Cloud SQL; incremental test strategy (local A2A → deployed A2A → partial → full) |
| Multi-Agent Systems with Agent2Agent | [Codelab](https://codelabs.developers.google.com/next26/adk-agent2agent) | ~15 min | Optional, quick | Multiple independently-developed agents unified via A2A host agent |
| Getting Started with A2A: Purchasing Concierge + Remote Seller Agents | [Codelab](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge) | ~60 min | Optional | ADK purchasing-concierge agent acting as an A2A client to remote seller agents — useful for understanding A2A's framework-agnostic discovery/task model |
| Build a Google Workspace AI Agent with ADK and MCP | [Codelab](https://codelabs.developers.google.com/google-workspace-mcp-adk) | ~60–90 min | Skip unless Workspace use case | OAuth/token handling for MCP servers, GEAP Agent Runtime registration |

---

## 5. LinkedIn Learning

### ADK

| Course | Link | Priority | Notes |
|---|---|---|---|
| Hands-On AI: Building Agents with Google's Agent Development Toolkit (ADK) | [LinkedIn Learning](https://www.linkedin.com/learning/hands-on-ai-building-agents-with-the-google-agent-development-toolkit-adk?u=95233017) | Good secondary source | Direct ADK-specific course — second explanation style alongside Google Skills/Codelabs if a concept isn't clicking |
| Building Agents with the Google Agent Developer Kit | [LinkedIn Learning](https://www.linkedin.com/learning/building-agents-with-the-google-agent-developer-kit?u=95233017) | Good secondary source | Instructor Fikayo Adepoju. Defining agents, custom and third-party tools, model configuration, input/output/context management, workflow agents (sequential, loop, parallel), and built-in plus MCP tools |
| Evaluating AI Agents with Google ADK | [LinkedIn Learning](https://www.linkedin.com/learning/evaluating-ai-agents-with-google-adk?u=95233017) | **High value for RUAI** | Instructor Jigyasa Grover. Eval-ready agent design (structured tools, Pydantic schemas), trace analysis with trajectory matching and golden traces, batch evals and Pass@k reliability tests, LLM-as-a-judge rubrics, groundedness checks, and CI/CD regression gates. Nothing else in this guide covers agent evaluation |

### A2A

| Course | Link | Priority | Notes |
|---|---|---|---|
| Hands-On AI: Building AI Agents with MCP and Agent2Agent (A2A) | [LinkedIn Learning](https://www.linkedin.com/learning/hands-on-ai-building-ai-agents-with-model-context-protocol-mcp-and-agent2agent-a2a) | Optional / second opinion | Builds a multi-agent HR assistant using A2A; Codelabs covers this ground more deeply with Google's actual production target (Cloud Run/Agent Runtime), but useful as a framework-agnostic conceptual grounding |

### RAG

| Course | Link | Priority | Notes |
|---|---|---|---|
| LLM Foundations: Vector Databases for Caching and Retrieval Augmented Generation (RAG) | [LinkedIn Learning](https://www.linkedin.com/learning/llm-foundations-vector-databases-for-caching-and-retrieval-augmented-generation-rag) | Optional | Generic (not Google-specific) — vector DB fundamentals underlying RAG; useful as conceptual grounding before/alongside the Vertex AI-specific Codelabs in Section 2 |

### MCP

| Course | Link | Priority | Notes |
|---|---|---|---|
| Introduction to Model Context Protocol by Anthropic | [LinkedIn Learning](https://www.linkedin.com/learning/introduction-to-model-context-protocol-by-anthropic?u=95233017) | Keep — reference | Anthropic-authored; most precise conceptual grounding on MCP primitives (tools/resources/prompts) |
| Model Context Protocol (MCP): Hands-On with Agentic AI | [LinkedIn Learning](https://www.linkedin.com/learning/model-context-protocol-mcp-hands-on-with-agentic-ai) | Optional | Build MCP servers in Python/TypeScript; extend Claude Desktop |
| Model Context Protocol (MCP) and agentic AI (micro-lesson) | [LinkedIn Learning](https://www.linkedin.com/learning/30-practical-ai-tips/model-context-protocol-mcp-and-agentic-ai) | Optional, short | Part of a broader "30 practical AI tips" course |
| Model Context Protocol (MCP) — Hands-On AI | [LinkedIn Learning](https://www.linkedin.com/learning/hands-on-ai-implementing-agentic-systems/model-context-protocol-mcp) | Optional | Part of broader "Implementing Agentic Systems" course |

---

## 6. Educative — **Optional**

Not required to finish this week's plan — Google Skills + Codelabs already cover ADK/MCP/A2A/RAG hands-on. These two fill narrow, specific gaps (multi-server MCP security/authorization, and a general architecture-pattern reference) and are only worth it after this week's plan is complete.

| Course | Link | Est. Time | Priority | Why it's additive (not redundant) |
|---|---|---|---|---|
| Mastering MCP: Building Advanced Agentic Applications | [Educative](https://www.educative.io/courses/advanced-model-context-protocol) | ~4–6 hrs | Optional | Multi-server MCP architecture, RAG-server implementation, **authorization/security and debugging** — not covered elsewhere in this guide |
| Agentic System Design | [Educative](https://www.educative.io/courses/agentic-ai-systems) | ~4–6 hrs | Optional | Architecture-pattern-level: orchestration patterns, safety/guardrails, human-oversight, resilience |

### Grokking courses — Not Needed for this sprint

| Course | Link | Why it's excluded now |
|---|---|---|
| Grokking the Generative AI System Design | [Educative](https://www.educative.io/courses/generative-ai-system-design) | Interview-prep / system-design-at-scale framing (latency, cost, throughput trade-offs for FAANG-style interviews) — not hands-on ADK/MCP/RAG build skills. Revisit only if prepping for a system-design interview or exec-facing architecture narrative. |
| Grokking AI for Engineering & Product Managers | (Educative catalog — search within platform) | No-code, leadership-oriented AI overview — not relevant to hands-on production implementation work. |

---

## 7. ADK: From Zero to Hero — Post-Plan Refresher (Optional)

Added as the final entry of the plan. It is **not** part of the Oct 23–29 window — it is a refresher to run after the core week. Because it follows the main plan, the concepts from Sections 3–4 should be enough to debug any lab that breaks (the author's own changelog lists several labs that were broken before v1.0.3).

_Links in this section were loaded on Oct 24, 2026 and are not covered by the "43 links validated" line at the top._

| Resource | Link | Est. Time | Priority | Notes |
|---|---|---|---|---|
| ADK: From Zero to Hero (course site) | [Docs](https://mauripsale.github.io/doc-adk-training/docs/) | ~29 hrs 35 min full self-service (author's estimate, includes a 25% troubleshooting factor) | Optional refresher | 40 modules in 7 parts, built on ADK 2.x graph-based workflows; Codespaces / Cloud Shell options; current version v1.0.3 |
| Course GitHub repo | [GitHub](https://github.com/mauripsale/doc-adk-training) | — | Reference | Sample agents in `sample-agents/`; text CC BY 4.0, code Apache 2.0 |
| Self-service timetable | [Timetable](https://mauripsale.github.io/doc-adk-training/docs/timetable-self-service) | — | Reference | Per-module durations |

### Suggested focus for BeCCA (~9 hrs)

| Modules | Topic | Est. Time | Why it matters |
|---|---|---|---|
| 16–21 | Static/structured/dynamic orchestration, collaborative teams, cyclic workflows, distributed graphs (A2A) | ~4 hrs | Refreshes the Day 4–5 orchestration patterns in ADK 2.x graph form |
| 24 | Evaluation | 50 min | Evaluation is otherwise only covered by the LinkedIn course in Section 5 |
| 26 | Callbacks and guardrails | 40 min | Safety/monitoring hooks for production agents |
| 27–28 | Intro to MCP; building MCP tools | 80 min | Directly relevant to the BeCCA MCP server |
| 34 | Deploying an MCP server to Cloud Run | 70 min | Closest course match for deploying the MCP server |
| 33 | Deployment to GKE | 60 min | BeCCA is deployed on GKE; the week's codelabs deploy to Cloud Run only |

**Optional add-ons:** Modules 29–30 (UI integration, custom streaming client, ~80 min) if the work touches the React UI path; Module 35 (Agent Runtime deployment, 60 min).

**Caveats:**
- **No RAG coverage in the outline** — nothing on Vertex AI Search, RAG Engine, or MCP Toolbox for Databases; use Section 2 for that.
- **Community project** — single author, not Google-official.
- **ADK version** — the course targets ADK 2.x; check which version each codelab pins before mixing code between them.

---

## Recommended Sequencing

1. **Google Skills** — Agentic AI on Google Cloud path → Develop Agents with ADK path
2. **Codelabs (Agent/MCP/A2A)** — Getting Started with MCP & A2A with ADK → Google's Agent Stack in Action → Build a Multi-Agent Creative Studio
3. **Codelabs (RAG)** — Building Agents with Retrieval-Augmented Generation → Database as a Tool: Agentic RAG with ADK, MCP Toolbox, and Cloud SQL (this one also feeds directly into the Agent Runtime / A2A-at-scale codelabs in Section 4 as a prerequisite)
4. **LinkedIn Learning** — *Evaluating AI Agents with Google ADK* first (fills the agent-evaluation gap, key for RUAI). Then Introduction to MCP by Anthropic (reference), the two ADK build courses as secondary explanation sources, and the A2A course for cross-framework grounding
5. **Educative (optional)** — Mastering MCP (security/multi-server) + Agentic System Design, only if time remains after the core week-one plan
6. **Grokking courses** — skip for this sprint; revisit only for interview prep or leadership-facing architecture communication
7. **ADK: From Zero to Hero (post-plan refresher, optional)** — after the core week, work through the BeCCA-relevant modules in Section 7 (orchestration 16–21, evaluation 24, callbacks 26, MCP 27–28 and 34, GKE 33)
