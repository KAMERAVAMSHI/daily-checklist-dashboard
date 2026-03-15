import datetime

# File and Output
OUTFILE_HORIZONTAL = "KV_Daily_Checklist_OS_1.xlsx"

# Grid Configuration
DAYS_IN_YEAR = 365
START_DATE = datetime.date(datetime.date.today().year, 1, 1)

# Dashboard Text
DASHBOARD_TITLE = "🚀 KV LIFE OS — ANNUAL DASHBOARD"
DASHBOARD_SUBTITLE = "Discipline is the bridge between goals and accomplishment. This is your Annual Transformation Matrix."

# Google Sheets Integration
# If you are using Google Sheets, paste your full URL here (e.g., https://docs.google.com/spreadsheets/d/1o7SJw.../edit#gid=...)
# Make sure the sheet is set to "Anyone with the link can view".
GOOGLE_SHEETS_URL = "https://docs.google.com/spreadsheets/d/1o7SJW7DKQTBb7bcU1pDykpalUV3icbi9MwSr9BkZOgs/edit?gid=158675056#gid=158675056"
"""
Life OS — OKR Constants
The Master Goal System for an ambitious, success-driven man.
"""

# OKR Instructions
OKR_INSTRUCTIONS = [
    "YOUR LIFE OKR SYSTEM — HOW TO USE:",
    "1. 'Objective' is your big ambition for the year.",
    "2. 'Key Result' is the specific measurable outcome that proves you achieved it.",
    "3. Fill 'Current Progress' every week. The % auto-updates.",
    "4. Status: Not Started → On Track → At Risk → Completed",
    "Principle: You do not rise to the level of your goals. You fall to the level of your SYSTEMS.",
]

