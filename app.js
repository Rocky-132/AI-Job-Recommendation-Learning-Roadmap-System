// frontend/js/app.js

// Global Application State
const state = {
    skills: [],
    experienceLevel: "Mid",
    jobs: [],
    selectedJobId: null,
    backendOnline: false,
    apiBaseUrl: window.location.origin // Dynamic backend URL
};

// Mock local database for offline fallback demo
const LOCAL_MOCK_JOBS = [
    {
        "id": "job_1",
        "title": "Senior Machine Learning Engineer",
        "company": "Cognitive Nexus",
        "location": "San Francisco, CA (Hybrid)",
        "department": "AI & Engineering",
        "salary_range": "$160,000 - $200,000",
        "experience_level": "Senior",
        "description": "We are seeking a Senior ML Engineer to architect and deploy large language model pipelines. You will lead a small team to build robust NLP and recommender systems utilizing PyTorch, transformer architectures, and modern MLOps pipelines.",
        "required_skills": ["Python", "Machine Learning", "NLP", "PyTorch", "Docker", "Kubernetes", "AWS", "SQL"]
    },
    {
        "id": "job_2",
        "title": "Full Stack Software Engineer",
        "company": "SaaSify Systems",
        "location": "Austin, TX (Remote)",
        "department": "Engineering",
        "salary_range": "$110,000 - $140,000",
        "experience_level": "Mid",
        "description": "Join our fast-paced product development team. You will be responsible for building frontend features in React and TypeScript while scaling backend REST services in Node.js, Express, and PostgreSQL.",
        "required_skills": ["JavaScript", "TypeScript", "React", "Node.js", "SQL", "Git", "HTML", "CSS", "Docker"]
    },
    {
        "id": "job_3",
        "title": "Junior Data Analyst",
        "company": "InsightFlow Analytics",
        "location": "New York, NY (Onsite)",
        "department": "Analytics",
        "salary_range": "$75,000 - $95,000",
        "experience_level": "Junior",
        "description": "Looking for a detail-oriented Junior Data Analyst to query databases, design BI dashboards in Tableau, and build basic statistical reports. Python and SQL skills are highly required.",
        "required_skills": ["Python", "SQL", "Excel", "Data Science", "Git"]
    },
    {
        "id": "job_6",
        "title": "Senior Frontend Developer",
        "company": "PixelCrafters Studio",
        "location": "Los Angeles, CA (Remote)",
        "department": "Design & Frontend",
        "salary_range": "$130,000 - $160,000",
        "experience_level": "Senior",
        "description": "Lead the design system implementation and core frontend architecture. Build interactive dashboard elements using React, CSS Grid/Flexbox, and ensure smooth micro-animations. Experience with UI/UX Design is a huge plus.",
        "required_skills": ["React", "JavaScript", "TypeScript", "HTML", "CSS", "UX Design", "Figma", "Git"]
    }
];

