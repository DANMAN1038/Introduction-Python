class TestScore:
    def __init__(self, name, i_d, problem_scores, max_scores):
        #initialize everything needed to carry over from function to function
        self.name = name
        self.id = i_d
        self.problem_scores = problem_scores
        self.max_scores = max_scores
        total_score = 0
        self.total_score = total_score
        total_max = 0
        self.total_max = total_max
        percent = 0
        self.percent = percent
        self.total_max_scores = 0
        self.total_score = 0
        #getters return value of attribute
    def get_name(self):
        return self.get_name
    def get_id(self):
        return self.get_id
    def set_name(self, new_name):
        self.get_name = new_name
    def set_id(self, new_id):
        self.id = new_id
        #setters change attribute to new value
    def set_problem_scores(self, new_problem_scores):
        self.problem_scores = new_problem_scores
    def set_max_scores(self, new_max_scores):
        self.max_scores = new_max_scores
        #adding dictionary into a tuple of dictionaries
    def add_scores(self, key, another_problem_score, another_max_score):
        self.problem_scores[key] = another_problem_score
        self.max_scores[key] = another_max_score
    def get_total_score(self):
        total_score = 0
        #access each dictionary from the tuple
        for ele in self.problem_scores:
            for i, val in self.problem_scores.items():
                total_score += val
        self.total_score = total_score / len(self.problem_scores)
        return self.total_score
    def get_max_score(self):
        total_max = 0
        for ele in self.max_scores:
            for i, val in self.max_scores.items():
                total_max += val
        self.total_max_scores = total_max / len(self.max_scores)
        return self.total_max_scores
    def get_percent(self):
        percent_decimal = self.total_score / self.total_max_scores
        percent = percent_decimal * 100
        self.percent = percent
        return self.percent
    def get_grade(self):
        grade = ''
        if self.percent >= 93 and self.percent <= 100:
            grade = 'A'
        elif self.percent >= 90 and self.percent < 93:
            grade = 'A-'
        elif self.percent >= 87 and self.percent < 90:
            grade = 'B+'
        elif self.percent >= 83 and self.percent < 87:
            grade = 'B'
        elif self.percent >= 80 and self.percent < 83:
            grade = 'B-'
        elif self.percent >= 77 and self.percent < 80:
            grade = 'C+'
        elif self.percent >= 73 and self.percent < 77:
            grade = 'C'
        elif self.percent >= 70 and self.percent < 73:
            grade = 'C-'
        elif self.percent >= 67 and self.percent < 70:
            grade = 'D+'
        elif self.percent >= 60 and self.percent < 67:
            grade = 'D'
        #Edge if negative
        elif self.percent < 0:
            grade = "Grade can not be negative"
        #Edge if > 100 (as illustrated by scale)
        elif self.percent > 100:
            grade = "Grade can not be above 100%"
        else:
            grade = 'F'
        return grade
    def __str__(self):
        #seperated by , also turns numerator and denominator into ints for display, but is floats for calculation
        #rounds percent(If this isn't necessary, delete round
        return self.name + ', ' + str(self.id)+ ', ' + str(int(self.total_score))+ '/'+ str(int(self.total_max_scores)) + ' ' + '(' + str(round(self.percent)) + '%)'
if __name__ == '__main__':
    student = TestScore("Richard Nixon", 420, {1: 31, 2: 27, 3: 19}, {1: 35, 2: 35, 3: 30})
    student.add_scores(4, 10, 20)
    student.get_total_score()
    student.get_max_score()
    student.get_percent()
    print(student.get_grade())
    print(student.__str__())
