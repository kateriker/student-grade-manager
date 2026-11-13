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
body {
    font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial,
        sans-serif;
    background: linear-gradient(160deg, #eef2ff 0%, #f8fafc 45%,
        #ecfeff 100%);
    background-attachment: fixed;
    color: #1e293b;
    line-height: 1.55;
    margin: 0;
    padding: 24px 16px 56px 16px;
}
form, [id^="drafter-form"] {
    max-width: 880px;
    margin: 0 auto;
}
h1 {
    font-size: 2.3rem;
    margin: 0 0 2px 0;
    color: #4338ca;
    letter-spacing: -0.02em;
}
h2 {
    font-size: 1.2rem;
    margin: 26px 0 10px 0;
    color: #334155;
}
.subtitle { color: #64748b; margin-bottom: 18px; }
.muted { color: #64748b; font-size: 0.92rem; }

.card, .stat, table {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(30, 41, 59, 0.06);
}
.card { padding: 18px 20px; margin: 14px 0; }
.stats { display: flex; flex-wrap: wrap; gap: 14px; margin: 16px 0; }
.stat { flex: 1 1 180px; padding: 16px 18px; }
.stat-label {
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: #64748b;
}
.stat-value { font-size: 2rem; font-weight: 700; color: #4338ca; }
.stat-note { font-size: 0.88rem; color: #64748b; }
.up-name { font-size: 1.4rem; font-weight: 700; margin: 4px 0; }

button, input[type=submit], input[type=button] {
    background: #4f46e5;
    color: #ffffff;
    border: 0;
    border-radius: 10px;
    padding: 10px 18px;
    margin: 4px 8px 4px 0;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.15s, transform 0.15s;
}
button:hover, input[type=submit]:hover, input[type=button]:hover {
    background: #4338ca;
    transform: translateY(-1px);
}
a { color: #4f46e5; font-weight: 600; text-decoration: none; }
a:hover { text-decoration: underline; }

input[type=text], input[type=number], select, textarea {
    padding: 9px 12px;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    font-size: 1rem;
    margin: 4px 0 10px 0;
    max-width: 100%;
    box-sizing: border-box;
    background: #ffffff;
}
input:focus, select:focus, textarea:focus {
    outline: 2px solid #a5b4fc;
    border-color: #6366f1;
}
.label { display: block; font-weight: 600; margin-top: 8px; }

table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    overflow: hidden;
    margin: 12px 0;
}
th {
    background: #4f46e5;
    color: #ffffff;
    text-align: left;
    padding: 10px 12px;
    font-size: 0.85rem;
}
td { padding: 10px 12px; border-bottom: 1px solid #eef2f7; }
tr:nth-child(even) td { background: #f8fafc; }

progress {
    width: 100%;
    height: 16px;
    accent-color: #4f46e5;
    margin: 8px 0;
}

.task { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.rank {
    background: #e0e7ff;
    color: #4338ca;
    font-weight: 700;
    border-radius: 999px;
    width: 30px;
    height: 30px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}
.task-name { font-weight: 700; flex: 1 1 200px; }
.pill {
    font-size: 0.78rem;
    font-weight: 700;
    border-radius: 999px;
    padding: 3px 12px;
}
.pill-high { background: #fee2e2; color: #b91c1c; }
.pill-medium { background: #fef3c7; color: #b45309; }
.pill-low { background: #dcfce7; color: #15803d; }

.msg {
    border-radius: 12px;
    padding: 10px 14px;
    margin: 12px 0;
    font-weight: 600;
}
.msg-error { background: #fee2e2; color: #b91c1c; }
.msg-info { background: #e0e7ff; color: #3730a3; }
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
        ""
    )

    refresh_priorities(state)
    return state


# -------------------------
# UI HELPERS
# -------------------------

def stat_tile(label: str, value: str, note: str) -> Div:
    """A small dashboard tile with a label, big value, and note."""
    return Div(
        Div(label, classes="stat-label"),
        Div(value, classes="stat-value"),
        Div(note, classes="stat-note"),
        classes="stat"
    )


def priority_pill(score: float) -> Span:
    """A colored High / Medium / Low label for a priority score."""
    if score >= 20:
        return Span("High priority", classes="pill pill-high")
    if score >= 12:
        return Span("Medium priority", classes="pill pill-medium")
    return Span("Low priority", classes="pill pill-low")


def message_box(text: str, kind: str = "info"):
    """Show a colored message box, or nothing if there is no text."""
    if not text:
        return ""
    return Div(text, classes="msg msg-" + kind)


def field_label(text: str) -> Span:
    """A bold label that sits above a form field."""
    return Span(text, classes="label")


def up_next_card(state: State) -> Div:
    """Show the single most important unfinished assignment."""
    ranked = ranked_unfinished(state)

    if not ranked:
        return Div(
            Div("Up next", classes="stat-label"),
            Div("You're all caught up!", classes="up-name"),
            Div("No unfinished assignments. Enjoy the break.",
                classes="muted"),
            classes="card"
        )

    top = ranked[0]

    return Div(
        Div("Up next", classes="stat-label"),
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

        Div(
            stat_tile("Current GPA", str(round(gpa, 2)), gpa_note),
            stat_tile("Target GPA", str(state.target_gpa),
                      "Your goal this term"),
            stat_tile("Assignments done",
                      str(finished) + " / " + str(total),
                      "Keep the streak going"),
            stat_tile("Weekly study goal",
                      str(state.weekly_study_goal),
                      "minutes per week"),
            classes="stats"
        ),

        up_next_card(state),

        Header("Jump to", 2),
        Button("Assignments", "assignments"),
        Button("Grades", "grades"),
        Button("Priorities", "priorities"),
        Button("Progress", "progress")
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
        Div("Everything on your plate, in one place.",
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
        Div("Add something new and we'll work out its priority.",
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
        Div("See where you stand in every class.",
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
        cards = [Div("No unfinished assignments!", classes="card")]

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
        Div("Small wins add up. Here's how you're doing.",
            classes="subtitle"),

        Div(
            stat_tile("Completed",
                      str(finished) + " / " + str(total),
                      "assignments finished"),
            stat_tile("Completion",
                      str(round(percentage, 1)) + "%",
                      "of your workload"),
            stat_tile("Weekly goal",
                      str(hours) + " h",
                      str(state.weekly_study_goal) + " minutes"),
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
    test_priority_calculation()
    test_required_score_calculation()


# -------------------------
# START WEBSITE
# -------------------------

run_tests()
start_server(make_initial_state())
