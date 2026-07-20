case_base = [
    {
        "case_id": 1,
        "Course": "Calculus 101",
        "Course Department": "Mathematics",
        "Assignment Submission Status": "Always on Time",
        "Test Performance": "Average",
        "Participation in Class Activities": "Minimal",
        "Private Consultation with Instructor": "Never",
        "Specific Learning Difficulties": "Algebraic Manipulation",
        "Solution": "focus on practicing problems and seek help from the instructor during office hours."
    },
    {
        "case_id": 2,
        "Course": "Linear Algebra 201",
        "Course Department": "Mathematics",
        "Assignment Submission Status": "Sometimes Late",
        "Test Performance": "Below Average",
        "Participation in Class Activities": "Moderate",
        "Private Consultation with Instructor": "Occasionally",
        "Specific Learning Difficulties": "Vector Spaces",
        "Solution": "focus on understanding the theoretical concepts and practice solving problems related to vector spaces."
    },
    {
        "case_id": 3,
        "Course": "Physics 101",
        "Course Department": "Physics",
        "Assignment Submission Status": "Always Late",
        "Test Performance": "Poor",
        "Participation in Class Activities": "Minimal",
        "Private Consultation with Instructor": "Never",
        "Specific Learning Difficulties": "Mechanics",
        "Solution": "participate more in class and try to do assignments and seek consultation with the instructor."
    },
    {
        "case_id": 4,
        "Course": "Chemistry 101",
        "Course Department": "Chemistry",
        "Assignment Submission Status": "Always on Time",
        "Test Performance": "Average",
        "Participation in Class Activities": "Active",
        "Private Consultation with Instructor": "Occasionally",
        "Specific Learning Difficulties": "Organic Chemistry",
        "Solution": "focus on understanding the concepts and practice solving problems related to organic chemistry."
    },
    {
        "case_id": 5,
        "Course": "Biology 101",
        "Course Department": "Biology",
        "Assignment Submission Status": "Sometimes Late",
        "Test Performance": "Below Average",
        "Participation in Class Activities": "Moderate",
        "Private Consultation with Instructor": "Occasionally",
        "Specific Learning Difficulties": "Cell Biology",
        "Solution": "focus on understanding the cellular processes and practice solving problems related to cell biology."
    },
    {
        "case_id": 6,
        "Course": "Computer Science 101",
        "Course Department": "Computer Science",
        "Assignment Submission Status": "Always on Time",
        "Test Performance": "Above Average",
        "Participation in Class Activities": "Active",
        "Private Consultation with Instructor": "Occasionally",
        "Specific Learning Difficulties": "Programming Concepts",
        "Solution": "focus on practicing programming problems and seek help from the instructor during office hours."
    },
    {
        "case_id": 7,
        "Course": "Economics 101",
        "Course Department": "Economics",
        "Assignment Submission Status": "Sometimes Late",
        "Test Performance": "Average",
        "Participation in Class Activities": "Moderate",
        "Private Consultation with Instructor": "Occasionally",
        "Specific Learning Difficulties": "Microeconomics",
        "Solution": "focus on understanding the microeconomic concepts and practice solving problems related to microeconomics."
    },
    {
        "case_id": 8,
        "Course": "Psychology 101",
        "Course Department": "Psychology",
        "Assignment Submission Status": "Always on Time",
        "Test Performance": "Above Average",
        "Participation in Class Activities": "Active",
        "Private Consultation with Instructor": "Occasionally",
        "Specific Learning Difficulties": "Cognitive Psychology",
        "Solution": "focus on understanding the cognitive processes and practice solving problems related to cognitive psychology."
    }
]


def get_new_case():
    new_case = {
        "course": input("Enter the course name: "),
        "course_department": input("Enter the course department: "),
        "assignment_submission_status": input("Enter the assignment submission status (Always on Time, Sometimes Late, Always Late): "),
        "test_performance": input("Enter the test performance (Above Average, Average, Below Average, Poor): "),
        "participation_in_class_activities": input("Enter the participation in class activities (Active, Moderate, Minimal): "),
        "private_consultation_with_instructor": input("Enter the private consultation with instructor (Always, Occasionally, Never): "),
        "specific_learning_difficulties": input("Enter the specific learning difficulties: ")
    }
    return new_case


def calculate_similarity(new_case, case_base):
    score = 0
    for case in case_base:
        if new_case.get("course") == case.get("Course"):
            score += 1
        if new_case.get("course_department") == case.get("Course Department"):
            score += 2
    if new_case.get("assignment_submission_status") == case.get("Assignment Submission Status"):
        score += 3
    if new_case.get("test_performance") == case.get("Test Performance"):
        score += 4
    if new_case.get("participation_in_class_activities") == case.get("Participation in Class Activities"):
        score += 3
    if new_case.get("private_consultation_with_instructor") == case.get("Private Consultation with Instructor"):
        score += 2
    if new_case.get("specific_learning_difficulties") == case.get("Specific Learning Difficulties"):
        score += 1
    return score


def retrieve_best_case(new_case, case_base):
    best_case = None
    best_score = -1
    for case in case_base:
        score = calculate_similarity(new_case, case)
        if score > best_score:
            best_score = score
            best_case = case
    return best_case, best_score

similarity_percentage = (best_score / 16) * 100 if best_score != -1 else 0