const LOCAL_MOCK_ROADMAPS = {
    "python": {
        "skill": "Python",
        "est_hours": 30,
        "difficulty": "Beginner",
        "courses": [{"name": "Python for Everybody", "platform": "Coursera"}],
        "books": ["Python Crash Course by Eric Matthes"],
        "projects": ["Build a personal portfolio website with FastAPI"]
    },
    "machine learning": {
        "skill": "Machine Learning",
        "est_hours": 60,
        "difficulty": "Intermediate",
        "courses": [{"name": "Machine Learning Specialization", "platform": "Coursera"}],
        "books": ["Hands-On Machine Learning with Scikit-Learn"],
        "projects": ["Train a classification model to predict customer churn"]
    },
    "nlp": {
        "skill": "NLP (Natural Language Processing)",
        "est_hours": 50,
        "difficulty": "Advanced",
        "courses": [{"name": "Hugging Face Course on Transformers", "platform": "Hugging Face"}],
        "books": ["Speech and Language Processing by Dan Jurafsky"],
        "projects": ["Build an interactive chat sentiment analyzer"]
    },
    "pytorch": {
        "skill": "PyTorch",
        "est_hours": 40,
        "difficulty": "Advanced",
        "courses": [{"name": "PyTorch for Deep Learning", "platform": "LearnPyTorch.io"}],
        "books": ["Deep Learning with PyTorch by Eli Stevens"],
        "projects": ["Build and train a CNN for image recognition"]
    },
    "docker": {
        "skill": "Docker",
        "est_hours": 20,
        "difficulty": "Intermediate",
        "courses": [{"name": "Docker and Kubernetes: Complete Guide", "platform": "Udemy"}],
        "books": ["Docker Deep Dive by Nigel Poulton"],
        "projects": ["Containerize a multi-service web app"]
    },
    "kubernetes": {
        "skill": "Kubernetes",
        "est_hours": 45,
        "difficulty": "Advanced",
        "courses": [{"name": "CKA Preparation", "platform": "KodeKloud"}],
        "books": ["Kubernetes up and Running by Kelsey Hightower"],
        "projects": ["Deploy a microservices application with auto-scaling"]
    },
    "aws": {
        "skill": "AWS",
        "est_hours": 35,
        "difficulty": "Intermediate",
        "courses": [{"name": "Solutions Architect Associate", "platform": "Udemy"}],
        "books": ["AWS in Action by Michael Wittig"],
        "projects": ["Host a secure static website on S3 behind CloudFront"]
    },
    "sql": {
        "skill": "SQL",
        "est_hours": 15,
        "difficulty": "Beginner",
        "courses": [{"name": "SQL for Data Science", "platform": "Coursera"}],
        "books": ["SQL Queries for Mere Mortals"],
        "projects": ["Design database schemas for an e-commerce platform"]
    },
    "react": {
        "skill": "React",
        "est_hours": 35,
        "difficulty": "Intermediate",
        "courses": [{"name": "React - The Complete Guide", "platform": "Udemy"}],
        "books": ["Learning React by Alex Banks"],
        "projects": ["Build a real-time collaborative canvas workspace"]
    },
    "ux design": {
        "skill": "UX/UI Design",
        "est_hours": 30,
        "difficulty": "Intermediate",
        "courses": [{"name": "Google UX Design Professional", "platform": "Coursera"}],
        "books": ["The Design of Everyday Things by Don Norman"],
        "projects": ["Conduct structured user interviews and map user personas"]
    }
};

const MASTER_SKILLS_LIST = [
    "Python", "Machine Learning", "NLP", "PyTorch", "Docker", 
    "Kubernetes", "AWS", "SQL", "JavaScript", "TypeScript", 
    "React", "Node.js", "Git", "HTML", "CSS", "Data Science", 
    "CI/CD", "Product Management", "Scrum", "UX Design", 
    "Figma", "Data Engineering", "Excel"
];

// Wait for DOM to load
document.addEventListener("DOMContentLoaded", () => {
    initApp();
});

function initApp() {
    setupDOMReferences();
    setupEventListeners();
    checkBackendHealth();
    
    // Periodically ping backend to monitor state
    setInterval(checkBackendHealth, 8000);
}

// Global DOM elements references
let DOM = {};
function setupDOMReferences() {
    DOM = {
        statusDot: document.getElementById("status-dot"),
        statusText: document.getElementById("status-text"),
        fileInput: document.getElementById("resume-file-input"),
        dropzone: document.getElementById("dropzone"),
        browseBtn: document.getElementById("browse-btn"),
        fileInfoContainer: document.getElementById("file-info-container"),
        uploadedFileName: document.getElementById("uploaded-file-name"),
        uploadPercentage: document.getElementById("upload-percentage"),
        progressBarFill: document.getElementById("progress-bar-fill"),
        pasteTextarea: document.getElementById("paste-resume-textarea"),
        analyzeTextBtn: document.getElementById("analyze-text-btn"),
        expLevelSelect: document.getElementById("experience-level-select"),
        expExtractedLabel: document.getElementById("experience-extracted-label"),
        detectedExpYears: document.getElementById("detected-exp-years"),
        detectedExpLevel: document.getElementById("detected-exp-level"),
        addSkillInput: document.getElementById("add-skill-input"),
        addSkillBtn: document.getElementById("add-skill-button"),
        skillsCloud: document.getElementById("skills-cloud-container"),
        matchesCountBadge: document.getElementById("matches-count-badge"),
        jobResultsContainer: document.getElementById("job-results-container"),
        roadmapContainer: document.getElementById("learning-roadmap-container")
    };
}

