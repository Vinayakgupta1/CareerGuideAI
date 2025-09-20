# core_functions.py
from data import jobs, courses, job_seekers

def recommend_jobs(seeker):
    """
    Recommend jobs for a job seeker based on matching skills.
    Returns a list of job dicts where the seeker has at least one required skill.
    """
    recommendations = []
    for job in jobs:
        # Count the number of matching skills
        skill_match = len(set(seeker["skills"]).intersection(set(job["skills_required"])))
        if skill_match > 0:
            recommendations.append(job)
    return recommendations


def analyze_skill_gaps(seeker):
    """
    Analyze skill gaps for a job seeker for each job.
    Returns a dict: {job_title: set of missing skills}
    """
    gaps = {}
    for job in jobs:
        # Find skills required by the job that the seeker does not have
        missing_skills = set(job["skills_required"]) - set(seeker["skills"])
        if missing_skills:
            gaps[job["title"]] = missing_skills
    return gaps

def recommend_courses(seeker):
    """
    Recommend courses to fill the skill gaps for a job seeker.
    Returns a list of course dicts that target missing skills.
    """
    recommended_courses = []
    gaps = analyze_skill_gaps(seeker)
    for job_title, missing_skills in gaps.items():
        for course in courses:
            # Recommend course if it targets any missing skill
            if any(skill in course["skills_targeted"] for skill in missing_skills):
                recommended_courses.append(course)
    return recommended_courses

def build_resume(seeker):
    """
    Build a simple resume string for the job seeker.
    """
    resume = f"Resume for {seeker['name']}\n"
    resume += "Skills:\n"
    resume += "\n".join(seeker["skills"]) + "\n"
    resume += "Experience:\n"
    resume += f"{seeker['experience']} years\n"
    return resume
