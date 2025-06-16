import sqlite3
import streamlit as st

# Connect to SQLite database
conn = sqlite3.connect("healthcare_data.db")
cursor = conn.cursor()

# Create table for patient details (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS patient_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    dob TEXT,
    gender TEXT,
    national_id TEXT,
    huduma_number INTEGER,
    birth_certificate_number INTEGER,
    mobile_number TEXT,
    area_of_residence TEXT,
    landmark TEXT,
    marital_status TEXT,
    religion TEXT,
    education_level TEXT,
    citizenship TEXT,
    nationality TEXT,
    occupation TEXT,
    county TEXT,
    sub_county TEXT,
    ward TEXT,
    insurance_scheme TEXT,
    member_number TEXT,
    scheme_relationship TEXT,
    inpatient_limit TEXT,
    outpatient_limit TEXT
);
""")
conn.commit()
conn.close()

# Streamlit Form
st.title("Patient Registration Form")

with st.form("patient_form"):
    # Personal Details
    first_name = st.text_input("First Name")
    middle_name = st.text_input("Middle Name")
    last_name = st.text_input("Last Name")
    dob = st.date_input("Date of Birth")
    gender = st.selectbox("Gender", ["Male", "Female", "Intersex"])
    national_id = st.text_input("National ID")
    huduma_number = st.number_input("Huduma Number", min_value=0, step=1)
    birth_certificate_number = st.number_input("Birth Certificate Number", min_value=0, step=1)
    mobile_number = st.text_input("Mobile Number")
    area_of_residence = st.text_input("Area of Residence")
    landmark = st.text_input("Landmark (Optional)")

    # Marital & Religious Details
    marital_status = st.radio("Marital Status", ["Single", "Married", "Divorced", "Separated", "Widowed"])
    religion = st.selectbox("Religion", ["Christian", "Islam", "Hindu", "Non-believer"])
    education_level = st.selectbox("Education Level", ["Primary", "Secondary", "Tertiary", "None"])

    # Citizenship & Residence
    citizenship = st.radio("Citizenship", ["Kenyan", "Foreigner"])
    nationality = st.text_input("Nationality (if Foreigner)")
    occupation = st.text_input("Occupation")
    county = st.text_input("County of Residence")
    sub_county = st.text_input("Sub-county")
    ward = st.text_input("Ward")

    # Insurance Details
    insurance_scheme = st.text_input("Insurance Scheme")
    member_number = st.text_input("Member Number")
    scheme_relationship = st.radio("Scheme Relationship", ["Self", "Child", "Spouse"])
    inpatient_limit = st.text_input("Inpatient Limit")
    outpatient_limit = st.text_input("Outpatient Limit")

    # Submit Button
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        conn = sqlite3.connect("healthcare_data.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO patient_details (
            first_name, middle_name, last_name, dob, gender, national_id, huduma_number, 
            birth_certificate_number, mobile_number, area_of_residence, landmark, 
            marital_status, religion, education_level, citizenship, nationality, occupation, 
            county, sub_county, ward, insurance_scheme, member_number, scheme_relationship, 
            inpatient_limit, outpatient_limit
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            first_name, middle_name, last_name, str(dob), gender, national_id, huduma_number, 
            birth_certificate_number, mobile_number, area_of_residence, landmark, marital_status, 
            religion, education_level, citizenship, nationality, occupation, county, sub_county, 
            ward, insurance_scheme, member_number, scheme_relationship, inpatient_limit, outpatient_limit
        ))

        conn.commit()
        conn.close()
        st.success("Data saved successfully!")

# View Records Section
st.subheader("Stored Records")
if st.button("View Records"):
    conn = sqlite3.connect("healthcare_data.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM patient_details")
    records = cursor.fetchall()
    
    conn.close()
    
    if records:
        for record in records:
            st.write(record)
    else:
        st.write("No records found.")
