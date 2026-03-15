"""
KV Life OS — Daily Checklist Excel Generator
Horizontal Layout: 1 Row = 1 Day for 365 Days
Life Score System with 6 Dimensions.
"""

import datetime
import xlsxwriter

from app.const import (
    OUTFILE_HORIZONTAL, DAYS_IN_YEAR, START_DATE,
    DASHBOARD_TITLE, DASHBOARD_SUBTITLE,
    TASKS, WAKE_OPTIONS, CALORIE_OPTIONS, WATER_OPTIONS, PROTEIN_OPTIONS,
    FEEL_OPTIONS, SLEEP_OPTIONS, DEEPWORK_OPTIONS, STEPS_OPTIONS,
    NEGATIVE_HABIT_TASKS, CATEGORY_WEIGHTS,
    OKRS, OKR_INSTRUCTIONS
)
import app.const as styles

workbook = xlsxwriter.Workbook(OUTFILE_HORIZONTAL)

# ── Formats ────────────────────────────────────────────────────────────────────
bold        = workbook.add_format({"bold": True, "font_name": "Arial"})
datefmt     = workbook.add_format({"num_format": "mmm-dd-yyyy", "font_name": "Arial", "align": "center"})
center      = workbook.add_format({"align": "center", "font_name": "Arial"})
normal      = workbook.add_format({"font_name": "Arial"})
item_alt    = workbook.add_format({"font_name": "Arial", "bg_color": styles.COLOR_OKR_ROW_BG})

CATEGORIES = ["Date", "Body", "Mind", "Career", "Wealth", "Focus", "Relationships", "Other", "Score"]

# Header background colours based on Category
hdr_formats = {
    "Date":          workbook.add_format({"bold": True, "font_name": "Arial", "font_color": styles.COLOR_DASHBOARD_TEXT,  "bg_color": styles.COLOR_DASHBOARD_BG,        "border": 1, "align": "center", "valign": "vcenter"}),
    "Body":          workbook.add_format({"bold": True, "font_name": "Arial", "bg_color": styles.COLOR_CAT_BODY,          "border": 1, "align": "center", "valign": "vcenter", "text_wrap": True}),
    "Mind":          workbook.add_format({"bold": True, "font_name": "Arial", "bg_color": styles.COLOR_CAT_MIND,          "border": 1, "align": "center", "valign": "vcenter", "text_wrap": True}),
    "Career":        workbook.add_format({"bold": True, "font_name": "Arial", "bg_color": styles.COLOR_CAT_CAREER,        "border": 1, "align": "center", "valign": "vcenter", "text_wrap": True}),
    "Wealth":        workbook.add_format({"bold": True, "font_name": "Arial", "bg_color": styles.COLOR_CAT_WEALTH,        "border": 1, "align": "center", "valign": "vcenter", "text_wrap": True}),
    "Focus":         workbook.add_format({"bold": True, "font_name": "Arial", "bg_color": styles.COLOR_CAT_FOCUS,         "border": 1, "align": "center", "valign": "vcenter", "text_wrap": True}),
    "Relationships": workbook.add_format({"bold": True, "font_name": "Arial", "bg_color": styles.COLOR_CAT_RELATIONSHIPS, "border": 1, "align": "center", "valign": "vcenter", "text_wrap": True}),
    "Other":         workbook.add_format({"bold": True, "font_name": "Arial", "bg_color": styles.COLOR_CAT_OTHER,         "border": 1, "align": "center", "valign": "vcenter", "text_wrap": True}),
    "Score":         workbook.add_format({"bold": True, "font_name": "Arial", "font_color": styles.COLOR_DASHBOARD_TEXT,  "bg_color": styles.COLOR_SCORE_BG,            "border": 1, "align": "center", "valign": "vcenter", "text_wrap": True}),
}

# ── HIDDEN LISTS (For Dropdowns) ──────────────────────────────────────────────
hidden_ws = workbook.add_worksheet("hidden_lists")
hidden_ws.hide()

