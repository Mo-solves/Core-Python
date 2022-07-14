class Teacher():
    def teach_class(self):
        print('Teaching stuff...')

    def grab_lunch(self):
        print('Yum yum yum!')

    def grade_testes(self):
        print('F! F! F!')


class CollegeProfessor(Teacher):
    def publish_book(self):
        print('Hoorey, I\'m an author')

    def grade_testes(self):
        print('A! A! A!')


teacher = Teacher()
professor = CollegeProfessor()

teacher.teach_class()
teacher.grab_lunch()
teacher.grade_testes()
print()

professor.teach_class()
professor.grab_lunch()
professor.publish_book()
professor.grade_testes()
