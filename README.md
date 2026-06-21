# 📚 PageTurn Books — FastAPI E-Commerce Application

A modern, full-stack **Book Store Web Application** built using **FastAPI**, featuring dynamic UI rendering, RESTful APIs, and deployed on the cloud using **Docker** and **Google Cloud Run**.

---

## 🚀 Live Demo

🔗 *https://bookstore-app-768123148807.asia-south1.run.app/*

---

## 🧠 Project Overview

PageTurn Books is a lightweight and scalable e-commerce platform designed to showcase a collection of books with category-based filtering and user interaction features.

The application combines:

* FastAPI backend ⚡
* Jinja2 templating 🎨
* SQLAlchemy ORM 🗄️
* Cloud deployment ☁️
* HTML, CSS and JS for frontend and styling

---

## ✨ Features

* 🛍️ Browse books dynamically
* 🔍 Filter books by category
* 📄 Multiple pages (Home, About, Contact)
* 📬 Contact form with backend handling
* ⚡ Fast and asynchronous API responses
* 🌐 Fully deployed on cloud

---

## 🛠️ Tech Stack

**Backend:**

* Python
* FastAPI
* SQLAlchemy

**Frontend:**

* HTML
* CSS
* Jinja2 Templates

**DevOps & Deployment:**

* Docker
* Google Cloud Run

---

## 📂 Project Structure

```
├── main.py              # FastAPI application
├── models.py            # Database models
├── database.py          # DB connection setup
├── seed_data.py         # Initial data population
├── templates/           # HTML templates
├── static/              # CSS, JS, assets
├── requirements.txt     # Dependencies
├── Dockerfile           # Container configuration
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/SriCharan-23/GFG-Project.git
cd GFG-Project
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run locally

```
python main.py
```

👉 Open: http://localhost:8080   To deploy project on cloud run it is important to run on port 8080

---

## 🐳 Docker Setup

```
docker build -t bookstore-app .
docker run -p 8080:8080 bookstore-app
```

---

## ☁️ Cloud Deployment

This application is deployed using:

* Docker containerization
* Google Cloud Run (serverless deployment)

---

## 📈 Key Learnings

* Building RESTful APIs using FastAPI
* Server-side rendering with Jinja2
* Database handling with SQLAlchemy
* Containerization using Docker
* Cloud deployment and IAM debugging on Google Cloud

---

## 👨‍💻 Author

**Sri Charan**

* 💼 AI/ML Enthusiast
* 🐍 Python Developer
* 🤖 Interested in building intelligent systems

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

This project was completed during the GeeksforGeeks × Google Developers' Agent Builder Camp, an online workshop held in May. I attended a particular session focused on Antigravity (vibe coding). The task was to create an application using Antigravity and deploy it on Cloud Run.