lists = [
    ("WakeOpts",     WAKE_OPTIONS,     0),
    ("CalorieOpts",  CALORIE_OPTIONS,  1),
    ("WaterOpts",    WATER_OPTIONS,    2),
    ("ProteinOpts",  PROTEIN_OPTIONS,  3),
    ("FeelOpts",     FEEL_OPTIONS,     4),
    ("SleepOpts",    SLEEP_OPTIONS,    5),
    ("DeepWorkOpts", DEEPWORK_OPTIONS, 6),
    ("StepsOpts",    STEPS_OPTIONS,    7),
]

for name, opts, col in lists:
    for i, opt in enumerate(opts):
        hidden_ws.write(i, col, opt)
    col_letter = chr(65 + col)
    workbook.define_name(name, f"hidden_lists!${col_letter}$1:${col_letter}${len(opts)}")

# ── TASKS SHEET (HORIZONTAL) ──────────────────────────────────────────────────
tasks_ws = workbook.add_worksheet("Tasks")
tasks_ws.freeze_panes(1, 1)

# 1. Write Headers (Row 0)
tasks_ws.write(0, 0, "Date", hdr_formats["Date"])
tasks_ws.set_column(0, 0, 14)

col_idx = 1
col_mapping = {}

for task_name, category, input_type in TASKS:
    tasks_ws.write(0, col_idx, task_name, hdr_formats.get(category, hdr_formats["Other"]))
    header_len = len(task_name)
    calculated_width = max(header_len + 4, 30) if input_type == "Text" else header_len + 4
    tasks_ws.set_column(col_idx, col_idx, calculated_width)
    col_mapping[task_name] = {
        'col':        col_idx,
        'category':   category,
        'input_type': input_type,
        'letter':     xlsxwriter.utility.xl_col_to_name(col_idx)
    }
    col_idx += 1

# Score columns
score_col = col_idx
tasks_ws.write(0, score_col, "Daily Life Score (0-100)", hdr_formats["Score"])
tasks_ws.set_column(score_col, score_col, 26)

dopa_col = col_idx + 1
tasks_ws.write(0, dopa_col, "Dopamine Control Score", hdr_formats["Score"])
tasks_ws.set_column(dopa_col, dopa_col, 26)

tasks_ws.set_row(0, 40)

# 2. Write 365 Days & Formulas (Rows 1 to 365)
for day in range(DAYS_IN_YEAR):
    row_idx = day + 1
    current_date = START_DATE + datetime.timedelta(days=day)

    # Write date
    tasks_ws.write_datetime(
        row_idx, 0,
        datetime.datetime.combine(current_date, datetime.time()),
        datefmt
    )

    # Empty cells for tasks
    for _, info in col_mapping.items():
        tasks_ws.write(row_idx, info['col'], "", center)

    # Daily Life Score — ratio of "Yes" per positive YesNo tasks (0-100)
    positive_yesno_cols = [
        info['letter'] for task, info in col_mapping.items()
        if info['input_type'] == "YesNo" and task not in NEGATIVE_HABIT_TASKS
    ]
    total_possible = len(positive_yesno_cols)
    if positive_yesno_cols and total_possible > 0:
        score_parts = [f'IF({c}{row_idx+1}="Yes",1,0)' for c in positive_yesno_cols]
        formula = f"=ROUND(({'+'.join(score_parts)})/{total_possible}*100,1)"
        tasks_ws.write_formula(row_idx, score_col, formula, center)

    # Dopamine Control Score: 100 - 15 per negative habit used
    neg_cols = [col_mapping[t]['letter'] for t in NEGATIVE_HABIT_TASKS if t in col_mapping]
    dopa_formula = "=100"
    for nc in neg_cols:
        dopa_formula += f'-IF({nc}{row_idx+1}="Yes",15,0)'
    tasks_ws.write_formula(row_idx, dopa_col, dopa_formula, center)

