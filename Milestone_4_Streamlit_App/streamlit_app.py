import streamlit as st
import os, json
from PIL import Image
from datetime import datetime

st.set_page_config(page_title="AI-Enhanced EHR", layout="wide", initial_sidebar_state="collapsed")

if "page" not in st.session_state:
    st.session_state.page = "landing"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Mono&display=swap');
:root {
    --navy: #0d1b2a; --blue: #1a3a5c; --accent: #2e86de;
    --teal: #17c3b2; --amber: #f4a261; --green: #2dc653;
    --bg: #f4f6f9; --card: #fff; --border: #e2e8f0;
    --text: #1e293b; --muted: #64748b;
}
* { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; }
.stButton > button {
    background: var(--accent) !important; color: white !important;
    border: none !important; border-radius: 8px !important; font-weight: 600 !important;
}
/* Back button override — slate/neutral tone */
[data-testid="stHorizontalBlock"]:has([data-testid="stButton"]) > div:first-child .stButton > button {
    background: #334155 !important;
}
/* Patient selectbox highlight */
[data-testid="stHorizontalBlock"] [data-baseweb="select"] > div {
    border: 2px solid var(--accent) !important;
    border-radius: 8px !important;
    background: #eff6ff !important;
    font-weight: 600 !important;
    color: var(--blue) !important;
}
</style>
""", unsafe_allow_html=True)


def landing_page():
    st.markdown("""
    <style>
    .stApp { background: var(--navy); }
    .hero { text-align: center; padding: 50px 40px 20px; }
    .eyebrow {
        display: inline-block; background: rgba(46,134,222,0.15);
        color: var(--teal); font-size: 0.75rem; font-weight: 600;
        letter-spacing: 2px; text-transform: uppercase;
        padding: 5px 14px; border-radius: 999px;
        border: 1px solid rgba(23,195,178,0.3); margin-bottom: 24px;
    }
    .hero h1 { color: #fff; font-size: clamp(1.8rem, 4vw, 3rem); font-weight: 700; margin: 0 0 16px; letter-spacing: -0.5px; }
    .hero h1 span { color: var(--teal); }
    .hero p { color: #94a3b8; font-size: 1rem; max-width: 560px; margin: 0 auto 36px; line-height: 1.7; }
    .pills { margin-bottom: 20px; }
    .pill { display: inline-block; margin: 3px; padding: 5px 13px; border-radius: 999px; background: rgba(255,255,255,0.06); color: #cbd5e1; font-size: 0.8rem; border: 1px solid rgba(255,255,255,0.1); }
    .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; max-width: 1000px; margin: 20px auto 40px; padding: 0 20px; }
    .card { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 24px 20px; transition: background 0.3s, border-color 0.3s; }
    .card:hover { background: rgba(46,134,222,0.08); border-color: rgba(46,134,222,0.3); }
    .card-title { color: #e2e8f0; font-weight: 600; font-size: 0.92rem; margin-bottom: 6px; }
    .card-text  { color: #64748b; font-size: 0.83rem; line-height: 1.6; margin: 0; }
    .note { text-align: center; color: #475569; font-size: 0.75rem; padding-bottom: 40px; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">Infosys Springboard - Team A</div>
        <h1>AI-Powered Enhanced<br><span>EHR Imaging & Documentation</span></h1>
        <p>Generative AI for medical imaging, automated clinical notes, and ICD-10 coding - in one platform.</p>
        <div class="pills">
            <span class="pill">Medical Imaging</span>
            <span class="pill">Clinical Notes</span>
            <span class="pill">ICD-10 Coding</span>
            <span class="pill">Azure OpenAI</span>
            <span class="pill">HIPAA-Ready</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, mid, _ = st.columns([1.5, 1, 1.5])
    with mid:
        if st.button("Open Clinical Dashboard", use_container_width=True):
            st.session_state.page = "dashboard"
            st.rerun()

    st.markdown("""
    <div class="cards">
        <div class="card">
            <div class="card-title">AI Image Enhancement</div>
            <p class="card-text">Computer Vision denoises and reconstructs X-rays, MRIs, and CT scans for sharper diagnostic clarity.</p>
        </div>
        <div class="card">
            <div class="card-title">Automated Clinical Notes</div>
            <p class="card-text">Azure OpenAI generates structured documentation from patient data, reducing documentation time.</p>
        </div>
        <div class="card">
            <div class="card-title">ICD-10 Coding</div>
            <p class="card-text">Automatic diagnosis-to-code mapping for billing accuracy and regulatory compliance.</p>
        </div>
        <div class="card">
            <div class="card-title">Unified Patient View</div>
            <p class="card-text">Records, imaging, and AI outputs consolidated in one intuitive clinical dashboard.</p>
        </div>
    </div>
    <div class="note">Prototype for demonstration purposes only. Not for clinical use.</div>
    """, unsafe_allow_html=True)


def dashboard_page():
    st.markdown("""
    <style>
    .stApp { background: var(--bg); }
    .top-bar { background: linear-gradient(135deg, var(--navy), var(--blue)); padding: 16px 24px; border-radius: 12px; margin-bottom: 18px; display: flex; justify-content: space-between; align-items: center; }
    .top-bar h2 { color: #fff; font-size: 1.2rem; font-weight: 600; margin: 0; }
    .top-bar p  { color: #94a3b8; font-size: 0.82rem; margin: 3px 0 0; }
    .top-right  { color: #64748b; font-size: 0.78rem; text-align: right; }
    .patient-strip { background: var(--card); border-left: 5px solid var(--accent); border-radius: 10px; padding: 14px 20px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 6px rgba(0,0,0,0.06); }
    .pid  { font-size: 1.05rem; font-weight: 700; color: var(--text); }
    .psub { font-size: 0.8rem; color: var(--muted); margin-top: 2px; }
    .badge { background: #dcfce7; color: #166534; padding: 3px 10px; border-radius: 999px; font-size: 0.72rem; font-weight: 600; }
    .metrics { display: flex; gap: 12px; margin-bottom: 16px; flex-wrap: wrap; }
    .mc { flex: 1; min-width: 110px; background: var(--card); border-radius: 10px; padding: 12px 16px; box-shadow: 0 1px 5px rgba(0,0,0,0.05); border-top: 3px solid var(--accent); }
    .mc.green { border-top-color: var(--green); } .mc.teal { border-top-color: var(--teal); } .mc.amber { border-top-color: var(--amber); }
    .ml { font-size: 0.68rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.6px; }
    .mv { font-size: 1rem; font-weight: 700; color: var(--text); margin-top: 3px; }
    .scard { background: var(--card); border-radius: 10px; padding: 18px 20px; margin-bottom: 12px; box-shadow: 0 1px 6px rgba(0,0,0,0.05); }
    .sh { font-size: 0.88rem; font-weight: 600; color: var(--blue); border-bottom: 1px solid var(--border); padding-bottom: 10px; margin-bottom: 12px; }
    .note-box   { background: #f0fdf9; border-left: 4px solid var(--teal);  border-radius: 0 6px 6px 0; padding: 12px 14px; color: #134e4a; font-size: 0.88rem; line-height: 1.65; }
    .assess-box { background: #fff8f0; border-left: 4px solid var(--amber); border-radius: 0 6px 6px 0; padding: 12px 14px; color: #7c4a00; font-size: 0.88rem; line-height: 1.6; }
    .icd-badge  { display: inline-block; background: var(--navy); color: var(--teal); font-family: 'DM Mono', monospace; font-size: 1.1rem; padding: 8px 18px; border-radius: 8px; margin: 6px 0 4px; }
    .ai-tag     { display: inline-block; background: #dcfce7; color: #166534; padding: 3px 10px; border-radius: 999px; font-size: 0.7rem; font-weight: 600; margin-top: 8px; }
    .img-meta   { background: #f8fafc; border-radius: 8px; padding: 10px; display: flex; justify-content: space-around; margin-top: 10px; font-size: 0.78rem; text-align: center; }
    .stTabs [data-baseweb="tab-list"] { background: var(--card); padding: 5px; border-radius: 10px; gap: 5px; box-shadow: 0 1px 5px rgba(0,0,0,0.05); }
    .stTabs [data-baseweb="tab"]      { border-radius: 7px; padding: 7px 18px; font-size: 0.83rem; font-weight: 500; color: var(--muted) !important; }
    .stTabs [aria-selected="true"]    { background: var(--navy) !important; color: #fff !important; }
    .footer { text-align: center; color: var(--muted); font-size: 0.75rem; padding: 18px; border-top: 1px solid var(--border); margin-top: 24px; }
    </style>
    """, unsafe_allow_html=True)

    BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
    NOTES_DIR  = os.path.join(BASE_DIR, "data", "notes")
    IMAGES_DIR = os.path.join(BASE_DIR, "data", "images")
    os.makedirs(NOTES_DIR, exist_ok=True)

    patient_ids = sorted([f.replace(".json", "") for f in os.listdir(NOTES_DIR) if f.endswith(".json")])
    if not patient_ids:
        st.warning("No patient records found in data/notes/")
        st.stop()

    st.markdown(f"""
    <div class="top-bar">
        <div><h2>AI-Enhanced EHR Viewer</h2><p>Clinical summary, documentation & medical imaging</p></div>
        <div class="top-right">{datetime.now().strftime("%d %B %Y")}<br><span style="color:#4ade80; font-size:0.72rem;">Live</span></div>
    </div>
    """, unsafe_allow_html=True)

    col_back, col_select, _ = st.columns([1, 2, 4])
    with col_back:
        if st.button("Back to Home", use_container_width=True):
            st.session_state.page = "landing"
            st.rerun()
    with col_select:
        selected = st.selectbox("Patient", patient_ids, label_visibility="collapsed")

    note_path  = os.path.join(NOTES_DIR,  f"{selected}.json")
    image_path = os.path.join(IMAGES_DIR, f"{selected}.jpg")

    if not os.path.exists(note_path):
        st.error("Record not found.")
        st.stop()

    with open(note_path) as f:
        data = json.load(f)

    pid      = data.get("patient_id", selected)
    note     = data.get("clinical_note", "Not available")
    assess   = data.get("assessment", "Not available")
    icd_code = data.get("icd10_code", "N/A")
    icd_desc = data.get("icd10_description", "")
    has_img  = os.path.exists(image_path)

    if isinstance(icd_code, list): icd_code = ", ".join(icd_code)
    if isinstance(icd_code, dict): icd_code = icd_code.get("code", "N/A")

    st.markdown(f"""
    <div class="patient-strip">
        <div><div class="pid">Patient {pid}</div><div class="psub">Electronic Health Record — AI-Enhanced</div></div>
        <span class="badge">Active Record</span>
    </div>
    <div class="metrics">
        <div class="mc teal"><div class="ml">Patient ID</div><div class="mv">{pid}</div></div>
        <div class="mc"><div class="ml">ICD-10 Code</div><div class="mv">{icd_code}</div></div>
        <div class="mc green"><div class="ml">Record Status</div><div class="mv">Active</div></div>
        <div class="mc {'green' if has_img else 'amber'}"><div class="ml">Medical Image</div><div class="mv">{'Available' if has_img else 'Pending'}</div></div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Clinical Summary", "Medical Imaging", "Raw EHR Data"])

    with tab1:
        left, right = st.columns([3, 2])
        with left:
            st.markdown(f"""
            <div class="scard">
                <div class="sh">Clinical Note</div>
                <div class="note-box">{note}</div>
                <div class="ai-tag">AI Processing Complete — Azure OpenAI</div>
            </div>
            <div class="scard">
                <div class="sh">Clinical Assessment</div>
                <div class="assess-box">{assess}</div>
            </div>
            """, unsafe_allow_html=True)
        with right:
            img_color = "var(--green)" if has_img else "var(--amber)"
            img_label = "Available" if has_img else "Pending"
            st.markdown(f"""
            <div class="scard" style="text-align:center;">
                <div class="sh" style="text-align:left;">ICD-10 Diagnosis</div>
                <div class="icd-badge">{icd_code}</div>
                <div style="color:var(--muted); font-size:0.8rem; margin-top:6px;">{icd_desc}</div>
            </div>
            <div class="scard">
                <div class="sh">Record Info</div>
                <div style="font-size:0.83rem;">
                    <div style="padding:5px 0; border-bottom:1px solid var(--border); display:flex; justify-content:space-between;"><span style="color:var(--muted);">Patient ID</span><strong>{pid}</strong></div>
                    <div style="padding:5px 0; border-bottom:1px solid var(--border); display:flex; justify-content:space-between;"><span style="color:var(--muted);">Image</span><strong style="color:{img_color};">{img_label}</strong></div>
                    <div style="padding:5px 0; display:flex; justify-content:space-between;"><span style="color:var(--muted);">Backend</span><strong>Azure OpenAI</strong></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='scard'><div class='sh'>AI-Enhanced Medical Image</div><div style='color:var(--muted); font-size:0.82rem;'>Denoised and reconstructed via Computer Vision for improved diagnostic clarity.</div></div>", unsafe_allow_html=True)
        if has_img:
            _, mid, _ = st.columns([1, 3, 1])
            with mid:
                img = Image.open(image_path)
                st.image(img, use_container_width=True)
                w, h = img.size
                ext = os.path.splitext(image_path)[1].upper().lstrip(".")
                st.markdown(f"""
                <div class="img-meta">
                    <div><div style="color:var(--muted);">Format</div><strong>{ext}</strong></div>
                    <div><div style="color:var(--muted);">Dimensions</div><strong>{w} x {h}</strong></div>
                    <div><div style="color:var(--muted);">Enhancement</div><strong style="color:var(--green);">AI-Enhanced</strong></div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align:center; padding:50px; background:#f8fafc; border-radius:10px; border:2px dashed var(--border);">
                <div style="font-size:1.5rem; margin-bottom:10px; color:var(--muted);">[ No Image ]</div>
                <p style="color:var(--muted); font-size:0.83rem; margin:0;">Medical imaging for this patient is being processed.</p>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        json_str = json.dumps(data, indent=2)
        st.download_button("Download JSON", data=json_str, file_name=f"{pid}_ehr.json", mime="application/json")
        st.json(data)

    st.markdown("""
    <div class="footer">
        AI-Enhanced EHR System &nbsp;·&nbsp; Infosys Springboard Team A &nbsp;·&nbsp; Powered by Azure OpenAI<br>
        <span style="color:#94a3b8;">For demonstration only, not for clinical use.</span>
    </div>
    """, unsafe_allow_html=True)


if st.session_state.page == "landing":
    landing_page()
else:
    dashboard_page()