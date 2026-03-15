"""
KV Life OS — Premium Streamlit Dashboard
A world-class life management analytics system.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime
import random

from app.const import OUTFILE_HORIZONTAL, GOOGLE_SHEETS_URL
from app.const import (
    CATEGORIES_MAP, CATEGORY_WEIGHTS, CATEGORY_EMOJIS,
    NEGATIVE_HABIT_TASKS, TASKS
)
from app.const import OKRS

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="KV Life OS",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded",  # FORCE SIDEBAR OPEN
)

# ── Premium CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* === ROOT PALETTE === */
:root {
    --bg:        #080818;
    --bg-card:   #0f0f2a;
    --bg-card2:  #15153a;
    --border:    rgba(80,80,180,0.18);
    --accent1:   #6C63FF;
    --accent2:   #00D4AA;
    --accent3:   #FF6B6B;
    --accent4:   #FFD166;
    --text1:     #F0F0FF;
    --text2:     #9090BB;
    --green:     #10B981;
    --red:       #EF4444;
    --gold:      #F59E0B;
    --blue:      #3B82F6;
    --purple:    #8B5CF6;
    --orange:    #F97316;
    --pink:      #EC4899;
    --cyan:      #06B6D4;
}

/* === GLOBAL BACKGROUND === */
.stApp, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #080818 0%, #0c0c28 50%, #080818 100%) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text1) !important;
}

/* === SIDEBAR === */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0a22 0%, #12123a 100%) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text1) !important; }

/* === HIDE DEFAULT STREAMLIT ELEMENTS === */
#MainMenu, footer { visibility: hidden; }
header { background-color: transparent !important; }
.block-container { padding-top: 1rem !important; padding-bottom: 2rem !important; }

/* === METRIC CARDS === */
.metric-card {
    background: linear-gradient(135deg, #12123a 0%, #1a1a4a 100%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 22px 24px;
    margin: 6px 0;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
}
.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 32px rgba(108,99,255,0.25);
}
.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--accent1), var(--accent2));
    border-radius: 16px 16px 0 0;
}
.metric-label {
    font-size: 14px; font-weight: 600; letter-spacing: 1.5px;
    text-transform: uppercase; color: var(--text2); margin-bottom: 8px;
}
.metric-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 42px; font-weight: 700; color: var(--text1); line-height: 1;
}
.metric-value.green { color: var(--green); }
.metric-value.gold  { color: var(--gold);  }
.metric-value.red   { color: var(--red);   }
.metric-value.blue  { color: var(--blue);  }
.metric-delta {
    font-size: 15px; margin-top: 6px; color: var(--text2);
}

/* === SECTION HEADERS === */
.section-header {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 24px; font-weight: 700;
    color: var(--text1);
    padding: 12px 0 6px 0;
    border-bottom: 2px solid;
    border-image: linear-gradient(90deg, var(--accent1), transparent) 1;
    margin-bottom: 18px;
    letter-spacing: -0.3px;
}

/* === HERO BANNER === */
.hero-banner {
    background: linear-gradient(135deg, #1a0a4a 0%, #0a1a4a 50%, #0a2a3a 100%);
    border: 1px solid rgba(108,99,255,0.3);
    border-radius: 20px;
    padding: 32px 36px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}
.hero-banner::after {
    content: '';
    position: absolute;
    top: -50%; right: -10%;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(108,99,255,0.15) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 36px; font-weight: 800;
    background: linear-gradient(135deg, #6C63FF, #00D4AA, #FFD166);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; margin-bottom: 6px;
}
.hero-subtitle {
    color: var(--text2); font-size: 17px; font-weight: 400;
}
.hero-quote {
    margin-top: 16px;
    font-style: italic; color: var(--accent4);
    font-size: 15px; font-weight: 500;
    border-left: 3px solid var(--accent4);
    padding-left: 12px;
}

/* === PROGRESS BAR === */
.prog-wrap { margin: 8px 0 14px 0; }
.prog-label-row { display: flex; justify-content: space-between; margin-bottom: 5px; }
.prog-label { font-size: 15px; font-weight: 600; color: var(--text1); }
.prog-pct   { font-size: 15px; font-weight: 700; color: var(--accent2); }
.prog-bar-bg {
    background: rgba(255,255,255,0.06); border-radius: 50px;
    height: 8px; overflow: hidden;
}
.prog-bar-fill {
    height: 100%; border-radius: 50px;
    background: linear-gradient(90deg, var(--accent1), var(--accent2));
    transition: width 0.6s ease;
}

/* === HABIT CHIP === */
.habit-chip {
    display: inline-block; padding: 4px 14px; border-radius: 50px;
    font-size: 14px; font-weight: 600; margin: 3px;
}
.chip-yes  { background: rgba(16,185,129,0.15); color: #10B981; border: 1px solid rgba(16,185,129,0.3); }
.chip-no   { background: rgba(239,68,68,0.15);  color: #EF4444; border: 1px solid rgba(239,68,68,0.3); }
.chip-skip { background: rgba(148,163,184,0.1); color: #94A3B8; border: 1px solid rgba(148,163,184,0.2); }

/* === OKR CARD === */
.okr-card {
    background: linear-gradient(135deg, #0f1535 0%, #151840 100%);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px 20px;
    margin: 10px 0;
}
.okr-objective { font-size: 15px; font-weight: 700; color: var(--accent4); margin-bottom: 8px; }
.okr-kr        { font-size: 15px; color: var(--text1); margin-bottom: 10px; }
.okr-meta      { display: flex; gap: 16px; font-size: 14px; color: var(--text2); }

/* === IDEAL MAN SECTION === */
.ideal-section {
    background: linear-gradient(135deg, #0a1228 0%, #0d1830 100%);
    border: 1px solid rgba(108,99,255,0.2);
    border-radius: 14px; padding: 18px 22px; margin: 8px 0;
}
.ideal-heading {
    font-size: 15px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; color: var(--accent1); margin-bottom: 12px;
}
.ideal-item {
    font-size: 15px; color: var(--text1); padding: 5px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.ideal-item:last-child { border-bottom: none; }

/* === QUOTE BOX === */
.quote-box {
    background: linear-gradient(135deg, rgba(108,99,255,0.1), rgba(0,212,170,0.05));
    border: 1px solid rgba(108,99,255,0.2);
    border-radius: 12px; padding: 16px 20px; margin: 12px 0;
    font-style: italic; color: var(--accent4);
    font-size: 16px; font-weight: 500;
}

/* === STATUS BADGE === */
.badge { display: inline-block; padding: 3px 10px; border-radius: 50px; font-size: 13px; font-weight: 700; }
.badge-green  { background: rgba(16,185,129,0.2); color: #10B981; }
.badge-red    { background: rgba(239,68,68,0.2);  color: #EF4444; }
.badge-gold   { background: rgba(245,158,11,0.2); color: #F59E0B; }
.badge-blue   { background: rgba(59,130,246,0.2); color: #3B82F6; }
.badge-grey   { background: rgba(148,163,184,0.1); color: #94A3B8; }

/* === PLOTLY CHART THEME === */
.stPlotlyChart { border-radius: 16px; overflow: hidden; }

/* === SIDEBAR RADIO === */
.stRadio > label { color: var(--text2) !important; font-size: 16px !important; }
div[data-testid="stSidebarNav"] { display: none; }

/* === SIDEBAR WIDTH FIX (prevent accidental shrinking) === */
section[data-testid="stSidebar"] {
    min-width: 250px !important;
    max-width: 300px !important;
}
/* Keep the collapse button visible so the user can un-collapse it if they accidentally clicked the margin earlier */
button[kind="header"] {
    color: #9090BB !important;
}

/* === DATE / TEXT INPUTS (fix white-on-white) === */
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] [data-baseweb="input"] input,
[data-testid="stSidebar"] [data-baseweb="datepicker"] input,
[data-testid="stDateInput"] input,
[data-baseweb="input"] input,
[data-baseweb="datepicker"] input {
    background-color: #1e1e42 !important;
    color: #F0F0FF !important;
    border: 1px solid rgba(108,99,255,0.35) !important;
    border-radius: 8px !important;
}
[data-testid="stDateInput"] input::placeholder,
[data-baseweb="input"] input::placeholder {
    color: #6060AA !important;
}
/* Calendar popover */
[data-baseweb="calendar"] {
    background: #12122a !important;
    color: #F0F0FF !important;
}
[data-baseweb="calendar"] button {
    color: #F0F0FF !important;
}
[data-baseweb="calendar"] [aria-selected="true"] {
    background: #6C63FF !important;
}
</style>
""", unsafe_allow_html=True)

