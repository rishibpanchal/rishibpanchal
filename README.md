<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c1b,50:6b21a8,100:0d0b21&height=220&section=header&text=Rishi%20Panchal&fontSize=65&fontColor=ffffff" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=24&color=a78bfa&center=true&vCenter=true&width=600&height=50&lines=Software+Engineer;Backend+Architect;AI+%2F%20ML+Practitioner;Systems+Engineer" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Education-B.Tech%20Information%20Technology-6b21a8?style=flat-square&logo=academia&logoColor=white" />
  <img src="https://img.shields.io/badge/GPA-8.78%2F10.0-4c1d95?style=flat-square" />
  <img src="https://img.shields.io/badge/Location-Mumbai%2C%20India-blueviolet?style=flat-square&logo=googlemaps&logoColor=white" />
</p>

<p align="center">
  <a href="https://linkedin.com/in/rishi-panchal"><img src="https://img.shields.io/badge/LinkedIn-Rishi%20Panchal-0077B5?style=flat-square&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:rishibpanchal006@gmail.com"><img src="https://img.shields.io/badge/Email-rishibpanchal006%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white" /></a>
  <a href="https://github.com/rishibpanchal"><img src="https://img.shields.io/badge/GitHub-rishibpanchal-181717?style=flat-square&logo=github&logoColor=white" /></a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=rishibpanchal&color=8A2BE2&style=flat-square&label=Profile+Views" />
</p>

---

## 📌 About Me

I am a final-year Information Technology student at SVKM's Dwarkadas J Sanghvi College of Engineering. I am a curious engineer who enjoys building software products from scratch and solving real-world problems. 

My technical interests lie at the intersection of backend architecture, distributed systems, and artificial intelligence. I enjoy exploring how highly concurrent systems are designed, and I like combining AI with software engineering to build practical applications. Rather than just learning technologies in theory, I prefer to master them by designing, coding, and optimizing real projects.

### 🎯 Current Focus & Philosophy

- **Currently Building**: Secure transaction engines, backtesting architectures, and low-latency API wrappers.
- **Currently Learning**: High-throughput distributed transaction strategies, Java Virtual Threads optimization, and custom vector search indexing.
- **What Excites Me**: Reading about database internals, optimizing garbage collection for high-performance applications, and building tools that make unstructured data useful.
- **Engineering Interests**: Systems engineering, concurrency models, financial technology, and MLOps.
- **My Philosophy**: Code should be readable, tests should be exhaustive, and architectures should be built for reliability under load.

> *"Simplicity is the ultimate sophistication. Great software is built at the intersection of robust engineering and human-centric design."*

---

## 🛠️ Tech Stack

### 💻 Languages
<p align="left">
  <img src="https://skillicons.dev/icons?i=java,py,cpp,c,js,postgres&perline=6" />
</p>

### ⚙️ Backend Engineering & Frameworks
<p align="left">
  <img src="https://skillicons.dev/icons?i=spring,fastapi,flask&perline=3" />
</p>

### 🎨 Frontend & GUI
<p align="left">
  <img src="https://skillicons.dev/icons?i=react,nextjs&perline=2" />
</p>

### 🤖 Machine Learning & AI
<p align="left">
  <img src="https://skillicons.dev/icons?i=pytorch,tensorflow&perline=2" />
</p>

### 🗄️ Databases & Caching
<p align="left">
  <img src="https://skillicons.dev/icons?i=postgres,redis,sqlite&perline=3" />
</p>

### 🔧 Developer Tools
<p align="left">
  <img src="https://skillicons.dev/icons?i=git,docker,maven&perline=3" />
</p>

**Core Frameworks & Tools:** `Spring Security` `PyQt6` `KùzuDB` `NetworkX` `Ollama (Phi-3-mini, Gemma)` `scikit-learn` `XGBoost` `SHAP` `REST APIs` `JWT Authentication` `Concurrent Programming` `Multithreading` `OOP`

---

