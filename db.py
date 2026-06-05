# backend/db.py

JOBS_DATABASE = [
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
        "id": "job_4",
        "title": "Lead DevOps Architect",
        "company": "CloudScale Solutions",
        "location": "Seattle, WA (Remote)",
        "department": "Infrastructure",
        "salary_range": "$175,000 - $210,000",
        "experience_level": "Senior",
        "description": "Architect cloud-native infrastructure solutions. You will build and optimize automated CI/CD pipelines, configure Terraform scripts, manage massive Kubernetes clusters, and oversee multi-region AWS cloud environments.",
        "required_skills": ["Docker", "Kubernetes", "AWS", "CI/CD", "Git", "Python", "SQL"]
    },
    {
        "id": "job_5",
        "title": "Product Manager - AI Platform",
        "company": "Vertex AI",
        "location": "San Francisco, CA (Hybrid)",
        "department": "Product",
        "salary_range": "$140,000 - $180,000",
        "experience_level": "Senior",
        "description": "Drive the product lifecycle of our new developer tools. Partner with engineering and ML research teams to build NLP APIs. Strong understanding of Agile frameworks, Scrum, and basic data science concepts is required.",
        "required_skills": ["Product Management", "Scrum", "Data Science", "NLP"]
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
    },
    {
        "id": "job_7",
        "title": "Data Engineer",
        "company": "StreamPipe Systems",
        "location": "Chicago, IL (Hybrid)",
        "department": "Data Platform",
        "salary_range": "$125,000 - $150,000",
        "experience_level": "Mid",
        "description": "Design and build data warehouses and ETL pipelines. You will capture stream and batch data using Apache Spark, structure databases in PostgreSQL, and orchestrate pipelines using Docker and airflow.",
        "required_skills": ["Python", "SQL", "Data Engineering", "Docker", "AWS", "Git"]
    },
    {
        "id": "job_8",
        "title": "UI/UX Product Designer",
        "company": "PixelCrafters Studio",
        "location": "Los Angeles, CA (Remote)",
        "department": "Design",
        "salary_range": "$90,000 - $120,000",
        "experience_level": "Mid",
        "description": "Craft intuitive designs, wireframes, and high-fidelity mockups. You will map user journeys and collaborate with engineers to ensure pixel-perfect CSS frontend integrations. Mastery of Figma and design systems is required.",
        "required_skills": ["UX Design", "Figma", "HTML", "CSS", "JavaScript"]
    }
]

