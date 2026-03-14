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
