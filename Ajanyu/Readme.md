# 🕷️ Ajanyu

> *“Sifting joyfully through opportunities.”*

**Ajanyu** is a Python-based web scraper that collects job listings from [Opportunity Rwanda](https://opportunity.ini.rw/), optionally filters them by type (e.g., internship or contract), and uploads the curated results to an Airtable database.

---

## 💡 Name Origin

The name **Ajanyu** is a fusion of:

- **Sanyu** – meaning *“joy”* in Luganda
- **Ajira** – meaning *“job” or “employment”* in Swahili

Together, *Ajanyu* represents the idea of **joyful work** or **happy employment** — a beautiful sentiment for a job-finding tool built with purpose.

---

## 📁 Project Structure

```

Ajanyu/
├── airtable/
│   └── uploader.py        # Airtable upload logic
├── scraper/
│   └── jobs.py            # BeautifulSoup scraper logic
├── main.py                # Project entry point
├── .env                   # Secret keys & config
├── Readme.md              # Project documentation
└── requirements.txt       # Python dependencies

````

---

## 🚀 Usage

### 1. 📦 Install Dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

### 2. 🔐 Set Environment Variables

Copy the example file and update it with your own credentials:

```bash
cp .env.example .env
```

### 3. ▶️ Run the Scraper

```bash
python3 main.py
```

---

## 🧠 Features

* Scrapes job listings from a real-world job portal
* Filters by job type (internship, contract, etc.)
* Uploads structured results to Airtable
* `.env` configuration for easy setup and secrets management
* Modular structure for maintainability and extension

---

## 📌 Topics

* 🧹 Web Scraping
* 🔌 Airtable API Integration
* 🔁 Automation
* 🐍 Python 3
* 🍲 BeautifulSoup4

---

## 🙋‍♂️ Author

Built with ❤️ by [Mr-Ndi](https://github.com/Mr-Ndi)
🌐 [Personal Website](https://mr-ndi.github.io/me/)
🔗 [LinkedIn](https://www.linkedin.com/in/mr-ndi)

---

## 📄 License

This project is licensed under a **Custom License**. See the [`LICENSE`](LICENSE) file for details.

---

## 🛠️ Contributions

Contributions are welcome! Feel free to fork, improve, and send a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a pull request

---

## 🗓️ Last Updated

June 2025
