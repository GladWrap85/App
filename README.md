# 📊 Knowby Dashboard

An interactive web-based dashboard built with Flask and CSS Grid to visualize employee engagement with Knowby training content. Designed for internal use by First Step Solutions.

---

## 🚀 Features

* View Knowby training engagement stats:

  * Total views
  * Completion time
  * Top and bottom performing Knowbys
  * Department engagement
  * Usage heatmap
* Visual theme switching (Sky Blue, Slime Green, Sun Yellow, Midnight Purple)
* Auto-detects stale Knowby data and prompts for reconnection
* PDF export via print-friendly layout
* Fully responsive CSS Grid layout
* Status indicator with time since last sync
* Secure login overlay on outdated or missing syncs

---

## 💠 Requirements

* Python 3.8+
* Flask
* Web browser (Chrome recommended)
* Knowby credentials for data access

---

## 📦 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/knowby-dashboard.git
   cd knowby-dashboard
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚧 Project Structure

```
knowby-dashboard/
│
├── app.py                  # Flask backend
├── knowby/                 # Folder containing login.py and scraper.py
│   ├── login.py
│   ├── scraper.py
│   └── config.json         # Stores theme & sync timestamp
│
├── static/
│   ├── style.css           # Main stylesheet
│   ├── main.js             # All JavaScript logic
│   ├── firststepsolutions_logo.png
│   ├── ffs_logo_full.png
│   └── [charts].jpg        # Chart images
│
├── templates/
│   └── index.html          # Main dashboard HTML
│
└── README.md
```

---

## 🧪 Running the App

```bash
python app.py
```

Then navigate to:

```
http://localhost:5000
```

---

## 🎨 Theme Customization

The app supports 4 themes:

* Sky Blue (default)
* Slime Green
* Sun Yellow
* Midnight Purple

To change the default theme, edit `knowby/config.json`:

```json
{
  "theme": "sky-blue",
  "last_sync": "2025-04-28T12:30:00"
}
```

---

## 🗘 Exporting the Dashboard

Click the **Export** button to open the browser's print dialog with a clean, print-optimized layout (landscape).

---

## 🔒 Security Notes

* A full-screen overlay hides dashboard content until Knowby is reconnected when data is stale (yellow/red/gray status).
* Logout and shutdown options are provided to cleanly exit and avoid unintended data syncs.

---

## 📄 License

MIT License. See `LICENSE` for details.

---

## 🤝 Acknowledgements

* Built by Oliver, Neil, Lucas, Ganna, Sahil, and Julie
