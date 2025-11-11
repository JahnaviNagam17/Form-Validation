import streamlit as st
import re

st.markdown("# Form Validation Project")

name = st.text_input("Enter Your Name")
name_valid = re.fullmatch("[a-zA-Z][a-zA-Z0-9]*", name)


dob = st.text_input("Enter DOB (MM-DD-YYYY)")
dob_valid = re.fullmatch(r"(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])-(?:[0-9]{4})", dob)


email = st.text_input("Enter valid Email ID")
email_valid = re.fullmatch(r"\b[a-zA-Z][a-zA-Z0-9]*@[a-zA-Z]+.[a-zA-Z]{2,3}\b", email)


mobile = st.text_input("Enter the 10 digit Mobile number")
mobile_valid = re.fullmatch(r"\b[0-9]{10}\b", mobile)


if st.button("SUBMIT"):
    if name_valid and dob_valid and email_valid and mobile_valid:
        st.success("All Input Data is Valid")
        st.markdown(f"**NAME** :{name}")
        st.markdown(f"**DOB** :{dob}")
        st.markdown(f"**EMAIL** :{email}")
        st.markdown(f"***MOBILE NUMBER*** :{mobile}")
    else:
        st.error("Any of the above input data is not in right format")

    if not name_valid:
        st.warning("NAME is not in correct format")


    if not dob_valid:
        st.warning("DOB is not in correct format")


    if not email_valid:
        st.warning("EMAIL is not in correct format")


    if not mobile_valid:
        st.warning("Mobile number is not in correct format")


