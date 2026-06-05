# backend/main.py

import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.schemas import SkillsRecommendationRequest, JobCreateRequest
from backend.db import JOBS_DATABASE
from backend.nlp_processor import analyze_resume_text
from backend.recommender import get_job_recommendations
from backend.utils import extract_text_from_file

app = FastAPI(
    title="CareerMatch AI API",
    description="Backend API for parsing resumes, extracting skills, and serving job match recommendations.",
    version="1.0.0"
)

# Enable CORS for browser testing and local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Resume Parser Endpoint
@app.post("/api/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):
    """
    Accepts a PDF or TXT resume upload, extracts text,
    and returns parsed skills and experience metrics.
    """
    try:
        content = await file.read()
        filename = file.filename or "resume.txt"
        
        # Extract raw text from file bytes
        raw_text = extract_text_from_file(content, filename)
        
        if not raw_text.strip():
            raise HTTPException(
                status_code=400, 
                detail="Could not extract readable text from the uploaded file."
            )
            
        # Analyze text for skills and experience
        analysis = analyze_resume_text(raw_text)
        return {
            "success": True,
            "filename": filename,
            **analysis
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Resume analysis failed: {str(e)}")

# 2. Recommender Engine Endpoint
@app.post("/api/recommend-jobs")
async def recommend_jobs(payload: SkillsRecommendationRequest):
    """
    Computes matching job recommendations based on user skills list and experience level.
    """
    try:
        recommendations = get_job_recommendations(payload.skills, payload.experience_level)
        return {
            "success": True,
            "recommendations": recommendations
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Recommendation computation failed: {str(e)}")

# 3. Job Database Administration Endpoints
@app.get("/api/jobs")
async def get_all_jobs():
    """
    Returns the current active list of all job listings in the database.
    """
    return {
        "success": True,
        "count": len(JOBS_DATABASE),
        "jobs": JOBS_DATABASE
    }

@app.post("/api/jobs")
async def add_new_job(job: JobCreateRequest):
    """
    Allows adding new custom job descriptions dynamically to the matching database pool.
    """
    new_job_dict = {
        "id": f"job_{len(JOBS_DATABASE) + 1}",
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "department": job.department,
        "salary_range": job.salary_range,
        "experience_level": job.experience_level,
        "description": job.description,
        "required_skills": job.required_skills
    }
    JOBS_DATABASE.append(new_job_dict)
    return {
        "success": True,
        "message": "Job listing added successfully.",
        "job": new_job_dict
    }

# 4. Serving Static Web Assets
# Create static asset folders in frontend if they don't exist
os.makedirs(os.path.join("frontend", "css"), exist_ok=True)
os.makedirs(os.path.join("frontend", "js"), exist_ok=True)

# Mount css and js static dirs for clean frontend relative links
app.mount("/css", StaticFiles(directory=os.path.join("frontend", "css")), name="css")
app.mount("/js", StaticFiles(directory=os.path.join("frontend", "js")), name="js")

@app.get("/")
async def serve_index():
    """
    Serves the main frontend Single Page Application (SPA) dashboard.
    """
    index_path = os.path.join("frontend", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {
        "message": "API is online. Frontend folder index.html is missing. Check file path placements."
    }
