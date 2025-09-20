# main.py
from core_functions import recommend_jobs, analyze_skill_gaps, recommend_courses, build_resume
from data import job_seekers
import argparse


def display_recommendations(seeker):
    """
    Display job recommendations, skill gaps, course recommendations, and resume for a job seeker.
    """
    print(f"Job Recommendations for {seeker['name']}:")
    jobs_recommended = recommend_jobs(seeker)
    for job in jobs_recommended:
        print(f"- {job['title']}")

    print(f"\nSkill Gaps for {seeker['name']}:")
    gaps = analyze_skill_gaps(seeker)
    for job_title, skills in gaps.items():
        print(f"{job_title}: Missing skills - {', '.join(skills)}")

    print(f"\nCourse Recommendations for {seeker['name']}:")
    courses_recommended = recommend_courses(seeker)
    for course in courses_recommended:
        print(f"- {course['title']} from {course['provider']}")

    print("\nGenerated Resume:")
    print(build_resume(seeker))
    print("-" * 30)


def cli_mode():
    """
    Run the CLI mode for user-driven input.
    """
    name = input("Enter your name: ")
    while True:
        try:
            experience = int(input("Enter your years of experience: "))
            if experience < 0:
                print("Experience cannot be negative. Please enter a valid number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for years of experience.")
    skills_input = input("Enter your skills (comma-separated): ")
    skills = [skill.strip() for skill in skills_input.split(",") if skill.strip()]
    seeker = {"name": name, "experience": experience, "skills": skills}
    display_recommendations(seeker)

def batch_mode():
    """
    Run recommendations for all job seekers in the sample data.
    """
    for seeker in job_seekers:
        display_recommendations(seeker)

def main():
    """
    Parse arguments and run the appropriate mode.
    """
    parser = argparse.ArgumentParser(description="Job Recommendation System")
    parser.add_argument('--cli', action='store_true', help='Run in interactive CLI mode')
    args = parser.parse_args()
    if args.cli:
        cli_mode()
    else:
        batch_mode()

if __name__ == "__main__":
    main()

