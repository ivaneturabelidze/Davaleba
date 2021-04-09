class TestPaper:
    def __init__(self, subject, mark_scheme, pass_mark):
        self.subject = subject
        self.mark_scheme = mark_scheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self, tests_taken='No tests taken'):
        self.tests_taken = tests_taken

    def take_test(self, test_paper, answers):
        correct_answers = 0
        for i in range(len(answers)):
            if answers[i] == test_paper.mark_scheme[i]:
                correct_answers += 1
        score = round(100/len(test_paper.mark_scheme) * correct_answers)
        if correct_answers >= len(test_paper.mark_scheme) * int(test_paper.pass_mark.replace("%", ""))/100:
            if self.tests_taken == "No tests taken":
                self.tests_taken = {f"{test_paper.subject}": f"Passed! ({score}%)"}
            else:
                self.tests_taken[f"{test_paper.subject}"] = f"Passed! ({score}%)"
        else:
            if self.tests_taken == "No tests taken":
                self.tests_taken = {f"{test_paper.subject}": f"Failed! ({score}%)"}
            else:
                self.tests_taken[f"{test_paper.subject}"] = f"Failed! ({score}%)"


if __name__ == '__main__':
    paper1 = TestPaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
    paper2 = TestPaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
    paper3 = TestPaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
    student1 = Student()
    print(student1.tests_taken)
    student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
    print(student1.tests_taken)
    student2 = Student()
    print(student2.tests_taken)
    student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
    student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
    print(student2.tests_taken)