# 3. Apply Data Validation (Dropdowns)
for task, info in col_mapping.items():
    col       = info['col']
    itype     = info['input_type']

    if itype in ("YesNo", "NegYesNo"):
        tasks_ws.data_validation(1, col, DAYS_IN_YEAR, col, {
            'validate': 'list', 'source': ['Yes', 'No'], 'input_title': 'Status'
        })
    elif itype == "WakeOpts":
        tasks_ws.data_validation(1, col, DAYS_IN_YEAR, col, {'validate': 'list', 'source': WAKE_OPTIONS, 'ignore_blank': True})
    elif itype == "CalorieOpts":
        tasks_ws.data_validation(1, col, DAYS_IN_YEAR, col, {'validate': 'list', 'source': CALORIE_OPTIONS, 'ignore_blank': True})
    elif itype == "WaterOpts":
        tasks_ws.data_validation(1, col, DAYS_IN_YEAR, col, {'validate': 'list', 'source': WATER_OPTIONS, 'ignore_blank': True})
    elif itype == "ProteinOpts":
        tasks_ws.data_validation(1, col, DAYS_IN_YEAR, col, {'validate': 'list', 'source': PROTEIN_OPTIONS, 'ignore_blank': True})
    elif itype == "FeelOpts":
        tasks_ws.data_validation(1, col, DAYS_IN_YEAR, col, {'validate': 'list', 'source': FEEL_OPTIONS, 'ignore_blank': True})
    elif itype == "SleepOpts":
        tasks_ws.data_validation(1, col, DAYS_IN_YEAR, col, {'validate': 'list', 'source': SLEEP_OPTIONS, 'ignore_blank': True})
    elif itype == "DeepWorkOpts":
        tasks_ws.data_validation(1, col, DAYS_IN_YEAR, col, {'validate': 'list', 'source': DEEPWORK_OPTIONS, 'ignore_blank': True})
    elif itype == "StepsOpts":
        tasks_ws.data_validation(1, col, DAYS_IN_YEAR, col, {'validate': 'list', 'source': STEPS_OPTIONS, 'ignore_blank': True})

# 4. Apply Conditional Formatting
green_format       = workbook.add_format({'bg_color': styles.COLOR_GOOD_BG,        'font_color': styles.COLOR_GOOD_TEXT})
red_format         = workbook.add_format({'bg_color': styles.COLOR_BAD_BG,         'font_color': styles.COLOR_BAD_TEXT})
yellow_format      = workbook.add_format({'bg_color': styles.COLOR_WARN_BG,        'font_color': styles.COLOR_WARN_TEXT})
strong_red_format  = workbook.add_format({'bg_color': styles.COLOR_STRONG_RED_BG,  'font_color': styles.COLOR_STRONG_RED_TEXT})
strong_green_format= workbook.add_format({'bg_color': styles.COLOR_STRONG_GREEN_BG,'font_color': styles.COLOR_STRONG_GREEN_TEXT})

