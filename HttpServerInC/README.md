# 🕸️ DarkSkills: HTTP Server (MVP)

> *“Learning systems by building them.”*

**DarkSkills HTTP Server** is a low-level, C-based implementation of a minimal HTTP server. It is designed as a learning playground to understand sockets, system calls, and the fundamentals of web communication — starting with a **simple static file server**.

---

## 💡 Name Origin

The name **DarkSkills** refers to:
- 🛠️ *"low-level"* systems skills — often unseen or “under the hood”
- 🎯 The sharp, foundational techniques in C, memory, and networking

---

## 📁 Project Structure (MVP)

```

http\_server/
├── main.c              # Entry point
├── server.c/h          # Socket setup, accept connections
├── request.c/h         # Basic HTTP request parsing
├── response.c/h        # HTTP response builder
├── utils.c/h           # Helpers (logging, string utils)
├── www/                # Static HTML folder
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

### ▶️ Run It

```bash
./http_server
```

Now visit [http://localhost:8080](http://localhost:8080) in your browser.

> 💡 The server will serve the `index.html` file found inside the `www/` folder.

---

## 🧠 Features (MVP Phase)

* Accepts basic `GET` requests
* Serves static HTML files (e.g., `index.html`)
* Minimal error handling
* Pure C (no external libraries)
* Project structure encourages modularity and learning

---

## 📌 Topics

* 🧠 Socket Programming
* 🧵 C Modular Design
* 🖧 HTTP Protocol Basics
* 🔁 Manual Request Parsing
* 🧹 Memory & File I/O
* 🧰 Makefiles

---

## 🙋‍♂️ Author

Built with 🧠 by [Mr-Ndi](https://github.com/Mr-Ndi)
🌐 [Personal Website](https://mr-ndi.github.io/me/)
🔗 [LinkedIn](https://www.linkedin.com/in/mr-ndi)

---

## 📄 License

This project is licensed under a **Custom License**. See the [`LICENCE`](LICENCE.md) file for terms.

---

## 🛠️ Contributions

This is a personal learning project. You’re welcome to fork or build your own version — just give credit.

---

## 🗓️ First Updated

August, 4th, 2025

```
