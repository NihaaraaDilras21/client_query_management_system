import mysql.connector
from mysql.connector import Error

# NOTE: For security, you can replace these values with environment variables.
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "nikkuy2k",
    "database": "client_query_system"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# -----------------------------
# CLIENTS
# -----------------------------
def add_client(name, email=None, phone=None):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO clients (client_name, email, phone) VALUES (%s, %s, %s)",
                (name, email, phone)
            )
        conn.commit()
    finally:
        conn.close()

def get_clients():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT client_id, client_name, email, phone FROM clients")
            data = cur.fetchall()
        return data
    finally:
        conn.close()

# -----------------------------
# SERVICES
# -----------------------------
def add_service(service_name, description=None):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO services (service_name, description) VALUES (%s, %s)",
                (service_name, description)
            )
        conn.commit()
    finally:
        conn.close()

def get_services():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT service_id, service_name, description FROM services")
            data = cur.fetchall()
        return data
    finally:
        conn.close()

def delete_service(service_id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM services WHERE service_id = %s", (service_id,))
        conn.commit()
    finally:
        conn.close()

# -----------------------------
# QUERIES
# -----------------------------
def add_query(client_id, service_id, query_text, status="Pending", created_at=None, closed_at=None):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            if created_at and closed_at:
                cur.execute(
                    "INSERT INTO queries (client_id, service_id, query_text, status, created_at, closed_at) "
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    (client_id, service_id, query_text, status, created_at, closed_at)
                )
            elif created_at:
                cur.execute(
                    "INSERT INTO queries (client_id, service_id, query_text, status, created_at) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (client_id, service_id, query_text, status, created_at)
                )
            else:
                cur.execute(
                    "INSERT INTO queries (client_id, service_id, query_text, status) "
                    "VALUES (%s, %s, %s, %s)",
                    (client_id, service_id, query_text, status)
                )
        conn.commit()
    finally:
        conn.close()

def get_queries():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT 
                    q.query_id,
                    q.client_id,
                    c.client_name,
                    q.service_id,
                    s.service_name,
                    q.query_text,
                    q.status,
                    q.created_at,
                    q.closed_at
                FROM queries q
                LEFT JOIN clients c ON q.client_id = c.client_id
                LEFT JOIN services s ON q.service_id = s.service_id
                ORDER BY q.query_id DESC
            """)
            data = cur.fetchall()
        return data
    finally:
        conn.close()

# -----------------------------
# ANALYTICS FUNCTIONS
# -----------------------------
def get_query_counts():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT COUNT(*) AS total_queries FROM queries")
            total = cur.fetchone()["total_queries"] or 0

            cur.execute("SELECT COUNT(*) AS pending FROM queries WHERE status='Pending'")
            pending = cur.fetchone()["pending"] or 0

            cur.execute("SELECT COUNT(*) AS resolved FROM queries WHERE status='Resolved'")
            resolved = cur.fetchone()["resolved"] or 0

            cur.execute("SELECT COUNT(*) AS closed FROM queries WHERE status='Closed'")
            closed = cur.fetchone()["closed"] or 0

        return {"total": total, "pending": pending, "resolved": resolved, "closed": closed}
    finally:
        conn.close()

def get_queries_per_service():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT s.service_name, COUNT(*) AS total
                FROM queries q
                JOIN services s ON q.service_id = s.service_id
                GROUP BY s.service_name
                ORDER BY total DESC
            """)
            return cur.fetchall()
    finally:
        conn.close()

def get_daily_query_trend():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("""
                SELECT DATE(created_at) AS date, COUNT(*) AS total
                FROM queries
                GROUP BY DATE(created_at)
                ORDER BY DATE(created_at)
            """)
            return cur.fetchall()
    finally:
        conn.close()

def resolve_query(query_id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE queries SET status = 'Resolved' WHERE query_id = %s", (query_id,))
        conn.commit()
    finally:
        conn.close()

def delete_query(query_id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM queries WHERE query_id = %s", (query_id,))
        conn.commit()
    finally:
        conn.close()
