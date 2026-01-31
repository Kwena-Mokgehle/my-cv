#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 23:29:52 2026

@author: moloko_mokgehle
"""


import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="Moloko's Resume", page_icon="📄")

# --- HEADER SECTION ---
st.title("Moloko Mokgehle")
st.write("Data Analyst, Developer")
st.write("📍 Cape Town, Western Cape | 📧 mgkofficial25@icloud.com")
# LinkedIn: 
st.write("https://linkedin.com/in/moloko-mokgehle")

# --- SUMMARY ---
st.subheader("ℹ️ Professional Summary")
st.write("Recent Mathematical Sciences graduate with Advanced Diploma (70% average) from Cape Peninsula University of Technology. Proficient in Python, R, SQL, and Machine Learning; led projects predicting student outcomes with XGBoost (top accuracy via F1-score) and statistical quality control. Seeking data analysis/science internship to apply data preprocessing, modeling, and visualization skills for impactful insights.")


# --- SKILLS & EDUCATION ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("⚒️ Skills")
    st.write("- Python (Pandas, Streamlit)")
    st.write("- SQL")
    st.write("- Git / GitHub")

with col2:
    st.subheader("🎓 Education")
    st.write("**Postgraduate Diploma in Mathematical Science, In Progress**")
    st.write("**Advanced Diploma in Mathematical Science**")
    st.write("**Diploma in Mathematical Science**")
    st.write("Cape Peninsula University of Technology")
    
    
# --- EXPERIENCE ---
st.subheader("🚀 Experience")
with st.expander("Personal Portfolio Website (Streamlit)"):
    st.write("Built an interactive CV using Streamlit and deployed it via GitHub.")
    
with st.expander("Research Intern"):
    ex_col1, ex_col2, ex_col3 = st.columns(3)
    
    with ex_col1:
        st.write("- Conducted a qualitative literature synthesis and online research, producing detailed reports that improved data presentation clarity for project deliverables.")
    with ex_col2:
        st.write("- Organized collaboratives data workflows using Google Drive and Docs, enhancing team version control and efficiency.")
    with ex_col3:
        st.write("- Managed references with Mendeley, ensuring accurate citations across 20+ sources for research outputs.")

with st.expander("Volunteer University Application Assistant"):
    st.write("- Guided 50+ high school students to apply for university and funding, overcoming resource gaps by developing mobile smartphone strategy at under equuipped schools.")
    st.write("- Built Excel tracking system capturing student details, enabling 100% follow-up completion rates for funding.")
    st.write("- Supported multilingual learners across stations, boosting communication and teamwork in diverse settings.")
    st.write("✌️ we are having fun this side!!")

# --- Projects ---
st.subheader("📽️ Research Projects")
with st.expander("Student Completion Time Prediction (Machine Learning)"):
    st.write("- Performed exploratory data analysis on Diploma student data using Python (Pandas, NumPy, Matplotlib, Seaborn); built Logistic Regression, Random Forest, XGBoost models to identify at-risk student at enrollment.")
    st.write("- Applied preprocessing (KNN Imputation, SMOTE balancing, RFE selection), achieving top XGBoost performance via accuracy.")

with st.expander("Statistical Quality Control in SA Drug Manufacturing"):
    st.write("- Analyzed process stability with R/Excel control charts, logistic regression, ANOVA, validated data for regulatory compliance insights.")


# --- References ---
st.write("---") # Visual divider
st.subheader("📚 References")

ref_col1, ref_col2 = st.columns(2)

with ref_col1:
    st.write("**Ms. Kemone Brown**")
    st.write("Tamarind Hill Press")
    st.write("Relationship: Research Supervisor")
    st.write("📧 info@tamarindhillpress.co.za")

with ref_col2:
    st.write("**Mr. William Manamela**")
    st.write("Cape Peninsula University of Technology")
    st.write("Relationship: Lecturer")
    st.write("📧 manamelawi@cput.ac.za")

# --- Skip a line ---
st.write("")
st.write("")

# --- DOWNLOAD BUTTON ---
# Place your actual PDF file in the same folder as this script
import os

# Define the file name
file_path = "Moloko Mokgehle_CV.pdf" 

# Check if the file exists before trying to open it
if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        pdf_data = f.read()
    bt_col1, bt_col2, bt_col3 = st.columns([1, 1, 1])
    
    with bt_col2:    
        st.download_button(
            label="📥 Download Resume",
            data=pdf_data,
            file_name="Moloko_Mokgehle_CV.pdf",
            mime="application/pdf"
        )
else:
    st.warning(f"⚠️ {file_path} not found. Please ensure it is in the 'Trials' folder.")