# ── The Master OKR Array ─────────────────────────────────────────────────────
# Format: (Objective, Key Result, Target, Current Progress, Deadline, Status, Notes)
OKRS = [

    # ════════════════════════════════════════════════════════════════
    # 1. CAREER — Become a Top Tech Professional
    # ════════════════════════════════════════════════════════════════
    (
        "Secure a ₹1.66L+/month data/tech role",
        "Apply to 15–20 quality jobs per week (total: 300+)",
        300, 0, "2026-12-31", "Not Started",
        "Volume + quality. If not hitting this, ₹1.66L is just a dream."
    ),
    (
        "Secure a ₹1.66L+/month data/tech role",
        "Get 10+ interview calls this year",
        10, 0, "2026-12-31", "Not Started",
        "Interviews = opportunities. Apply until the phone rings."
    ),
    (
        "Secure a ₹1.66L+/month data/tech role",
        "Build 3 strong portfolio projects (public GitHub + live demo)",
        3, 0, "2026-12-31", "Not Started",
        "Real projects > certificates. Show, don't tell."
    ),
    (
        "Secure a ₹1.66L+/month data/tech role",
        "Solve 200+ LeetCode problems (Easy + Medium + Hard)",
        200, 0, "2026-12-31", "Not Started",
        "DSA is the language of interviews. Master it."
    ),
    (
        "Secure a ₹1.66L+/month data/tech role",
        "Get 5+ LinkedIn referrals / warm connections",
        5, 0, "2026-12-31", "Not Started",
        "Your network is your net worth. Build it actively."
    ),

    # ════════════════════════════════════════════════════════════════
    # 2. BODY — Build a Powerful, Lean Physique
    # ════════════════════════════════════════════════════════════════
    (
        "Build a lean, strong, athletic body",
        "Gym 5–6 days per week (250+ sessions/year)",
        250, 0, "2026-12-31", "Not Started",
        "The real challenge is consistency — not a single workout."
    ),
    (
        "Build a lean, strong, athletic body",
        "Hit 120g+ protein daily for 300+ days",
        300, 0, "2026-12-31", "Not Started",
        "Protein is the bricks. Gym is the blueprint."
    ),
    (
        "Build a lean, strong, athletic body",
        "Achieve and maintain 12–15% body fat",
        15, 0, "2026-12-31", "Not Started",
        "Measure monthly. Abs are made in the kitchen."
    ),
    (
        "Build a lean, strong, athletic body",
        "Sleep 7+ hours, 300+ nights this year",
        300, 0, "2026-12-31", "Not Started",
        "Sleep is when your body rebuilds. Protect it."
    ),

    # ════════════════════════════════════════════════════════════════
    # 3. MIND — Become Mentally Unbreakable
    # ════════════════════════════════════════════════════════════════
    (
        "Build an unbreakable, disciplined mindset",
        "Meditate 10+ min daily for 300+ days",
        300, 0, "2026-12-31", "Not Started",
        "Meditation rewires your brain for calm and focus."
    ),
    (
        "Build an unbreakable, disciplined mindset",
        "Read 24+ books this year (2 per month)",
        24, 0, "2026-12-31", "Not Started",
        "Leaders are readers. Knowledge compounds like interest."
    ),
    (
        "Build an unbreakable, disciplined mindset",
        "Journal every morning for 300+ days",
        300, 0, "2026-12-31", "Not Started",
        "Clarity of thought precedes clarity of action."
    ),

    # ════════════════════════════════════════════════════════════════
    # 4. WEALTH — Build Financial Intelligence
    # ════════════════════════════════════════════════════════════════
    (
        "Build a strong financial foundation",
        "Track 100% of expenses every month (12 months)",
        12, 0, "2026-12-31", "Not Started",
        "What gets measured gets managed. Know where every rupee goes."
    ),
    (
        "Build a strong financial foundation",
        "Invest consistently every month (SIP + emergency fund)",
        12, 0, "2026-12-31", "Not Started",
        "Pay yourself first. Always."
    ),
    (
        "Build a strong financial foundation",
        "Create 1 additional income stream (freelance / project / content)",
        1, 0, "2026-12-31", "Not Started",
        "Don't rely on one source. Build alternatives."
    ),

    # ════════════════════════════════════════════════════════════════
    # 5. FOCUS — Eliminate Distractions, Own Your Attention
    # ════════════════════════════════════════════════════════════════
    (
        "Achieve master-level focus and discipline",
        "Zero Instagram days: 200+ this year",
        200, 0, "2026-12-31", "Not Started",
        "Instagram is designed to steal your attention. Reclaim it."
    ),
    (
        "Achieve master-level focus and discipline",
        "Complete 2+ hr deep work blocks: 250+ days",
        250, 0, "2026-12-31", "Not Started",
        "Deep work is the superpower of the 21st century."
    ),
]
"""
Life OS — Style Constants
All color tokens for Excel and Streamlit theming.
"""

# ── Core Dashboard (Excel) ────────────────────────────────────────────────────
COLOR_DASHBOARD_BG   = "#1a1a2e"
COLOR_DASHBOARD_TEXT = "white"
COLOR_SCORE_BG       = "#1F618D"
COLOR_CHART_LINE     = "#1F618D"

# ── Category Header Colors (Excel - Pastel) ───────────────────────────────────
COLOR_CAT_BODY          = "#A9CCE3"   # Blue
COLOR_CAT_MIND          = "#D7BDE2"   # Purple
COLOR_CAT_CAREER        = "#F9E79F"   # Yellow
COLOR_CAT_WEALTH        = "#A3E4D7"   # Teal
COLOR_CAT_FOCUS         = "#FAD7A0"   # Orange
COLOR_CAT_RELATIONSHIPS = "#F9B8C3"   # Pink
COLOR_CAT_ENTERTAINMENT = "#F5B7B1"   # Soft Red
COLOR_CAT_OTHER         = "#D5DBDB"   # Grey

# ── Conditional Colors (Pastel Meaningful Shading) ────────────────────────────
COLOR_GOOD_BG   = "#C6EFCE"
COLOR_GOOD_TEXT = "#006100"

COLOR_BAD_BG    = "#FFC7CE"
COLOR_BAD_TEXT  = "#9C0006"

