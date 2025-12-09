import pandas as pd
from datetime import datetime
from db import get_connection

CSV_PATH = "synthetic_client_queries.csv"  # adjust path if needed

def find_or_create_client(email, mobile):
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT client_id FROM clients WHERE email = %s OR phone = %s", (email, mobile))
            row = cur.fetchone()
            if row:
                return row["client_id"]
            # create new client: name derive from email local part if available
            name = None
            if email and "@" in email:
                name = email.split("@")[0]
            if not name:
                name = email or mobile or "Unknown"
            cur.execute("INSERT INTO clients (client_name, email, phone) VALUES (%s, %s, %s)", (name, email, mobile))
            conn.commit()
            return cur.lastrowid
    finally:
        conn.close()

def find_or_create_service(service_name):
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT service_id FROM services WHERE service_name = %s", (service_name,))
            row = cur.fetchone()
            if row:
                return row["service_id"]
            cur.execute("INSERT INTO services (service_name) VALUES (%s)", (service_name,))
            conn.commit()
            return cur.lastrowid
    finally:
        conn.close()

def insert_query(client_id, service_id, text, status, created_at, closed_at):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            if pd.notna(closed_at):
                cur.execute(
                    "INSERT INTO queries (client_id, service_id, query_text, status, created_at, closed_at) "
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    (client_id, service_id, text, status, created_at, closed_at)
                )
            else:
                cur.execute(
                    "INSERT INTO queries (client_id, service_id, query_text, status, created_at) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (client_id, service_id, text, status, created_at)
                )
        conn.commit()
    finally:
        conn.close()

def parse_date(s):
    if pd.isna(s):
        return None
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(str(s).strip(), fmt)
        except Exception:
            continue
    # fallback - try pandas
    try:
        t = pd.to_datetime(s)
        return t.to_pydatetime()
    except Exception:
        return None

def main():
    df = pd.read_csv(CSV_PATH)
    # adjust column names in case headers differ
    # expected columns (example from mentor file): query_id, client_email, client_mobile, query_heading, query_description, status, date_raised, date_closed
    for idx, row in df.iterrows():
        email = row.get("client_email") or row.get("mail_id") or None
        mobile = row.get("client_mobile") or row.get("mobile_number") or None
        heading = row.get("query_heading") or row.get("query_heading") or "General Support"
        description = row.get("query_description") or row.get("query_text") or ""
        status = row.get("status") or "Closed"
        date_raised = parse_date(row.get("date_raised") or row.get("created_at"))
        date_closed = parse_date(row.get("date_closed") or row.get("closed_at"))

        client_id = find_or_create_client(email, mobile)
        service_id = find_or_create_service(heading.strip())

        insert_query(client_id, service_id, description, status, date_raised, date_closed)
        print(f"Inserted row {idx+1} -> client {client_id}, service {service_id}")

if __name__ == "__main__":
    main()
