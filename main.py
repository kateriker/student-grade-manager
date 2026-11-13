from drafter import *
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Any, Optional


# -------------------------
# SITE SETTINGS (GitHub Pages)
# -------------------------

set_site_information(
    author="your_email@udel.edu",
    description="""GradePilot helps students track assignments, plan
    what to work on next, and figure out the grades they need.""",
    sources=["List any help resources or sources you used"],
    planning=["your_planning_document.pdf"],
    links=["https://github.com/your-username/your-repo"]
)
hide_debug_information()
set_website_title("GradePilot")
set_website_framed(False)
set_website_style("none")

add_website_css("""
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

:root {
    --bg1: #f5f3ff; --bg2: #fdf2f8; --bg3: #ecfeff;
    --card: rgba(255, 255, 255, 0.85);
    --field: #ffffff;
    --text: #1f2340;
    --muted: #6b7280;
    --border: #e9e5ff;
    --primary: #7c3aed;
    --pink: #ec4899;
    --amber: #f59e0b;
    --shadow: 0 10px 30px rgba(124, 58, 237, 0.12);
}
@media (prefers-color-scheme: dark) {
    :root {
        --bg1: #0f0b24; --bg2: #1a1038; --bg3: #0b1f33;
        --card: rgba(30, 26, 70, 0.85);
        --field: #25214f;
        --text: #eef0ff;
        --muted: #a5a8c8;
        --border: #38337a;
        --shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
    }
}

body {
    font-family: "Nunito", -apple-system, "Segoe UI", Roboto,
        Helvetica, Arial, sans-serif;
    background: linear-gradient(135deg, var(--bg1) 0%, var(--bg2) 50%,
        var(--bg3) 100%);
    background-attachment: fixed;
    color: var(--text);
    line-height: 1.6;
    margin: 0;
    padding: 28px 16px 64px 16px;
}
form, [id^="drafter-form"] { max-width: 900px; margin: 0 auto; }

h1 {
    font-size: 3rem;
    font-weight: 800;
    margin: 0 0 4px 0;
    letter-spacing: -0.03em;
    color: var(--primary);
    background: linear-gradient(90deg, #7c3aed, #ec4899, #f59e0b);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}
h2 {
    font-size: 1.25rem;
    font-weight: 800;
    margin: 28px 0 10px 0;
    color: var(--text);
}
.subtitle { color: var(--muted); font-size: 1.05rem; }
.vibe {
    display: inline-block;
    margin: 10px 0 6px 0;
    padding: 8px 16px;
    border-radius: 999px;
    font-weight: 700;
    color: #ffffff;
    background: linear-gradient(90deg, #7c3aed, #ec4899);
    box-shadow: 0 6px 16px rgba(236, 72, 153, 0.3);
}
.muted { color: var(--muted); font-size: 0.95rem; }

.card, .stat, table {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    box-shadow: var(--shadow);
    backdrop-filter: blur(8px);
    animation: pop 0.35s ease both;
}
.card { padding: 20px 22px; margin: 16px 0; }
.card:hover, .stat:hover {
    transform: translateY(-3px);
    transition: transform 0.2s;
}
.stats { display: flex; flex-wrap: wrap; gap: 16px; margin: 20px 0; }
.stat {
    flex: 1 1 190px;
    padding: 16px 18px;
    border-top: 6px solid var(--c, #7c3aed);
}
.stats .stat:nth-child(1) { --c: #7c3aed; }
.stats .stat:nth-child(2) { --c: #ec4899; }
.stats .stat:nth-child(3) { --c: #10b981; }
.stats .stat:nth-child(4) { --c: #f59e0b; }
.stat-icon { font-size: 1.6rem; }
.stat-label {
    font-size: 0.78rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--muted);
}
.stat-value {
    font-size: 2.2rem;
    font-weight: 800;
    color: var(--c, #7c3aed);
    line-height: 1.2;
}
.stat-note { font-size: 0.9rem; color: var(--muted); }
.up-name { font-size: 1.6rem; font-weight: 800; margin: 4px 0; }

button, input[type=submit], input[type=button] {
    background: linear-gradient(90deg, #7c3aed, #ec4899);
    color: #ffffff;
    border: 0;
    border-radius: 999px;
    padding: 11px 24px;
    margin: 6px 10px 6px 0;
    font-family: inherit;
    font-size: 1rem;
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 6px 16px rgba(124, 58, 237, 0.3);
    transition: transform 0.15s, box-shadow 0.15s;
}
button:hover, input[type=submit]:hover, input[type=button]:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 10px 22px rgba(236, 72, 153, 0.35);
}
button:active, input[type=submit]:active { transform: scale(0.97); }
a { color: var(--primary); font-weight: 800; text-decoration: none; }
a:hover { text-decoration: underline; }

input[type=text], input[type=number], select, textarea {
    padding: 10px 14px;
    border: 2px solid var(--border);
    border-radius: 12px;
    font-family: inherit;
    font-size: 1rem;
    margin: 4px 0 10px 0;
    max-width: 100%;
    box-sizing: border-box;
    background: var(--field);
    color: var(--text);
}
input:focus, select:focus, textarea:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 4px rgba(124, 58, 237, 0.2);
}
input[type=checkbox] {
    width: 20px;
    height: 20px;
    accent-color: #7c3aed;
    vertical-align: middle;
}
.label { display: block; font-weight: 800; margin-top: 10px; }

table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    overflow: hidden;
    margin: 14px 0;
}
th {
    background: linear-gradient(90deg, #7c3aed, #ec4899);
    color: #ffffff;
    text-align: left;
    padding: 12px 14px;
    font-size: 0.85rem;
    letter-spacing: 0.04em;
}
td { padding: 12px 14px; border-bottom: 1px solid var(--border); }
tr:hover td { background: rgba(124, 58, 237, 0.08); }

progress {
    width: 100%;
    height: 20px;
    margin: 10px 0;
    border: 0;
    border-radius: 999px;
    overflow: hidden;
    appearance: none;
    -webkit-appearance: none;
    accent-color: #ec4899;
}
progress::-webkit-progress-bar { background: var(--border); }
progress::-webkit-progress-value {
    background: linear-gradient(90deg, #7c3aed, #ec4899, #f59e0b);
    border-radius: 999px;
}
progress::-moz-progress-bar {
    background: linear-gradient(90deg, #7c3aed, #ec4899, #f59e0b);
}

.task { display: flex; align-items: center; gap: 14px; flex-wrap: wrap; }
.rank {
    background: linear-gradient(135deg, #7c3aed, #ec4899);
    color: #ffffff;
    font-weight: 800;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}
.task-name { font-weight: 800; font-size: 1.1rem; flex: 1 1 200px; }
.pill {
    font-size: 0.82rem;
    font-weight: 800;
    border-radius: 999px;
    padding: 4px 14px;
}
.pill-high { background: #fee2e2; color: #b91c1c; }
.pill-medium { background: #fef3c7; color: #b45309; }
.pill-low { background: #d1fae5; color: #047857; }

.msg {
    border-radius: 14px;
    padding: 12px 16px;
    margin: 14px 0;
    font-weight: 700;
}
.msg-error { background: #fee2e2; color: #b91c1c; }
.msg-info { background: #ede9fe; color: #5b21b6; }

@keyframes pop {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
@media (prefers-reduced-motion: reduce) {
    * { animation: none !important; transition: none !important; }
}
""")


