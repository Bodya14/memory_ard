class Question:
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    def show_quest(self, q_lb, rb_list):
        q_lb.setText(self.question)
        rb_list[0].setText(self.right)
        rb_list[1].setText(self.wrong1)
        rb_list[2].setText(self.wrong2)
        rb_list[3].setText(self.wrong3)

    def show_res(self, r_lb, answ_lb, rb_list):
        if rb_list[0].isChecked():
            r_lb.setText("Вірно")
        else:
            r_lb.setText("Невірно")
        answ_lb.setText(self.right)


q1 = Question("Коли був створений Python?", " 1990", "1950", "незнаю", "2000")
q2 = Question("Хто створив Python?", "Гвідо ван Россум.", "Бьёрн Страуструп", "незнаю", "Тарас Григорович Шевченко")
q3 = Question("12+10?", "22", "5", "незнаю", "10")
q4 = Question("Хто такий Наруто?", "персонаж із аніме", "художник", "вчитель", "незнаю")
q5 = Question("Хто такий Windy31?", "Ютубер який знімає копм. ігри", "Тік токер", "Програміст", "незнаю")
q6 = Question("Скільки частит є в гта?", "5", "7", "3", "6")
q7 = Question("Як звали брата Санса з гри Undertale?", "Папірус", "Флауи", "Фроггит", "Андайн")
q8 = Question("Як звали головного героя гри Portal?", "Челл", "Алла", "Гладос", "Надежда")
q9 = Question("яка різниця між майнкрафтом і террарії?", "майнкрафт 3D а террарія 2D", "нема різниці", "різні сюжети",
              "незнаю")
q10 = Question("Хто я?", "хто я?", "хтось", "а я звідки знаю", "це ти")
q11 = Question("Скільки підпісників в 2023 у MrBeast?", "141мільонів", "200мільонів", "100тисяч", "багато")
q12 = Question("Коли з'явився фільм Гра в кальмара?", "2021", "2020", "2023", "2019")
q13 = Question("Коли з'явилася маршрутка Богдан в Україні?", "2003 року", "2014 року", "2008 року", "2020 року")
q14 = Question("Коли з'явилася Україна?", "1187 року", "1290 року", "1023 року", "2008 року")
q15 = Question("Якого кольору ялинка", "зелений", "червоний", "оранжевий", "фіолетовий")

q_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]