COLOR_WARN_BG   = "#FFEB9C"
COLOR_WARN_TEXT = "#9C6500"

# Stronger Alerts (Addiction / Special Wins)
COLOR_STRONG_RED_BG    = "#FADBD8"
COLOR_STRONG_RED_TEXT  = "#B71C1C"

COLOR_STRONG_GREEN_BG  = "#C8E6C9"
COLOR_STRONG_GREEN_TEXT= "#1B5E20"

# ── OKR Tracker Colors ────────────────────────────────────────────────────────
COLOR_OKR_CAREER_BG    = "#E3F2FD"
COLOR_OKR_CAREER_TEXT  = "#0D47A1"
COLOR_OKR_CAREER_BORDER= "#BBDEFB"

COLOR_OKR_FITNESS_BG   = "#E0F2F1"
COLOR_OKR_FITNESS_TEXT = "#004D40"
COLOR_OKR_FITNESS_BORDER="#B2DFDB"

COLOR_OKR_ROW_BG       = "#FAFAFA"
COLOR_OKR_ROW_BORDER   = "#EEEEEE"

# ── OKR Status Badges ─────────────────────────────────────────────────────────
COLOR_STATUS_NOT_STARTED_BG  = "#F2F3F4"
COLOR_STATUS_NOT_STARTED_TEXT= "#5D6D7E"

COLOR_STATUS_ON_TRACK_BG     = "#EBF5FB"
COLOR_STATUS_ON_TRACK_TEXT   = "#154360"

COLOR_STATUS_AT_RISK_BG      = "#FDEDEC"
COLOR_STATUS_AT_RISK_TEXT    = "#78281F"

COLOR_STATUS_COMPLETED_BG    = "#E9F7EF"
COLOR_STATUS_COMPLETED_TEXT  = "#145A32"

# ── 3-Color Scale for Progress % ─────────────────────────────────────────────
COLOR_SCALE_MIN = "#FADBD8"
COLOR_SCALE_MID = "#FCF3CF"
COLOR_SCALE_MAX = "#D5F5E3"

# ── Streamlit Dashboard Palette ───────────────────────────────────────────────
# These are used by dashboard.py for inline CSS / Plotly theming

ST_BG_DARK        = "#0a0a1a"
ST_BG_CARD        = "#12122a"
ST_BG_CARD2       = "#1a1a35"
ST_ACCENT_BLUE    = "#3B82F6"
ST_ACCENT_PURPLE  = "#8B5CF6"
ST_ACCENT_GREEN   = "#10B981"
ST_ACCENT_GOLD    = "#F59E0B"
ST_ACCENT_RED     = "#EF4444"
ST_ACCENT_CYAN    = "#06B6D4"
ST_ACCENT_PINK    = "#EC4899"
ST_TEXT_PRIMARY   = "#F1F5F9"
ST_TEXT_SECONDARY = "#94A3B8"
ST_BORDER         = "#1E2A3A"

# Category colors for Streamlit (vibrant)
ST_CAT_BODY          = "#3B82F6"  # Blue
ST_CAT_MIND          = "#8B5CF6"  # Purple
ST_CAT_CAREER        = "#F59E0B"  # Gold
ST_CAT_WEALTH        = "#10B981"  # Green
ST_CAT_FOCUS         = "#F97316"  # Orange
ST_CAT_RELATIONSHIPS = "#EC4899"  # Pink
"""
Life OS — Task Constants
All task definitions, categories, and dropdown options.
"""

