# RISHI PANCHAL

**Systems, concurrency, and deterministic software.**

Based in Mumbai. I design backend architectures and analytical engines that remain correct when things start competing for state — concurrent transactions, financial ledgers, and systems where deterministic guarantees matter more than hopeful abstractions.

---

### 01 / IDENTITY

Most software feels easy when there is only one user, one thread, and happy-path data. It gets interesting when fifty concurrent workers attempt to mutate the exact same balance at the same millisecond, or when an AI workflow needs to touch enterprise data without hallucinating away state.

My focus sits at the intersection of **systems engineering, transactional data stores, and applied ML**. I build around a core conviction: *probabilistic models can suggest and summarize, but deterministic architectures must always validate, order, and commit.*

---

### 02 / SELECTED WORK

#### [ApexLedger](https://github.com/rishibpanchal/ApexLedger)
`Java 21` &nbsp;&middot;&nbsp; `Spring Boot 3` &nbsp;&middot;&nbsp; `Virtual Threads (Loom)` &nbsp;&middot;&nbsp; `PostgreSQL` &nbsp;&middot;&nbsp; `Docker`

An asynchronous financial settlement engine built to test concurrency control under high transaction volume.
- Eliminates cyclic deadlocks during multi-account transfers by enforcing deterministic, alphabetical lock acquisition order (breaking Coffman’s circular wait condition).
- Leverages Java 21 Virtual Threads to decouple request concurrency from OS carrier threads, maintaining low-latency execution under concurrent load.
- Implements linear SHA-256 cryptographic ledger chaining for tamper evidence and an isolated Dead-Letter Queue (DLQ) with exponential backoff across separate transaction boundaries.

#### [WealthOps](https://github.com/rishibpanchal/WealthOps)
`Python 3.13` &nbsp;&middot;&nbsp; `FastAPI` &nbsp;&middot;&nbsp; `LangGraph` &nbsp;&middot;&nbsp; `TypeScript` &nbsp;&middot;&nbsp; `React 19`

An operations automation platform that converts natural language wealth management requests into auditable, governed workflows.
- Replaces unconstrained LLM execution with a multi-step LangGraph state machine paired with semantic policy retrieval.
- Enforces strict non-LLM deterministic guardrails (hard caps on trade value and percentage drift thresholds).
- Routes sensitive or anomalous portfolio adjustments into a Chief Risk Officer dual-authorization approval queue before any action executes.

#### [TransactX](https://github.com/rishibpanchal/TransactX)
`Java` &nbsp;&middot;&nbsp; `Spring Boot` &nbsp;&middot;&nbsp; `PostgreSQL` &nbsp;&middot;&nbsp; `Redis` &nbsp;&middot;&nbsp; `React`

A core banking engine and interactive simulation harness created to explore transaction isolation and lock contention.
- Features a concurrency test harness comparing the throughput and conflict characteristics of Optimistic (`@Version`) versus Pessimistic (`PESSIMISTIC_WRITE`) locking strategies.
- Enforces double-entry bookkeeping ledgers where balances are never modified without matching debit/credit entries.
- Employs Redis-backed idempotency tokens to guarantee zero duplicate postings during network retries, with audit logs persisting in independent transactional boundaries (`REQUIRES_NEW`).

#### [QuantScope](https://github.com/rishibpanchal/QuantScope)
`FastAPI` &nbsp;&middot;&nbsp; `React 18` &nbsp;&middot;&nbsp; `TypeScript` &nbsp;&middot;&nbsp; `NumPy / Pandas` &nbsp;&middot;&nbsp; `TradingView Charts`

A quantitative research terminal for market data streaming, signal discovery, and historical portfolio backtesting.
- Vectorized risk engine computing Sharpe Ratio, Value at Risk (VaR), maximum drawdown, and asset correlation matrices across historical market series.
- Detects technical divergences, momentum crossovers, and volume breakouts in real time.
- Pairs low-latency streaming endpoints with TradingView lightweight charts and AG Grid tables for sub-second visual analysis.

#### [RecycleIT](https://github.com/rishibpanchal/RecycleIT)
`Python` &nbsp;&middot;&nbsp; `FastAPI` &nbsp;&middot;&nbsp; `Next.js` &nbsp;&middot;&nbsp; `KùzuDB` &nbsp;&middot;&nbsp; `NetworkX` &nbsp;&middot;&nbsp; `Prophet`

An intelligent circular supply-chain platform transforming fragmented recycling records into a queryable material traceability graph.
- Combines KùzuDB graph storage with NetworkX topological path analysis to identify material loss hotspots and processing bottlenecks.
- Strictly decouples language parsing from analytics: LLMs extract structured ingestion payloads from unstructured logs, while deterministic algorithms calculate yield and transit deltas.
- Persists all provenance movements to a SHA-256 tamper-evident audit ledger.

---

### 03 / ARCHITECTURAL NOTES

A few opinions formed while building and breaking things:

- **Deadlocks are design flaws, not bad luck.** When multiple transactions require multiple resources, ordering resource acquisition globally prevents circular wait before it can ever form.
- **LLMs are untrusted callers.** In workflows touching money, compliance, or physical assets, language models can propose operations, but only deterministic code with hard boundaries should have write access to the database.
- **Virtual threads don't make the database faster.** They eliminate OS thread context-switching overhead on I/O, but your connection pool, lock contention, and index structures remain the actual bottlenecks.
- **Audit logs require isolation.** A failed transaction must roll back its state mutations, but the audit entry recording the failure must persist. Independent transaction boundaries (`REQUIRES_NEW`) are non-negotiable.

---

### 04 / TOOLBOX

```text
Languages          Java (21+), Python, TypeScript, SQL, C/C++
Backend & APIs     Spring Boot, Spring Data JPA, FastAPI, REST, Node.js
Storage & State    PostgreSQL, Redis, KùzuDB (Graph), SQLite
Concurrency & ML   Virtual Threads (Project Loom), LangGraph, NumPy/Pandas, scikit-learn
Infrastructure     Docker, Git, Maven, Linux environments
```

---

### 05 / ELSEWHERE

- **GitHub**: [github.com/rishibpanchal](https://github.com/rishibpanchal)
- **LinkedIn**: [linkedin.com/in/rishi-panchal](https://linkedin.com/in/rishi-panchal)
- **Email**: [rishibpanchal006@gmail.com](mailto:rishibpanchal006@gmail.com)
