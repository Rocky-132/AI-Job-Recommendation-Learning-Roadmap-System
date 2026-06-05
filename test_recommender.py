# backend/test_recommender.py

import sys
import os

# Append workspace directory to Python system path to resolve backend imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.nlp_processor import analyze_resume_text
from backend.recommender import get_job_recommendations

def test_resume_nlp_processor():
    print("Testing Resume NLP Processor...")
    
    # Test case 1: Senior Data Scientist resume text
    resume_text_1 = """
    John Doe
    Lead Machine Learning Engineer
    Over 6 years of experience working with Python, PyTorch, Docker, and SQL.
    Developed scalable ML pipelines and natural language processing (NLP) models.
    Familiar with Git and cloud workflows on AWS.
    """
    
    analysis_1 = analyze_resume_text(resume_text_1)
    
    print(f"Extracted Skills: {analysis_1['skills']}")
    print(f"Years of Experience: {analysis_1['years_of_experience']}")
    print(f"Experience Level: {analysis_1['experience_level']}")
    
    # Assertions
    assert "Python" in analysis_1["skills"]
    assert "Machine Learning" in analysis_1["skills"]
    assert "NLP" in analysis_1["skills"]
    assert "PyTorch" in analysis_1["skills"]
    assert "SQL" in analysis_1["skills"]
    assert "Git" in analysis_1["skills"]
    assert "AWS" in analysis_1["skills"]
    assert analysis_1["years_of_experience"] == 6
    assert analysis_1["experience_level"] == "Senior"
    
    print("NLP processor tests passed successfully!\n")
    return analysis_1

def test_recommender_matching(user_profile):
    print("Testing Recommender Matching Engine...")
    
    skills = user_profile["skills"]
    level = user_profile["experience_level"]
    
    recommendations = get_job_recommendations(skills, level)
    
    # Print ranked matches
    print("Ranked Job Matches:")
    for rank, job in enumerate(recommendations[:3], 1):
        print(f"  {rank}. {job['title']} at {job['company']} - Match: {job['match_score']}% (Overlap: {job['overlap_pct']}%)")
        print(f"     Matched Skills: {job['matched_skills']}")
        print(f"     Missing Skills: {job['missing_skills']}")
        print(f"     Roadmap Hours: {job['total_roadmap_hours']} hrs")
        print()
        
    # Assertions
    # Job 1 (Senior Machine Learning Engineer) should be the top recommendation since user has 6 years (Senior) 
    # and has most required skills: Python, Machine Learning, NLP, PyTorch, Docker, AWS, SQL (7/8 skills matched).
    top_match = recommendations[0]
    assert top_match["title"] == "Senior Machine Learning Engineer"
    assert top_match["match_score"] > 80
    assert "Kubernetes" in top_match["missing_skills"]
    
    # Verify roadmap structure exists
    assert len(top_match["learning_roadmap"]) > 0
    k8s_roadmap = next((item for item in top_match["learning_roadmap"] if item["skill"].lower() == "kubernetes"), None)
    assert k8s_roadmap is not None
    assert k8s_roadmap["est_hours"] > 0
    assert len(k8s_roadmap["courses"]) > 0
    
    print("Recommender engine tests passed successfully!\n")

if __name__ == "__main__":
    try:
        profile = test_resume_nlp_processor()
        test_recommender_matching(profile)
        print("ALL BACKEND VERIFICATION TESTS PASSED!")
    except AssertionError as e:
        print(f"Verification test FAILED: Assertion error.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Verification test FAILED: {str(e)}", file=sys.stderr)
        sys.exit(1)
