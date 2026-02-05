# SettleWise 💸

![SettleWise Logo](logo.png)

**SettleWise** is a smart, efficient, and user-friendly expense-sharing and debt-settlement platform. Designed to eliminate the awkwardness of money talk, SettleWise helps friends, families, and roommates track shared expenses, manage group budgets, and settle debts with ease.

---

## 🚀 Key Features

- **Intuitive Expense Tracking**: Quickly log expenses and split them among group members using various methods (equal, percentage, fixed amounts).
- **Group Management**: Create dedicated groups for trips, households, or events.
- **Settlement Optimization**: Smart algorithms to minimize the number of transactions needed to settle all debts within a group.
- **Real-time Notifications**: Stay updated with instant alerts for new expenses, reminders, and settlements.
- **Dashboard Analytics**: Visualize your spending habits and debt status with beautiful, interactive charts.
- **Multi-currency Support**: Seamlessly handle expenses in different currencies with real-time exchange rates.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Django 6.0
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **API**: Django REST Framework
- **Authentication**: JWT (JSON Web Tokens)
- **Frontend**: (Planned) React / Next.js

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- pip
- virtualenv

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aniketverma11/SettleWise.git
   cd SettleWise
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: Ensure requirements.txt is updated with all necessary packages)*

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

## 📁 project Structure

```text
SettleWise/
├── config/             # Project settings and core configuration
├── apps/               # Application modules (Expenses, Users, Groups)
├── media/              # User-uploaded files
├── static/             # Static assets (CSS, JS, Images)
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve SettleWise, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ by <a href="https://github.com/aniketverma11">Aniket Verma</a></p>