# ── Constants ─────────────────────────────────────────────────────────────────
MOTIVATIONAL_QUOTES = [
    "You do not rise to the level of your goals. You fall to the level of your systems.",
    "Discipline equals freedom. — Jocko Willink",
    "Success is the sum of small efforts, repeated day in and day out.",
    "The man who moves a mountain begins by carrying away small stones.",
    "Consistency beats motivation. Every. Single. Time.",
    "Don't wish it were easier. Wish you were better.",
    "An hour of deep work is worth more than a day of shallow hustle.",
    "Your future self is watching you right now through your memories.",
    "Excellence is not a destination. It is a continuous journey.",
    "The secret of your future is hidden in your daily routine.",
]

CAT_COLORS = {
    "Body":          "#3B82F6",
    "Mind":          "#8B5CF6",
    "Career":        "#F59E0B",
    "Wealth":        "#10B981",
    "Focus":         "#F97316",
    "Relationships": "#EC4899",
    "Other":         "#64748B",
}

IDEAL_MAN_CODE = {
    "⚡ IDENTITY": [
        "I am a disciplined, focused, relentless man who builds every day.",
        "I do not wait for motivation. I act from commitment.",
        "I take full ownership — my results, my mind, my body.",
        "I am not who I was yesterday. I am becoming who I was meant to be.",
    ],
    "💪 BODY": [
        "I wake up early. Early mornings belong to winners.",
        "I train my body like a warrior. Weakness has no home here.",
        "I eat to perform, not to comfort.",
        "I sleep 7+ hours. Recovery is part of the system.",
        "Cold showers build character. No excuses.",
    ],
    "🧘 MIND": [
        "I read every day. Knowledge is my compound interest.",
        "I journal every morning. Clarity precedes great decisions.",
        "I meditate. A calm mind outperforms an anxious one.",
        "I eliminate negative self-talk. My words shape my world.",
    ],
    "🚀 CAREER": [
        "I do deep work daily. Shallow work builds shallow results.",
        "I apply to jobs relentlessly. Persistence beats talent.",
        "I build projects that prove my skills. Actions > words.",
        "I review my OKRs weekly. Goals without reviews are wishes.",
    ],
    "💰 WEALTH": [
        "I track every rupee. Financial awareness is financial power.",
        "I invest before I spend. Pay yourself first, always.",
        "I build income streams. One source of income is poverty.",
    ],
    "🎯 FOCUS": [
        "I control my dopamine. Instagram and shorts steal my future.",
        "I do the hardest task first. Mornings are sacred.",
        "I keep my phone away in the morning.",
        "Discipline equals freedom. That is my operating system.",
    ],
    "📖 PHILOSOPHY": [
        "Consistency beats motivation. Every single time.",
        "One day or day one. I choose day one. Every day.",
        "Success is built daily, not in a single grand moment.",
    ],
}

# ── Data Loading ──────────────────────────────────────────────────────────────
@st.cache_data(ttl=300)
def load_data(filepath=OUTFILE_HORIZONTAL, gsheets_url=GOOGLE_SHEETS_URL):
    import re
    
    # Try Google Sheets first if configured
    if gsheets_url and gsheets_url.strip():
        url = gsheets_url.strip()
        try:
            if "export?format=csv" not in url:
                match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)
                gid_match = re.search(r'gid=([0-9]+)', url)
                if match:
                    sheet_id = match.group(1)
                    gid = gid_match.group(1) if gid_match else "0"
                    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
            
            df = pd.read_csv(url)
            if "Date" in df.columns:
                df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.date
                df = df.dropna(subset=["Date"])
            return df
        except Exception as e:
            st.sidebar.error(f"⚠️ Failed to load from Google Sheets: {e}")
            pass # Fall back to local file
            
    # Local Excel Fallback
    try:
        df = pd.read_excel(filepath, sheet_name="Tasks")
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.date
            df = df.dropna(subset=["Date"])
        return df
    except Exception as e:
        return pd.DataFrame()

