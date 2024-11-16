
# Chocolate House Seasonal Flavors Application

This is a simple Python-Flask web application designed for managing seasonal flavors in a fictional chocolate house. The application allows users to add new flavors, view all seasonal flavors, and integrates a database for storing flavor details.

---

## Features

- **Add Seasonal Flavors:** Users can input the name, description, and availability status of a flavor.
- **View Seasonal Flavors:** Displays all flavors stored in the database.
- **Database Management:** Uses SQLite to store and retrieve flavor details, making the application lightweight and efficient.

---

## Prerequisites

- Python 3.x installed on your system
- Flask installed (can be installed using `pip install flask`)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/chocolate-house-app.git
   cd chocolate-house-app
   ```

2. Install required dependencies:
   ```bash
   pip install flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Folder Structure

```
chocolate-house-app/
│
├── app.py               # Main application file
├── templates/
│   ├── index.html       # Homepage
│   └── view_flavors.html# Page to display all flavors
└── chocolate_house.db   # SQLite database (auto-generated)
```

---

## Routes

1. `/` - Home page
2. `/add_flavor` - Handles the addition of new flavors (POST request)
3. `/view_flavors` - Displays the list of all seasonal flavors

---

## Technologies Used

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML (Flask templating engine)

---