for task, info in col_mapping.items():
    col   = info['col']
    itype = info['input_type']

    if itype == "NegYesNo":
        # Negative habit: Yes = Strong Red, No = Strong Green
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"Yes"', 'format': strong_red_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"No"',  'format': green_format})

    elif itype == "YesNo":
        if task == "Do You Feel Guilty Today":
            tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"Yes"', 'format': strong_red_format})
            tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"No"',  'format': green_format})
        elif task in ("No Instagram", "No YouTube Shorts", "No Random Scrolling", "No Procrastination Today", "Phone-Free Morning (1 hr)"):
            # Discipline positive: Yes = strong green, No = strong red
            tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"Yes"', 'format': strong_green_format})
            tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"No"',  'format': strong_red_format})
        else:
            tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"Yes"', 'format': green_format})
            tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"No"',  'format': red_format})

    elif itype == "CalorieOpts":
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"<1200 kcal"',     'format': red_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"1200-1500 kcal"', 'format': yellow_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"1500-1800 kcal"', 'format': green_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"1800-2200 kcal"', 'format': green_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"2200-2700 kcal"', 'format': yellow_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '">2700 kcal"',     'format': red_format})

    elif itype == "WaterOpts":
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"<2L"', 'format': red_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"2L"',  'format': yellow_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"2.5L"','format': yellow_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"3L"',  'format': green_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"3.5L"','format': green_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"4L+"', 'format': strong_green_format})

    elif itype == "ProteinOpts":
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"<50g"',    'format': strong_red_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"50-80g"',  'format': red_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"80-100g"', 'format': yellow_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"100-120g"','format': green_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"120g+"',   'format': strong_green_format})

    elif itype == "FeelOpts":
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"VERY BAD"', 'format': strong_red_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"ANXIOUS"',  'format': strong_red_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"HECTIC"',   'format': red_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"OK"',       'format': yellow_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"GOOD"',     'format': green_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"GREAT"',    'format': strong_green_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"EXCELLENT"','format': strong_green_format})

    elif itype == "SleepOpts":
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"<5 hrs"',  'format': strong_red_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"5-6 hrs"', 'format': red_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"6-7 hrs"', 'format': yellow_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"7-8 hrs"', 'format': strong_green_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '"8-9 hrs"', 'format': green_format})
        tasks_ws.conditional_format(1, col, DAYS_IN_YEAR, col, {'type': 'cell', 'criteria': '==', 'value': '">9 hrs"',  'format': yellow_format})

# Score column colour scale
score_col_letter = xlsxwriter.utility.xl_col_to_name(score_col)
dopa_col_letter  = xlsxwriter.utility.xl_col_to_name(dopa_col)
tasks_ws.conditional_format(1, score_col, DAYS_IN_YEAR, score_col, {
    'type': '3_color_scale',
    'min_color': '#FF6B6B', 'min_type': 'num', 'min_value': 0,
    'mid_color': '#FFE066', 'mid_type': 'num', 'mid_value': 50,
    'max_color': '#51CF66', 'max_type': 'num', 'max_value': 100,
})
tasks_ws.conditional_format(1, dopa_col, DAYS_IN_YEAR, dopa_col, {
    'type': '3_color_scale',
    'min_color': '#FF6B6B', 'min_type': 'num', 'min_value': 70,
    'mid_color': '#FFE066', 'mid_type': 'num', 'mid_value': 85,
    'max_color': '#51CF66', 'max_type': 'num', 'max_value': 100,
})

# ── SUMMARY DASHBOARD ─────────────────────────────────────────────────────────
sum_ws = workbook.add_worksheet("Summary Dashboard")
sum_ws.set_column(0, 0, 36)
sum_ws.set_column(1, 3, 26)
sum_ws.set_column(4, 15, 14)

title_fmt = workbook.add_format({
    "bold": True, "font_name": "Arial", "font_size": 20,
    "font_color": styles.COLOR_DASHBOARD_TEXT, "bg_color": styles.COLOR_DASHBOARD_BG,
    "valign": "vcenter"
})
subtitle_fmt = workbook.add_format({
    "italic": True, "font_name": "Arial", "font_size": 11,
    "font_color": "#888888"
})
sum_ws.merge_range("A1:L2", f" {DASHBOARD_TITLE}", title_fmt)
sum_ws.write(3, 0, DASHBOARD_SUBTITLE, subtitle_fmt)

sum_ws.write(5, 0, "LIFE DIMENSION", bold)
sum_ws.write(4, 1, "Annual Done (Yes)", bold)
sum_ws.write(4, 2, "Annual Not Done (No)", bold)
sum_ws.write(4, 3, "Completion %", bold)

row_start = 6
scoring_categories = ["Body", "Mind", "Career", "Wealth", "Focus", "Relationships"]

