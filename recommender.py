# backend/recommender.py

import numpy as np
from backend.db import JOBS_DATABASE, LEARNING_PATH_DATABASE

# Try to import scikit-learn for advanced matching; define fallback if not available.
SKLEARN_AVAILABLE = False
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    pass

def calculate_experience_multiplier(user_level: str, job_level: str) -> float:
    """
    Returns a compatibility multiplier based on the user's level vs. the job's level.
    """
    levels = ["Junior", "Mid", "Senior"]
    try:
        user_idx = levels.index(user_level)
        job_idx = levels.index(job_level)
    except ValueError:
        return 0.8  # Default conservative multiplier for unrecognized levels

    # Match matrix
    if user_idx == job_idx:
        return 1.0
    elif user_idx > job_idx:
        # Overqualified, still acceptable
        if user_idx - job_idx == 1:
            return 0.95
        return 0.90
    else:
        # Underqualified
        if job_idx - user_idx == 1:
            return 0.80  # Junior applying to Mid (stretch)
        return 0.50  # Junior applying to Senior (very hard)

def get_fallback_similarities(user_skills: list[str], job_listings: list[dict]) -> list[float]:
    """
    Simple Jaccard-style matching fallback if scikit-learn is not available.
    """
    scores = []
    user_skills_set = set(s.lower() for s in user_skills)
    
    for job in job_listings:
        job_skills = set(s.lower() for s in job["required_skills"])
        if not job_skills:
            scores.append(0.0)
            continue
            
        intersection = user_skills_set.intersection(job_skills)
        # Jaccard overlap score
        score = len(intersection) / len(job_skills)
        scores.append(score)
        
    return scores

def get_job_recommendations(user_skills: list[str], user_level: str = "Mid") -> list[dict]:
    """
    Computes matches between user skills and database jobs.
    Returns ranked list of jobs with match score, matched skills, missing skills,
    and a custom learning roadmap.
    """
    if not JOBS_DATABASE:
        return []

    # 1. Clean and normalize skills list
    user_skills_clean = [s.strip() for s in user_skills if s.strip()]
    user_skills_lower = [s.lower() for s in user_skills_clean]
    
    # 2. Calculate Base Skill Similarities
    base_scores = []
    if SKLEARN_AVAILABLE and len(user_skills_clean) > 0:
        try:
            # Prepare corpus where each 'document' is a list of skill strings.
            # We use a pass-through analyzer to preserve exact multi-word skills.
            corpus = [job["required_skills"] for job in JOBS_DATABASE]
            
            vectorizer = TfidfVectorizer(analyzer=lambda x: [s.lower() for s in x], lowercase=False)
            tfidf_matrix = vectorizer.fit_transform(corpus)
            user_vector = vectorizer.transform([user_skills_lower])
            
            similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
            base_scores = similarities.tolist()
        except Exception as e:
            # Fallback in case of runtime issues with tfidf vectorizer
            base_scores = get_fallback_similarities(user_skills_clean, JOBS_DATABASE)
    else:
        # Fallback to Jaccard-style score
        base_scores = get_fallback_similarities(user_skills_clean, JOBS_DATABASE)

    # 3. Assemble and rank results
    recommendations = []
    for i, job in enumerate(JOBS_DATABASE):
        # Base score
        raw_score = base_scores[i]
        
        # Apply experience alignment penalty
        exp_multiplier = calculate_experience_multiplier(user_level, job["experience_level"])
        final_score = raw_score * exp_multiplier
        
        # Determine overlapping and missing skills
        job_skills = job["required_skills"]
        matched_skills = [s for s in job_skills if s.lower() in user_skills_lower]
        missing_skills = [s for s in job_skills if s.lower() not in user_skills_lower]
        
        # Calculate skill overlap percentage for clear user display
        overlap_pct = int((len(matched_skills) / len(job_skills)) * 100) if job_skills else 0
        
        # Construct learning roadmap for missing skills
        learning_roadmap = []
        total_learning_hours = 0
        for skill in missing_skills:
            res = LEARNING_PATH_DATABASE.get(skill.lower())
            if res:
                learning_roadmap.append(res)
                total_learning_hours += res["est_hours"]
            else:
                # Add default placeholder if skill details are not in DB
                learning_roadmap.append({
                    "skill": skill,
                    "est_hours": 15,
                    "difficulty": "Intermediate",
                    "courses": [{"name": f"Introduction to {skill}", "platform": "Online Tutorials"}],
                    "books": [f"Mastering {skill} (Documentation)"],
                    "projects": [f"Create a mini-project implementing {skill}"]
                })
                total_learning_hours += 15

        recommendations.append({
            "job_id": job["id"],
            "title": job["title"],
            "company": job["company"],
            "location": job["location"],
            "department": job["department"],
            "salary_range": job["salary_range"],
            "experience_level": job["experience_level"],
            "description": job["description"],
            "match_score": round(final_score * 100),
            "overlap_pct": overlap_pct,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "learning_roadmap": learning_roadmap,
            "total_roadmap_hours": total_learning_hours
        })

    # Sort recommendations descending by match score
    recommendations.sort(key=lambda x: x["match_score"], reverse=True)
    return recommendations
