
import re
import pymupdf
import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

SKILLS_DATABASE = [
    "Python", "SQL", "Excel", "Power BI", "Tableau",
    "Machine Learning", "Deep Learning", "NLP",
    "Pandas", "NumPy", "Scikit-learn", "TensorFlow",
    "PyTorch", "Data Analysis", "Data Visualization",
    "Statistics", "Data Cleaning", "EDA",
    "HTML", "CSS", "JavaScript", "React",
    "Flask", "Django", "Streamlit",
    "AWS", "Azure", "GCP", "Git", "GitHub",
    "MySQL", "PostgreSQL", "MongoDB",
    "REST API", "ETL", "Data Warehousing"
]

SKILL_ALIASES = {
    "Machine Learning": ["ML", "machine-learning"],
    "Deep Learning": ["DL", "deep-learning"],
    "NLP": ["Natural Language Processing"],
    "Scikit-learn": ["sklearn", "scikit learn"],
    "Power BI": ["powerbi", "power-bi"],
    "AWS": ["Amazon Web Services"],
    "Azure": ["Microsoft Azure"],
    "GCP": ["Google Cloud Platform"],
    "EDA": ["Exploratory Data Analysis"],
    "REST API": ["RESTful API", "REST APIs"],
    "Data Analysis": ["Data Analytics"],
    "Data Visualization": ["Data Viz"],
    "PostgreSQL": ["Postgres"],
    "JavaScript": ["JS"],
    "GitHub": ["Git Hub"],
    "MySQL": ["My SQL"],
    "TensorFlow": ["Tensor Flow"],
    "Scikit-learn": ["scikit learn", "sklearn"]
}

LEARNING_SUGGESTIONS = {
    "Python": "Practise Python basics, functions, lists, dictionaries and OOP.",
    "SQL": "Learn SELECT, filtering, JOINs, GROUP BY and subqueries.",
    "Power BI": "Practise Power Query, data modelling, DAX and dashboards.",
    "Excel": "Learn PivotTables, lookup functions and charts.",
    "Machine Learning": "Study regression, classification, model evaluation and scikit-learn.",
    "Pandas": "Practise DataFrames, filtering, grouping and missing-value handling.",
    "NumPy": "Learn arrays, indexing and numerical operations.",
    "Tableau": "Build dashboards and practise calculated fields.",
    "AWS": "Start with cloud fundamentals, S3 and basic IAM concepts.",
    "Git": "Practise Git commits, branches, push and pull.",
    "GitHub": "Learn repositories, README files and version control workflows.",
    "REST API": "Learn HTTP methods, JSON and API requests using Python.",
    "Data Analysis": "Practise data cleaning, exploratory analysis and insight generation.",
    "Data Visualization": "Learn chart selection, storytelling and dashboard design."
}


def extract_pdf_text(pdf_bytes):
    """Extract readable text from an uploaded PDF."""
    text = ""

    with pymupdf.open(stream=pdf_bytes, filetype="pdf") as document:
        for page in document:
            text += page.get_text() + "\n"

    return text.strip()


def extract_skills(text, skills_database):
    """Extract skills using keywords and their aliases."""

    found_skills = []
    normalized_text = re.sub(r"\s+", " ", text).lower()

    for skill in skills_database:
        keywords = [skill]
        keywords.extend(SKILL_ALIASES.get(skill, []))

        for keyword in keywords:
            keyword_pattern = re.escape(keyword.lower())
            keyword_pattern = keyword_pattern.replace(
                r"\ ", r"\s+"
            )

            pattern = (
                r"(?<!\w)" +
                keyword_pattern +
                r"(?!\w)"
            )

            if re.search(pattern, normalized_text):
                found_skills.append(skill)
                break

    return found_skills
    

def calculate_match(resume_skills, job_skills):
    """Calculate the percentage of job-description skills found in the resume."""
    if not job_skills:
        return 0

    matched = set(resume_skills) & set(job_skills)
    return round((len(matched) / len(set(job_skills))) * 100, 2)


st.title("📄 AI-Powered Resume Analyzer")
st.write(
    "Upload your resume and compare its listed skills with a job description."
)
st.info(
    "This prototype uses predefined skill keywords. "
    "Its match percentage is a skill-coverage estimate, not a hiring prediction."
)

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "Upload your resume (PDF)",
        type=["pdf"]
    )

with col2:
    job_description = st.text_area(
        "Paste the job description",
        height=220,
        placeholder="Paste the complete job description here..."
    )

if st.button("Analyze Resume", type="primary", use_container_width=True):

    if resume_file is None:
        st.warning("Please upload your resume as a PDF.")

    elif not job_description.strip():
        st.warning("Please paste a job description.")

    else:
        try:
            with st.spinner("Analyzing your resume..."):
                resume_text = extract_pdf_text(resume_file.getvalue())

                if not resume_text:
                    st.error(
                        "No readable text was found. "
                        "Your PDF may be scanned or image-based."
                    )
                    st.stop()

                resume_skills = extract_skills(
                    resume_text, SKILLS_DATABASE
                )
                job_skills = extract_skills(
                    job_description, SKILLS_DATABASE
                )

                matched_skills = sorted(
                    set(resume_skills) & set(job_skills)
                )
                missing_skills = sorted(
                    set(job_skills) - set(resume_skills)
                )
                match_score = calculate_match(
                    resume_skills, job_skills
                )

            st.divider()
            st.subheader("Analysis Results")

            metric1, metric2, metric3 = st.columns(3)

            metric1.metric("Skill Coverage", f"{match_score}%")
            metric2.metric("Matched Skills", len(matched_skills))
            metric3.metric("Missing Skills", len(missing_skills))

            st.progress(int(match_score))

            left, right = st.columns(2)

            with left:
                st.subheader("✅ Matched Skills")
                if matched_skills:
                    for skill in matched_skills:
                        st.write(f"• {skill}")
                else:
                    st.write("No matching skills were detected.")

            with right:
                st.subheader("📌 Skills to Consider Learning")
                if missing_skills:
                    for skill in missing_skills:
                        st.write(f"• {skill}")
                else:
                    st.write(
                        "No missing skills were detected from "
                        "the predefined skill list."
                    )

            st.divider()
            st.subheader("📚 Learning Suggestions")

            suggestions_found = False

            for skill in missing_skills:
                if skill in LEARNING_SUGGESTIONS:
                    st.write(
                        f"**{skill}:** "
                        f"{LEARNING_SUGGESTIONS[skill]}"
                    )
                    suggestions_found = True

            if missing_skills and not suggestions_found:
                st.write(
                    "Search for beginner tutorials and practical "
                    "projects for the missing skills listed above."
                )
            elif not missing_skills:
                st.write(
                    "Review the job requirements and keep practising "
                    "the skills you already have."
                )

            with st.expander("View extracted resume text"):
                st.text(resume_text)

            st.caption(
                "Note: Results depend on keyword detection. "
                "Synonyms, context, experience level and scanned PDFs "
                "may not be interpreted correctly."
            )

        except Exception as error:
            st.error(
                "Could not analyze this PDF. Please try a valid, "
                "text-readable PDF file."
            )
            st.caption(f"Technical detail: {error}")
