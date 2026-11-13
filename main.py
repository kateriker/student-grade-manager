
from drafter import *
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional


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


def calculate_priority_score(
    assignment: Assignment,
    today: Optional[date] = None
) -> float:
    """Calculate an assignment priority score."""
    if today is None:
        today = date.today()

    try:
        due = date.fromisoformat(assignment.due_date)
        days_left = (due - today).days
    except ValueError:
        days_left = 30

    urgency = max(0, 14 - days_left)
    overdue_bonus = 10 if days_left < 0 else 0

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

    return Page(state, [
        Header("GradePilot"),
        Header("Your Academic Dashboard", 2),

        "Current GPA: " + str(round(gpa, 2)) + "\n",
        "Target GPA: " + str(state.target_gpa) + "\n",
        "Completed assignments: " + str(finished)
        + " / " + str(total) + "\n",
        "Weekly study goal: "
        + str(state.weekly_study_goal) + " minutes\n",

        Header("Navigate", 2),
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

    visible_assignments = []

    for assignment in state.assignments:
        if state.show_completed or not assignment.completed:
            visible_assignments.append([
                assignment.name,
                assignment.course,
                assignment.due_date,
                str(assignment.difficulty),
                str(assignment.estimated_hours),
                "Yes" if assignment.completed else "No"
            ])

    if not visible_assignments:
        visible_assignments = [["No assignments to display",
                                "-", "-", "-", "-", "-"]]

    return Page(state, [
        Header("Assignments"),

        Table(
            visible_assignments,
            ["Name", "Course", "Due Date", "Difficulty",
             "Hours", "Completed"]
        ),

        "Show completed assignments: ",
        CheckBox("show_completed", state.show_completed),
        Button("Update Assignment List", "assignments"),
        Button("Add Assignment", "add_assignment"),
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
        else:
            try:
                date.fromisoformat(due_date)

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

            except ValueError:
                state.form_message = (
                    "Enter the due date as YYYY-MM-DD."
                )

    course_names = [course.name for course in state.courses]

    if state.selected_course not in course_names:
        selected = course_names[0]
    else:
        selected = state.selected_course

    return Page(state, [
        Header("Add Assignment"),

        state.form_message,

        "Assignment name:",
        TextBox("assignment_name"),

        "Course:",
        SelectBox("course_name", course_names, selected),

        "Due date (YYYY-MM-DD):",
        TextBox("due_date", date.today().isoformat()),

        "Difficulty (1-5):",
        SelectBox(
            "difficulty",
            ["1", "2", "3", "4", "5"],
            "3"
        ),

        "Estimated hours:",
        TextBox("estimated_hours", 1.0, "number"),

        "Grade received (enter 0 if unknown):",
        TextBox("grade", 0.0, "number"),

        "Already completed:",
        CheckBox("completed"),

        Button("Save Assignment", "add_assignment")
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

    grade_rows = []

    for course in state.courses:
        grade_rows.append([
            course.name,
            str(course.current_grade) + "%",
            str(course.target_grade) + "%",
            str(course.weight * 100) + "%"
        ])

    course_names = [course.name for course in state.courses]

    return Page(state, [
        Header("Grades"),

        Table(
            grade_rows,
            ["Course", "Current Grade", "Target Grade",
             "Course Weight"]
        ),

        "Select a course to calculate its target grade:",
        SelectBox(
            "course_name",
            course_names,
            state.selected_course
        ),

        Button("Open Grade Calculator", "calculate_grade"),
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

        "Course: " + course.name,

        "Current grade:",
        TextBox("current_grade", course.current_grade, "number"),

        "Target grade:",
        TextBox("target_grade", course.target_grade, "number"),

        "Percentage of grade still remaining:",
        TextBox("remaining_weight", remaining_weight, "number"),

        Button("Calculate Required Score", "calculate_grade"),

        state.calculation_message,

        Button("Back to Grades", "grades")
    ])


# -------------------------
# PRIORITIES PAGE
# -------------------------

@route
def priorities(state: State) -> Page:
    """Display assignments ranked by priority score."""
    refresh_priorities(state)

    ranked_assignments = sorted(
        state.assignments,
        key=lambda assignment: assignment.priority_score,
        reverse=True
    )

    priority_list = []

    for assignment in ranked_assignments:
        if not assignment.completed:
            priority_list.append(
                assignment.name
                + " | " + assignment.course
                + " | Due: " + assignment.due_date
                + " | Priority: "
                + str(assignment.priority_score)
            )

    if not priority_list:
        priority_list = ["No unfinished assignments!"]

    return Page(state, [
        Header("Assignment Priorities"),
        "Assignments are ranked from highest to lowest priority.",
        NumberedList(priority_list),
        Button("View Assignments", "assignments"),
        Link("Return Home", "home")
    ])


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

    return Page(state, [
        Header("Academic Progress"),

        "Completed assignments: "
        + str(finished) + " out of " + str(total),

        ProgressBar(finished, max(total, 1)),

        "Completion percentage: "
        + str(round(percentage, 1)) + "%",

        "Weekly study goal (minutes):",
        TextBox(
            "weekly_study_goal",
            state.weekly_study_goal,
            "number"
        ),

        Button("Update Study Goal", "progress"),
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
    assert assert_has(page, "Target GPA")


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
    assert assert_has(page, "Chapter 4 Review")


def test_progress_route() -> None:
    """Test progress display and updating the study goal."""
    state = make_initial_state()
    page = progress(state, 300)

    assert state.weekly_study_goal == 300
    assert assert_has(page, "Completed assignments")
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