function setupEventListeners() {
    // Dropzone interactions
    DOM.browseBtn.addEventListener("click", () => DOM.fileInput.click());
    DOM.fileInput.addEventListener("change", handleFileSelection);
    
    DOM.dropzone.addEventListener("dragover", (e) => {
        e.preventDefault();
        DOM.dropzone.classList.add("dragover");
    });
    DOM.dropzone.addEventListener("dragleave", () => {
        DOM.dropzone.classList.remove("dragover");
    });
    DOM.dropzone.addEventListener("drop", (e) => {
        e.preventDefault();
        DOM.dropzone.classList.remove("dragover");
        if (e.dataTransfer.files.length > 0) {
            handleFile(e.dataTransfer.files[0]);
        }
    });

    // Textarea analyze button
    DOM.analyzeTextBtn.addEventListener("click", handleTextAnalysis);

    // Experience Level calibration dropdown change
    DOM.expLevelSelect.addEventListener("change", (e) => {
        state.experienceLevel = e.target.value;
        if (state.skills.length > 0) {
            triggerJobMatching();
        }
    });

    // Add skill pill listeners
    DOM.addSkillBtn.addEventListener("click", handleCustomSkillAdd);
    DOM.addSkillInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            handleCustomSkillAdd();
        }
    });
}

// Verify backend server connectivity
async function checkBackendHealth() {
    try {
        const response = await fetch(`${state.apiBaseUrl}/api/jobs`);
        if (response.ok) {
            if (!state.backendOnline) {
                state.backendOnline = true;
                DOM.statusDot.className = "status-dot dot-online";
                DOM.statusText.textContent = "Backend Online";
                console.log("Connected to FastAPI Backend.");
                // If we already have skills loaded, fetch recommendations from API
                if (state.skills.length > 0) {
                    triggerJobMatching();
                }
            }
        } else {
            setBackendOfflineState();
        }
    } catch (err) {
        setBackendOfflineState();
    }
}

function setBackendOfflineState() {
    state.backendOnline = false;
    DOM.statusDot.className = "status-dot dot-offline";
    DOM.statusText.textContent = "Demo Offline Mode";
}

// File Parsing Trigger
function handleFileSelection(e) {
    if (e.target.files.length > 0) {
        handleFile(e.target.files[0]);
    }
}

async function handleFile(file) {
    // UI feedback for upload progress
    DOM.fileInfoContainer.classList.remove("hidden");
    DOM.uploadedFileName.textContent = file.name;
    updateUploadProgress(0);
    
    // Simulate loading/upload progress indicator animation
    let progress = 0;
    const interval = setInterval(() => {
        progress += 25;
        updateUploadProgress(progress);
        if (progress >= 100) {
            clearInterval(interval);
            processUploadAPI(file);
        }
    }, 120);
}

function updateUploadProgress(percentage) {
    DOM.progressBarFill.style.width = `${percentage}%`;
    DOM.uploadPercentage.textContent = `${percentage}%`;
}

// Send resume file binary to backend
async function processUploadAPI(file) {
    if (state.backendOnline) {
        try {
            const formData = new FormData();
            formData.append("file", file);
            
            const response = await fetch(`${state.apiBaseUrl}/api/analyze-resume`, {
                method: "POST",
                body: formData
            });
            
            if (response.ok) {
                const data = await response.json();
                console.log("Extracted profile analysis:", data);
                applyExtractedProfile(data.skills, data.years_of_experience, data.experience_level);
            } else {
                alert("Backend failed parsing PDF. Falling back to local demonstration analyzer.");
                runLocalTextAnalysis(file.name + " dummy text. Python SQL React JS.");
            }
        } catch (err) {
            console.error("Upload API Error:", err);
            runLocalTextAnalysis(file.name + " dummy text. Python SQL React JS.");
        }
    } else {
        // Offline backup engine parsing mockup
        console.warn("Backend offline. Analyzing file text using fallback engine.");
        const textSeed = `${file.name} analyst programmer data science python sql machine learning aws docker git html css. 3 years experience.`;
        runLocalTextAnalysis(textSeed);
    }
}

