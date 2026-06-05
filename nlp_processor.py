# backend/nlp_processor.py

import re

# Domain-specific skill dictionary mapping canonical names to lists of case-insensitive aliases.
SKILL_ALIASES = {
    "Python": ["python", "py"],
    "Machine Learning": ["machine learning", "ml", "machine-learning"],
    "NLP": ["nlp", "natural language processing", "n.l.p."],
    "PyTorch": ["pytorch", "py-torch"],
    "Docker": ["docker", "dockerfile", "dockerized"],
    "Kubernetes": ["kubernetes", "k8s"],
    "AWS": ["aws", "amazon web services", "ec2", "s3"],
    "SQL": ["sql", "mysql", "postgresql", "postgres", "sqlite", "mssql"],
    "JavaScript": ["javascript", "js", "ecmascript"],
    "TypeScript": ["typescript", "ts"],
    "React": ["react", "react.js", "reactjs"],
    "Node.js": ["node.js", "nodejs", "node"],
    "Git": ["git", "github", "gitlab"],
    "HTML": ["html", "html5", "semantic html"],
    "CSS": ["css", "css3", "flexbox", "css grid", "sass", "scss"],
    "Data Science": ["data science", "data-science", "analytics"],
    "CI/CD": ["ci/cd", "cicd", "continuous integration", "continuous deployment", "github actions", "jenkins"],
    "Product Management": ["product management", "product manager", "prd", "roadmap planning"],
    "Scrum": ["scrum", "agile", "kanban", "sprints"],
    "UX Design": ["ux design", "ui/ux", "user experience", "ui/ux design", "product design", "wireframing"],
    "Figma": ["figma", "sketch", "adobe xd"],
    "Data Engineering": ["data engineering", "etl", "data pipelines", "airflow", "spark", "hadoop"],
    "Excel": ["excel", "microsoft excel", "spreadsheets"]
}

def clean_text(text: str) -> str:
    """Preprocess and clean text for matching."""
    if not text:
        return ""
    # Normalize whitespaces
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_skills(text: str) -> list[str]:
    """
    Extract skills from text based on alias matching.
    Uses custom boundary checks to safely handle punctuation-rich names (like .net, node.js, c++, c#).
    """
    if not text:
        return []
        
    cleaned_text = clean_text(text).lower()
    extracted = []

    for skill, aliases in SKILL_ALIASES.items():
        matched = False
        for alias in aliases:
            # Boundary check: alias must not be preceded or followed by alphanumeric, underscore, #, or +
            # This allows c++, c#, .net to match correctly while avoiding matching 'git' in 'digital'.
            pattern = rf"(?:^|[^a-zA-Z0-9_#+]){re.escape(alias)}(?:$|[^a-zA-Z0-9_#+])"
            if re.search(pattern, cleaned_text):
                matched = True
                break
        if matched:
            extracted.append(skill)
            
    return extracted

def extract_experience(text: str) -> dict:
    """
    Analyzes experience levels and extracts years of experience using regex.
    """
    if not text:
        return {"years": 0, "level": "Junior"}
        
    cleaned_text = clean_text(text).lower()
    
    # 1. Regex search for years of experience
    # Matches patterns like: "5 years", "3+ yrs", "10+ years of experience"
    years_patterns = [
        r"(\d+)\+?\s*(?:years?|yrs?)\b\s*(?:of)?\s*(?:experience|work)?",
        r"(?:experience|worked for)\s*(\d+)\+?\s*(?:years?|yrs?)"
    ]
    
    found_years = []
    for pattern in years_patterns:
        matches = re.findall(pattern, cleaned_text)
        for m in matches:
            try:
                found_years.append(int(m))
            except ValueError:
                pass
                
    years = max(found_years) if found_years else 0
    
    # 2. Determine Seniority Level
    if years > 0:
        if years >= 5:
            level = "Senior"
        elif years >= 2:
            level = "Mid"
        else:
            level = "Junior"
    else:
        # Fallback keyword indicators if years of experience are not explicitly listed
        senior_keywords = ["senior", "lead", "architect", "manager", "principal", "head"]
        junior_keywords = ["junior", "entry", "intern", "associate", "beginner"]
        
        is_senior = any(rf"\b{word}\b" in cleaned_text for word in senior_keywords)
        is_junior = any(rf"\b{word}\b" in cleaned_text for word in junior_keywords)
        
        if is_senior and not is_junior:
            level = "Senior"
        elif is_junior and not is_senior:
            level = "Junior"
        else:
            level = "Mid" # Default fallback
            
    return {
        "years": years,
        "level": level
    }

def analyze_resume_text(text: str) -> dict:
    """Combines skill extraction and experience parsing."""
    skills = extract_skills(text)
    exp = extract_experience(text)
    return {
        "skills": skills,
        "years_of_experience": exp["years"],
        "experience_level": exp["level"]
    }