def get_category_score(row_data, category):
    """Return 0-100 score for a single category based on YesNo tasks."""
    tasks_in_cat = [
        t for t, cat, itype in TASKS
        if cat == category and itype == "YesNo" and t not in NEGATIVE_HABIT_TASKS
    ]
    if not tasks_in_cat:
        return None
    yes = sum(1 for t in tasks_in_cat if row_data.get(t) == "Yes")
    return round(yes / len(tasks_in_cat) * 100, 1)

def get_life_score(row_data):
    """Weighted Life Score across all dimensions."""
    total, weight_sum = 0.0, 0.0
    for cat, weight in CATEGORY_WEIGHTS.items():
        s = get_category_score(row_data, cat)
        if s is not None:
            total      += s * weight
            weight_sum += weight
    return round(total / weight_sum, 1) if weight_sum > 0 else 0.0

def get_dopamine_score(row_data):
    score = 100
    for t in NEGATIVE_HABIT_TASKS:
        if row_data.get(t) == "Yes":
            score -= 15
    return max(score, 0)

def score_color(score):
    if score >= 80:
        return "green"
    elif score >= 55:
        return "gold"
    else:
        return "red"

def make_progress_bar(label, value, max_val=100, color="#6C63FF"):
    pct = min(int(value / max_val * 100), 100)
    return f"""
    <div class="prog-wrap">
        <div class="prog-label-row">
            <span class="prog-label">{label}</span>
            <span class="prog-pct">{value:.0f} / {max_val}</span>
        </div>
        <div class="prog-bar-bg">
            <div class="prog-bar-fill" style="width:{pct}%; background: linear-gradient(90deg, {color}, {color}aa);"></div>
        </div>
    </div>
    """

def plotly_dark_layout():
    return dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color="#9090BB", size=14),
        margin=dict(l=20, r=20, t=40, b=20),
        hoverlabel=dict(
            bgcolor="rgba(20,20,30,0.95)",
            font_size=16,
            font_family="Inter",
            font_color="white"
        ),
    )

def safe_val(val, default="—"):
    """Return empty string for NaN / None / blank values from Excel."""
    if val is None:
        return default
    try:
        import math
        if isinstance(val, float) and math.isnan(val):
            return default
    except Exception:
        pass
    s = str(val).strip()
    return s if s not in ("", "nan", "NaN", "None") else default

