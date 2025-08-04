# 🕸️ DarkSkills: HTTP Server (MVP)

> *“Learning systems by building them.”*

**DarkSkills HTTP Server** is a minimal, low-level HTTP server written in pure C.  
It's part of a personal initiative — **DarkSkills** — which focuses on exploring and reclaiming underused, often overlooked technical skills through hands-on projects.  
This project serves as both a learning tool and a working artifact — starting with a simple static file server.

---

## 💡 Name Origin

**DarkSkills** symbolizes:
- 🛠️ Low-level skills that operate “under the hood”
- 🧭 A commitment to mastering the foundational layer of computing, even when it's not trendy or in demand
- 🧱 Building for the sake of skill, clarity, and future independence

---

## 📁 Project Structure

```

http\_server/
├── main.c              # Entry point
├── server.c/h          # Socket setup, connection handling
├── request.c/h         # Basic HTTP request parsing
├── response.c/h        # HTTP response builder
├── utils.c/h           # Logging and string utilities
├── www/                # Static HTML content
│   └── index.html
├── Makefile            # Build automation
└── README.md           # Project documentation

````

---

## 🚀 Usage

### 🔧 Compile the Server

```bash
make
````

### ▶️ Run the Server

```bash
./http_server
```

Then open your browser and go to: [http://localhost:8080](http://localhost:8080)

> 💡 By default, it serves the `index.html` file inside the `www/` directory.

---

## 🧠 Features (MVP Phase)

* Handles basic `GET` requests
* Serves static HTML content
* Simple manual parsing of HTTP requests
* Pure C implementation — no frameworks or libraries
* Designed for clarity and modularity
* Ideal as a starter system-level project

---

## 📌 Topics Explored

* 🧠 Socket Programming
* 🧵 Modular C Design
* 🖧 HTTP Basics
* 🔁 Request Parsing
* 🧹 File I/O
* 🧰 Makefiles and Build Automation

---

## 🙋‍♂️ Author

Crafted with intention by [Mr-Ndi](https://github.com/Mr-Ndi)
🌐 [mr-ndi.github.io/me](https://mr-ndi.github.io/me)
🔗 [LinkedIn](https://www.linkedin.com/in/mr-ndi)

---

## 📄 License

This project is licensed under a **Custom Proprietary License**.
See the [`LICENCE.md`](LICENCE.md) file for full terms.

---

## 🛠️ Contributions

This is a self-driven learning project.
Forks and explorations are welcome — just provide proper attribution.

---

## 🗓️ First Updated

**August 4th, 2025**

```