ROADMAP_DATA = {

    "Python": {
        "level": "Beginner",
        "topic": "Python Programming",
        "description": "Learn Python fundamentals, functions, loops, lists, dictionaries and file handling."
    },

    "SQL": {
        "level": "Intermediate",
        "topic": "Advanced SQL",
        "description": "Learn joins, subqueries, CTEs, window functions and advanced SQL queries."
    },

    "Excel": {
        "level": "Beginner",
        "topic": "Advanced Excel",
        "description": "Learn formulas, Pivot Tables, charts, lookup functions and data cleaning."
    },

    "Power BI": {
        "level": "Intermediate",
        "topic": "Power BI Dashboard Development",
        "description": "Learn Power Query, data modelling, DAX and interactive dashboard development."
    },

    "Statistics": {
        "level": "Intermediate",
        "topic": "Statistics for Data Analysis",
        "description": "Learn mean, median, probability, correlation, regression and hypothesis testing."
    },

    "Data Analysis": {
        "level": "Intermediate",
        "topic": "Data Analysis",
        "description": "Learn data cleaning, EDA, visualization and extracting insights from datasets."
    },

    "Data Visualization": {
        "level": "Beginner",
        "topic": "Data Visualization",
        "description": "Learn how to create effective charts and communicate insights using data."
    },

    "Communication": {
        "level": "Beginner",
        "topic": "Communication Skills",
        "description": "Improve professional communication, presentation and workplace interaction skills."
    },

    "Reporting": {
        "level": "Beginner",
        "topic": "Business Reporting",
        "description": "Learn how to prepare professional reports, summaries and business insights."
    },

    "Accounting": {
        "level": "Beginner",
        "topic": "Accounting Fundamentals",
        "description": "Learn basic accounting concepts, financial statements and bookkeeping."
    },

    "Digital Marketing": {
        "level": "Beginner",
        "topic": "Digital Marketing",
        "description": "Learn SEO, social media marketing, content marketing and digital campaign basics."
    },

    "Recruitment": {
        "level": "Beginner",
        "topic": "Recruitment Fundamentals",
        "description": "Learn candidate sourcing, screening, interviewing and recruitment processes."
    },

    "Graphic Design": {
        "level": "Beginner",
        "topic": "Graphic Design",
        "description": "Learn design principles, typography, branding and visual composition."
    }
}


def generate_roadmap(missing_skills):

    roadmap = []

    for index, skill in enumerate(missing_skills, start=1):

        skill_data = ROADMAP_DATA.get(skill)

        if skill_data:

            roadmap.append({
                "skill": skill,
                "level": skill_data["level"],
                "topic": skill_data["topic"],
                "description": skill_data["description"],
                "order": index
            })

        else:

            roadmap.append({
                "skill": skill,
                "level": "Beginner",
                "topic": f"Learn {skill}",
                "description": f"Build your knowledge and practical skills in {skill}.",
                "order": index
            })

    return roadmap