// Paste text input submission handler
async function handleTextAnalysis() {
    const text = DOM.pasteTextarea.value.trim();
    if (!text) {
        alert("Please enter resume text to analyze.");
        return;
    }
    
    DOM.analyzeTextBtn.disabled = true;
    DOM.analyzeTextBtn.textContent = "Analyzing Profile...";
    
    if (state.backendOnline) {
        try {
            // Write temporary file blob to match file upload
            const fileBlob = new Blob([text], { type: "text/plain" });
            const formData = new FormData();
            formData.append("file", fileBlob, "resume_pasted.txt");
            
            const response = await fetch(`${state.apiBaseUrl}/api/analyze-resume`, {
                method: "POST",
                body: formData
            });
            
            if (response.ok) {
                const data = await response.json();
                applyExtractedProfile(data.skills, data.years_of_experience, data.experience_level);
            } else {
                runLocalTextAnalysis(text);
            }
        } catch (err) {
            console.error("Paste Analyze API Error:", err);
            runLocalTextAnalysis(text);
        }
    } else {
        runLocalTextAnalysis(text);
    }
    
    DOM.analyzeTextBtn.disabled = false;
    DOM.analyzeTextBtn.textContent = "Analyze Resume Text";
}

// Local Fallback text parser (NLP mock simulator)
function runLocalTextAnalysis(text) {
    const normalizedText = text.toLowerCase();
    const extractedSkills = [];
    
    // Simple word boundary scan matching master skill database
    MASTER_SKILLS_LIST.forEach(skill => {
        const escapedSkill = skill.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
        // Match boundary logic
        const regex = new RegExp(`(?:^|[^a-zA-Z0-9_#+])${escapedSkill}(?:$|[^a-zA-Z0-9_#+])`, 'i');
        if (regex.test(normalizedText)) {
            extractedSkills.push(skill);
        }
    });

    // Guess years of experience
    let years = 0;
    const yearMatch = normalizedText.match(/(\d+)\+?\s*(?:years?|yrs?)/);
    if (yearMatch) {
        years = parseInt(yearMatch[1]);
    }
    
    let level = "Mid";
    if (years >= 5 || normalizedText.includes("senior") || normalizedText.includes("lead")) {
        level = "Senior";
    } else if (years > 0 && years < 2 || normalizedText.includes("junior")) {
        level = "Junior";
    }
    
    applyExtractedProfile(extractedSkills, years, level);
}

// Bind extracted details back into the UI
function applyExtractedProfile(skills, years, level) {
    // 1. Update state
    state.skills = [...new Set(skills)];
    state.experienceLevel = level;
    
    // 2. Reflect on DOM dropdown and labels
    DOM.expLevelSelect.value = level;
    DOM.detectedExpYears.textContent = years;
    DOM.detectedExpLevel.textContent = level;
    DOM.expExtractedLabel.classList.remove("hidden");
    
    // 3. Render and compute recommendations
    renderSkillsCloud();
    triggerJobMatching();
}

// Custom manual skill insertion
function handleCustomSkillAdd() {
    const rawVal = DOM.addSkillInput.value.trim();
    if (!rawVal) return;
    
    // Capitalize correctly based on master list if matches, otherwise keep as is
    const matchedMaster = MASTER_SKILLS_LIST.find(s => s.toLowerCase() === rawVal.toLowerCase());
    const finalSkillName = matchedMaster || rawVal;
    
    if (!state.skills.includes(finalSkillName)) {
        state.skills.push(finalSkillName);
        renderSkillsCloud();
        triggerJobMatching();
    }
    
    DOM.addSkillInput.value = "";
}

// Remove skill tag chip
function handleSkillRemove(skillName) {
    state.skills = state.skills.filter(s => s !== skillName);
    renderSkillsCloud();
    triggerJobMatching();
}

