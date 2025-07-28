# 🕷️ Ajanyu

> *“Sifting joyfully through opportunities.”*

**Ajanyu** is a Python-based web scraper that collects job listings from [Opportunity Rwanda](https://opportunity.ini.rw/), optionally filters them by type (e.g., internship or contract), and uploads the curated results to an Airtable database.

---

## 💡 Name Origin

The name **Ajanyu** is a fusion of:

- **Sanyu** — meaning *“joy”* in Luganda
- **Ajira** — meaning *“job” or “employment”* in Swahili

Together, **Ajanyu** conveys the idea of **joyful work** — a beautiful sentiment for a job-finding tool built with intention and purpose.

---

## 📁 Project Structure

```

Ajanyu/
├── airtable/
│   ├── **init**.py
│   └── uploader.py         # Airtable upload logic
├── scraper/
│   ├── **init**.py
│   └── jobs.py             # BeautifulSoup scraper logic
├── main.py                 # Project entry point
├── Dockerfile              # Docker setup
├── .env.example            # Template for environment variables
├── Readme.md               # Project documentation
└── requirements.txt        # Python dependencies

````

---

## 🚀 Usage

### 🔧 Option 1: Run Locally (Recommended for Development)

#### 1. 📦 Install Dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

#### 2. 🔐 Set Environment Variables

Copy the example config and update with your own values:

```bash
cp .env.example .env
```

#### 3. ▶️ Run the Scraper

```bash
python3 main.py
```

---

### 🐳 Option 2: Run with Docker

Ensure Docker is installed on your system, then build and run:

```bash
# Build the image
docker build -t ajanyu .

# Run the container
docker run --env-file .env ajanyu
```

> 💡 **Tip**: `.env` should contain your Airtable keys and scraper config (based on `.env.example`).

---

## 🧠 Features

* Scrapes job listings from a real-world job portal
* Filters by job type (internship, contract, etc.)
* Uploads structured results to Airtable
* Environment-based config (`.env`) for portability
* Docker-ready for production or deployment
* Modular and extensible structure

---

## 📌 Topics

* 🧹 Web Scraping
* 🔌 Airtable API Integration
* 🔁 Automation
* 🐍 Python 3
* 🍲 Selanium
* 🐳 Docker

---

## 🙋‍♂️ Author

Built with ❤️ by [Mr-Ndi](https://github.com/Mr-Ndi)
🌐 [Personal Website](https://mr-ndi.github.io/me/)
🔗 [LinkedIn](https://www.linkedin.com/in/mr-ndi)

---

## 📄 License

This project is licensed under a **Custom License**. See the [`LICENSE`](LICENSE) file for full terms.

---

## 🛠️ Contributions

Contributions are welcome! Feel free to fork, improve, and send a pull request:

```bash
git checkout -b feature/your-feature
git commit -m "Add something awesome"
git push origin feature/your-feature
```

Then open a Pull Request. Let's build this together!

---

## 🗓️ Last Updated

June 2025