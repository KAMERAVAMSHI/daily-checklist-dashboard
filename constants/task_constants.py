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