// Render Skill Pill Cloud DOM
function renderSkillsCloud() {
    DOM.skillsCloud.innerHTML = "";
    
    if (state.skills.length === 0) {
        DOM.skillsCloud.innerHTML = `<p class="empty-cloud-message">No skills loaded yet. Upload your resume or add custom skills manually.</p>`;
        return;
    }
    
    state.skills.forEach(skill => {
        const skillTag = document.createElement("div");
        skillTag.className = "skill-tag";
        skillTag.innerHTML = `
            <span>${skill}</span>
            <span class="skill-tag-remove"><i class="fa-solid fa-xmark"></i></span>
        `;
        
        skillTag.querySelector(".skill-tag-remove").addEventListener("click", (e) => {
            e.stopPropagation();
            handleSkillRemove(skill);
        });
        
        DOM.skillsCloud.appendChild(skillTag);
    });
}

// Launch Matching Pipeline (API or Offline calculations)
async function triggerJobMatching() {
    if (state.skills.length === 0) {
        renderJobMatches([]);
        return;
    }
    
    if (state.backendOnline) {
        try {
            const response = await fetch(`${state.apiBaseUrl}/api/recommend-jobs`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    skills: state.skills,
                    experience_level: state.experienceLevel
                })
            });
            
            if (response.ok) {
                const data = await response.json();
                state.jobs = data.recommendations;
                renderJobMatches(state.jobs);
            } else {
                runLocalJobMatching();
            }
        } catch (err) {
            console.error("Match API Error:", err);
            runLocalJobMatching();
        }
    } else {
        runLocalJobMatching();
    }
}

// Local Fallback Recommender Engine Logic
function runLocalJobMatching() {
    console.warn("Performing Jaccard overlap job matching locally.");
    const userSkillsSet = new Set(state.skills.map(s => s.toLowerCase()));
    const results = [];
    
    LOCAL_MOCK_JOBS.forEach((job, idx) => {
        const requiredSkillsLower = job.required_skills.map(s => s.toLowerCase());
        const matchIntersection = requiredSkillsLower.filter(s => userSkillsSet.has(s));
        
        // Jaccard similarity percentage
        const baseRatio = requiredSkillsLower.length > 0 ? (matchIntersection.length / requiredSkillsLower.length) : 0;
        
        // Experience alignment factor
        let expMultiplier = 1.0;
        if (state.experienceLevel === "Junior" && job.experience_level === "Senior") {
            expMultiplier = 0.5;
        } else if (state.experienceLevel === "Junior" && job.experience_level === "Mid") {
            expMultiplier = 0.8;
        } else if (state.experienceLevel === "Mid" && job.experience_level === "Senior") {
            expMultiplier = 0.85;
        }
        
        const finalScore = Math.round(baseRatio * expMultiplier * 100);
        const missingSkills = job.required_skills.filter(s => !state.skills.map(us => us.toLowerCase()).includes(s.toLowerCase()));
        
        // Populate custom learning roadmap for missing skills
        const roadmap = [];
        let totalHours = 0;
        missingSkills.forEach(skill => {
            const pathRes = LOCAL_MOCK_ROADMAPS[skill.toLowerCase()];
            if (pathRes) {
                roadmap.push(pathRes);
                totalHours += pathRes.est_hours;
            } else {
                const genericPath = {
                    skill: skill,
                    est_hours: 15,
                    difficulty: "Intermediate",
                    courses: [{"name": `Introduction to ${skill}`, "platform": "Online Course"}],
                    books: [`Mastering ${skill}`],
                    projects: [`Deploy a ${skill} application`]
                };
                roadmap.push(genericPath);
                totalHours += 15;
            }
        });

        results.push({
            job_id: job.id,
            title: job.title,
            company: job.company,
            location: job.location,
            department: job.department,
            salary_range: job.salary_range,
            experience_level: job.experience_level,
            description: job.description,
            match_score: finalScore,
            overlap_pct: Math.round(baseRatio * 100),
            matched_skills: matchIntersection.map(s => {
                // Return casing correct name
                return job.required_skills.find(os => os.toLowerCase() === s) || s;
            }),
            missing_skills: missingSkills,
            learning_roadmap: roadmap,
            total_roadmap_hours: totalHours
        });
    });
    
    // Sort descending score
    results.sort((a, b) => b.match_score - a.match_score);
    state.jobs = results;
    renderJobMatches(results);
}