for i, cat in enumerate(scoring_categories):
    r = row_start + i
    sum_ws.write(r, 0, cat, normal)

    cat_cols = [info['letter'] for task, info in col_mapping.items()
                if info['category'] == cat and info['input_type'] in ("YesNo",)]

    if cat_cols:
        yes_parts = [f'COUNTIF(Tasks!{c}$2:{c}${DAYS_IN_YEAR+1},"Yes")' for c in cat_cols]
        no_parts  = [f'COUNTIF(Tasks!{c}$2:{c}${DAYS_IN_YEAR+1},"No")'  for c in cat_cols]
        total_possible = len(cat_cols) * DAYS_IN_YEAR

        sum_ws.write_formula(r, 1, "=" + "+".join(yes_parts))
        sum_ws.write_formula(r, 2, "=" + "+".join(no_parts))
        sum_ws.write_formula(r, 3, f'=IFERROR(({"+".join(yes_parts)})/{total_possible},0)',
                             workbook.add_format({'num_format': '0%', 'align': 'center'}))
    else:
        sum_ws.write(r, 1, 0)
        sum_ws.write(r, 2, 0)
        sum_ws.write(r, 3, 0)

# Total section
tot_row = row_start + len(scoring_categories) + 1
sum_ws.write(tot_row, 0, "Total Daily Life Score Points (YTD)", bold)
sum_ws.write_formula(tot_row, 1, f'=SUM(Tasks!{score_col_letter}$2:{score_col_letter}${DAYS_IN_YEAR+1})')
sum_ws.write(tot_row, 3, "← Your cumulative life execution score.", normal)

sum_ws.write(tot_row + 1, 0, "Avg Daily Life Score (%)", bold)
sum_ws.write_formula(tot_row + 1, 1, f'=IFERROR(AVERAGE(Tasks!{score_col_letter}$2:{score_col_letter}${DAYS_IN_YEAR+1}),0)',
                     workbook.add_format({'num_format': '0.0', 'align': 'center'}))
sum_ws.write(tot_row + 1, 3, "← Target: 80+. Below 60 = below standard.", normal)

sum_ws.write(tot_row + 2, 0, "Avg Dopamine Control Score", bold)
sum_ws.write_formula(tot_row + 2, 1, f'=IFERROR(AVERAGE(Tasks!{dopa_col_letter}$2:{dopa_col_letter}${DAYS_IN_YEAR+1}),0)',
                     workbook.add_format({'num_format': '0.0', 'align': 'center'}))
sum_ws.write(tot_row + 2, 3, "← Target: 85+. Cheap dopamine kills focus.", normal)

# ── CHARTS ────────────────────────────────────────────────────────────────────
# 1. Line chart — Daily Life Score Trend
line_chart = workbook.add_chart({'type': 'line'})
line_chart.add_series({
    'name': 'Daily Life Score',
    'categories': f'=Tasks!$A$2:$A$31',
    'values': f'=Tasks!${score_col_letter}$2:${score_col_letter}$31',
    'line': {'color': styles.COLOR_CHART_LINE, 'width': 2.5}
})
line_chart.add_series({
    'name': 'Dopamine Control Score',
    'categories': f'=Tasks!$A$2:$A$31',
    'values': f'=Tasks!${dopa_col_letter}$2:${dopa_col_letter}$31',
    'line': {'color': '#E74C3C', 'width': 2}
})
line_chart.set_title({'name': 'First 30 Days — Life Score vs Dopamine Control'})
line_chart.set_x_axis({'name': 'Date'})
line_chart.set_y_axis({'name': 'Score (0–100)', 'major_gridlines': {'visible': True}, 'min': 0, 'max': 100})
line_chart.set_legend({'position': 'bottom'})
sum_ws.insert_chart('F5', line_chart, {'x_scale': 2.4, 'y_scale': 1.6})

