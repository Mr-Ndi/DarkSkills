# 🧠 DarkSkills

DarkSkills is a curated collection of technical mini-projects, coding skills, and tools that go beyond the surface — from low-level memory management in C to high-level automation and backend workflows in Go and Python.

> Think of this as your technical playground for sharpening deep dev skills across different tech perspecives and disciplines.

---

## 🗂️ Project Structure

```

DarkSkills/
├── HttpServerInC      # Systems-level C code (planned)
├── KigaliKit          # (Active) Python tools: scraping, CLI experiments for Rwandan devs
├── MicroLab           # (Planned) Microservices & CLI tooling experiments in Go/Python
├── TeraTune           # (Planned) Spotify API project for audio analytics
├── README.md

````

---

## 🔧 Core Projects & Ideas

### ⚙️ 1. Kubernetes Playground *(coming soon in `MicroLab`)*
A DevOps-focused project to build and deploy microservices using:
- **Go / Node.js** for services
- **Docker + Minikube** for local clusters
- **GitHub Actions** for CI/CD
- *(Optional)* Helm for Kubernetes packaging

> **Goal**: Escape frontend fatigue. Build infra awareness.

---

### 💬 2. KigaliKit — CLI Tools for Rwandan Devs *(currently active, under `Web-Scrapper`)*
A lightweight CLI utility (Python or Go) that provides:
- 🧑‍💻 Local tech job listings
- 📅 Developer events in Rwanda
- 📚 Quick access to dev tips/resources

Planned usage:

```bash
$ rwdev list-jobs
$ rwdev events
$ rwdev tips --topic golang
````

> **Goal**: Empower local devs with useful, no-UI tooling.

---

### 🎧 3. TeraTune — Spotify Listening Stats API *(coming soon)*

A personal data project using the Spotify Web API:

* OAuth-based login
* Store listening data in PostgreSQL
* Expose a custom API
* *(Optional)* Visual dashboard with Streamlit

> **Goal**: Playfully explore personal data with real backend + DB skills.

---

## 🔍 Other Experiments

### 🕸️ Web Scraping *(in progress within `KigaliKit`)*

* Using `BeautifulSoup` to parse HTML (e.g., courses, job posts)
* Handling broken tags, missing data, and messy structure
* Foundations for KigaliKit’s CLI data layer

### 🧠 Systems in C *(planned under `HttpServerInC`)*

* Memory management and raw networking
* A basic HTTP server built in C
* Reinforce understanding of systems-level programming

---

## 🛠️ Stack Highlights

| Language | Use Case                          |
| -------- | --------------------------------- |
| Python   | Web scraping, automation, CLIs    |
| Go       | Systems tools, CLI, microservices |
| C        | Low-level memory/server code      |
| Node.js  | APIs, event-driven services       |

---

## 📌 Vision

This repo is a **skill incubator** — not just another app graveyard.
Every folder is a ladder out of shallow dev work and toward technical depth.

🕶️ Build quietly. Learn deeply. Escape frontend fatigue.

---

## 🧱 Getting Started

Clone and explore project directories:

```bash
git clone https://github.com/your-username/DarkSkills.git
cd DarkSkills/Web-Scrapper  # Soon to be renamed to KigaliKit
python3 main.py
```

> More instructions will be added as new projects are launched.

---

## 📍 Author

**me\@192** — Tinkerer of tools, not just apps
🇷🇼 Based in Rwanda | Focused on backend, infra, and purposeful dev work

---

## 🕳️ Down the Rabbit Hole?

Want to build your own version of these projects?

Reach out or open an issue to get guidance on:

* Deploying microservices with Kubernetes
* Building developer CLIs in Python or Go
* Using the Spotify API + PostgreSQL for personal data projects

---

- Rename the folder `Web-Scrapper` to `KigaliKit`:
