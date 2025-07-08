### 📘 EY OneNote — Your Daily Learning Tracker

**EY OneNote** is a minimal, intuitive Django web app built to help users track their daily learnings, notes, or reflections. It includes activity streaks, email reminders, and a smooth UI with Tailwind CSS.

---

### 🚀 Features

* 📝 **Daily Note Entry** – Add/edit a note for each day
* 📅 **My Notes History** – View and manage previous notes
* 🔐 **User Authentication** – Login, register, and secure note access
* 📊 **Activity Streaks** – Visual feedback for consistent usage
* 📧 **Email Reminder** – Get a daily reminder if no note is added before 10PM IST
* 👤 **Profile Panel** – Slide-in panel showing username, email, join date, and note count
* 🧩 **Edit Profile Info** – Update real name and email easily

---

### 🛠️ Tech Stack

* **Backend**: Django 5
* **Frontend**: Tailwind CSS
* **Database**: SQLite (dev), PostgreSQL (production-ready)
* **Email**: EmailJS (frontend-based email notifications)

---

### 🔧 Setup Instructions (Local)

1. **Clone the Repo**

   ```bash
   git clone https://github.com/hemanthnagasai/Note.git
   cd Note
   ```

2. **Create Virtual Env**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # on Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser (Optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**

   ```bash
   python manage.py runserver
   ```

---

### 🌐 Deployment Guide

> Free hosting options: **Render** (recommended)

#### Render Setup:

* Create a new **Web Service**
* Connect your GitHub repo
* Set `Build Command`: `pip install -r requirements.txt`
* Set `Start Command`: `gunicorn eynote.wsgi`
* Add environment variable:

  * `PYTHON_VERSION = 3.12`
  * `DJANGO_SETTINGS_MODULE = eynote.settings`
* Add your database (PostgreSQL or keep SQLite if supported)

---

### 📬 Reminder Script (Optional, for servers or CRON jobs)

Run the daily reminder manually:

```bash
python manage.py send_reminders
```

> Or automate using `CRON` / Render jobs.

---

### 🤝 Contribution

Open to contributions, feedback, or feature requests!
Feel free to fork and submit a pull request.

---

### 📄 License

This project is under the **MIT License** — free to use and modify.