# 2. Radar/Bar Chart for Category Completion %
bar_chart = workbook.add_chart({'type': 'bar'})
bar_chart.add_series({
    'name': 'Completion %',
    'categories': ['Summary Dashboard', row_start, 0, row_start + len(scoring_categories) - 1, 0],
    'values':     ['Summary Dashboard', row_start, 3, row_start + len(scoring_categories) - 1, 3],
    'fill': {'color': '#1F618D'}
})
bar_chart.set_title({'name': 'Life Dimension Completion Rate'})
bar_chart.set_x_axis({'name': 'Completion %'})
bar_chart.set_legend({'position': 'none'})
sum_ws.insert_chart(tot_row + 5, 0, bar_chart, {'x_scale': 2.0, 'y_scale': 1.4})


# ── IDEAL MAN SHEET ───────────────────────────────────────────────────────────
ideal_ws = workbook.add_worksheet("Ideal Man Code")

ideal_title_fmt = workbook.add_format({
    "bold": True, "font_name": "Arial", "font_size": 16,
    "font_color": "#FFFFFF", "bg_color": "#1a1a2e",
    "align": "center", "valign": "vcenter"
})
section_fmt = workbook.add_format({
    "bold": True, "font_name": "Arial", "font_size": 12,
    "font_color": "#1F618D", "bg_color": "#EBF5FB"
})
code_fmt = workbook.add_format({
    "font_name": "Arial", "font_size": 11,
    "font_color": "#2C3E50", "bg_color": "#FDFEFE",
    "left": 3, "left_color": "#1F618D"
})
quote_fmt = workbook.add_format({
    "italic": True, "font_name": "Arial", "font_size": 11,
    "font_color": "#7F8C8D", "bg_color": "#FAFAFA"
})

ideal_ws.set_column(0, 0, 5)
ideal_ws.set_column(1, 1, 80)
ideal_ws.merge_range("A1:B2", "⚡ THE IDEAL MAN — KV's DAILY CODE OF CONDUCT ⚡", ideal_title_fmt)
ideal_ws.set_row(0, 30)

IDEAL_MAN_CODE = [
    ("IDENTITY", [
        "I am a disciplined, focused, and relentless man who builds every day.",
        "I do not wait for motivation. I act from commitment.",
        "I am not who I was yesterday. I am becoming who I was meant to be.",
        "I take full ownership of my life — my results, my mind, my body.",
    ]),
    ("BODY", [
        "I wake up early every day. Early mornings belong to winners.",
        "I train my body like a warrior. Weakness has no home here.",
        "I eat to perform, not to comfort. My food is my fuel.",
        "I sleep 7+ hours every night. Recovery is part of the system.",
        "I take cold showers. Discomfort builds strength of character.",
    ]),
    ("MIND", [
        "I read every day. Knowledge is my compound interest.",
        "I journal every morning. Clarity precedes great decisions.",
        "I meditate. A calm mind outperforms an anxious one.",
        "I eliminate negative self-talk. My words shape my world.",
        "I visualize my goals every day. The mind leads the body.",
    ]),
    ("CAREER", [
        "I do deep work daily. Shallow work builds shallow results.",
        "I apply to jobs relentlessly. Persistence beats talent.",
        "I build projects that prove my skills. Actions > words.",
        "I learn something technical every single day.",
        "I review my OKRs weekly. Goals without reviews are wishes.",
    ]),
    ("WEALTH", [
        "I track every rupee spent. Financial awareness is financial power.",
        "I invest before I spend. Pay yourself first, always.",
        "I build income streams. One source of income is poverty.",
        "I study money, business, and markets daily.",
        "I avoid impulse purchases. Discipline in money is discipline in life.",
    ]),
    ("FOCUS & DISCIPLINE", [
        "I control my dopamine. Instagram and shorts steal my future.",
        "I do the hard thing first. The most important task gets my first hour.",
        "I keep my phone away in the morning. Mornings are sacred.",
        "I track my habits. What gets measured gets improved.",
        "I eliminate excuses. Discipline equals freedom.",
    ]),
    ("PHILOSOPHY", [
        "You do not rise to the level of your goals.",
        "You fall to the level of your systems.",
        "Success is not an event. It is a daily practice.",
        "Consistency beats motivation. Every single time.",
        "One day or day one. You decide.",
    ]),
]

