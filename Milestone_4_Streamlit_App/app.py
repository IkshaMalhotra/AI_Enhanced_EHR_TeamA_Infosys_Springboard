import streamlit as st
import os
import json
from PIL import Image

st.set_page_config(
    page_title="AI-Powered Enhanced EHR Imaging & Documentation",
    page_icon="🏥",
    layout="wide"
)

if "started" not in st.session_state:
    st.session_state.started = False


if not st.session_state.started:

    st.markdown("""
    <style>
        .premium-card {
            background: linear-gradient(145deg, #0f2027, #203a43, #2c5364);
            padding: 60px 50px;
            border-radius: 24px;
            color: white;
            box-shadow: 0 25px 60px rgba(0,0,0,0.35);
            text-align: center;
        }

        .premium-title {
            font-size: 44px;
            font-weight: 700;
            margin-bottom: 18px;
        }

        .premium-subtitle {
            font-size: 18px;
            color: #d7e9ff;
            line-height: 1.7;
            margin-bottom: 30px;
        }

        .badge {
            display: inline-block;
            margin: 6px;
            padding: 10px 18px;
            border-radius: 999px;
            background: rgba(255,255,255,0.15);
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)


    left, center, right = st.columns([1, 3, 1])

    with center:
        st.markdown("""
        <div class="premium-card">
            <div class="premium-title">
            AI-Powered Enhanced EHR Imaging & Documentation
            </div>

        <div class="premium-subtitle">
            An advanced healthcare application integrating Generative AI with Electronic Health Records (EHR) to enhance medical imaging, automate clinical documentation, and improve ICD-10 coding accuracy.  
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Continue to Clinical Dashboard", use_container_width=True):
            st.session_state.started = True
            st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        st.caption("⚠️Prototype for demonstration purposes only.")

    st.stop()



st.markdown("""
# AI-Powered Enhanced EHR Imaging & Documentation
**An advanced healthcare application integrating Generative AI with Electronic Health Records (EHR) to enhance medical imaging, automate clinical documentation, and improve ICD-10 coding accuracy.**

---
""")

NOTES_DIR = "data/notes"
IMAGES_DIR = "data/images"

os.makedirs(NOTES_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

patient_files = [f for f in os.listdir(NOTES_DIR) if f.endswith(".json")]

if not patient_files:
    st.warning("No clinical records available yet.")
    st.info("Please upload or generate patient data to continue.")
    st.stop()


patient_ids = sorted([f.replace(".json", "") for f in patient_files])

st.sidebar.markdown("## 🏥 Clinical Dashboard")
st.sidebar.markdown("Select a patient record to review AI-enhanced outputs.")

selected_patient = st.sidebar.selectbox(
    "Patient ID",
    patient_ids
)

st.sidebar.markdown("---")
st.sidebar.info(
    "This system leverages Computer Vision and Generative AI models "
    "to assist clinicians with imaging enhancement, documentation, "
    "and diagnosis classification."
)

image_path = os.path.join(IMAGES_DIR, f"{selected_patient}.jpg")
note_path = os.path.join(NOTES_DIR, f"{selected_patient}.json")

if not os.path.exists(note_path):
    st.error("Clinical note not found for the selected patient.")
    st.stop()

with open(note_path, "r") as f:
    data = json.load(f)

patient_id = data.get("patient_id", selected_patient)
clinical_note = data.get("clinical_note", "Not available")
assessment = data.get("assessment", "Not available")
icd_code = data.get("icd10_code")
icd_desc = data.get("icd10_description", "")

if isinstance(icd_code, list):
    icd_code = ", ".join(icd_code)

if isinstance(icd_code, dict):
    icd_code = icd_code.get("code")

col1, col2 = st.columns([1.3, 1])

with col1:
    st.subheader("Patient Overview")
    st.markdown(f"**Patient ID:** {patient_id}")

    st.subheader("Enhanced Medical Image")

    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, use_container_width=True)
        st.caption(
            "AI-enhanced medical image generated using Computer Vision "
            "techniques for improved clarity and noise reduction."
        )
    else:
        st.warning("Enhanced medical image not available.")

with col2:
    st.subheader("AI-Generated Clinical Documentation")

    st.markdown(
        f"""
        <div style="
            background-color:#f9f9f9;
            padding:16px;
            border-radius:10px;
            border-left:5px solid #4CAF50;
            line-height:1.6;
        ">
        {clinical_note}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Clinical Assessment")
    st.markdown(
        f"""
        <div style="
            background-color:#fff7e6;
            padding:12px;
            border-radius:8px;
            border-left:5px solid #ff9800;
        ">
        {assessment}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("ICD-10 Diagnosis Code")
    st.markdown(
        f"""
        <div style="
            background-color:#eef3ff;
            padding:14px;
            border-radius:8px;
            font-size:18px;
            font-weight:600;
            color:#1a3cff;
            text-align:center;
        ">
        {icd_code if icd_code else "Not available"}
        </div>
        """,
        unsafe_allow_html=True
    )

    if icd_desc:
        st.caption(icd_desc)

    st.markdown(
        """
        <span style="
            background-color:#e6f4ea;
            color:#137333;
            padding:6px 12px;
            border-radius:20px;
            font-size:12px;
            display:inline-block;
            margin-top:10px;
        ">
        AI Processing Complete
        </span>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.caption(
    "⚠️ This system is intended to support clinical decision-making and does not replace "
    "professional medical judgment. Outputs are generated using AI models trained on "
    "structured healthcare data."
)
