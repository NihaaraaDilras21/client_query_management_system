import streamlit as st
import pandas as pd
import plotly.express as px

from db import (
    add_client, get_clients,
    add_query, get_queries,
    add_service, get_services, delete_service,
    resolve_query, delete_query,
    get_query_counts, get_queries_per_service, get_daily_query_trend
)

st.set_page_config(page_title="Client Query Management System", layout="wide")
st.title("Client Query Management System")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Add Client",
    "Add Query",
    "View Queries",
    "Manage Services",
    "Resolve Query",
    "Delete Query",
    "Analytics & Reports"
])

# --------------------------------------------------------------------------
# PAGE 1 — ADD CLIENT
# --------------------------------------------------------------------------
if page == "Add Client":
    st.header("Add Client")

    name = st.text_input("Client Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    if st.button("Save Client"):
        if name:
            add_client(name.strip(), email.strip() or None, phone.strip() or None)
            st.success("Client added successfully!")
        else:
            st.error("Client name cannot be empty!")

    st.subheader("Current Clients")
    clients = get_clients()
    st.dataframe(clients)

# --------------------------------------------------------------------------
# PAGE 2 — ADD QUERY
# --------------------------------------------------------------------------
elif page == "Add Query":
    st.header("Add Query")

    clients = get_clients()
    services = get_services()

    client_map = {c["client_name"]: c["client_id"] for c in clients}
    service_map = {s["service_name"]: s["service_id"] for s in services}

    client_choice = st.selectbox("Select Client", list(client_map.keys()) or ["No clients"])
    service_choice = st.selectbox("Select Service", list(service_map.keys()) or ["No services"])

    query_text = st.text_area("Query Description")

    if st.button("Submit Query"):
        if client_map and service_map and client_choice in client_map and service_choice in service_map:
            add_query(client_map[client_choice], service_map[service_choice], query_text)
            st.success("Query submitted successfully!")
        else:
            st.error("You must add clients and services first!")

# --------------------------------------------------------------------------
# PAGE 3 — VIEW QUERIES
# --------------------------------------------------------------------------
elif page == "View Queries":
    st.header("📄 View All Client Queries")

    data = get_queries()

    if not data:
        st.info("No queries found.")
    else:
        df = pd.DataFrame(data)
        st.dataframe(df)

# --------------------------------------------------------------------------
# PAGE 4 — MANAGE SERVICES
# --------------------------------------------------------------------------
elif page == "Manage Services":
    st.header("⚙️ Manage Services")

    service_name = st.text_input("Service Name")
    service_desc = st.text_area("Service Description")

    if st.button("Add Service"):
        if service_name:
            add_service(service_name.strip(), service_desc.strip() or None)
            st.success("Service added successfully!")
        else:
            st.error("Service name cannot be empty!")

    st.subheader("Existing Services")
    data = get_services()
    st.table(data)

    st.subheader("Delete a Service")
    if data:
        ids = [s["service_id"] for s in data]
        remove_id = st.selectbox("Select Service ID to delete", ids)

        if st.button("Delete Service"):
            delete_service(remove_id)
            st.warning("Service deleted!")
    else:
        st.info("No services available.")

# --------------------------------------------------------------------------
# PAGE 5 — RESOLVE QUERY
# --------------------------------------------------------------------------
elif page == "Resolve Query":
    st.header("✔️ Resolve a Query")

    data = get_queries()

    if not data:
        st.info("No queries found.")
    else:
        st.table(data)
        ids = [q["query_id"] for q in data]
        qid = st.selectbox("Select Query ID to mark as Resolved", ids)

        if st.button("Resolve Query"):
            resolve_query(qid)
            st.success(f"Query {qid} marked as Resolved!")

# --------------------------------------------------------------------------
# PAGE 6 — DELETE QUERY
# --------------------------------------------------------------------------
elif page == "Delete Query":
    st.header("🗑️ Delete a Query")

    data = get_queries()

    if not data:
        st.info("No queries found.")
    else:
        st.table(data)
        ids = [q["query_id"] for q in data]
        qid = st.selectbox("Select Query ID to Delete", ids)

        if st.button("Delete Query"):
            delete_query(qid)
            st.warning(f"Query {qid} deleted!")

# --------------------------------------------------------------------------
# PAGE 7 — ANALYTICS & REPORTS
# --------------------------------------------------------------------------
elif page == "Analytics & Reports":
    st.header("📊 Analytics & Reports")

    # Fetch summary counts
    counts = get_query_counts()

    st.subheader("Summary Stats")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Queries", counts["total"])
    col2.metric("Pending", counts["pending"])
    col3.metric("Resolved", counts["resolved"])
    col4.metric("Closed", counts["closed"])

    st.divider()

    # Pie Chart (Query status)
    st.subheader("Query Status Distribution")
    pie_data = pd.DataFrame({
        "Status": ["Pending", "Resolved", "Closed"],
        "Count": [counts["pending"], counts["resolved"], counts["closed"]]
    })
    fig_pie = px.pie(pie_data, names="Status", values="Count", hole=0.3)
    st.plotly_chart(fig_pie, use_container_width=True)

    st.divider()

    # Bar Chart
    st.subheader("Queries Per Service")
    service_data = get_queries_per_service()
    df_service = pd.DataFrame(service_data)

    if not df_service.empty:
        fig_bar = px.bar(df_service, x="service_name", y="total", text="total")
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("No queries yet to generate service report.")

    st.divider()

    # Line Chart
    st.subheader("Daily Query Trend")
    trend_data = get_daily_query_trend()
    df_trend = pd.DataFrame(trend_data)

    if not df_trend.empty:
        fig_line = px.line(df_trend, x="date", y="total", markers=True)
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("No queries found for trend analysis.")
