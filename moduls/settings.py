

config_site = {"main":  {"styles": "main.css", "title": "Главная"},
               "All_students_visitings": {"styles": "ASV.css", "title": "Посещение учеников"},
               "All_students_latings": {"styles": "ASL.css", "title": "Посещение учеников"},
               "All_grades_visitings": {"styles": "AGV.css", "title": "Посещение классов"},
               "grade_students_visitings": {"styles": "GSV.css", "title": "Посещение учеников класса"},
               "student_visiting": {"styles": "SV.css", "title": "Посещение учеников"},
               }


def Configs(name):
    global config_site
    return config_site[name]