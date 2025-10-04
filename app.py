
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Resume data
resume_data = {
    "personal_info": {
        "name": "Bhagyashri Mane",
        "location": "Latur (MH), India",
        "phone": "(+91) 8999389628",
        "email": "bhagyashri49641@gmail.com",
        "linkedin": "https://www.linkedin.com/in/bhagyashri49641/",
        "github": "https://github.com/bhagyashri49641"
    },
    "summary": "I am an analytical professional with expertise in data analytics excelling at transforming raw data into actionable insights to drive business decisions, proficient in Python, SQL, R, Tableau, Power BI, and Google Workspace (Docs, Sheets, Drive, Gmail). Skilled in statistical analysis, data cleaning, data wrangling, and business intelligence, with hands-on experience using BigQuery and cloud-based data analytics tools. Strong problem-solving and critical thinking abilities, with a proven ability to learn quickly through training documentation and presentations. Adept at communicating insights effectively and collaborating in cross-functional teams to deliver actionable, data-driven solutions.",

    "technical_skills": {
        "Programming Languages": [
            {"name": "Python (Pandas, NumPy)", "level": 90},
            {"name": "SQL", "level": 85},
            {"name": "R", "level": 80},
            {"name": "C++", "level": 70},
            {"name": "Java", "level": 65}
        ],
        "Data Visualization": [
            {"name": "Tableau", "level": 85},
            {"name": "Microsoft Power BI", "level": 85}
        ],
        "Data Tools & Platforms": [
            {"name": "MySQL Workbench", "level": 80},
            {"name": "Google BigQuery", "level": 75},
            {"name": "Microsoft Excel", "level": 90},
            {"name": "Google Sheets", "level": 90}
        ],
        "Data Analysis": [
            {"name": "Statistical Analysis", "level": 85},
            {"name": "Data Cleaning", "level": 90},
            {"name": "Data Wrangling", "level": 90},
            {"name": "Anomaly Detection", "level": 75}
        ]
    },

    "work_experience": [
        {
            "company": "Infosys Limited",
            "position": "Systems Engineer",
            "duration": "Dec. 2021 - Oct 2023",
            "responsibilities": [
                "Interpreted and analyzed test data to identify defects, improve test coverage, and enhance software quality.",
                "Managed test cases and logged defects using Jira, ensuring efficient communication and collaboration with cross-functional development teams.",
                "Collaborated in Agile ceremonies including weekly stand-ups to report QA progress, resolve blockers, and align with sprint goals and project deadlines."
            ]
        },
        {
            "company": "Self Development",
            "position": "Data Analytics Transition & Skill Development",
            "duration": "Nov 2023 - Present",
            "responsibilities": [
                "Completed Google Data Analytics Professional Certificate and advanced SQL programming certifications",
                "Developed comprehensive data analytics projects using Python, R, Tableau, and Power BI",
                "Mastered statistical analysis, data cleaning, and business intelligence techniques",
                "Built expertise in Google Cloud Platform"
            ]
        }
    ],

    "certifications": [
        {"name": "Google Cloud Data Analytics Professional Certificate", "provider": "Coursera", "date": "Sep 2025"},
        {"name": "Google Data Analytics Professional Certificate", "provider": "Coursera", "date": "Mar 2025"},
        {"name": "Python for Everybody", "provider": "Coursera", "date": "Apr 2025"},
        {"name": "SQL-MYSQL for data analysis and business intelligence", "provider": "Udemy", "date": "Sep 2024"}
    ],

    "projects": [
        {
            "name": "Google Data Analytics Capstone – Bellabeat Fitbit Case Study",
            "tech_stack": "R, Tableau",
            "date": "March 2025",
            "image": "bellabeat-project.jpg",
            "description": [
                "Conducted end-to-end analysis of Fitbit user data to uncover insights into user behavior.",
                "Applied R packages (ggplot2, dplyr, tidyr) to clean and analyze datasets, ensuring accuracy.",
                "Designed compelling data visualizations in R and interactive dashboards in Tableau.",
                "Generated actionable insights to inform Bellabeat's marketing strategy."
            ]
        },
        {
            "name": "T20 Cricket Data Analysis",
            "tech_stack": "Python, Pandas, Power BI",
            "date": "April 2024",
            "image": "cricket-analysis.jpg",
            "description": [
                "Conducted a comprehensive analysis of player data to identify the optimal eleven cricket players based on specific performance criteria, enhancing team composition for competitive advantage.",
                "Converted raw data from JSON to CSV and conducted thorough data cleaning using Pandas in Jupyter Notebook.",
                "Used power query editor for basic data transformations and to create required DAX measures."
            ]
        },
        {
            "name": "Pizza Sales Analysis",
            "tech_stack": "MYSQL, Power BI",
            "date": "May 2024",
            "image": "pizza-sales.jpg",
            "description": [
                "Developed a Power BI dashboard that identified top-selling pizzas, increasing sales insights by 20%.",
                "Wrote SQL queries to extract KPIs and monitor performance metrics for business insights.",
                "Leveraged Power Query Editor to clean and structure data, and created DAX measures for insightful dashboards."
            ]
        },
        {
            "name": "Superstore Sales Data Visualization",
            "tech_stack": "Power BI",
            "date": "April 2024",
            "image": "superstore-sales.jpg",
            "description": [
                "Analyzing sales data to find out which category of products gives more sales, region wise sales, per month sales and profit and 15 days sales forecast."
            ]
        }
    ],

    "education": [
        {
            "degree": "M.Tech in Electronics and Communication Engineering",
            "institution": "College of Engineering Pune",
            "duration": "Aug 2018 - Oct 2020",
            "grade": "CGPA: 7.2/10"
        },
        {
            "degree": "B.E in Electronics",
            "institution": "M.S. Bidve Engineering College latur",
            "duration": "Aug 2012 – Aug 2017",
            "grade": "63%"
        },
        {
            "degree": "HSC (PCM)",
            "institution": "Dayanand Science College Latur",
            "duration": "Aug 2010 - Aug 2012",
            "grade": "80%"
        },
        {
            "degree": "SSC",
            "institution": "Shree Deshikendra High School Latur",
            "duration": "Jun 2009 - Jun 2010",
            "grade": "96%"
        }
    ],

    "languages": ["English", "Hindi", "Marathi"],

    "coding_profiles": {
        "leetcode": "https://leetcode.com/u/bhagyashri49641/",
        "hackerrank": "https://www.hackerrank.com/profile/bhagyashri49641",
        "codolio": "https://codolio.com/profile/bhagyashri49641",
        "github": "https://github.com/bhagyashri49641",
        "takeyouforward": "https://takeuforward.org/plus/profile/Bhagya146"
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=resume_data)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Here you would typically save to database or send email
        # For now, just return success response
        return jsonify({
            'status': 'success',
            'message': 'Thank you for your message! I will get back to you soon.'
        })

    return jsonify({'status': 'error', 'message': 'Invalid request method'})

if __name__ == '__main__':
    app.run(debug=True)