## 🚀 Featured Projects

<details>
<summary><b>1. TransactX — Secure Digital Banking System</b></summary>
<br />

### Description
A secure digital banking system supporting deposits, withdrawals, fund transfers, account management, and transaction logging.

### Metrics & Architecture
| Dimension | Specification |
| :--- | :--- |
| **Stack** | Java, Spring Boot, PostgreSQL, Redis, React |
| **Scale** | Handles account operations through 10+ REST endpoints |
| **Performance** | Validated state consistency under 50+ concurrent requests |
| **Security** | ACID-compliant transaction engine with double-entry bookkeeping, idempotency, and ordered lock acquisition |
| **Impact** | Built a sandbox comparing locking performance using Java Virtual Threads |
| **Repository** | [TransactX](https://github.com/rishibpanchal/TransactX) |

### Architecture Diagram
```mermaid
graph TD
    Client[React Frontend] -->|REST APIs| API[Spring Boot App]
    API -->|JWT Auth / Security| Auth[Spring Security]
    API -->|Virtual Threads| Exec[Concurrency Sandbox]
    Exec -->|Ordered Lock Acquisition| Ledger[ACID Transaction Engine]
    Ledger -->|Write-Ahead / Double-Entry| DB[(PostgreSQL)]
    Ledger -->|Idempotency / Cache| Cache[(Redis)]
```

### Engineering Details
- Engineered an ACID-compliant transaction engine using double-entry bookkeeping and ordered lock acquisition to guarantee transaction consistency under high concurrency.
- Designed a concurrency testing sandbox leveraging Java Virtual Threads to compare locking strategies.
</details>

<details>
<summary><b>2. ApexLedger — High-Throughput Financial Settlement Engine</b></summary>
<br />

### Description
An enterprise-grade financial settlement engine engineered to process transaction flows with minimal overhead.

### Metrics & Architecture
| Dimension | Specification |
| :--- | :--- |
| **Stack** | Java 21, Spring Boot, PostgreSQL |
| **Scale** | Asynchronously processes 10,000+ synthetic financial transactions per second |
| **Performance** | Sub-millisecond latency profile using Virtual Threads for async execution |
| **Security** | 100% elimination of cyclic deadlocks using pessimistic database locking; SHA-256 tamper-evident ledger chaining |
| **Impact** | Implemented a custom Dead-Letter Queue (DLQ) with up to 3 exponential backoff retries |
| **Repository** | [ApexLedger](https://github.com/rishibpanchal/ApexLedger) |

### Architecture Diagram
```mermaid
graph TD
    Trades[Synthetic Trade Stream] -->|Async Ingest| Queue[Virtual Threads Worker Pool]
    Queue -->|Pessimistic Locking| Ledger[Double-Entry Bookkeeping Engine]
    Ledger -->|SHA-256 Chaining| Hash[Tamper-Evident Ledger Builder]
    Hash -->|Commit| DB[(PostgreSQL)]
    Queue -->|Failed Trades| DLQ[Dead-Letter Queue]
    DLQ -->|Exponential Backoff - 3 Retries| Retry[Retry Executor]
```

### Engineering Details
- Leveraged Java 21 Virtual Threads to asynchronously process 10,000+ synthetic financial transactions per second.
- Prevented race conditions and resolved deadlock hazards under heavy loads by implementing pessimistic locking on the database layer.
- Secured transaction history integrity with tamper-evident cryptographic chaining (SHA-256).
</details>

<details>
<summary><b>3. QuantScope — Quantitative Research & Backtesting Platform</b></summary>
<br />

### Description
A quantitative research terminal for real-time market analysis, signal discovery, and historical portfolio backtesting.

### Metrics & Architecture
| Dimension | Specification |
| :--- | :--- |
| **Stack** | React, FastAPI, Python (Pandas, NumPy) |
| **Scale** | Real-time market analysis and signal discovery across 500+ securities |
| **Performance** | Backtests historical market data representing 10+ years of activity |
| **Security** | Mathematical validation of metrics: Sharpe Ratio, VaR, drawdown, and correlation |
| **Impact** | Developed low-latency streaming infrastructure with WebSockets and intelligent caching |
| **Repository** | [QuantScope](https://github.com/rishibpanchal/QuantScope) |

### Architecture Diagram
```mermaid
graph TD
    Client[React Frontend] -->|WebSocket Stream| Stream[Low-Latency Server]
    Client -->|REST APIs| API[FastAPI Backend]
    API -->|Backtesting Engine| Risk[Sharpe / VaR / Drawdown Calculator]
    Risk -->|10+ Years Historical Data| DB[(Historical Market DB)]
    API -->|Portfolio Optimization| Engine[NumPy / Pandas Portfolio Analytics]
```

### Engineering Details
- Engineered a low-latency market visualizer integrating WebSocket streaming and caching pipelines.
- Implemented a risk engine that calculates Sharpe Ratio, Value at Risk (VaR), drawdown, and correlation metrics across massive market histories.
</details>

<details>
<summary><b>4. NextGen — Machine Learning Insurance Risk Engine</b></summary>
<br />

### Description
A production-grade machine learning risk analytics pipeline designed to detect fraudulent insurance claims.

### Metrics & Architecture
| Dimension | Specification |
| :--- | :--- |
| **Stack** | FastAPI, Python (scikit-learn, XGBoost, Random Forest, Isolation Forest, SHAP) |
| **Scale** | Analyzes risk factors across 5,000+ claims |
| **Performance** | Accelerates model inference speed by 60% using asynchronous memory loading |
| **Security** | Isolated feature mappings (ColumnTransformer, TargetGuidedEncoder) to prevent data leakage |
| **Impact** | Boosts claim analyst productivity by 40% with explainable AI insights (SHAP) |
| **Repository** | [NextGen](https://github.com/rishibpanchal/NextGen) |

### Architecture Diagram
```mermaid
graph TD
    Client[Claim Request] -->|FastAPI Endpoint| API[Risk Analytics API]
    API -->|Async Memory Load| Loader[Model Loader]
    Loader -->|Preprocess: ColumnTransformer| Transform[Feature Pipeline]
    Transform -->|Inference: XGBoost / Random Forest / Isolation Forest| Models[Multi-Model Inference]
    Models -->|Explainability| SHAP[SHAP Explainers]
    SHAP -->|Output: Score + Explanation| Client
```

### Engineering Details
- Deployed a multi-model risk engine evaluating Random Forest, Isolation Forest, and XGBoost models.
- Resolved preprocessing data leakages during training/calibration using secure pipeline mappings.
- Integrated SHAP explainability arrays to output human-readable rationales for flagged anomalies.
</details>

<details>
<summary><b>5. RecycleIT — Intelligent Traceability for Circular Economy</b></summary>
<br />

### Description
A conversational NLP data ingestion pipeline and supply chain graph traceability system.

### Metrics & Architecture
| Dimension | Specification |
| :--- | :--- |
| **Stack** | Flask, React, KùzuDB, NetworkX, Ollama (Phi-3-mini) |
| **Scale** | Maps complex graph topologies of supply chains to identify loss hotspots |
| **Performance** | Accelerates raw data ingestion by 45% |
| **Security** | Conversational NLP parser extracting structured JSON from natural text |
| **Impact** | Reduces supply chain audit time by 40%; improves decision-making metrics by 35% |
| **Repository** | [RecycleIT](https://github.com/rishibpanchal/RecycleIT) |

### Architecture Diagram
```mermaid
graph TD
    Records[Unstructured Log / Text] -->|Ingest| Ollama[Ollama: Phi-3-mini]
    Ollama -->|NLP Parsing| Parser[JSON Extractor]
    Parser -->|Structured JSON| Flask[Flask API Backend]
    Flask -->|Graph Construction| Graph[NetworkX Graph Engine]
    Graph -->|Persist Nodes & Edges| DB[(KùzuDB Graph Database)]
    Flask -->|Sustainability Metrics & Alerts| Dashboard[React Dashboard]
```

### Engineering Details
- Designed an intelligent data parsing pipeline leveraging local LLMs (Phi-3-mini via Ollama) to convert unstructured operational records into clean JSON structure.
- Developed supply chain graph trace systems with NetworkX and KùzuDB to mapping dependencies.
</details>

---

## 💼 Professional Experience

### Software Developer Intern — **DataNorth Technologies Pvt. Ltd.**
**June 2025 — August 2025**

- **Problem Solved**: Manual data extraction and validation from complex business documents was highly inefficient and prone to analytical errors.
- **Tech Stack**: `Python` `pdfplumber` `Ollama (Gemma)` `PyQt6`
- **Engineering Contribution**:
  - Developed an automated Document AI pipeline using local LLMs (Gemma via Ollama) and `pdfplumber` to extract and structure unstructured data from complex business PDFs.
  - Built an asynchronous desktop interface using `PyQt6` to process large batches of documents concurrently.
  - Implemented robust verification schemas and exception handling layers to sanitize outputs.
- **Impact**:
  - Reduced manual processing effort for complex business documents by **90%+**.
  - Improved downstream data ingestion accuracy by **85%**.

---

## 👥 Leadership Experience

### Placement Coordinator — **SVKM's Dwarkadas J Sanghvi College of Engineering**
**August 2025 — Present**
- Managing data workflows, scheduling databases, and candidate tracking for a cohort of **1000+ students**.
- Coordinating corporate relationships, facilitating communications with recruiting teams, and streamlining the campus placement workflow.

### Creatives Head — **Computer Society of India (DJCSI)**
**August 2025 — June 2026**
- Led the creatives team in structuring digital branding, marketing strategies, and design campaigns for technical events and college hackathons.
- Headed promotional outreach to build branding elements for developer-centric workshops and hackathons.

---

## 🏆 Achievements

| Recognition | Awarding Organization / Event | Details |
| :--- | :--- | :--- |
| **2nd Prize Winner** | Nirmaan Project Showcase (DJ InIT.AI) | Awarded for outstanding project engineering and live prototype implementation. |
| **AI/ML Domain Winner** | Lines Of Code 8.0 Hackathon (DJSCE ACM) | Secured the domain championship for designing and deploying an optimized machine learning pipeline under a strict 24-hour deadline. |

---

## 📊 GitHub Analytics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=rishibpanchal&show_icons=true&bg_color=0f0c1b&title_color=a78bfa&text_color=e2e8f0&icon_color=8b5cf6&border_color=2e2050" alt="GitHub Stats" />
  &nbsp;&nbsp;
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=rishibpanchal&layout=compact&bg_color=0f0c1b&title_color=a78bfa&text_color=e2e8f0&icon_color=8b5cf6&border_color=2e2050" alt="Top Languages" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=rishibpanchal&theme=dark&background=0f0c1b&fire=8b5cf6&ring=a78bfa&score=e2e8f0&border=2e2050&stroke=2e2050" alt="GitHub Streak" />
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=rishibpanchal&theme=radical&no-background=false&margin-w=10&margin-h=10" alt="GitHub Trophies" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=rishibpanchal&theme=react-dark&bg_color=0f0c1b&color=a78bfa&line=8b5cf6&point=ffffff&area=true&hide_border=true" width="100%" alt="Activity Graph" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/rishibpanchal/rishibpanchal/output/github-contribution-grid-snake-dark.svg" alt="GitHub Contribution Snake" />
</p>

---

## 🤝 Connect With Me

<p align="center">
  <a href="mailto:rishibpanchal006@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  &nbsp;&nbsp;
  <a href="https://linkedin.com/in/rishi-panchal">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/rishibpanchal">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0b21,50:6b21a8,100:0f0c1b&height=120&section=footer" />
</p>
