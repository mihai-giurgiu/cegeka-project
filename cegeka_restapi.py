from flask import Flask, jsonify

app = Flask(__name__)

cv = {
    'personal_data': {
        'name': 'Mihai Giurgiu',
        'email': 'mihaigiurgiu100@gmail.com',
        'github': 'github.com/mihai-giurgiu'
    },
    'experience_data': [
        {
            'title': 'Software Engineer',
            'company': 'Kantana Technologies',
            'period': '06/2022 - present'
        },
        {
            'title': 'Application Engineer',
            'company': 'IT Vizion',
            'period': '11/2020 - 06/2022'
        },
        {
            'title': 'Research Platform Administrator',
            'company': 'InSites Consulting',
            'period': '03/2020 - 11/2020'
        }
    ],
    'education_data': [
        {
            'studies': 'Cyber Security Master Degree',
            'university': 'West University of Timisoara',
            'period': '2019-2021'
        },
        {
            'studies': 'Web Development Courses',
            'university': 'Informal IT School',
            'period': '2019-2020'
        },
        {
            'studies': 'Marketing and Management Degree',
            'university': 'Faculty of Business and Economics Timisoara',
            'period': '2017-2019'
        }
    ]
}

@app.route('/personal', methods=['GET'])
def get_personal():
    return jsonify(cv['personal_data'])

@app.cli.command("personal")
def print_personal():
    print(cv['personal_data'])

@app.route('/experience', methods=['GET'])
def get_experience():
    return jsonify(cv['experience_data'])

@app.cli.command("experience")
def print_experience():
    print(cv['experience_data'])

@app.route('/education', methods=['GET'])
def get_education():
    return jsonify(cv['education_data'])

@app.cli.command("education")
def print_education():
    print(cv['education_data'])

if __name__ == '__main__':
    app.run()
