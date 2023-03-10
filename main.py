import pprint
import json

import pandas as pd

df = pd.read_excel(io='xls-src/progress.xlsx')

# получаем все уникальные электронные почты
user_emails = df['Электронная почта'].unique().tolist()

# список с данными по каждому студенту
src_data =[]
for email in user_emails:
    data = df[df['Электронная почта'] == email]
    src_data.append(data)


# записываем в словарь json с курсами и уроками
with open('src/fullstack_cource.json') as f:
    prof_data = json.load(f)

data_for_df = {
    'Название': [],
    'Курс': [],
    'slug курса': [],
}
for course in prof_data['courses']:
    for lesson in course['lessons']:
        data_for_df['Название'].append(lesson['lesson-name'])
        data_for_df['Курс'].append(course['course-name'])
        data_for_df['slug курса'].append(course['course-title'])

# Получаем df из всех уроков до конца профессии
course_df = pd.DataFrame(data_for_df)


