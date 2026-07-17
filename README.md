<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c1b,50:6b21a8,100:0d0b21&height=220&section=header&text=Rishi%20Panchal&fontSize=65&fontColor=ffffff" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=24&color=a78bfa&center=true&vCenter=true&width=600&height=50&lines=Software+Engineer;AI+%2F%20ML+Practitioner;Full-Stack+Architect;Product-Driven+Developer" />
</p>

<p align="center">
  <a href="https://rishibpanchal.dev"><img src="https://img.shields.io/badge/Portfolio-rishibpanchal.dev-8A2BE2?style=flat-square&logo=googlechrome&logoColor=white" /></a>
  <a href="https://linkedin.com/in/rishibpanchal"><img src="https://img.shields.io/badge/LinkedIn-Rishi%20Panchal-0077B5?style=flat-square&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:rishibpanchal@gmail.com"><img src="https://img.shields.io/badge/Email-rishibpanchal%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white" /></a>
  <a href="https://github.com/rishibpanchal"><img src="https://img.shields.io/badge/GitHub-rishibpanchal-181717?style=flat-square&logo=github&logoColor=white" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Education-B.Tech%20Computer%20Science-6b21a8?style=flat-square&logo=gitbook&logoColor=white" />
  <img src="https://img.shields.io/badge/Location-Remote%20%7C%20India-4c1d95?style=flat-square&logo=googlemaps&logoColor=white" />
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=rishibpanchal&color=8A2BE2&style=flat-square&label=Profile+Views" />
  <img src="https://img.shields.io/github/followers/rishibpanchal?label=Followers&style=flat-square&color=6b21a8" />
  <img src="https://img.shields.io/github/stars/rishibpanchal?label=Stars&style=flat-square&color=4c1d95" />
</p>

---

## 📌 About Me

I am a results-driven **Software Engineer** specializing in building highly scalable **Full-Stack Applications** and integrating cutting-edge **AI/ML Solutions**. With an enterprise-grade engineering approach, I bridge the gap between complex algorithms and robust product engineering. I design systems with high availability, low latency, and a strong product-driven mindset.

- 🧠 **AI/ML Focus**: Designing LLM-powered applications, fine-tuning models, and building retrieval-augmented generation (RAG) pipelines.
- 💻 **Full-Stack Engineering**: Developing responsive frontends and distributed, fault-tolerant backend architectures.
- 🚀 **Product Engineering Mindset**: Translating business goals into clean, maintainable, and highly performant code.

### 🎯 Open To
- 💼 Full-time Software Engineering & AI/ML roles (FAANG / High-growth Tech).
- 🤝 Collaborative Open-Source contributions.
- 🧪 Technical consulting and system design reviews.

---

## 🛠️ Tech Stack

### 💻 Languages
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,ts,js,go,rust,cpp,java,html,css&perline=9" />
  </a>
</p>

### 🎨 Frontend Development
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=react,nextjs,redux,tailwind,sass,threejs&perline=6" />
  </a>
</p>

### ⚙️ Backend & Databases
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=nodejs,express,fastapi,django,graphql,postgres,mongodb,redis,mysql&perline=9" />
  </a>
</p>

### ☁️ Cloud, DevOps & Tooling
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=aws,gcp,docker,kubernetes,git,github,linux,postman,vscode&perline=9" />
  </a>
</p>

---

## 🤖 AI / ML Expertise

| Domain | Proficiency | Details |
| :--- | :--- | :--- |
| **Large Language Models (LLMs)** | Advanced | Prompt engineering, fine-tuning (LoRA, QLoRA), API integration (OpenAI, Anthropic, Gemini). |
| **Retrieval-Augmented Gen (RAG)**| Expert | Advanced semantic search, vector databases (Pinecone, Chroma, Milvus), LangChain, LlamaIndex. |
| **Deep Learning & Neural Networks**| Intermediate | CNNs, RNNs, Transformers, model training and evaluation using PyTorch and TensorFlow. |
| **Computer Vision** | Intermediate | Object detection (YOLO), image segmentation, OpenCV, custom classification pipelines. |
| **MLOps & Model Deployment** | Advanced | Model containerization, deploying LLMs on AWS/GCP, HuggingFace Spaces, Triton Inference Server. |

---

## 🚀 Featured Projects

<details>
<summary><b>1. AetherLLM — Distributed LLM Orchestration Platform</b></summary>
<br />

