# **Client Query Management System**

A **Streamlit + MySQL** based application that allows businesses to **collect, track, manage, resolve, and analyze client support queries** in real time.
The system includes:

* Client management
* Service category management
* Query logging and tracking
* Support team workflows (resolve/delete)
* Analytics and daily monitoring dashboards

---

## ⭐ **Key Features**

### ✅ **1. Client Management**

* Add new clients
* Store client name, email, phone
* View all clients

### ✅ **2. Service Management**

* Add services offered by the company
* Manage descriptions for each service
* Delete services

### ✅ **3. Query Management**

* Log new client queries
* Automatically timestamped `created_at`
* Status defaults to **Pending**
* Resolve a query (moves to Resolved)
* Delete a query
* View all queries with client + service mapping

### ✅ **4. Analytics Dashboard**

Built using **Plotly** (interactive charts):

* KPI Stats:

  * Total Queries
  * Pending
  * Resolved
  * Closed

* Query Status Distribution – Pie Chart

* Query Volume per Service – Bar Chart

* Daily Query Trend – Line Chart

---

## 🛠 **Tech Stack**

### **Frontend**

* Streamlit

### **Backend**

* Python
* MySQL (Relational DB)
* mysql-connector-python

### **Libraries Used**

* pandas
* plotly.express
* streamlit

---

## 📁 **Project Structure**

```
query_management_system/
│
├── app.py                    # Main Streamlit application
├── db.py                     # Database connection + SQL functions
├── load_dataset.py           # Loads provided CSV dataset into MySQL
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
│
├── schema.sql                # (Optional) MySQL table creation script
├── synthetic_client_queries.csv  # Provided dataset
│
├── venv/                     # Virtual environment
└── .gitignore                # Git ignored files
```

---

## ⚙️ **Installation Guide**

### **1. Clone or Create Folder**

```
mkdir query_management_system
cd query_management_system
```

### **2. Create Virtual Environment**

```
python -m venv venv
```

Activate it:

```
venv\Scripts\activate
```

### **3. Install Dependencies**

```
pip install -r requirements.txt
```

---

## 🗄 **MySQL Setup**

### **1. Create Database**

In MySQL Workbench:

```sql
CREATE DATABASE client_query_system;
USE client_query_system;
```

### **2. Create Tables**

```sql
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50)
);

CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(255),
    description TEXT
);

CREATE TABLE queries (
    query_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    service_id INT,
    query_text TEXT,
    status VARCHAR(50) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);
```

---

## 📥 **Loading Provided Dataset**

This project includes a clean dataset:

```
synthetic_client_queries.csv
```

Load it using:

```
python load_dataset.py
```

This script will:

* Insert unique clients
* Insert unique services
* Insert 5200 query records

---

## ▶️ **Run the Application**

Activate virtual environment:

```
venv\Scripts\activate
```

Start Streamlit:

```
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

---

## 📊 **How to Use the Application**

### **1. Add Clients**

* Enter name, email, phone → saved to MySQL

### **2. Add Services**

* Create and categorize service types

### **3. Add Query**

* Select a client
* Select a service
* Enter problem description

### **4. View Queries**

* See complete list with timestamps & statuses

### **5. Resolve / Delete Queries**

* Resolve → status changes to "Resolved"
* Delete → permanently removes the query

### **6. Analytics Dashboard**

* KPI counts
* Status distribution
* Query volume per service
* Daily query trends

---

## 🧪 **Testing Performed**

Manually tested:

* Adding clients
* Adding services
* Creating multiple queries
* Resolving and deleting queries
* Monitoring dashboard updates
* Dataset loading with 5200 records

---

## 📦 **Final Deliverables**

* `app.py`
* `db.py`
* `load_dataset.py`
* `schema.sql`
* `requirements.txt`
* `README.md`
* Project report (PDF)
* Project PPT (slides)

---

## 👩🏻‍💻 **Author**

**Nihaaraa Dilras**

---