LEARNING_PATH_DATABASE = {
    "python": {
        "skill": "Python",
        "est_hours": 30,
        "difficulty": "Beginner",
        "courses": [
            {"name": "Python for Everybody Specialization", "platform": "Coursera"},
            {"name": "Complete Python Bootcamp: Go from Zero to Hero", "platform": "Udemy"}
        ],
        "books": ["Python Crash Course by Eric Matthes", "Fluent Python by Luciano Ramalho"],
        "projects": [
            "Build a personal portfolio website with FastAPI/Flask",
            "Write a script to automate daily report parsing and data scraping"
        ]
    },
    "machine learning": {
        "skill": "Machine Learning",
        "est_hours": 60,
        "difficulty": "Intermediate",
        "courses": [
            {"name": "Machine Learning Specialization by Andrew Ng", "platform": "DeepLearning.AI / Coursera"},
            {"name": "Applied Machine Learning in Python", "platform": "Coursera"}
        ],
        "books": ["Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron"],
        "projects": [
            "Train a classification model to predict customer churn using Scikit-Learn",
            "Build a movie recommendation engine using collaborative filtering techniques"
        ]
    },
    "nlp": {
        "skill": "NLP (Natural Language Processing)",
        "est_hours": 50,
        "difficulty": "Advanced",
        "courses": [
            {"name": "Natural Language Processing Specialization", "platform": "DeepLearning.AI"},
            {"name": "Hugging Face Course on Transformers", "platform": "Hugging Face"}
        ],
        "books": ["Speech and Language Processing by Dan Jurafsky & James H. Martin"],
        "projects": [
            "Build an interactive chat sentiment analyzer",
            "Train a Named Entity Recognition (NER) model to parse resumes"
        ]
    },
    "pytorch": {
        "skill": "PyTorch",
        "est_hours": 40,
        "difficulty": "Advanced",
        "courses": [
            {"name": "Deep Learning with PyTorch: Zero to GANs", "platform": "Jovian.ai"},
            {"name": "PyTorch for Deep Learning Bootcamp", "platform": "LearnPyTorch.io"}
        ],
        "books": ["Deep Learning with PyTorch by Eli Stevens, Luca Antiga, and Thomas Viehmann"],
        "projects": [
            "Build and train a convolutional neural network (CNN) for image recognition",
            "Finetune a small GPT model using custom text files"
        ]
    },
    "docker": {
        "skill": "Docker",
        "est_hours": 20,
        "difficulty": "Intermediate",
        "courses": [
            {"name": "Docker and Kubernetes: The Complete Guide", "platform": "Udemy"},
            {"name": "Docker for Beginners", "platform": "Docker Official Labs"}
        ],
        "books": ["Docker Deep Dive by Nigel Poulton"],
        "projects": [
            "Containerize a multi-service web app (FastAPI backend + React frontend + PostgreSQL)",
            "Optimize container sizes using multi-stage builds"
        ]
    },
    "kubernetes": {
        "skill": "Kubernetes",
        "est_hours": 45,
        "difficulty": "Advanced",
        "courses": [
            {"name": "Certified Kubernetes Administrator (CKA)", "platform": "KodeKloud / Udemy"},
            {"name": "Kubernetes: Getting Started", "platform": "Pluralsight"}
        ],
        "books": ["Kubernetes up and Running by Kelsey Hightower"],
        "projects": [
            "Deploy a microservices application with load balancing and auto-scaling rules",
            "Configure helm charts and ingress controllers for production setup"
        ]
    },
    "aws": {
        "skill": "AWS",
        "est_hours": 35,
        "difficulty": "Intermediate",
        "courses": [
            {"name": "AWS Certified Solutions Architect Associate", "platform": "Cantrill.io / Udemy"},
            {"name": "AWS Technical Essentials", "platform": "Coursera"}
        ],
        "books": ["AWS in Action by Michael Wittig and Andreas Wittig"],
        "projects": [
            "Host a secure static website on S3 behind CloudFront with SSL",
            "Build a serverless pipeline using API Gateway, Lambda, and DynamoDB"
        ]
    },
    "sql": {
        "skill": "SQL",
        "est_hours": 15,
        "difficulty": "Beginner",
        "courses": [
            {"name": "SQL for Data Science", "platform": "Coursera"},
            {"name": "The Ultimate MySQL Bootcamp", "platform": "Udemy"}
        ],
        "books": ["SQL Queries for Mere Mortals by John L. Viescas"],
        "projects": [
            "Design database schemas for an e-commerce platform and write complex analytical queries",
            "Optimize long-running query execution times using indices and partition tables"
        ]
    },
    "javascript": {
        "skill": "JavaScript",
        "est_hours": 25,
        "difficulty": "Beginner",
        "courses": [
            {"name": "The Complete JavaScript Course 2026", "platform": "Udemy"},
            {"name": "JavaScript: The Hard Parts", "platform": "Frontend Masters"}
        ],
        "books": ["You Don't Know JS Yet by Kyle Simpson", "Eloquent JavaScript by Marijn Haverbeke"],
        "projects": [
            "Build an interactive task planner dashboard with drag-and-drop actions",
            "Build a client-side API caching layer using localStorage and Fetch API"
        ]
    },
    "typescript": {
        "skill": "TypeScript",
        "est_hours": 20,
        "difficulty": "Intermediate",
        "courses": [
            {"name": "Understanding TypeScript", "platform": "Udemy"},
            {"name": "TypeScript Deep Dive", "platform": "GitBook"}
        ],
        "books": ["Effective TypeScript by Dan Vanderkam"],
        "projects": [
            "Refactor a JavaScript library to be strictly typed with interfaces and generics",
            "Create a type-safe API helper layer wrapper for a frontend client"
        ]
    },
    "react": {
        "skill": "React",
        "est_hours": 35,
        "difficulty": "Intermediate",
        "courses": [
            {"name": "React - The Complete Guide (incl. Next.js)", "platform": "Udemy"},
            {"name": "Full Stack Open", "platform": "University of Helsinki"}
        ],
        "books": ["Learning React by Alex Banks and Eve Porcello"],
        "projects": [
            "Build a real-time collaborative workspace canvas using WebSockets",
            "Create a custom React state management hook library with context optimization"
        ]
    },
    "node.js": {
        "skill": "Node.js",
        "est_hours": 30,
        "difficulty": "Intermediate",
        "courses": [
            {"name": "The Complete Node.js Developer Course", "platform": "Udemy"},
            {"name": "Node.js Design Patterns", "platform": "NodePatterns"}
        ],
        "books": ["Node.js Design Patterns by Mario Casciaro and Luciano Mammino"],
        "projects": [
            "Build a scalable file compression and streaming server backend",
            "Create a secure OAuth2 server using Express and JWT authentication"
        ]
    },
    "git": {
        "skill": "Git",
        "est_hours": 10,
        "difficulty": "Beginner",
        "courses": [
            {"name": "Git & GitHub Bootcamp", "platform": "Udemy"},
            {"name": "Introduction to Git", "platform": "GitHub Skills"}
        ],
        "books": ["Pro Git by Scott Chacon and Ben Straub"],
        "projects": [
            "Set up multi-branch deployment workflows with git hooks",
            "Successfully resolve a complex repository merge conflict structure manually"
        ]
    },
    "html": {
        "skill": "HTML & Semantics",
        "est_hours": 8,
        "difficulty": "Beginner",
        "courses": [
            {"name": "HTML & CSS for Beginners", "platform": "freeCodeCamp"},
            {"name": "Web Accessibility (A11y)", "platform": "Udacity"}
        ],
        "books": ["HTML and CSS: Design and Build Websites by Jon Duckett"],
        "projects": [
            "Refactor a layout to use complete semantic HTML5 landmarks",
            "Build an accessible user registration form complying with WCAG guidelines"
        ]
    },
    "css": {
        "skill": "CSS & Modern Layouts",
        "est_hours": 15,
        "difficulty": "Beginner",
        "courses": [
            {"name": "CSS Demystified", "platform": "Kevin Powell"},
            {"name": "Advanced CSS and Sass", "platform": "Udemy"}
        ],
        "books": ["CSS Secrets by Lea Verou"],
        "projects": [
            "Design and build a responsive dashboard layouts using purely CSS Grid and Flexbox",
            "Implement a dark/light mode toggle with custom CSS custom properties (variables)"
        ]
    },
    "data science": {
        "skill": "Data Science",
        "est_hours": 50,
        "difficulty": "Intermediate",
        "courses": [
            {"name": "Data Science Specialization", "platform": "Johns Hopkins / Coursera"},
            {"name": "Python for Data Science and Machine Learning Bootcamp", "platform": "Udemy"}
        ],
        "books": ["Python for Data Analysis by Wes McKinney", "Introduction to Probability by Joseph K. Blitzstein"],
        "projects": [
            "Perform Exploratory Data Analysis (EDA) on a dataset of 1M rows using Pandas & Seaborn",
            "Clean and resolve noisy timeseries sensor logs for anomaly profiling"
        ]
    },
    "ci/cd": {
        "skill": "CI/CD Pipelines",
        "est_hours": 20,
        "difficulty": "Intermediate",
        "courses": [
            {"name": "GitHub Actions: Automated Workflows", "platform": "Udemy"},
            {"name": "DevOps Foundations: CI/CD", "platform": "LinkedIn Learning"}
        ],
        "books": ["Continuous Delivery by Jez Humble and David Farley"],
        "projects": [
            "Configure a GitHub Action to run test suites, lint code, and build containers automatically",
            "Set up blue-green deploy pipelines on an application cluster using ArgoCD"
        ]
    },
    "product management": {
        "skill": "Product Management",
        "est_hours": 40,
        "difficulty": "Intermediate",
        "courses": [
            {"name": "Brand New Product Manager", "platform": "Product School"},
            {"name": "Become a Product Manager: Learn the Skills", "platform": "Udemy"}
        ],
        "books": ["Inspired: How to Create Tech Products Customers Love by Marty Cagan"],
        "projects": [
            "Draft a detailed Product Requirement Document (PRD) for a new user flow feature",
            "Analyze and map core funnel drops and present a data-driven feature prioritization chart"
        ]
    },
    "scrum": {
        "skill": "Scrum & Agile Development",
        "est_hours": 12,
        "difficulty": "Beginner",
        "courses": [
            {"name": "Scrum Master Certification Prep", "platform": "Scrum.org"},
            {"name": "Agile Development Specialization", "platform": "Coursera"}
        ],
        "books": ["Scrum: The Art of Doing Twice the Work in Half the Time by Jeff Sutherland"],
        "projects": [
            "Lead mock sprint planning, grooming, and retro sessions for a project team",
            "Setup and map workflow transitions in Jira for a complex engineering product launch"
        ]
    },
    "ux design": {
        "skill": "UX/UI Design",
        "est_hours": 30,
        "difficulty": "Intermediate",
        "courses": [
            {"name": "Google UX Design Professional Certificate", "platform": "Coursera"},
            {"name": "UX Design Fundamentals", "platform": "Interaction Design Foundation"}
        ],
        "books": ["The Design of Everyday Things by Don Norman", "Don't Make Me Think by Steve Krug"],
        "projects": [
            "Conduct structured user interviews and map user personas and affinity diagrams",
            "Perform comprehensive heuristic evaluations on an existing landing page dashboard"
        ]
    },
    "figma": {
        "skill": "Figma",
        "est_hours": 15,
        "difficulty": "Beginner",
        "courses": [
            {"name": "Figma UI/UX Design Essentials", "platform": "Udemy"},
            {"name": "Learn Figma Official Courses", "platform": "Figma Help Center"}
        ],
        "books": ["Designing with Figma by various authors"],
        "projects": [
            "Design an interactive high-fidelity mobile application prototype with variables",
            "Build a reusable responsive UI design system with components, variants, and auto-layout"
        ]
    },
    "data engineering": {
        "skill": "Data Engineering",
        "est_hours": 55,
        "difficulty": "Advanced",
        "courses": [
            {"name": "Data Engineering Zoomcamp", "platform": "DataTalks.Club"},
            {"name": "Google Cloud Data Engineer Professional Certificate", "platform": "Coursera"}
        ],
        "books": ["Fundamentals of Data Engineering by Joe Reis and Matt Housley"],
        "projects": [
            "Build a batch ETL pipeline collecting data using Apache Airflow and loading to BigQuery",
            "Process live telemetry events in real-time using Apache Spark Streaming"
        ]
    },
    "excel": {
        "skill": "Microsoft Excel",
        "est_hours": 10,
        "difficulty": "Beginner",
        "courses": [
            {"name": "Excel Skills for Business", "platform": "Coursera"},
            {"name": "Microsoft Excel: Advanced Excel Formulas & Functions", "platform": "Udemy"}
        ],
        "books": ["Ctrl+Shift+Enter: Mastering Excel Array Formulas by Mike Girvin"],
        "projects": [
            "Build an interactive financial model using lookup formulas, Pivot tables, and charts",
            "Write a VBA/Macro script to automate weekly tabular data cleanup"
        ]
    }
}