# ── Dropdown Option Lists ────────────────────────────────────────────────────
WAKE_OPTIONS   = ["4:30-5:30 AM", "5:30-6:30 AM", "6:30-7:30 AM", "7:30-8:30 AM", "8:30-10 AM", "After 10 AM"]
CALORIE_OPTIONS = ["<1200 kcal", "1200-1500 kcal", "1500-1800 kcal", "1800-2200 kcal", "2200-2700 kcal", ">2700 kcal"]
WATER_OPTIONS  = ["<2L", "2L", "2.5L", "3L", "3.5L", "4L+"]
PROTEIN_OPTIONS = ["<50g", "50-80g", "80-100g", "100-120g", "120g+"]
FEEL_OPTIONS   = ["VERY BAD", "ANXIOUS", "HECTIC", "OK", "GOOD", "GREAT", "EXCELLENT"]
SLEEP_OPTIONS  = ["<5 hrs", "5-6 hrs", "6-7 hrs", "7-8 hrs", "8-9 hrs", ">9 hrs"]
DEEPWORK_OPTIONS = ["0 hrs", "0.5-1 hr", "1-2 hrs", "2-3 hrs", "3-4 hrs", "4+ hrs"]
STEPS_OPTIONS  = ["<3000", "3000-5000", "5000-8000", "8000-10000", "10000-12000", "12000+"]

# ── The Core Tasks Array ─────────────────────────────────────────────────────
# Format: (Task Name, Category, Input Type)
TASKS = [

    # ═══════════════════════════════════════════════════════════════
    # BODY — Physical Dominance & Health
    # ═══════════════════════════════════════════════════════════════
    ("Wake Up Time",                    "Body",         "WakeOpts"),
    ("Sleep Hours (prev night)",        "Body",         "SleepOpts"),
    ("Gym / Workout",                   "Body",         "YesNo"),
    ("Cardio / Steps",                  "Body",         "StepsOpts"),
    ("Cold Shower",                     "Body",         "YesNo"),
    ("Protein Intake",                  "Body",         "ProteinOpts"),
    ("Calorie Count",                   "Body",         "CalorieOpts"),
    ("Water Intake",                    "Body",         "WaterOpts"),
    ("No Junk Food",                    "Body",         "YesNo"),
    ("Protein Shake",                   "Body",         "YesNo"),
    ("Stretching / Mobility",           "Body",         "YesNo"),

    # ═══════════════════════════════════════════════════════════════
    # MIND — Mental Strength & Clarity
    # ═══════════════════════════════════════════════════════════════
    ("Meditation / Breathwork",         "Mind",         "YesNo"),
    ("Morning Journaling",              "Mind",         "YesNo"),
    ("Book Reading (20 min+)",          "Mind",         "YesNo"),
    ("Visualization (5 min)",           "Mind",         "YesNo"),
    ("Positive Affirmations",           "Mind",         "YesNo"),
    ("Avoided Negative Self-Talk",      "Mind",         "YesNo"),
    ("Evening Reflection",              "Mind",         "YesNo"),
    ("How Do You Feel Today",           "Mind",         "FeelOpts"),
    ("Gratitude 1",                     "Mind",         "Text"),
    ("Gratitude 2",                     "Mind",         "Text"),
    ("Gratitude 3",                     "Mind",         "Text"),
    ("Lesson Learned Today",            "Mind",         "Text"),
    ("What Can I Improve Tomorrow",     "Mind",         "Text"),
    ("Do You Feel Guilty Today",        "Mind",         "YesNo"),

    # ═══════════════════════════════════════════════════════════════
    # CAREER — Execution & Growth
    # ═══════════════════════════════════════════════════════════════
    ("Deep Work Block",                 "Career",       "DeepWorkOpts"),
    ("Applied Jobs Today",              "Career",       "YesNo"),
    ("LeetCode / DSA Problem",          "Career",       "YesNo"),
    ("Practiced Python / SQL",          "Career",       "YesNo"),
    ("Worked on Portfolio Project",     "Career",       "YesNo"),
    ("LinkedIn / Networking",           "Career",       "YesNo"),
    ("Researched Industry / Market",    "Career",       "YesNo"),
    ("Reviewed Goals / OKRs",           "Career",       "YesNo"),
    ("Learned New Technical Skill",     "Career",       "YesNo"),
    ("Coding Practice (1 hr+)",         "Career",       "YesNo"),

    # ═══════════════════════════════════════════════════════════════
    # WEALTH — Financial Intelligence
    # ═══════════════════════════════════════════════════════════════
    ("Tracked All Expenses",            "Wealth",       "YesNo"),
    ("Invested / SIP Done",             "Wealth",       "YesNo"),
    ("Read Finance / Business Content", "Wealth",       "YesNo"),
    ("Worked on Income Stream",         "Wealth",       "YesNo"),
    ("Studied Successful Person",       "Wealth",       "YesNo"),
    ("Avoided Impulse Spending",        "Wealth",       "YesNo"),
    ("Income Activity Today",           "Wealth",       "Text"),

    # ═══════════════════════════════════════════════════════════════
    # FOCUS — Discipline & Dopamine Control
    # ═══════════════════════════════════════════════════════════════
    ("No Instagram",                    "Focus",        "YesNo"),
    ("No YouTube Shorts",               "Focus",        "YesNo"),
    ("No Random Scrolling",             "Focus",        "YesNo"),
    ("No Procrastination Today",        "Focus",        "YesNo"),
    ("Phone-Free Morning (1 hr)",       "Focus",        "YesNo"),
    ("Done Top Priority Task First",    "Focus",        "YesNo"),
    ("Instagram Used (negative)",       "Focus",        "NegYesNo"),
    ("YouTube Shorts Used (negative)",  "Focus",        "NegYesNo"),

    # ═══════════════════════════════════════════════════════════════
    # RELATIONSHIPS — Connection & Communication
    # ═══════════════════════════════════════════════════════════════
    ("Talked with Priya",               "Relationships","YesNo"),
    ("Quality Time with Family",        "Relationships","YesNo"),
    ("Reached Out to a Friend",         "Relationships","YesNo"),
    ("Helped Someone Today",            "Relationships","YesNo"),
    ("Meaningful Conversation",         "Relationships","YesNo"),

    # ═══════════════════════════════════════════════════════════════
    # OTHER — Notes
    # ═══════════════════════════════════════════════════════════════
    ("Any Comments / Notes",            "Other",        "Text"),
]