row_cursor = 3
for section, lines in IDEAL_MAN_CODE:
    ideal_ws.write(row_cursor, 1, f"▶  {section}", section_fmt)
    ideal_ws.set_row(row_cursor, 22)
    row_cursor += 1
    for line in lines:
        ideal_ws.write(row_cursor, 1, f"  ✓  {line}", code_fmt)
        ideal_ws.set_row(row_cursor, 20)
        row_cursor += 1
    # Spacer
    ideal_ws.write(row_cursor, 1, "", normal)
    row_cursor += 1

# Final motivational quote
ideal_ws.merge_range(row_cursor, 0, row_cursor, 1,
    '"The man who moves a mountain begins by carrying away small stones." — Confucius', quote_fmt)
ideal_ws.set_row(row_cursor, 28)

# ── OKR TRACKER SHEET ─────────────────────────────────────────────────────────
okr_ws = workbook.add_worksheet("OKR Tracker")
okr_headers = ["Objective", "Key Result", "Target", "Current Progress", "Progress %", "Deadline", "Status", "Notes"]

for col, h in enumerate(okr_headers):
    okr_ws.write(0, col, h, hdr_formats["Date"])

okr_ws.set_column(0, 0, 50)
okr_ws.set_column(1, 1, 60)
okr_ws.set_column(2, 6, 18)
okr_ws.set_column(7, 7, 55)
okr_ws.set_row(0, 25)

for r, line in enumerate(OKR_INSTRUCTIONS, start=len(OKRS) + 3):
    okr_ws.write(r, 0, line, normal if r > len(OKRS) + 3 else bold)

# OKR category format map
okr_obj_formats = {
    "career": workbook.add_format({"bold": True, "font_name": "Arial", "font_color": styles.COLOR_OKR_CAREER_TEXT, "bg_color": styles.COLOR_OKR_CAREER_BG, "text_wrap": True, "valign": "vcenter", "border": 1, "border_color": styles.COLOR_OKR_CAREER_BORDER}),
    "body":   workbook.add_format({"bold": True, "font_name": "Arial", "font_color": styles.COLOR_OKR_FITNESS_TEXT, "bg_color": styles.COLOR_OKR_FITNESS_BG, "text_wrap": True, "valign": "vcenter", "border": 1, "border_color": styles.COLOR_OKR_FITNESS_BORDER}),
    "mind":   workbook.add_format({"bold": True, "font_name": "Arial", "font_color": "#4A235A", "bg_color": "#F5EEF8", "text_wrap": True, "valign": "vcenter", "border": 1, "border_color": "#D7BDE2"}),
    "wealth": workbook.add_format({"bold": True, "font_name": "Arial", "font_color": "#145A32", "bg_color": "#EAFAF1", "text_wrap": True, "valign": "vcenter", "border": 1, "border_color": "#A9DFBF"}),
    "focus":  workbook.add_format({"bold": True, "font_name": "Arial", "font_color": "#7D6608", "bg_color": "#FEFBD8", "text_wrap": True, "valign": "vcenter", "border": 1, "border_color": "#F9E79F"}),
}
kr_fmt = workbook.add_format({"font_name": "Arial", "bg_color": styles.COLOR_OKR_ROW_BG, "text_wrap": True, "valign": "vcenter", "bottom": 1, "bottom_color": styles.COLOR_OKR_ROW_BORDER})

