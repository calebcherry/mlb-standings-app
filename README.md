


# ⚾ MLB Standings Viewer [🚨 STILL IN DEVELOPMENT | INCOMPLETE 🚨]

A Python-powered web app that reimagines how you view MLB standings — see not just where your team ranks in their division, but where they'd stack up in every other division too.

> _"The 4th place team in the NL West would be leading any other division in baseball right now."_  
This app makes that kind of hot take visual and interactive.

---

## 🚀 Features

- 📊 Displays current MLB standings in a clean table
- 🔁 Shows *cross-division rankings* — how each team would rank if placed in another division
- 🐍 Built with Python, pandas, and [Streamlit](https://streamlit.io/)
- 🌐 Planned for Docker + AWS deployment
- 🔧 Designed to grow — future features may include team filters, graphs, projections, and historical views

---

## 🧱 Tech Stack

- `Python 3.10+`
- [`pandas`](https://pandas.pydata.org/) for data wrangling
- [`httpx`](https://www.python-httpx.org/) for async API calls
- [`Streamlit`](https://streamlit.io/) for web interface
- [`uv`](https://github.com/astral-sh/uv) for modern Python dependency management
- Jupyter for testing python logic.
- Docker & AWS (planned)

---

## 🏗️ Running Locally

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/mlb-standings-app.git
   cd mlb-standings-app
   ```

2. Set up your environment  
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -r pyproject.toml
   ```

3. Launch the app  
   ```bash
   streamlit run app/main.py
   ```

---

## 🚧 Roadmap

- [ ] Add historical standings
- [ ] Add Index (json) of all League, Division, and Team metadata, sources (img links), etc.
- [ ] Add non-traditional team season stats (like series wins, division h2h, etc)
- [ ] Add charts for better visual comparison
- [ ] Team filtering & views
- [ ] Deploy using Docker & AWS

---

## 🤝 Contributions Welcome!

Got an idea? Want to help add features or fix bugs? PRs and issues are always welcome.  
Baseball fans, stat nerds, and code lovers unite! 🧢📈

---

## 📜 License

MIT License