# -------------------------
# DATACLASSES
# -------------------------

@dataclass
class Course:
    name: str
    current_grade: float
    target_grade: float
    weight: float


@dataclass
class Assignment:
    name: str
    course: str
    due_date: str
    difficulty: int
    estimated_hours: float
    grade: float
    completed: bool
    priority_score: float


@dataclass
class State:
    assignments: list[Assignment]
    courses: list[Course]
    selected_course: str
    target_gpa: float
    show_completed: bool
    weekly_study_goal: int
    calculation_message: str
    form_message: str
    goals_message: str


# -------------------------
# HELPER FUNCTIONS
# -------------------------

def find_course(
    state: State, course_name: str
) -> Optional[Course]:
    """Find and return a course by its name."""
    for course in state.courses:
        if course.name == course_name:
            return course
    return None


def calculate_gpa(state: State) -> float:
    """Calculate the weighted GPA from all course grades."""
    total_points = 0.0
    total_weight = 0.0

    for course in state.courses:
        if course.current_grade >= 90:
            grade_points = 4.0
        elif course.current_grade >= 80:
            grade_points = 3.0
        elif course.current_grade >= 70:
            grade_points = 2.0
        elif course.current_grade >= 60:
            grade_points = 1.0
        else:
            grade_points = 0.0

        total_points += grade_points * course.weight
        total_weight += course.weight

    if total_weight == 0:
        return 0.0

    return total_points / total_weight


