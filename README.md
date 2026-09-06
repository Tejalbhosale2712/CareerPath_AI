# CareerPath AI

## AI-Powered Career Recommendation & Skill Gap Analysis System

CareerPath AI is a web-based Django application that helps students and job seekers understand their career readiness by analyzing their resumes, identifying skill gaps, recommending suitable jobs, and generating personalized learning roadmaps.

## Features

- User Registration and Login
- Resume PDF Upload
- Resume Text Extraction
- Resume Skill Extraction
- Education, Experience, Projects and Certifications Extraction
- Target Career Role Selection
- Skill Gap Analysis
- Readiness Score
- Matched and Missing Skills
- Job Recommendations
- Job Match Percentage
- Personalized Learning Roadmap
- Django Admin Panel

## Project Workflow

Home
↓
Register / Login
↓
Dashboard
↓
Upload Resume
↓
Resume Analysis
↓
Select Target Career Role
↓
Skill Gap Analysis
↓
Job Recommendations
↓
Learning Roadmap

## Technology Stack

### Backend
- Python
- Django
- MySQL

### Libraries
- pypdf

### Frontend
- HTML
- CSS
- Django Templates

### Development Tools
- Visual Studio Code
- Git
- GitHub

## Project Modules

### 1. Accounts
Handles:
- User registration
- User login
- User logout

### 2. Resume
Handles:
- Resume PDF upload
- Resume text extraction
- Skill extraction
- Education extraction
- Experience extraction
- Project extraction
- Certification extraction

### 3. Career
Handles:
- Target career role selection
- Career profile management

### 4. Skill Analysis
Handles:
- Skill gap analysis
- Readiness score calculation
- Matched skills
- Missing skills
- Job recommendations
- Learning roadmap

### 5. Dashboard
Displays:
- Uploaded resumes
- Readiness score
- Matched skills
- Available jobs
- Career tools

## Skill Gap Analysis

The system compares the skills extracted from the uploaded resume with the required skills for the selected career role.

### Example

Target Role:

Data Analyst

Resume Skills:

Python, SQL, Excel, Power BI

Required Skills:

Python, SQL, Excel, Power BI, Statistics, Data Analysis

The system identifies:

Matched Skills:
- Python
- SQL
- Excel
- Power BI

Missing Skills:
- Statistics
- Data Analysis

A readiness score is then calculated based on the matched and required skills.

## Job Recommendation

The system compares the user's skills with the required skills of available jobs and calculates a match percentage.

Jobs are displayed in descending order of match percentage.

## Learning Roadmap

The learning roadmap is generated using the missing skills identified during the Skill Gap Analysis.

For each missing skill, the system provides:

- Skill
- Level
- Topic
- Description
- Learning order

## Database Models

The project contains models for:

- User
- Resume
- CareerProfile
- JobRole
- SkillGapAnalysis
- Job
- LearningRoadmap

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Tejalbhosale2712/CareerPath_AI.git