def get_okr_fmt(objective):
    obj_lower = objective.lower()
    if "role" in obj_lower or "career" in obj_lower or "salary" in obj_lower or "job" in obj_lower or "data" in obj_lower or "tech" in obj_lower:
        return okr_obj_formats["career"]
    elif "body" in obj_lower or "lean" in obj_lower or "strong" in obj_lower or "gym" in obj_lower or "fit" in obj_lower:
        return okr_obj_formats["body"]
    elif "mind" in obj_lower or "mindset" in obj_lower or "disciplin" in obj_lower or "mental" in obj_lower or "unbreak" in obj_lower:
        return okr_obj_formats["mind"]
    elif "wealth" in obj_lower or "financ" in obj_lower or "money" in obj_lower or "invest" in obj_lower:
        return okr_obj_formats["wealth"]
    elif "focus" in obj_lower or "attention" in obj_lower or "distract" in obj_lower:
        return okr_obj_formats["focus"]
    return okr_obj_formats["career"]

for r, (obj, kr, target, curr, deadline, status, notes) in enumerate(OKRS, start=1):
    okr_ws.write(r, 0, obj, get_okr_fmt(obj))
    okr_ws.write(r, 1, kr, kr_fmt)
    okr_ws.write(r, 2, target, center)
    okr_ws.write(r, 3, curr, center)
    okr_ws.write(r, 5, deadline, center)
    okr_ws.write(r, 6, status, center)
    okr_ws.write(r, 7, notes, normal)
    okr_ws.set_row(r, 36)

# Progress % formula and colour scale
total_okr_rows = len(OKRS)
okr_ws.conditional_format(1, 4, total_okr_rows, 4, {
    'type': '3_color_scale',
    'min_color': styles.COLOR_SCALE_MIN, 'min_type': 'num', 'min_value': 0,
    'mid_color': styles.COLOR_SCALE_MID, 'mid_type': 'num', 'mid_value': 0.5,
    'max_color': styles.COLOR_SCALE_MAX, 'max_type': 'num', 'max_value': 1
})

okr_ws.conditional_format(1, 6, total_okr_rows, 6, {'type': 'cell', 'criteria': '==', 'value': '"Not Started"',  'format': workbook.add_format({'bg_color': styles.COLOR_STATUS_NOT_STARTED_BG, 'font_color': styles.COLOR_STATUS_NOT_STARTED_TEXT})})
okr_ws.conditional_format(1, 6, total_okr_rows, 6, {'type': 'cell', 'criteria': '==', 'value': '"On Track"',     'format': workbook.add_format({'bg_color': styles.COLOR_STATUS_ON_TRACK_BG,    'font_color': styles.COLOR_STATUS_ON_TRACK_TEXT})})
okr_ws.conditional_format(1, 6, total_okr_rows, 6, {'type': 'cell', 'criteria': '==', 'value': '"At Risk"',      'format': workbook.add_format({'bg_color': styles.COLOR_STATUS_AT_RISK_BG,     'font_color': styles.COLOR_STATUS_AT_RISK_TEXT})})
okr_ws.conditional_format(1, 6, total_okr_rows, 6, {'type': 'cell', 'criteria': '==', 'value': '"Completed"',   'format': workbook.add_format({'bg_color': styles.COLOR_STATUS_COMPLETED_BG,   'font_color': styles.COLOR_STATUS_COMPLETED_TEXT})})

for r in range(1, total_okr_rows + 1):
    okr_ws.write_formula(r, 4, f'=IF(C{r+1}="","",IF(D{r+1}="","",D{r+1}/C{r+1}))',
                         workbook.add_format({'num_format': '0%', 'align': 'center'}))
    okr_ws.data_validation(r, 6, r, 6, {'validate': 'list', 'source': ['Not Started', 'On Track', 'At Risk', 'Completed']})

workbook.close()
print(f"✅  Done → {OUTFILE_HORIZONTAL}")
print(f"   Sheets: Tasks (365 days), Summary Dashboard, OKR Tracker, Ideal Man Code")
print(f"   Total task columns: {len(col_mapping)} + 2 score columns")
print(f"   Total OKRs: {len(OKRS)}")