// Render Job Match Cards Feed
function renderJobMatches(jobsList) {
    DOM.jobResultsContainer.innerHTML = "";
    DOM.matchesCountBadge.textContent = `${jobsList.length} Matches`;
    
    if (jobsList.length === 0) {
        DOM.jobResultsContainer.innerHTML = `
            <div class="empty-results-card glass-card">
                <div class="empty-icon-bubble"><i class="fa-solid fa-search"></i></div>
                <h3>No Job Matches Found</h3>
                <p>Try refining your skill tags list or adjusting the seniority level selection to find compatible jobs.</p>
            </div>
        `;
        renderRoadmapEmptyState();
        return;
    }
    
    jobsList.forEach((job, index) => {
        const jobCard = document.createElement("article");
        jobCard.className = `glass-card job-card ${state.selectedJobId === job.job_id ? 'selected-job' : ''}`;
        jobCard.dataset.jobId = job.job_id;
        
        // Choose logo class based on index
        const logoIndexClass = `bg-logo-${(index % 3) + 1}`;
        const firstLetter = job.company.charAt(0);
        
        // Set circular SVG stroke variables
        const radius = 24;
        const circumference = 2 * Math.PI * radius;
        const offset = circumference - (job.match_score / 100) * circumference;
        
        // Class rating for circle color
        let ratingColorClass = "low-match";
        if (job.match_score >= 75) ratingColorClass = "high-match";
        else if (job.match_score >= 40) ratingColorClass = "mid-match";

        jobCard.innerHTML = `
            <div class="job-card-header">
                <div class="job-card-info-group">
                    <div class="company-logo-circle ${logoIndexClass}">${firstLetter}</div>
                    <div class="job-titles-block">
                        <h3>${job.title}</h3>
                        <span class="job-company-name">${job.company}</span>
                    </div>
                </div>
                
                <!-- Matching Circle Progress SVGs -->
                <div class="score-circle-wrapper">
                    <svg class="svg-score-circle">
                        <circle class="circle-track" cx="27" cy="27" r="${radius}"></circle>
                        <circle class="circle-fill ${ratingColorClass}" cx="27" cy="27" r="${radius}" 
                                stroke-dasharray="${circumference}" stroke-dashoffset="${offset}"></circle>
                    </svg>
                    <div class="score-text-label">${job.match_score}%</div>
                </div>
            </div>
            
            <div class="job-meta-flex">
                <span class="job-meta-item"><i class="fa-solid fa-folder"></i> ${job.department}</span>
                <span class="job-meta-item"><i class="fa-solid fa-location-dot"></i> ${job.location}</span>
                <span class="job-meta-item"><i class="fa-solid fa-money-bill-wave"></i> ${job.salary_range}</span>
                <span class="job-meta-item"><i class="fa-solid fa-signal"></i> ${job.experience_level}</span>
            </div>
            
            <p class="job-description-teaser">${job.description}</p>
            
            <div class="job-skills-showcase">
                <span class="skills-group-title">Job Requirements</span>
                <div class="job-skills-wrap">
                    ${job.matched_skills.map(s => `<span class="job-skill-pill match"><i class="fa-solid fa-circle-check"></i> ${s}</span>`).join('')}
                    ${job.missing_skills.map(s => `<span class="job-skill-pill missing"><i class="fa-solid fa-circle-xmark"></i> ${s}</span>`).join('')}
                </div>
            </div>
        `;
        
        jobCard.addEventListener("click", () => {
            selectJobRecommendation(job.job_id);
        });
        
        DOM.jobResultsContainer.appendChild(jobCard);
    });

    // Auto-select first job if none selected
    if (jobsList.length > 0) {
        if (!state.selectedJobId || !jobsList.find(j => j.job_id === state.selectedJobId)) {
            selectJobRecommendation(jobsList[0].job_id);
        } else {
            // Update selected roadmap details panel
            const currentSelected = jobsList.find(j => j.job_id === state.selectedJobId);
            renderLearningRoadmap(currentSelected);
        }
    }
}

// Select a job item to display its timeline roadmap
function selectJobRecommendation(jobId) {
    state.selectedJobId = jobId;
    
    // Toggle active visual card classes
    document.querySelectorAll(".job-card").forEach(card => {
        if (card.dataset.jobId === jobId) {
            card.classList.add("selected-job");
        } else {
            card.classList.remove("selected-job");
        }
    });
    
    const matchedJob = state.jobs.find(j => j.job_id === jobId);
    if (matchedJob) {
        renderLearningRoadmap(matchedJob);
    }
}

