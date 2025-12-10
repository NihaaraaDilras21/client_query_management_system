# 🧪 Test Cases – Client Query Management System

This document contains functional test cases for validating the Client Query Management System (Streamlit + MySQL).

---

## ✔️ Test Case 1: Add Client

| Field | Details |
|------|---------|
| **Test Case ID** | TC_CLIENT_01 |
| **Title** | Add a new client |
| **Precondition** | Database is connected |
| **Steps** | 1. Open "Add Client" page <br> 2. Enter valid name, email, phone <br> 3. Click "Save Client" |
| **Expected Result** | Client is added successfully and appears in the client list |
| **Actual Result** | _To be filled after testing_ |
| **Status** | Pass / Fail |

---

## ✔️ Test Case 2: Add Client (Missing Name)

| Field | Details |
|------|---------|
| **Test Case ID** | TC_CLIENT_02 |
| **Title** | Add client without name |
| **Steps** | 1. Leave name empty <br> 2. Enter email & phone <br> 3. Click "Save Client" |
| **Expected Result** | Error message: “Client name cannot be empty!” |
| **Status** | Pass / Fail |

---

## ✔️ Test Case 3: View Clients Table

| Field | Details |
|------|---------|
| **Test Case ID** | TC_CLIENT_03 |
| **Title** | Check if clients appear in the table |
| **Expected Result** | Newly added clients appear correctly in table |

---

---

## ✔️ Test Case 4: Add Service

| Field | Details |
|------|---------|
| **Test Case ID** | TC_SERVICE_01 |
| **Title** | Add a new service |
| **Steps** | Enter service name + description and click "Add Service" |
| **Expected Result** | Service appears in services table |

---

## ✔️ Test Case 5: Delete Service

| Field | Details |
|------|---------|
| **Test Case ID** | TC_SERVICE_02 |
| **Title** | Delete an existing service |
| **Steps** | Select service ID → click “Delete Service” |
| **Expected Result** | Service removed from table |

---

---

## ✔️ Test Case 6: Add Query

| Field | Details |
|------|---------|
| **Test Case ID** | TC_QUERY_01 |
| **Title** | Submit a new query |
| **Precondition** | At least 1 client & 1 service must exist |
| **Steps** | Select client → select service → enter query → Submit |
| **Expected Result** | Query added with status "Pending" |

---

## ✔️ Test Case 7: Resolve Query

| Field | Details |
|------|---------|
| **Test Case ID** | TC_QUERY_02 |
| **Title** | Mark a query as resolved |
| **Expected Result** | Query status changes to “Resolved” |

---

## ✔️ Test Case 8: Delete Query

| Field | Details |
|------|---------|
| **Test Case ID** | TC_QUERY_03 |
| **Title** | Delete a query |
| **Expected Result** | Query removed from database |

---

## ✔️ Test Case 9: View Queries Table

| Field | Details |
|------|---------|
| **Test Case ID** | TC_QUERY_04 |
| **Title** | Display all queries |
| **Expected Result** | Table shows all queries with correct columns |

---

---

## ✔️ Test Case 10: Analytics Dashboard Loads Correctly

| Field | Details |
|------|---------|
| **Test Case ID** | TC_ANALYTICS_01 |
| **Title** | Analytics page loads without errors |
| **Expected Result** | KPIs + Pie + Bar + Line chart all render successfully |

---

## ✔️ Test Case 11: Correct KPI Values

| Field | Details |
|------|---------|
| **Test Case ID** | TC_ANALYTICS_02 |
| **Title** | KPI data matches database |
| **Steps** | Compare dashboard values with SQL queries |
| **Expected Result** | Dashboard numbers match MySQL counts |

---

## ✔️ Test Case 12: Dataset Loading Script

| Field | Details |
|------|---------|
| **Test Case ID** | TC_DATASET_01 |
| **Title** | load_dataset.py loads CSV correctly |
| **Steps** | Run `python load_dataset.py` |
| **Expected Result** | CSV data inserted with no duplicates |

---

## ✔️ Test Case 13: Database Connection

| Field | Details |
|------|---------|
| **Test Case ID** | TC_DB_01 |
| **Title** | Check MySQL connection |
| **Expected Result** | Application connects without authentication errors |

---

## ✔️ Test Case 14: Handle Empty Tables

| Field | Details |
|------|---------|
| **Test Case ID** | TC_EMPTY_01 |
| **Title** | Display pages with no data |
| **Expected Result** | Proper messages like “No queries found” |

---

## ✔️ Test Case 15: Form Validation

| Field | Details |
|------|---------|
| **Test Case ID** | TC_VALIDATION_01 |
| **Title** | Check required fields |
| **Expected Result** | App prevents submitting blank forms |

---

# ✔️ Optional Advanced Test Cases (If you want to impress!)

### TC_ADV_01 – Load 5,000+ records from CSV without crashing  
### TC_ADV_02 – Response time of dashboard < 2 seconds  
### TC_ADV_03 – SQL injection check (inputs sanitized)  

---

# 🎉 End of Test Cases
These test cases make your project **professional**, **industry-ready**, and **internship-grade**.