# ── Negative habits (penalised in Dopamine score) ───────────────────────────
NEGATIVE_HABIT_TASKS = [
    "Instagram Used (negative)",
    "YouTube Shorts Used (negative)",
]

# ── Positive Focus tasks (not negative) ─────────────────────────────────────
POSITIVE_FOCUS_TASKS = [
    "No Instagram",
    "No YouTube Shorts",
    "No Random Scrolling",
    "No Procrastination Today",
    "Phone-Free Morning (1 hr)",
    "Done Top Priority Task First",
]

# ── Category Scoring Weights (for Life Score system) ────────────────────────
CATEGORY_WEIGHTS = {
    "Body":          0.20,   # 20% — physical health is the foundation
    "Mind":          0.20,   # 20% — mental strength and self-awareness
    "Career":        0.25,   # 25% — career builds wealth and identity
    "Wealth":        0.15,   # 15% — financial intelligence
    "Focus":         0.15,   # 15% — discipline and dopamine control
    "Relationships": 0.05,   # 5%  — connection
}

# ── Category Emojis ─────────────────────────────────────────────────────────
CATEGORY_EMOJIS = {
    "Body":          "💪",
    "Mind":          "🧘",
    "Career":        "🚀",
    "Wealth":        "💰",
    "Focus":         "🎯",
    "Relationships": "❤️",
    "Other":         "📝",
}

# ── Generate CATEGORIES_MAP automatically ───────────────────────────────────
def generate_categories_map(tasks_list):
    cat_map = {}
    for task_name, category, _ in tasks_list:
        if category not in cat_map:
            cat_map[category] = []
        cat_map[category].append(task_name)
    return cat_map

CATEGORIES_MAP = generate_categories_map(TASKS)

# ── YesNo-only tasks per category (for scoring) ─────────────────────────────
def get_yesno_tasks_by_category(tasks_list):
    result = {}
    for task_name, category, input_type in tasks_list:
        if input_type == "YesNo":
            if category not in result:
                result[category] = []
            result[category].append(task_name)
    return result

YESNO_TASKS_BY_CATEGORY = get_yesno_tasks_by_category(TASKS)