def parse_date(text: str) -> Optional[date]:
    """Turn 'YYYY-MM-DD' into a date, or None if it is invalid."""
    parts = text.strip().split("-")

    if len(parts) != 3:
        return None

    try:
        return date(int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError:
        return None


def days_left(
    due_text: str, today: Optional[date] = None
) -> Optional[int]:
    """Return days until a due date, or None if the date is invalid."""
    if today is None:
        today = date.today()

    due = parse_date(due_text)

    if due is None:
        return None

    return (due - today).days


def due_description(due_text: str) -> str:
    """Describe a due date in friendly words."""
    days = days_left(due_text)

    if days is None:
        return "No valid due date"
    if days < 0:
        late = -days
        if late == 1:
            return "Overdue by 1 day"
        return "Overdue by " + str(late) + " days"
    if days == 0:
        return "Due today"
    if days == 1:
        return "Due tomorrow"
    return "Due in " + str(days) + " days"


def calculate_priority_score(
    assignment: Assignment,
    today: Optional[date] = None
) -> float:
    """Calculate an assignment priority score."""
    days = days_left(assignment.due_date, today)

    if days is None:
        days = 30

    urgency = max(0, 14 - days)
    overdue_bonus = 10 if days < 0 else 0

    score = (
        assignment.difficulty * 2
        + urgency * 1.5
        + min(assignment.estimated_hours, 10) * 0.5
        + overdue_bonus
    )

    return round(score, 2)


def refresh_priorities(state: State) -> None:
    """Update priority scores for every assignment."""
    for assignment in state.assignments:
        assignment.priority_score = calculate_priority_score(
            assignment
        )


def ranked_unfinished(state: State) -> list[Assignment]:
    """Return unfinished assignments, highest priority first."""
    refresh_priorities(state)

    ranked = sorted(
        state.assignments,
        key=lambda assignment: assignment.priority_score,
        reverse=True
    )

    result = []

    for assignment in ranked:
        if not assignment.completed:
            result.append(assignment)

    return result


def calculate_required_score(
    current_grade: float,
    target_grade: float,
    remaining_weight: float
) -> Optional[float]:
    """Calculate the score needed on remaining coursework."""
    if remaining_weight <= 0 or remaining_weight > 100:
        return None

    remaining_fraction = remaining_weight / 100
    completed_fraction = 1 - remaining_fraction

    required = (
        target_grade - current_grade * completed_fraction
    ) / remaining_fraction

    return round(required, 2)


def completed_count(state: State) -> int:
    """Count the number of completed assignments."""
    count = 0

    for assignment in state.assignments:
        if assignment.completed:
            count += 1

    return count


def make_initial_state() -> State:
    """Create the starting courses and sample assignments."""
    today = date.today()

    courses = [
        Course("Biology", 88.0, 92.0, 0.40),
        Course("Computer Science", 94.0, 95.0, 0.35),
        Course("Math", 83.0, 90.0, 0.25)
    ]

    assignments = [
        Assignment(
            "Chapter 4 Review",
            "Biology",
            (today + timedelta(days=2)).isoformat(),
            3, 2.0, 0.0, False, 0.0
        ),
        Assignment(
            "Programming Lab",
            "Computer Science",
            (today + timedelta(days=4)).isoformat(),
            4, 3.5, 0.0, False, 0.0
        ),
        Assignment(
            "Practice Problems",
            "Math",
            (today + timedelta(days=7)).isoformat(),
            2, 1.5, 95.0, True, 0.0
        )
    ]

    state = State(
        assignments,
        courses,
        "Biology",
        3.5,
        False,
        600,
        "",
        "",
        ""
    )

    refresh_priorities(state)
    return state


# -------------------------
# UI HELPERS
# -------------------------

def stat_tile(
    label: str, value: str, note: str, icon: str = ""
) -> Div:
    """A small dashboard tile with a label, big value, and note."""
    return Div(
        Div(icon, classes="stat-icon"),
        Div(label, classes="stat-label"),
        Div(value, classes="stat-value"),
        Div(note, classes="stat-note"),
        classes="stat"
    )


def priority_pill(score: float) -> Span:
    """A colored High / Medium / Low label for a priority score."""
    if score >= 20:
        return Span("🔥 High priority", classes="pill pill-high")
    if score >= 12:
        return Span("⚡ Medium priority", classes="pill pill-medium")
    return Span("🌱 Low priority", classes="pill pill-low")


def message_box(text: str, kind: str = "info"):
    """Show a colored message box, or nothing if there is no text."""
    if not text:
        return ""
    return Div(text, classes="msg msg-" + kind)


def field_label(text: str) -> Span:
    """A bold label that sits above a form field."""
    return Span(text, classes="label")


def vibe_message(percentage: float) -> str:
    """A short motivational message based on progress."""
    if percentage >= 100:
        return "🎉 Everything is done. You are unstoppable!"
    if percentage >= 50:
        return "🚀 Over halfway there. Keep the momentum!"
    if percentage > 0:
        return "🌱 Great start. One assignment at a time."
    return "☕ Fresh slate. Pick one task and begin!"


def up_next_card(state: State) -> Div:
    """Show the single most important unfinished assignment."""
    ranked = ranked_unfinished(state)

    if not ranked:
        return Div(
            Div("🎉 Up next", classes="stat-label"),
            Div("You're all caught up!", classes="up-name"),
            Div("No unfinished assignments. Enjoy the break.",
                classes="muted"),
            classes="card"
        )

    top = ranked[0]

    return Div(
        Div("🎯 Up next", classes="stat-label"),
        Div(top.name, classes="up-name"),
        Div(top.course + " · " + due_description(top.due_date),
            classes="muted"),
        priority_pill(top.priority_score),
        classes="card"
    )


# -------------------------
# HOME PAGE
# -------------------------

@route
def index(state: State) -> Page:
    """Open the website's main dashboard."""
    return home(state)


@route
def home(
    state: State,
    show_completed: bool = False,
    course_name: str = "",
    weekly_study_goal: int = 0
) -> Page:
    """Display the GradePilot dashboard."""
    state.show_completed = show_completed

    if course_name:
        state.selected_course = course_name

    if weekly_study_goal > 0:
        state.weekly_study_goal = weekly_study_goal

    gpa = calculate_gpa(state)
    finished = completed_count(state)
    total = len(state.assignments)
    percent_done = 0.0

    if total > 0:
        percent_done = finished / total * 100

    if gpa >= state.target_gpa:
        gpa_note = "You're on track!"
    else:
        gpa_note = (
            str(round(state.target_gpa - gpa, 2)) + " to go"
        )

    return Page(state, [
        Header("GradePilot"),
        Header("Your Academic Dashboard", 2),
        Div("Plan smarter, study steadier, and hit your target GPA.",
            classes="subtitle"),
        Div(vibe_message(percent_done), classes="vibe"),

        Div(
            stat_tile("Current GPA", str(round(gpa, 2)), gpa_note, "🎓"),
            stat_tile("Target GPA", str(state.target_gpa),
                      "Your goal this term", "🎯"),
            stat_tile("Assignments done",
                      str(finished) + " / " + str(total),
                      "Keep the streak going", "✅"),
            stat_tile("Weekly study goal",
                      str(state.weekly_study_goal),
                      "minutes per week", "⏱️"),
            classes="stats"
        ),

        up_next_card(state),

        Header("Jump to", 2),
        Button("Assignments", "assignments"),
        Button("Grades", "grades"),
        Button("Priorities", "priorities"),
        Button("Progress", "progress"),
        Button("Goals & GPA", "goals")
    ])


# -------------------------
# ASSIGNMENTS PAGE
# -------------------------

@route
def assignments(
    state: State,
    show_completed: bool = False
) -> Page:
    """Display assignments and completion information."""
    state.show_completed = show_completed

    visible_assignments: list[list[Any]] = []

    for assignment in state.assignments:
        if state.show_completed or not assignment.completed:
            visible_assignments.append([
                assignment.name,
                assignment.course,
                assignment.due_date,
                str(assignment.difficulty) + " / 5",
                str(assignment.estimated_hours) + " h",
                "Done" if assignment.completed else "To do"
            ])

    if not visible_assignments:
        visible_assignments = [["No assignments to display",
                                "-", "-", "-", "-", "-"]]

    return Page(state, [
        Header("Assignments"),
        Div("📚 Everything on your plate, in one place.",
            classes="subtitle"),

        Table(
            visible_assignments,
            ["Name", "Course", "Due Date", "Difficulty",
             "Hours", "Status"]
        ),

        "Show completed assignments: ",
        CheckBox("show_completed", state.show_completed),
        LineBreak(),
        Button("Update Assignment List", "assignments"),
        Button("Add Assignment", "add_assignment"),
        LineBreak(),
        Link("Return Home", "home")
    ])


# -------------------------
# ADD ASSIGNMENT PAGE
# -------------------------

@route
def add_assignment(
    state: State,
    assignment_name: str = "",
    course_name: str = "",
    due_date: str = "",
    difficulty: int = 3,
    estimated_hours: float = 1.0,
    grade: float = 0.0,
    completed: bool = False,
    show_completed: bool = False
) -> Page:
    """Display the assignment form or save a new assignment."""
    state.show_completed = show_completed

    if assignment_name.strip():
        if find_course(state, course_name) is None:
            state.form_message = "Please select a valid course."
        elif estimated_hours <= 0:
            state.form_message = "Hours must be greater than zero."
        elif difficulty < 1 or difficulty > 5:
            state.form_message = "Difficulty must be from 1 to 5."
        elif parse_date(due_date) is None:
            state.form_message = "Enter the due date as YYYY-MM-DD."
        else:
            new_assignment = Assignment(
                assignment_name.strip(),
                course_name,
                due_date,
                difficulty,
                estimated_hours,
                grade,
                completed,
                0.0
            )

            new_assignment.priority_score = (
                calculate_priority_score(new_assignment)
            )

            state.assignments.append(new_assignment)
            state.form_message = ""
            return assignments(state)

    course_names = [course.name for course in state.courses]

    if state.selected_course not in course_names:
        selected = course_names[0]
    else:
        selected = state.selected_course

    return Page(state, [
        Header("Add Assignment"),
        Div("✏️ Add something new and we'll work out its priority.",
            classes="subtitle"),

        message_box(state.form_message, "error"),

        Div(
            field_label("Assignment name"),
            TextBox("assignment_name"),

            field_label("Course"),
            SelectBox("course_name", course_names, selected),

            field_label("Due date (YYYY-MM-DD)"),
            TextBox("due_date", date.today().isoformat()),

            field_label("Difficulty (1-5)"),
            SelectBox(
                "difficulty",
                ["1", "2", "3", "4", "5"],
                "3"
            ),

            field_label("Estimated hours"),
            TextBox("estimated_hours", 1.0, "number"),

            field_label("Grade received (enter 0 if unknown)"),
            TextBox("grade", 0.0, "number"),

            field_label("Already completed"),
            CheckBox("completed"),

            classes="card"
        ),

        Button("Save Assignment", "add_assignment"),
        Link("Cancel", "assignments")
    ])


# -------------------------
# GRADES PAGE
# -------------------------

@route
def grades(
    state: State,
    course_name: str = "",
    current_grade: float = -1.0,
    target_grade: float = -1.0,
    remaining_weight: float = 30.0
) -> Page:
    """Display course grades and open the grade calculator."""
    if course_name:
        state.selected_course = course_name

    grade_rows: list[list[Any]] = []

    for course in state.courses:
        grade_rows.append([
            course.name,
            str(course.current_grade) + "%",
            str(course.target_grade) + "%",
            str(round(course.weight * 100)) + "%"
        ])

    course_names = [course.name for course in state.courses]

    return Page(state, [
        Header("Grades"),
        Div("📊 See where you stand in every class.",
            classes="subtitle"),

        Table(
            grade_rows,
            ["Course", "Current Grade", "Target Grade",
             "Course Weight"]
        ),

        Div(
            field_label("Select a course to calculate its target grade"),
            SelectBox(
                "course_name",
                course_names,
                state.selected_course
            ),
            classes="card"
        ),

        Button("Open Grade Calculator", "calculate_grade"),
        LineBreak(),
        Link("Return Home", "home")
    ])


# -------------------------
# CALCULATE GRADE PAGE
# -------------------------

@route
def calculate_grade(
    state: State,
    course_name: str = "",
    current_grade: float = -1.0,
    target_grade: float = -1.0,
    remaining_weight: float = 30.0
) -> Page:
    """Display and calculate the required grade."""
    course = find_course(state, course_name)

    if course is None:
        course = find_course(state, state.selected_course)

    if course is None:
        return Page(state, [
            Header("Calculate Grade"),
            "Please add a course first.",
            Button("Return to Grades", "grades")
        ])

    state.selected_course = course.name

    if current_grade >= 0 and target_grade >= 0:
        course.current_grade = current_grade
        course.target_grade = target_grade

        required = calculate_required_score(
            current_grade,
            target_grade,
            remaining_weight
        )

        if required is None:
            state.calculation_message = (
                "Remaining weight must be between 1 and 100."
            )
        elif required > 100:
            state.calculation_message = (
                "The target is not reachable with the "
                "remaining coursework."
            )
        elif required <= 0:
            state.calculation_message = (
                "You have already reached your target!"
            )
        else:
            state.calculation_message = (
                "You need " + str(required)
                + "% on the remaining coursework."
            )

    return Page(state, [
        Header("Calculate Grade"),
        Div("Course: " + course.name, classes="subtitle"),

        Div(
            field_label("Current grade"),
            TextBox("current_grade", course.current_grade, "number"),

            field_label("Target grade"),
            TextBox("target_grade", course.target_grade, "number"),

            field_label("Percentage of grade still remaining"),
            TextBox("remaining_weight", remaining_weight, "number"),

            classes="card"
        ),

        Button("Calculate Required Score", "calculate_grade"),

        message_box(state.calculation_message, "info"),

        Button("Back to Grades", "grades")
    ])


def parse_number(text: str) -> Optional[float]:
    """Turn typed text into a number, or None if it is not a number."""
    try:
        return float(text.strip())
    except ValueError:
        return None


# -------------------------
# GOALS & GPA PAGE
# -------------------------

def total_weight_percent(state: State) -> float:
    """Add up all course weights as a percentage."""
    total = 0.0

    for course in state.courses:
        total += course.weight

    return round(total * 100, 1)


def goals_page(state: State) -> Page:
    """Build the page where students edit goals, grades and courses."""
    gpa = calculate_gpa(state)
    course_names = [course.name for course in state.courses]

    if state.selected_course not in course_names:
        selected = course_names[0]
    else:
        selected = state.selected_course

    rows: list[list[Any]] = []

    for course in state.courses:
        rows.append([
            course.name,
            str(course.current_grade) + "%",
            str(round(course.weight * 100, 1)) + "%"
        ])

    if gpa >= state.target_gpa:
        gap_note = "You've reached your goal!"
    else:
        gap_note = str(round(state.target_gpa - gpa, 2)) + " to go"

    if state.goals_message.startswith("Please"):
        message_kind = "error"
    else:
        message_kind = "info"

    return Page(state, [
        Header("Goals & GPA"),
        Div("🎯 Set your target GPA and keep your courses up to date.",
            classes="subtitle"),

        message_box(state.goals_message, message_kind),

        Div(
            stat_tile("Current GPA", str(round(gpa, 2)),
                      "Calculated from your course grades", "🎓"),
            stat_tile("Target GPA", str(state.target_gpa),
                      gap_note, "🎯"),
            classes="stats"
        ),

        Div(
            field_label("Target GPA (0.0 - 4.0)"),
            TextBox("target_gpa", str(state.target_gpa)),
            Button("Save Target GPA", "save_target"),
            classes="card"
        ),

        Div(
            Div("✏️ Edit a course", classes="stat-label"),
            field_label("Course"),
            SelectBox("course_name", course_names, selected),
            field_label("New current grade (0 - 100)"),
            TextBox("new_grade", ""),
            Button("Save Course Grade", "save_grade"),
            field_label("New weight (1 - 100)"),
            TextBox("new_weight", ""),
            Div("Weight is how much the course counts toward your GPA, "
                "like credit hours. Weights don't need to add up to "
                "100.", classes="muted"),
            Button("Save Course Weight", "save_weight"),
            Div("Removing a course also removes its assignments.",
                classes="muted"),
            Button("Remove Course", "remove_course"),
            classes="card"
        ),

        Div(
            Div("➕ Add a course", classes="stat-label"),
            field_label("Course name"),
            TextBox("new_course_name", ""),
            field_label("Starting grade (0 - 100)"),
            TextBox("new_course_grade", ""),
            field_label("Weight (1 - 100)"),
            TextBox("new_course_weight", ""),
            Button("Add Course", "add_course"),
            classes="card"
        ),

        Table(rows, ["Course", "Current Grade", "Course Weight"]),
        Div("Weights currently add up to "
            + str(total_weight_percent(state)) + "%.",
            classes="muted"),

        Link("Return Home", "home")
    ])


@route
def goals(
    state: State,
    target_gpa: str = "",
    course_name: str = "",
    new_grade: str = "",
    new_weight: str = "",
    new_course_name: str = "",
    new_course_grade: str = "",
    new_course_weight: str = ""
) -> Page:
    """Open the goals and GPA page."""
    state.goals_message = ""
    return goals_page(state)


@route
def save_target(
    state: State,
    target_gpa: str = "",
    course_name: str = "",
    new_grade: str = "",
    new_weight: str = "",
    new_course_name: str = "",
    new_course_grade: str = "",
    new_course_weight: str = ""
) -> Page:
    """Save a new target GPA."""
    value = parse_number(target_gpa)

    if course_name:
        state.selected_course = course_name

    if value is None or value < 0 or value > 4:
        state.goals_message = (
            "Please enter a target GPA between 0.0 and 4.0."
        )
    else:
        state.target_gpa = round(value, 2)
        state.goals_message = (
            "Target GPA updated to " + str(state.target_gpa) + "."
        )

    return goals_page(state)


@route
def save_grade(
    state: State,
    target_gpa: str = "",
    course_name: str = "",
    new_grade: str = "",
    new_weight: str = "",
    new_course_name: str = "",
    new_course_grade: str = "",
    new_course_weight: str = ""
) -> Page:
    """Save a new current grade for one course."""
    course = find_course(state, course_name)
    value = parse_number(new_grade)

    if course is None:
        state.goals_message = "Please choose a valid course."
    elif value is None or value < 0 or value > 100:
        state.goals_message = (
            "Please enter a grade between 0 and 100."
        )
    else:
        course.current_grade = value
        state.selected_course = course.name
        state.goals_message = (
            course.name + " is now " + str(value) + "%. "
            "Your GPA is " + str(round(calculate_gpa(state), 2)) + "."
        )

    return goals_page(state)


@route
def save_weight(
    state: State,
    target_gpa: str = "",
    course_name: str = "",
    new_grade: str = "",
    new_weight: str = "",
    new_course_name: str = "",
    new_course_grade: str = "",
    new_course_weight: str = ""
) -> Page:
    """Save a new weight for one course."""
    course = find_course(state, course_name)
    value = parse_number(new_weight)

    if course is None:
        state.goals_message = "Please choose a valid course."
    elif value is None or value <= 0 or value > 100:
        state.goals_message = (
            "Please enter a weight greater than 0 and at most 100."
        )
    else:
        course.weight = round(value / 100, 4)
        state.selected_course = course.name
        state.goals_message = (
            course.name + " now has a weight of " + str(value)
            + ". Your GPA is "
            + str(round(calculate_gpa(state), 2)) + "."
        )

    return goals_page(state)


@route
def add_course(
    state: State,
    target_gpa: str = "",
    course_name: str = "",
    new_grade: str = "",
    new_weight: str = "",
    new_course_name: str = "",
    new_course_grade: str = "",
    new_course_weight: str = ""
) -> Page:
    """Add a new course."""
    name = new_course_name.strip()
    grade = parse_number(new_course_grade)
    weight = parse_number(new_course_weight)

    if name == "":
        state.goals_message = "Please enter a course name."
    elif find_course(state, name) is not None:
        state.goals_message = (
            "Please use a different name. That course already exists."
        )
    elif grade is None or grade < 0 or grade > 100:
        state.goals_message = (
            "Please enter a starting grade between 0 and 100."
        )
    elif weight is None or weight <= 0 or weight > 100:
        state.goals_message = (
            "Please enter a weight greater than 0 and at most 100."
        )
    else:
        state.courses.append(
            Course(name, grade, 90.0, round(weight / 100, 4))
        )
        state.selected_course = name
        state.goals_message = (
            "Added " + name + ". Your GPA is "
            + str(round(calculate_gpa(state), 2)) + "."
        )

    return goals_page(state)


@route
def remove_course(
    state: State,
    target_gpa: str = "",
    course_name: str = "",
    new_grade: str = "",
    new_weight: str = "",
    new_course_name: str = "",
    new_course_grade: str = "",
    new_course_weight: str = ""
) -> Page:
    """Remove a course and the assignments that belong to it."""
    course = find_course(state, course_name)

    if course is None:
        state.goals_message = "Please choose a valid course."
    elif len(state.courses) <= 1:
        state.goals_message = "Please keep at least one course."
    else:
        kept = []
        removed = 0

        for assignment in state.assignments:
            if assignment.course == course.name:
                removed += 1
            else:
                kept.append(assignment)

        state.assignments = kept
        state.courses.remove(course)
        state.selected_course = state.courses[0].name
        state.goals_message = (
            "Removed " + course.name + " and "
            + str(removed) + " assignment(s)."
        )

    return goals_page(state)


# -------------------------
# PRIORITIES PAGE
# -------------------------

@route
def priorities(state: State) -> Page:
    """Display assignments ranked by priority score."""
    ranked = ranked_unfinished(state)

    cards = []
    rank = 1

    for assignment in ranked:
        cards.append(Div(
            Div(
                Span(str(rank), classes="rank"),
                Span(assignment.name, classes="task-name"),
                Span(assignment.course + " · "
                     + due_description(assignment.due_date),
                     classes="muted"),
                priority_pill(assignment.priority_score),
                classes="task"
            ),
            classes="card"
        ))
        rank += 1

    if not cards:
        cards = [Div("🎉 No unfinished assignments!", classes="card")]

    content = [
        Header("Assignment Priorities"),
        "Assignments are ranked from highest to lowest priority."
    ]
    content.extend(cards)
    content.append(Button("View Assignments", "assignments"))
    content.append(Link("Return Home", "home"))

    return Page(state, content)


# -------------------------
# PROGRESS PAGE
# -------------------------

@route
def progress(
    state: State,
    weekly_study_goal: int = 0
) -> Page:
    """Display academic progress and update the study goal."""
    if weekly_study_goal > 0:
        state.weekly_study_goal = weekly_study_goal

    finished = completed_count(state)
    total = len(state.assignments)
    percentage = 0.0

    if total > 0:
        percentage = finished / total * 100

    hours = round(state.weekly_study_goal / 60, 1)

    return Page(state, [
        Header("Academic Progress"),
        Div(vibe_message(percentage), classes="vibe"),

        Div(
            stat_tile("Completed",
                      str(finished) + " / " + str(total),
                      "assignments finished", "✅"),
            stat_tile("Completion",
                      str(round(percentage, 1)) + "%",
                      "of your workload", "📈"),
            stat_tile("Weekly goal",
                      str(hours) + " h",
                      str(state.weekly_study_goal) + " minutes", "⏱️"),
            classes="stats"
        ),

        ProgressBar(finished, max(total, 1)),

        Div(
            field_label("Weekly study goal (minutes)"),
            TextBox(
                "weekly_study_goal",
                state.weekly_study_goal,
                "number"
            ),
            classes="card"
        ),

        Button("Update Study Goal", "progress"),
        LineBreak(),
        Link("Return Home", "home")
    ])


# -------------------------
# UNIT TESTS
# -------------------------

def test_index_route() -> None:
    """Test that the starting route opens the dashboard."""
    state = make_initial_state()
    page = index(state)
    assert assert_has(page, "GradePilot")


def test_home_route() -> None:
    """Test the dashboard and its navigation buttons."""
    state = make_initial_state()
    page = home(state)
    assert assert_has(page, Button("Assignments", "assignments"))
    assert assert_has(page, "Your Academic Dashboard")
    assert state.target_gpa == 3.5


def test_assignments_route() -> None:
    """Test the assignment list and its controls."""
    state = make_initial_state()
    page = assignments(state)
    assert assert_has(page, Button("Add Assignment",
                                   "add_assignment"))
    assert assert_has(page, "Chapter 4 Review")


def test_add_assignment_route() -> None:
    """Test the assignment form and saving an assignment."""
    state = make_initial_state()

    form_page = add_assignment(state)
    assert assert_has(form_page, "Add Assignment")

    old_count = len(state.assignments)

    add_assignment(
        state,
        "Unit Test Assignment",
        "Biology",
        date.today().isoformat(),
        4,
        2.0,
        0.0,
        False
    )

    assert len(state.assignments) == old_count + 1
    assert state.assignments[-1].name == "Unit Test Assignment"


def test_add_assignment_bad_date() -> None:
    """Test that an invalid date is rejected."""
    state = make_initial_state()
    old_count = len(state.assignments)

    add_assignment(
        state, "Bad Date", "Biology", "tomorrow", 3, 1.0, 0.0, False
    )

    assert len(state.assignments) == old_count
    assert state.form_message == "Enter the due date as YYYY-MM-DD."


def test_grades_route() -> None:
    """Test that the grades page displays course information."""
    state = make_initial_state()
    page = grades(state)
    assert assert_has(page, "Biology")
    assert assert_has(page, "Open Grade Calculator")


def test_calculate_grade_route() -> None:
    """Test the grade calculator and its result."""
    state = make_initial_state()

    page = calculate_grade(
        state,
        "Biology",
        80.0,
        90.0,
        50.0
    )

    assert state.calculation_message == (
        "You need 100.0% on the remaining coursework."
    )
    assert assert_has(page, "Calculate Grade")


def test_priorities_route() -> None:
    """Test that the priorities page ranks assignments."""
    state = make_initial_state()
    page = priorities(state)
    assert assert_has(page, "Assignment Priorities")
    assert ranked_unfinished(state)[0].name == "Chapter 4 Review"


def test_progress_route() -> None:
    """Test progress display and updating the study goal."""
    state = make_initial_state()
    page = progress(state, 300)

    assert state.weekly_study_goal == 300
    assert assert_has(page, "Academic Progress")


def test_priority_calculation() -> None:
    """Test that priority scores are calculated."""
    assignment = Assignment(
        "Test",
        "Biology",
        date.today().isoformat(),
        5,
        2.0,
        0.0,
        False,
        0.0
    )

    score = calculate_priority_score(
        assignment,
        date.today()
    )

    assert score > 0


def test_required_score_calculation() -> None:
    """Test the required score formula."""
    result = calculate_required_score(80.0, 90.0, 50.0)
    assert result == 100.0


def test_goals_route() -> None:
    """Test that the goals page opens."""
    state = make_initial_state()
    page = goals(state)
    assert assert_has(page, "Goals & GPA")


def test_save_target_route() -> None:
    """Test changing the target GPA, valid and invalid."""
    state = make_initial_state()

    save_target(state, "3.8")
    assert state.target_gpa == 3.8

    save_target(state, "9")
    assert state.target_gpa == 3.8
    assert state.goals_message.startswith("Please")

    save_target(state, "abc")
    assert state.target_gpa == 3.8


def test_save_grade_route() -> None:
    """Test changing a course grade and the resulting GPA."""
    state = make_initial_state()
    before = calculate_gpa(state)

    biology = find_course(state, "Biology")
    assert biology is not None

    save_grade(state, "", "Biology", "95")
    assert biology.current_grade == 95.0
    assert calculate_gpa(state) > before

    save_grade(state, "", "Biology", "150")
    assert biology.current_grade == 95.0


def test_save_weight_route() -> None:
    """Test changing a course weight."""
    state = make_initial_state()
    biology = find_course(state, "Biology")
    assert biology is not None

    save_weight(state, "", "Biology", "", "50")
    assert biology.weight == 0.5

    save_weight(state, "", "Biology", "", "0")
    assert biology.weight == 0.5
    assert state.goals_message.startswith("Please")


def test_add_course_route() -> None:
    """Test adding a course, and rejecting a duplicate."""
    state = make_initial_state()
    old_count = len(state.courses)

    add_course(state, "", "", "", "", "Chemistry", "85", "30")
    assert len(state.courses) == old_count + 1
    chemistry = find_course(state, "Chemistry")
    assert chemistry is not None
    assert chemistry.weight == 0.3

    add_course(state, "", "", "", "", "Chemistry", "85", "30")
    assert len(state.courses) == old_count + 1


def test_remove_course_route() -> None:
    """Test removing a course and its assignments."""
    state = make_initial_state()

    remove_course(state, "", "Biology")
    assert find_course(state, "Biology") is None

    for assignment in state.assignments:
        assert assignment.course != "Biology"

    remove_course(state, "", "Computer Science")
    remove_course(state, "", "Math")
    assert len(state.courses) == 1


def run_tests() -> None:
    """Run all route and helper function tests."""
    test_index_route()
    test_home_route()
    test_assignments_route()
    test_add_assignment_route()
    test_add_assignment_bad_date()
    test_grades_route()
    test_calculate_grade_route()
    test_priorities_route()
    test_progress_route()
    test_goals_route()
    test_save_target_route()
    test_save_grade_route()
    test_save_weight_route()
    test_add_course_route()
    test_remove_course_route()
    test_priority_calculation()
    test_required_score_calculation()


# -------------------------
# START WEBSITE
# -------------------------

run_tests()
start_server(make_initial_state())