# ── Load Data ─────────────────────────────────────────────────────────────────
df = load_data()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 16px 0 8px 0;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:22px; font-weight:800;
             background:linear-gradient(135deg,#6C63FF,#00D4AA); -webkit-background-clip:text;
             -webkit-text-fill-color:transparent; background-clip:text;">⚡ KV LIFE OS</div>
        <div style="color:#9090BB; font-size:14px; margin-top:2px;">COMMAND CENTER v2.0</div>
    </div>
    <hr style="border-color:rgba(80,80,180,0.2); margin:8px 0 16px 0;">
    """, unsafe_allow_html=True)

    today = datetime.date.today()
    nav = st.radio(
        "NAVIGATE",
        ["🏠 Daily Dashboard", "📊 Life Score", "📅 Weekly Review",
         "🎯 Goal Progress", "📈 Habit Analytics", "🪞 Reflection",
         "⚡ Ideal Man Code"],
        label_visibility="visible",
    )

    st.markdown("<hr style='border-color:rgba(80,80,180,0.2); margin:16px 0;'>", unsafe_allow_html=True)

    if not df.empty:
        available_dates = sorted(df["Date"].dropna().unique(), reverse=True)
        # Default to today if it exists in data, otherwise the closest past date
        if today in available_dates:
            default_d = today
        else:
            past = [d for d in available_dates if d <= today]
            default_d = max(past) if past else today
        selected_date = st.date_input("📅 Select Date", value=default_d,
                                      min_value=min(available_dates),
                                      max_value=max(available_dates))
    else:
        selected_date = today

    if st.button("🔄 Reload Data", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

    st.markdown(f"""
    <div style="color:#9090BB; font-size:13px; text-align:center; margin-top:12px;">
        Today: {today.strftime('%b-%d-%Y')}<br>
        Day {today.timetuple().tm_yday} of {today.year}
    </div>
    """, unsafe_allow_html=True)

    # Random quote in sidebar
    q = random.choice(MOTIVATIONAL_QUOTES)
    st.markdown(f"""
    <div style="margin-top:20px; padding:12px; background:rgba(108,99,255,0.08);
         border-left:3px solid #6C63FF; border-radius:0 8px 8px 0;
         font-size:14px; font-style:italic; color:#9090BB;">
        "{q}"
    </div>
    """, unsafe_allow_html=True)

# ── Row Data Setup ────────────────────────────────────────────────────────────
row_data = {}
data_available = False
data_filled    = False   # True only when at least 1 YesNo habit has a real value
if not df.empty:
    filtered = df[df["Date"] == selected_date]
    if not filtered.empty:
        row_data = filtered.iloc[0].to_dict()
        data_available = True
        # Check if any YesNo habit actually has Yes/No (not empty)
        data_filled = any(
            row_data.get(t) in ("Yes", "No")
            for t, cat, itype in TASKS
            if itype in ("YesNo", "NegYesNo")
        )

life_score    = get_life_score(row_data) if data_filled else 0
dopamine_score= get_dopamine_score(row_data) if data_filled else 100
cat_scores    = {cat: get_category_score(row_data, cat) or 0 for cat in CATEGORY_WEIGHTS}

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: DAILY DASHBOARD
# ═════════════════════════════════════════════════════════════════════════════
if nav == "🏠 Daily Dashboard":

    # Hero Banner
    day_of_year = selected_date.timetuple().tm_yday
    days_left   = 365 - day_of_year
    st.markdown(f"""
    <div class="hero-banner">
        <div class="hero-title">⚡ KV Life OS — Command Center</div>
        <div class="hero-subtitle">Daily Execution Report · {selected_date.strftime('%b-%d-%Y')}</div>
        <div class="hero-quote">"{random.choice(MOTIVATIONAL_QUOTES)}"</div>
        <div style="margin-top:14px; display:flex; gap:24px; font-size:15px; color:#9090BB;">
            <span>📅 Day <b style="color:#FFD166;">{day_of_year}</b> of 365</span>
            <span>⏳ <b style="color:#6C63FF;">{days_left}</b> days remaining in {selected_date.year}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if not data_available:
        st.markdown("""
        <div style="text-align:center; padding:40px; color:#9090BB;">
            <div style="font-size:48px; margin-bottom:12px;">📋</div>
            <div style="font-size:22px; font-weight:600; color:#F0F0FF;">No data for this date.</div>
            <div style="font-size:16px; margin-top:8px;">
                Open <b>KV_Daily_Checklist_OS_1.xlsx</b>, fill in the Tasks sheet for this date, then click <b>🔄 Reload Data</b>.
            </div>
        </div>
        """, unsafe_allow_html=True)
    elif not data_filled:
        st.markdown("""
        <div style="border:1px solid rgba(245,158,11,0.4); border-radius:12px; padding:18px 22px;
             background:rgba(245,158,11,0.06); margin-bottom:16px;">
            <div style="font-size:18px; font-weight:700; color:#F59E0B; margin-bottom:6px;">⚠️ Row found but no habits filled yet for this date</div>
            <div style="font-size:15px; color:#C0A050;">
                Open <b>KV_Daily_Checklist_OS_1.xlsx</b> → Tasks sheet → find today's row → fill your Yes/No habits → save → click <b>🔄 Reload Data</b>.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # ── Top Metric Cards ──────────────────────────────────────────────────
        m1, m2, m3, m4 = st.columns(4)

        with m1:
            sc = score_color(life_score)
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">🏆 Daily Life Score</div>
                <div class="metric-value {sc}">{life_score:.0f}<span style="font-size:20px; color:var(--text2);">/100</span></div>
                <div class="metric-delta">{"🔥 Excellent!" if life_score>=80 else "📈 Keep pushing!" if life_score>=55 else "⚠️ Below target"}</div>
            </div>
            """, unsafe_allow_html=True)

        with m2:
            dc = score_color(dopamine_score)
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">🧠 Dopamine Control</div>
                <div class="metric-value {dc}">{dopamine_score}<span style="font-size:20px; color:var(--text2);">/100</span></div>
                <div class="metric-delta">{"✅ Clean mind!" if dopamine_score==100 else "⚠️ Distractions detected"}</div>
            </div>
            """, unsafe_allow_html=True)

        with m3:
            total_tasks = sum(1 for t, cat, itype in TASKS if itype == "YesNo" and t not in NEGATIVE_HABIT_TASKS)
            done_tasks  = sum(1 for t, cat, itype in TASKS if itype == "YesNo" and t not in NEGATIVE_HABIT_TASKS and row_data.get(t) == "Yes")
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">✅ Tasks Completed</div>
                <div class="metric-value blue">{done_tasks}<span style="font-size:20px; color:var(--text2);">/{total_tasks}</span></div>
                <div class="metric-delta">{round(done_tasks/total_tasks*100) if total_tasks else 0}% completion rate</div>
            </div>
            """, unsafe_allow_html=True)

        with m4:
            feel = safe_val(row_data.get("How Do You Feel Today"), "Not logged")
            feel_emoji = {"EXCELLENT": "🌟", "GREAT": "😄", "GOOD": "😊", "OK": "😐", "HECTIC": "😤", "ANXIOUS": "😰", "VERY BAD": "😞"}.get(feel, "—")
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">💭 How You Feel</div>
                <div class="metric-value" style="font-size:22px;">{feel_emoji} {feel}</div>
                <div class="metric-delta">Logged today</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Category Progress Bars ────────────────────────────────────────────
        st.markdown('<div class="section-header">📊 Life Dimension Scores</div>', unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        cats = list(CATEGORY_WEIGHTS.keys())
        for i, cat in enumerate(cats):
            sc = cat_scores[cat]
            color = CAT_COLORS.get(cat, "#6C63FF")
            with (col_a if i % 2 == 0 else col_b):
                emoji = CATEGORY_EMOJIS.get(cat, "")
                st.markdown(make_progress_bar(f"{emoji} {cat}", sc, 100, color), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Habit Status Grid ─────────────────────────────────────────────────
        st.markdown('<div class="section-header">🎯 Today\'s Habit Execution</div>', unsafe_allow_html=True)

        for cat in ["Body", "Mind", "Career", "Wealth", "Focus", "Relationships"]:
            cat_tasks = [(t, itype) for t, c, itype in TASKS if c == cat and itype in ("YesNo", "NegYesNo")]
            if not cat_tasks:
                continue

            emoji = CATEGORY_EMOJIS.get(cat, "")
            chips = ""
            for t, itype in cat_tasks:
                val = row_data.get(t, "")
                is_negative = itype == "NegYesNo"
                if val == "Yes":
                    chip_cls = "chip-no" if is_negative else "chip-yes"
                    symbol   = "✗" if is_negative else "✓"
                elif val == "No":
                    chip_cls = "chip-yes" if is_negative else "chip-no"
                    symbol   = "✓" if is_negative else "✗"
                else:
                    chip_cls, symbol = "chip-skip", "·"
                chips += f'<span class="habit-chip {chip_cls}">{symbol} {t}</span>'

            color = CAT_COLORS.get(cat, "#6C63FF")
            st.markdown(f"""
            <div style="margin-bottom:12px;">
                <div style="font-size:15px; font-weight:700; color:{color}; text-transform:uppercase;
                     letter-spacing:1.5px; margin-bottom:6px;">{emoji} {cat}</div>
                <div>{chips}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── Gratitude & Reflection ────────────────────────────────────────────
        g1     = safe_val(row_data.get("Gratitude 1"), "")
        g2     = safe_val(row_data.get("Gratitude 2"), "")
        g3     = safe_val(row_data.get("Gratitude 3"), "")
        lesson = safe_val(row_data.get("Lesson Learned Today"), "")

        if any([g1, g2, g3, lesson]):
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="section-header">🪞 Today\'s Reflection</div>', unsafe_allow_html=True)
            rc1, rc2 = st.columns(2)
            with rc1:
                grats = [g for g in [g1, g2, g3] if g]
                if grats:
                    items = "".join([f"<div style='padding:5px 0; font-size:15px;'>🙏 {g}</div>" for g in grats])
                    st.markdown(f"""
                    <div class="ideal-section">
                        <div class="ideal-heading">Gratitude</div>
                        {items}
                    </div>""", unsafe_allow_html=True)
            with rc2:
                if lesson:
                    st.markdown(f"""
                    <div class="ideal-section">
                        <div class="ideal-heading">Lesson Learned</div>
                        <div style="font-size:15px; color:#F0F0FF;">{lesson}</div>
                    </div>""", unsafe_allow_html=True)

        # ── Raw Data Debug View ───────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("🔍 Debug — What the dashboard read from Excel for this date"):
            debug_rows = []
            for t, cat, itype in TASKS:
                raw = row_data.get(t)
                display = safe_val(raw, "(empty)")
                debug_rows.append({"Category": cat, "Task": t, "Type": itype, "Value Read": display})
            st.dataframe(pd.DataFrame(debug_rows), use_container_width=True)
            st.caption(f"Excel file: {OUTFILE_HORIZONTAL} | Date row found: {data_available} | Habits filled: {data_filled}")

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: LIFE SCORE
# ═════════════════════════════════════════════════════════════════════════════
elif nav == "📊 Life Score":
    st.markdown('<div class="section-header">📊 Life Score System — 6 Dimensions</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="quote-box">
        "You do not rise to the level of your goals. You fall to the level of your <b>systems</b>."
        This score is your system's health check.
    </div>
    """, unsafe_allow_html=True)

    if not data_available:
        st.info("No data available for the selected date. Fill in your Excel sheet first.")
    else:
        # Big life score display
        sc_class = score_color(life_score)
        gr_color = "#10B981" if life_score >= 80 else "#F59E0B" if life_score >= 55 else "#EF4444"
        st.markdown(f"""
        <div style="text-align:center; padding:32px 0 20px 0;">
            <div style="font-size:16px; color:#9090BB; text-transform:uppercase; letter-spacing:2px; margin-bottom:8px;">Overall Life Score</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:110px; font-weight:800; color:{gr_color}; line-height:1;">{life_score:.0f}</div>
            <div style="font-size:22px; color:#9090BB;">/100</div>
            <div style="margin-top:12px; font-size:18px; color:{gr_color}; font-weight:600;">
                {"🏆 ELITE — You are ahead of 95% of people" if life_score>=80 else "📈 PROGRESSING — Keep the momentum" if life_score>=55 else "⚠️ BELOW PAR — Time to level up"}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Radar Chart — vivid, highly visible version
        cats  = list(cat_scores.keys())
        vals  = list(cat_scores.values())
        vals_closed = vals + [vals[0]]
        cats_closed = cats + [cats[0]]
        emoji_cats  = [f"{CATEGORY_EMOJIS.get(c,'')} {c}" for c in cats] + [f"{CATEGORY_EMOJIS.get(cats[0],'')} {cats[0]}"]

        fig_radar = go.Figure()

        # Target ring — bright dashed
        fig_radar.add_trace(go.Scatterpolar(
            r=[80]*len(emoji_cats), theta=emoji_cats,
            mode='lines',
            line=dict(color='#FFD166', width=2, dash='dot'),
            name="🎯 Target (80)",
            hovertemplate='<b>%{theta}</b><br>Target: <b>80%</b><extra></extra>',
        ))
        # Score fill — vivid gradient effect using two layers
        fig_radar.add_trace(go.Scatterpolar(
            r=vals_closed, theta=emoji_cats,
            fill='toself',
            fillcolor='rgba(108,99,255,0.30)',
            line=dict(color='#00D4AA', width=3),
            name="📊 Your Score",
            hovertemplate='<b>%{theta}</b><br>Score: <b>%{r:.0f}%</b><extra></extra>',
            marker=dict(size=8, color='#00D4AA',
                        line=dict(color='#ffffff', width=2)),
        ))

        fig_radar.update_layout(
            paper_bgcolor='rgba(10,10,30,0.95)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Inter', color='#F0F0FF', size=13),
            margin=dict(l=60, r=60, t=60, b=40),
            polar=dict(
                bgcolor='rgba(15,15,45,0.8)',
                radialaxis=dict(
                    visible=True, range=[0, 100],
                    gridcolor='rgba(255,255,255,0.12)',
                    linecolor='rgba(255,255,255,0.15)',
                    tickfont=dict(color='#C0C0E0', size=14),
                    tickvals=[20,40,60,80,100],
                    ticktext=['20','40','60','80','100'],
                ),
                angularaxis=dict(
                    gridcolor='rgba(255,255,255,0.10)',
                    linecolor='rgba(255,255,255,0.15)',
                    tickfont=dict(color='#FFFFFF', size=16, family='Inter'),
                )
            ),
            showlegend=True,
            legend=dict(
                font=dict(color='#E0E0FF', size=14),
                bgcolor='rgba(20,20,50,0.8)',
                bordercolor='rgba(108,99,255,0.3)',
                borderwidth=1,
                x=1.05, y=1,
            ),
            height=480,
            title=dict(
                text="Life Score Radar — Today",
                font=dict(color='#FFFFFF', size=19),
                x=0.5, xanchor='center',
            ),
            hoverlabel=dict(
                bgcolor="rgba(20,20,30,0.95)",
                font_size=18,
                font_family="Inter",
                font_color="white"
            ),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        # Dimension breakdown cards
        st.markdown('<div class="section-header">Dimension Breakdown</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        for i, (cat, sc) in enumerate(cat_scores.items()):
            emoji = CATEGORY_EMOJIS.get(cat, "")
            color = CAT_COLORS.get(cat, "#6C63FF")
            sc_c  = score_color(sc)
            with [c1, c2, c3][i % 3]:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">{emoji} {cat.upper()}</div>
                    <div class="metric-value {sc_c}">{sc:.0f}<span style="font-size:18px; color:var(--text2);">%</span></div>
                    <div class="metric-delta">Weight: {CATEGORY_WEIGHTS.get(cat, 0)*100:.0f}% of Life Score</div>
                </div>
                """, unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: WEEKLY REVIEW
# ═════════════════════════════════════════════════════════════════════════════
elif nav == "📅 Weekly Review":
    st.markdown('<div class="section-header">📅 Weekly Performance Review</div>', unsafe_allow_html=True)

    if df.empty:
        st.info("No data available yet.")
    else:
        # Get last 7 days
        end_date   = selected_date
        start_date = end_date - datetime.timedelta(days=6)
        week_df    = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)].copy()

        if week_df.empty:
            st.info("No data available for the past 7 days.")
        else:
            week_df["Life Score"] = week_df.apply(
                lambda r: get_life_score(r.to_dict()), axis=1
            )
            week_df["Dopamine Score"] = week_df.apply(
                lambda r: get_dopamine_score(r.to_dict()), axis=1
            )

            # Weekly summary metrics
            avg_life    = week_df["Life Score"].mean()
            avg_dopa    = week_df["Dopamine Score"].mean()
            best_day    = week_df.loc[week_df["Life Score"].idxmax(), "Date"] if not week_df.empty else "—"
            days_filled = len(week_df)

            wm1, wm2, wm3, wm4 = st.columns(4)
            wm1.markdown(f'<div class="metric-card"><div class="metric-label">📈 Avg Life Score</div><div class="metric-value {score_color(avg_life)}">{avg_life:.0f}</div><div class="metric-delta">7-day average</div></div>', unsafe_allow_html=True)
            wm2.markdown(f'<div class="metric-card"><div class="metric-label">🧠 Avg Dopamine</div><div class="metric-value {score_color(avg_dopa)}">{avg_dopa:.0f}</div><div class="metric-delta">7-day average</div></div>', unsafe_allow_html=True)
            wm3.markdown(f'<div class="metric-card"><div class="metric-label">🏆 Best Day</div><div class="metric-value blue" style="font-size:24px;">{best_day}</div><div class="metric-delta">Highest score</div></div>', unsafe_allow_html=True)
            wm4.markdown(f'<div class="metric-card"><div class="metric-label">📋 Days Logged</div><div class="metric-value gold">{days_filled}<span style="font-size:20px; color:var(--text2);">/7</span></div><div class="metric-delta">Data availability</div></div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Line charts
            week_df["Date_str"] = week_df["Date"].astype(str)
            fig_line = go.Figure()
            fig_line.add_trace(go.Scatter(
                x=week_df["Date_str"], y=week_df["Life Score"],
                name="Life Score", mode="lines+markers",
                line=dict(color="#6C63FF", width=3),
                marker=dict(size=8, color="#6C63FF"),
                fill='tozeroy', fillcolor='rgba(108,99,255,0.08)',
                hovertemplate='<b>%{x}</b><br>Life Score: <b>%{y:.0f}%</b><extra></extra>',
            ))
            fig_line.add_trace(go.Scatter(
                x=week_df["Date_str"], y=week_df["Dopamine Score"],
                name="Dopamine Control", mode="lines+markers",
                line=dict(color="#00D4AA", width=2, dash='dot'),
                marker=dict(size=7, color="#00D4AA"),
                hovertemplate='<b>%{x}</b><br>Dopamine: <b>%{y:.0f}</b><extra></extra>',
            ))
            fig_line.add_hline(y=80, line_dash="dash", line_color="rgba(245,158,11,0.4)",
                               annotation_text="Target: 80", annotation_font_color="#F59E0B")
            fig_line.update_layout(**plotly_dark_layout(),
                height=320,
                xaxis=dict(gridcolor='rgba(255,255,255,0.04)', tickfont=dict(color='#9090BB')),
                yaxis=dict(range=[0, 105], gridcolor='rgba(255,255,255,0.04)', tickfont=dict(color='#9090BB')),
                showlegend=True,
                legend=dict(font=dict(color='#9090BB'), bgcolor='rgba(0,0,0,0)'),
                title=dict(text="7-Day Life Score Trend", font=dict(color="#F0F0FF", size=17)),
            )
            st.plotly_chart(fig_line, use_container_width=True)

            # Category bar chart for the week
            cat_avgs = {}
            for cat in CATEGORY_WEIGHTS:
                scores = week_df.apply(lambda r: get_category_score(r.to_dict(), cat) or 0, axis=1)
                cat_avgs[cat] = scores.mean()

            fig_bar = go.Figure(go.Bar(
                x=list(cat_avgs.keys()),
                y=list(cat_avgs.values()),
                marker_color=[CAT_COLORS.get(c, "#6C63FF") for c in cat_avgs],
                text=[f"{v:.0f}%" for v in cat_avgs.values()],
                textposition='outside',
                textfont=dict(color='#F0F0FF', size=14),
                hovertemplate='<b>%{x}</b><br>Average: <b>%{y:.0f}%</b><extra></extra>',
            ))
            fig_bar.add_hline(y=80, line_dash="dash", line_color="rgba(245,158,11,0.4)")
            fig_bar.update_layout(**plotly_dark_layout(),
                height=300,
                xaxis=dict(tickfont=dict(color='#9090BB'), gridcolor='rgba(0,0,0,0)'),
                yaxis=dict(range=[0, 115], gridcolor='rgba(255,255,255,0.04)', tickfont=dict(color='#9090BB')),
                title=dict(text="Weekly Category Performance", font=dict(color="#F0F0FF", size=17)),
                showlegend=False,
            )
            st.plotly_chart(fig_bar, use_container_width=True)

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: GOAL PROGRESS (OKRs)
# ═════════════════════════════════════════════════════════════════════════════
elif nav == "🎯 Goal Progress":
    st.markdown('<div class="section-header">🎯 OKR Goal Tracker — 2026</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="quote-box">
        Update <b>Current Progress</b> in the Excel OKR Tracker sheet. This page displays your static goal framework.
        Review your OKRs every Sunday. Goals without review are just wishes.
    </div>
    """, unsafe_allow_html=True)

    # Group OKRs by objective
    okr_groups = {}
    for obj, kr, target, curr, deadline, status, notes in OKRS:
        if obj not in okr_groups:
            okr_groups[obj] = []
        okr_groups[obj].append((kr, target, curr, deadline, status, notes))

    for obj, krs in okr_groups.items():
        # Objective header
        obj_pct = sum(c/t for _, t, c, *_ in krs if t > 0) / len(krs) * 100 if krs else 0
        badge_cl= "badge-green" if obj_pct>=70 else "badge-gold" if obj_pct>=30 else "badge-grey"
        st.markdown(f"""
        <div style="margin: 20px 0 6px 0;">
            <span style="font-family:'Space Grotesk',sans-serif; font-size:19px; font-weight:700; color:#F0F0FF;">
                🎯 {obj}
            </span>
            <span class="badge {badge_cl}" style="margin-left:12px;">{obj_pct:.0f}% overall</span>
        </div>
        """, unsafe_allow_html=True)

        for kr, target, curr, deadline, status, notes in krs:
            pct = int(curr / target * 100) if target > 0 else 0
            pct = min(pct, 100)
            bar_color = "#10B981" if pct >= 70 else "#F59E0B" if pct >= 30 else "#EF4444"
            status_badge = {
                "Not Started": "badge-grey", "On Track": "badge-green",
                "At Risk": "badge-red", "Completed": "badge-blue"
            }.get(status, "badge-grey")

            st.markdown(f"""
            <div class="okr-card">
                <div class="okr-kr">📌 {kr}</div>
                <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                    <span style="font-size:14px; color:#9090BB;">Progress: {curr} / {target}</span>
                    <span class="badge {status_badge}">{status}</span>
                </div>
                <div style="background:rgba(255,255,255,0.06); border-radius:50px; height:6px; overflow:hidden;">
                    <div style="width:{pct}%; height:100%; border-radius:50px; background:{bar_color};"></div>
                </div>
                <div class="okr-meta">
                    <span>📅 Deadline: {deadline}</span>
                    <span>✅ {pct}% complete</span>
                    {"<span>💡 " + notes[:60] + ("..." if len(notes)>60 else "") + "</span>" if notes else ""}
                </div>
            </div>
            """, unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: HABIT ANALYTICS
# ═════════════════════════════════════════════════════════════════════════════
elif nav == "📈 Habit Analytics":
    st.markdown('<div class="section-header">📈 Habit Analytics — All Time</div>', unsafe_allow_html=True)

    if df.empty:
        st.info("No data yet.")
    else:
        # Overall completion rates for all YesNo habits
        habit_rates = []
        for t, cat, itype in TASKS:
            if itype == "YesNo" and t in df.columns:
                total_filled = df[t].isin(["Yes", "No"]).sum()
                if total_filled > 0:
                    yes_rate = (df[t] == "Yes").sum() / total_filled * 100
                    habit_rates.append({
                        "Habit": t, "Category": cat,
                        "Completion %": round(yes_rate, 1),
                        "Days Logged": int(total_filled)
                    })

        if habit_rates:
            hr_df = pd.DataFrame(habit_rates).sort_values("Completion %", ascending=False)

            # Top habits chart
            fig_h = px.bar(
                hr_df.head(20), x="Completion %", y="Habit",
                orientation='h',
                color="Completion %",
                color_continuous_scale=[[0, "#EF4444"], [0.5, "#F59E0B"], [1, "#10B981"]],
                text="Completion %",
            )
            fig_h.update_traces(texttemplate="%{text:.0f}%", textposition="outside",
                                textfont=dict(color="#F0F0FF", size=13))
            fig_h.update_layout(**plotly_dark_layout(),
                height=500,
                xaxis=dict(range=[0, 115], gridcolor='rgba(255,255,255,0.04)', tickfont=dict(color='#9090BB')),
                yaxis=dict(gridcolor='rgba(0,0,0,0)', tickfont=dict(color='#F0F0FF', size=13)),
                coloraxis_showscale=False,
                showlegend=False,
                title=dict(text="Habit Completion Rates (All Time)", font=dict(color="#F0F0FF", size=18)),
            )
            st.plotly_chart(fig_h, use_container_width=True)

            # Category summary
            cat_summary = hr_df.groupby("Category")["Completion %"].mean().reset_index()
            cat_summary.columns = ["Category", "Avg Completion %"]
            fig_cat = px.pie(
                cat_summary, values="Avg Completion %", names="Category",
                color="Category",
                color_discrete_map=CAT_COLORS,
                hole=0.5,
            )
            fig_cat.update_layout(**plotly_dark_layout(),
                height=350,
                title=dict(text="Category Completion Balance", font=dict(color="#F0F0FF", size=18)),
                legend=dict(font=dict(color='#9090BB'), bgcolor='rgba(0,0,0,0)'),
            )
            fig_cat.update_traces(textfont=dict(color="#F0F0FF"), textinfo='percent+label')
            st.plotly_chart(fig_cat, use_container_width=True)

            # Raw table
            with st.expander("📋 Full Habit Completion Table"):
                st.dataframe(
                    hr_df.style.background_gradient(subset=["Completion %"], cmap="RdYlGn"),
                    use_container_width=True
                )

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: REFLECTION
# ═════════════════════════════════════════════════════════════════════════════
elif nav == "🪞 Reflection":
    st.markdown('<div class="section-header">🪞 Daily Reflection Journal</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="quote-box">
        "An unexamined life is not worth living." — Socrates<br>
        This section shows your logged reflections. Fill the corresponding columns in your Excel sheet daily.
    </div>
    """, unsafe_allow_html=True)

    if not data_available:
        st.info("No data for this date. Log your reflections in the Excel Tasks sheet.")
    else:
        r1, r2 = st.columns(2)
        with r1:
            feel = row_data.get("How Do You Feel Today", "—")
            feel_emoji = {"EXCELLENT": "🌟", "GREAT": "😄", "GOOD": "😊", "OK": "😐", "HECTIC": "😤", "ANXIOUS": "😰", "VERY BAD": "😞"}.get(str(feel), "❓")
            st.markdown(f"""
            <div class="ideal-section">
                <div class="ideal-heading">Today's Feeling</div>
                <div style="font-size:28px;">{feel_emoji} {feel}</div>
            </div>
            """, unsafe_allow_html=True)

            grats = [row_data.get(f"Gratitude {i}", "") for i in range(1, 4)]
            grat_items = "".join([f"<div class='ideal-item'>🙏 {g}</div>" for g in grats if g])
            if grat_items:
                st.markdown(f"""
                <div class="ideal-section" style="margin-top:12px;">
                    <div class="ideal-heading">Gratitude (3 Things)</div>
                    {grat_items}
                </div>
                """, unsafe_allow_html=True)

        with r2:
            lesson = row_data.get("Lesson Learned Today", "")
            improve = row_data.get("What Can I Improve Tomorrow", "")
            if lesson:
                st.markdown(f"""
                <div class="ideal-section">
                    <div class="ideal-heading">Lesson Learned</div>
                    <div style="font-size:13px; color:#F0F0FF;">{lesson}</div>
                </div>
                """, unsafe_allow_html=True)
            if improve:
                st.markdown(f"""
                <div class="ideal-section" style="margin-top:12px;">
                    <div class="ideal-heading">Tomorrow's Improvement</div>
                        <div style="font-size:15px; color:#F0F0FF;">{improve}</div>
                </div>
                """, unsafe_allow_html=True)

        comments = row_data.get("Any Comments / Notes", "")
        if comments and str(comments).strip():
            st.markdown(f"""
            <div class="ideal-section" style="margin-top:12px;">
                <div class="ideal-heading">Notes</div>
                <div style="font-size:15px; color:#F0F0FF;">{comments}</div>
            </div>
            """, unsafe_allow_html=True)

        # Reflection history
        if len(df) > 1:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.expander("📜 Reflection History (All Logged Days)"):
                ref_cols = ["Date", "How Do You Feel Today", "Gratitude 1", "Lesson Learned Today", "What Can I Improve Tomorrow"]
                ref_cols_available = [c for c in ref_cols if c in df.columns]
                ref_df = df[ref_cols_available].dropna(subset=["How Do You Feel Today"])
                st.dataframe(ref_df.sort_values("Date", ascending=False), use_container_width=True)

# ═════════════════════════════════════════════════════════════════════════════
# PAGE: IDEAL MAN CODE
# ═════════════════════════════════════════════════════════════════════════════
elif nav == "⚡ Ideal Man Code":
    st.markdown("""
    <div style="text-align:center; padding:24px 0 12px 0;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:36px; font-weight:800;
             background:linear-gradient(135deg,#6C63FF,#00D4AA,#FFD166);
             -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">
            ⚡ THE IDEAL MAN — KV's CODE OF CONDUCT
        </div>
        <div style="color:#9090BB; font-size:16px; margin-top:8px;">
            Read this every morning. Live it every day. Become it.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="quote-box" style="text-align:center; font-size:16px; font-weight:600;">
        "You do not rise to the level of your goals. You fall to the level of your systems."<br>
        <span style="font-size:15px; font-weight:400; color:#9090BB;">Build the system. Live the system. Become the result.</span>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns(2)
    items = list(IDEAL_MAN_CODE.items())
    for i, (section, lines) in enumerate(items):
        line_html = "".join([f'<div class="ideal-item">✓ {l}</div>' for l in lines])
        card_html  = f"""
        <div class="ideal-section">
            <div class="ideal-heading">{section}</div>
            {line_html}
        </div>
        """
        with (col_left if i % 2 == 0 else col_right):
            st.markdown(card_html, unsafe_allow_html=True)

    # Daily affirmations
    st.markdown("<br>", unsafe_allow_html=True)
    affirmations = [
        "⚡ I am building my best self — one day at a time.",
        "🔥 I embrace discomfort because that is where growth lives.",
        "🎯 My focus is my greatest asset. I protect it fiercely.",
        "💪 I am stronger today than I was yesterday.",
        "🚀 Every action I take today moves me towards the man I want to become.",
    ]
    st.markdown("""
    <div class="section-header">📣 Daily Affirmations</div>
    """, unsafe_allow_html=True)

    for a in affirmations:
        st.markdown(f"""
        <div style="padding:14px 18px; margin:6px 0;
             background:linear-gradient(90deg, rgba(108,99,255,0.08), rgba(0,212,170,0.04));
             border-left:3px solid #6C63FF; border-radius:0 10px 10px 0;
             font-size:16px; color:#F0F0FF; font-weight:500;">{a}</div>
        """, unsafe_allow_html=True)

    # Final mission statement
    st.markdown("""
    <div style="margin-top:28px; text-align:center; padding:28px;
         background:linear-gradient(135deg, #1a0a4a, #0a1a4a);
         border:1px solid rgba(108,99,255,0.25); border-radius:20px;">
        <div style="font-family:'Space Grotesk',sans-serif; font-size:24px; font-weight:800;
             color:#FFD166; margin-bottom:10px;">YOUR MISSION</div>
        <div style="font-size:18px; color:#F0F0FF; line-height:1.8; max-width:600px; margin:0 auto;">
            To become a disciplined, financially free, physically elite, mentally unbreakable man
            who executes his vision with relentless consistency — and inspires others by his example.
        </div>
        <div style="margin-top:16px; font-size:15px; color:#9090BB; font-style:italic;">
            One day or day one. You decide. Every single morning.
        </div>
    </div>
    """, unsafe_allow_html=True)