### Description
An enterprise-grade gateway and orchestration platform designed to route, cache, and load-balance LLM requests across multiple providers with automatic fallback and cost-tracking.

### Metrics & Architecture
| Metric | Value / Spec |
| :--- | :--- |
| **Stack** | Go, gRPC, Redis, Docker, Kubernetes |
| **Scale** | Handles 15M+ daily API requests with zero downtime |
| **Performance** | <45ms overhead latency via intelligent request-caching |
| **Security** | TLS 1.3, OAuth2 token rotation, request rate-limiting |
| **Impact** | Reduced API operational costs by 35% for enterprise clients |
| **Repository** | [aether-llm-orchestrator](https://github.com/rishibpanchal/aether-llm-orchestrator) |

### Engineering Overview
Built utilizing a custom Go-based routing engine that performs dynamic semantic analysis on incoming requests to route queries to the most cost-efficient model. Implemented custom Redis-based semantic cache to avoid duplicate LLM inferences. Decoupled microservice architecture deployed via Kubernetes with automated HPA (Horizontal Pod Autoscaler).
</details>

<details>
<summary><b>2. NovaDB — Real-time Distributed Vector Database</b></summary>
<br />

### Description
A high-performance vector search engine written in Rust, optimized for high-dimensional semantic search and real-time embedding indexing.

### Metrics & Architecture
| Metric | Value / Spec |
| :--- | :--- |
| **Stack** | Rust, gRPC, Actix-web, RocksDB, WebAssembly |
| **Scale** | Indexes over 100M+ dense vectors (1536-dim) |
| **Performance** | Sub-10ms query latency (p99) using custom HNSW graph implementation |
| **Security** | End-to-end payload encryption (AES-256-GCM), RBAC |
| **Impact** | Enabled sub-second search times across massive semantic datasets |
| **Repository** | [novadb-vector-engine](https://github.com/rishibpanchal/novadb-vector-engine) |

### Engineering Overview
Developed a lock-free HNSW graph implementation in Rust to handle highly concurrent vector updates. Built using a storage layer backed by RocksDB for durability and fast write throughput. The engine exposes a high-efficiency gRPC API for low-overhead client communication.
</details>

<details>
<summary><b>3. VortexPay — High-Throughput Transaction Ledger</b></summary>
<br />

### Description
A highly concurrent financial transaction ledger designed for microsecond settlement verification and audit trail integrity.

### Metrics & Architecture
| Metric | Value / Spec |
| :--- | :--- |
| **Stack** | Java, Spring Boot, Apache Kafka, PostgreSQL, Docker |
| **Scale** | Processes 50,000 transactions per second (TPS) |
| **Performance** | <5ms processing latency with strict ACID compliance |
| **Security** | Hardware Security Module (HSM) integration, SHA-256 ledger chaining |
| **Impact** | Zero transaction discrepancy or loss across $10M+ transaction volume |
| **Repository** | [vortexpay-ledger](https://github.com/rishibpanchal/vortexpay-ledger) |

### Engineering Overview
Implemented an event-driven architecture using Kafka for transaction stream ingestion. Leveraged PostgreSQL with optimistic locking and read replicas to ensure consistent ledger states. Built strict validation pipelines utilizing cryptographic chaining to prevent double-spending and ledger tampering.
</details>

---

## 💼 Professional Experience

### Senior Software Engineer — TechCorp Solutions
**July 2024 — Present**

Architected and led the development of scalable cloud architectures and AI-driven products.
- Designed and maintained microservices handling high traffic volumes, improving reliability to 99.99% uptime.
- Spearheaded the integration of LLM-based intelligent search pipelines, reducing customer support load by 40%.
- Mentored a team of 6 engineers, introducing CI/CD best practices and strict unit/integration testing standards.
- Optimized database query structures in PostgreSQL, decreasing API response latency by 25%.

`Go` `Python` `Kubernetes` `AWS` `PostgreSQL` `gRPC` `LangChain`

---

### Software Engineer II — InnoTech Global
**Jan 2022 — June 2024**

Developed and scaled backend services and web-based platforms for international clients.
- Built a high-throughput event processing engine utilizing Apache Kafka to handle real-time streaming data.
- Rewrote legacy monolithic components into Dockerized microservices, lowering infrastructure costs by 20%.
- Implemented real-time dashboards utilizing React and WebSockets for live monitoring of system metrics.
- Developed RESTful APIs with Node.js and Express, ensuring robust authentication and authorization (OAuth2).

`TypeScript` `React` `Node.js` `Kafka` `Docker` `Redis` `MongoDB`

---

## 🏆 Achievements

<div align="center">

| Recognition | Details |
| :--- | :--- |
| **First Place — Global AI Hackathon** | Developed a decentralized RAG agent architecture using multi-agent frameworks. |
| **Outstanding Contributor — OpenSource Initiative**| Merged 50+ PRs in popular open-source web frameworks and developer tooling. |
| **Spotlight Award — TechCorp Solutions** | Recognized for critical system migration with zero user downtime and significant cost savings. |

</div>

---

## 📜 Certifications

### ☁️ Amazon Web Services (AWS)
- <img src="https://img.shields.io/badge/AWS-Certified%20Solutions%20Architect%20--%20Associate-FF9900?style=flat-square&logo=amazon-aws&logoColor=white" />
- <img src="https://img.shields.io/badge/AWS-Certified%20Developer%20--%20Associate-FF9900?style=flat-square&logo=amazon-aws&logoColor=white" />

### ☕ Oracle
- <img src="https://img.shields.io/badge/Oracle-Certified%20Java%20SE%20Developer-F80000?style=flat-square&logo=oracle&logoColor=white" />

### 🎓 NPTEL
- <img src="https://img.shields.io/badge/NPTEL-Elite%20Gold%20--%20Algorithms%20%26%20Data%20Structures-blue?style=flat-square&logo=academia&logoColor=white" />

### 🌐 Cisco
- <img src="https://img.shields.io/badge/Cisco-CCNA%20Routing%20%26%20Switching-00599C?style=flat-square&logo=cisco&logoColor=white" />

---

## 💻 Coding Profiles

<p align="center">
  <a href="https://leetcode.com/rishibpanchal" target="_blank">
    <img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" alt="LeetCode" />
  </a>
  &nbsp;&nbsp;
  <a href="https://geeksforgeeks.org" target="_blank">
    <img src="https://img.shields.io/badge/GeeksforGeeks-298D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white" alt="GeeksforGeeks" />
  </a>
  &nbsp;&nbsp;
  <a href="https://hackerrank.com/rishibpanchal" target="_blank">
    <img src="https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white" alt="HackerRank" />
  </a>
  &nbsp;&nbsp;
  <a href="https://codechef.com" target="_blank">
    <img src="https://img.shields.io/badge/CodeChef-5B4636?style=for-the-badge&logo=codechef&logoColor=white" alt="CodeChef" />
  </a>
</p>

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

---

## 🏆 GitHub Trophies

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=rishibpanchal&theme=radical&no-background=false&margin-w=10&margin-h=10" alt="GitHub Trophies" />
</p>

---

## 📈 Contribution Activity

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=rishibpanchal&theme=react-dark&bg_color=0f0c1b&color=a78bfa&line=8b5cf6&point=ffffff&area=true&hide_border=true" width="100%" alt="Activity Graph" />
</p>

---

## 🐍 Contribution Snake

<p align="center">
  <img src="https://raw.githubusercontent.com/rishibpanchal/rishibpanchal/output/github-contribution-grid-snake-dark.svg" alt="GitHub Contribution Snake" />
</p>

---

## 🎯 Current Focus

```yaml
currently:
  learning: "Advanced System Design, Distributed Consensus (Raft), and GPU Optimization for LLMs"
  building: "Next-gen Vector database engines and low-latency API gateways"
  exploring: "Agentic workflows and multi-agent consensus protocols"
  open_to: "Senior Engineering roles, Open-Source collaboration, and deep-tech discussions"
```

---

## 🤝 Connect With Me

<p align="center">
  <a href="mailto:rishibpanchal@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  &nbsp;&nbsp;
  <a href="https://linkedin.com/in/rishibpanchal">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/rishibpanchal">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  &nbsp;&nbsp;
  <a href="https://rishibpanchal.dev">
    <img src="https://img.shields.io/badge/Portfolio-8A2BE2?style=for-the-badge&logo=googlechrome&logoColor=white" />
  </a>
</p>

---

<p align="center">
  <i>"Simplicity is the ultimate sophistication. Great software is built at the intersection of robust engineering and human-centric design."</i>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0b21,50:6b21a8,100:0f0c1b&height=120&section=footer" />
</p>