// Render personalized Learning Path Roadmap details panel
function renderLearningRoadmap(job) {
    DOM.roadmapContainer.innerHTML = "";
    
    if (!job.missing_skills || job.missing_skills.length === 0) {
        DOM.roadmapContainer.innerHTML = `
            <div class="roadmap-card glass-card text-center flex-column justify-center align-center" style="padding: 48px 24px;">
                <div class="empty-icon-bubble" style="background: rgba(16, 185, 129, 0.1); border-color: rgba(16, 185, 129, 0.2); color: var(--accent-emerald);">
                    <i class="fa-solid fa-circle-check"></i>
                </div>
                <h3>100% Match Reached!</h3>
                <p>Congratulations, you possess all the required skills for the <strong>${job.title}</strong> role at <strong>${job.company}</strong>. No skill gaps identified to build a roadmap.</p>
            </div>
        `;
        return;
    }
    
    const totalMissing = job.missing_skills.length;
    
    const roadmapLayout = document.createElement("div");
    roadmapLayout.className = "roadmap-card glass-card";
    roadmapLayout.innerHTML = `
        <div class="roadmap-overview-panel">
            <h3 class="roadmap-target-title">Target: ${job.title} (${job.company})</h3>
            <div class="roadmap-stats-row">
                <div class="roadmap-stat-item">
                    <span class="roadmap-stat-value">${totalMissing}</span>
                    <span class="roadmap-stat-label">Missing Skills</span>
                </div>
                <div class="roadmap-stat-item">
                    <span class="roadmap-stat-value">${job.total_roadmap_hours}h</span>
                    <span class="roadmap-stat-label">Est. Study Time</span>
                </div>
                <div class="roadmap-stat-item">
                    <span class="roadmap-stat-value">${job.overlap_pct}%</span>
                    <span class="roadmap-stat-label">Initial Overlap</span>
                </div>
            </div>
        </div>
        
        <!-- Timeline vertical track list -->
        <div class="roadmap-timeline">
            ${job.learning_roadmap.map((item, idx) => `
                <div class="timeline-node">
                    <div class="timeline-bullet"></div>
                    <div class="timeline-node-card">
                        <div class="timeline-skill-header">
                            <h4 class="timeline-skill-name">${item.skill}</h4>
                            <span class="timeline-hours-badge">${item.est_hours} hrs (${item.difficulty})</span>
                        </div>
                        
                        <div class="timeline-section-row">
                            <h5 class="timeline-section-title"><i class="fa-solid fa-video"></i> Recommended Courses</h5>
                            <ul class="timeline-items-list">
                                ${item.courses.map(c => `<li><strong>${c.name}</strong> - ${c.platform}</li>`).join('')}
                            </ul>
                        </div>
                        
                        <div class="timeline-section-row">
                            <h5 class="timeline-section-title"><i class="fa-solid fa-book"></i> Reference Books</h5>
                            <ul class="timeline-items-list">
                                ${item.books.map(b => `<li>${b}</li>`).join('')}
                            </ul>
                        </div>
                        
                        <div class="timeline-section-row">
                            <h5 class="timeline-section-title"><i class="fa-solid fa-code-fork"></i> Hands-on Practice Projects</h5>
                            <ul class="timeline-items-list">
                                ${item.projects.map(p => `<li>${p}</li>`).join('')}
                            </ul>
                        </div>
                    </div>
                </div>
            `).join('')}
        </div>
    `;
    
    DOM.roadmapContainer.appendChild(roadmapLayout);
}

function renderRoadmapEmptyState() {
    DOM.roadmapContainer.innerHTML = `
        <div class="empty-roadmap-card glass-card">
            <div class="empty-icon-bubble"><i class="fa-solid fa-map-signs"></i></div>
            <h3>Roadmap Building Tool</h3>
            <p>Select a job match on the left to generate a personalized learning roadmap. We'll identify your missing skills and compile targeted resources to bridge the gap.</p>
        </div>
    `;
}
