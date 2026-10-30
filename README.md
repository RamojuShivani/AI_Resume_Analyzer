#  AI Resume Analyzer

An AI-assisted Resume Analyzer built using Python that evaluates how well a candidate's resume matches a given job description by identifying matching skills, missing skills, and calculating a skill match percentage.

##  Project Overview

The AI Resume Analyzer helps job seekers understand how closely their resumes align with job requirements.

Users can upload a PDF resume and provide a job description. The system extracts resume text, identifies relevant technical skills, compares them against the required skills, and provides personalized learning recommendations.

##  Key Features

- **PDF Resume Upload:** Upload resumes in PDF format.
- **Text Extraction:** Extract resume content using PyMuPDF.
- **Skill Extraction:** Identify technical skills using a predefined skills database.
- **Job Description Analysis:** Extract required skills from job descriptions.
- **Skill Matching:** Identify matching and missing skills.
- **Match Percentage:** Calculate the percentage of required skills found in the resume.
- **Learning Recommendations:** Suggest areas to improve based on missing skills.
- **Interactive Interface:** Streamlit-based interface for displaying analysis results.

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyMuPDF | PDF text extraction |
| Scikit-learn | TF-IDF and cosine similarity experiments |
| Streamlit | Web application interface |
| Google Colab | Development and experimentation |
| Git & GitHub | Version control and project hosting |

##  Project Workflow

1. Upload a PDF resume.
2. Extract text from the uploaded document.
3. Paste the target job description.
4. Identify skills in both documents.
5. Compare resume skills with job requirements.
6. Calculate the skill match percentage.
7. Display matching and missing skills.
8. Generate learning recommendations.

##  Sample Output

**Example Skill Analysis**

- Total required skills: 8
- Matching skills: 5
- Missing skills: 3
- Skill match percentage: 62.50%

**Matching Skills**
- Python
- SQL
- AWS
- Git
- Data Analysis

**Missing Skills**
- Machine Learning
- FastAPI
- Docker

##  Project Structure

```text
AI_Resume_Analyzer/
│
├── AI_Resume_Analyzer.ipynb
├── app.py
└── README.md
```

##  Current Project Status

The project includes a working notebook prototype with resume analysis logic and Streamlit application code developed in Google Colab.

The standalone `app.py` file and local execution setup are planned for improvement.

##  Future Improvements

- Improve skill extraction using NLP techniques.
- Support additional resume formats.
- Improve skill matching with semantic similarity.
- Add resume scoring and detailed feedback.
- Expand the skills database.
- Deploy the application online.

##  Disclaimer

The skill match percentage is based on recognized keywords and should not be interpreted as a prediction of hiring success. A missing keyword does not necessarily mean a candidate lacks that skill.

##   Author

**Shivani Ramoju**

B.Tech Graduate | Data Science & AI/ML Enthusiast

- GitHub: [RamojuShivani](https://github.com/RamojuShivani)

---

 If you find this project useful, consider giving the repository a star!
