class StudentRating:
    def __init__(self):
        self.students_list = []

    def __get_students(self, cond):
        '''
        get student list
        :param cond: our conditional
        :return: filtered list of students
        '''
        return list(filter(lambda student: cond(student), self.students_list))

    def __get_aggregation_stat(self, func):
        '''
        make list of ratings and use argument func on this list
        :param func: function aggregation of a list of numbers
        :return: list of ratings on which some function was used
        '''
        if not self.students_list:
            return 0

        return func(student['rating'] for student in self.students_list)

    def add_student(self, name: str, rating: int):
        '''
        add student data to list
        :param name: student name
        :param rating: student rating
        '''
        if rating > 100:
            rating = 100
        if rating < 0:
            rating = 0

        student = {'name': name, 'rating': rating}
        self.students_list.append(student)

    def get_students(self):
        '''
        get students
        :return: students list
        '''
        return self.students_list

    def edit_students_rating(self, ind: int, new_rating: int):
        '''
        update student rating
        :param ind: student index
        :param new_rating: new rating
        '''
        if new_rating > 100:
            new_rating = 100
        if new_rating < 0:
            new_rating = 0
        self.students_list[ind].update({'rating': new_rating})

    def get_max_rating(self) -> int:
        '''
        find max rating
        :return: max rating
        '''

        return self.__get_aggregation_stat(max)

    def get_min_rating(self) -> int:
        '''
        find min rating
        :return: min rating
        '''

        return self.__get_aggregation_stat(min)

    def get_avg_rating(self) -> int:
        '''
        calculate avg rating
        :return: avg rating
        '''

        return self.__get_aggregation_stat(lambda ratings: round(
            sum(ratings) / len(self.students_list)
        ))

    def count_student_rating_bigger_avg(self) -> int:
        '''
        count students rating bigger avg rating
        :return: amount students rating bigger avg rating
        '''
        avg_rating = self.get_avg_rating()

        students = self.__get_students(lambda student: student['rating'] > avg_rating)
        return len(students)

    def count_student_rating_smaller_avg(self) -> int:
        '''
        count students rating smaller avg rating
        :return: amount students rating smaller avg rating
        '''
        avg_rating = self.get_avg_rating()
        students = self.__get_students(lambda student: student['rating'] < avg_rating)
        return len(students)

    def count_students_with_rating_excellent(self) -> int:
        '''
        count students with rating excellent
        :return: amount students with rating excellent
        '''
        students = self.__get_students(lambda student: student['rating'] > 90)
        return len(students)

    def count_students_with_rating_very_good(self) -> int:
        '''
        count students with rating very good
        :return: amount students with rating very good
        '''
        students = self.__get_students(lambda student: 70 < student['rating'] < 91)
        return len(students)

    def count_students_with_rating_good(self) -> int:
        '''
        count students with rating good
        :return: amount students with rating good
        '''
        students = self.__get_students(lambda student: 60 < student['rating'] < 71)
        return len(students)

    def count_students_with_rating_satisfactory(self) -> int:
        '''
        count students with rating satisfactory
        :return: amount students with rating satisfactory
        '''
        students = self.__get_students(lambda student: student['rating'] < 60)
        return len(students)

    def __str__(self) -> str:
        list_of_ratings = [student['rating'] for student in self.students_list]
        return f'all ratings: {list_of_ratings}'


students = StudentRating()
students.add_student('serg', 1000000)
students.add_student('serg', 1000000)
students.add_student('serg', 1000000)
students.add_student('serg', 65)
students.edit_students_rating(0, 1)
students.edit_students_rating(2, 90)
print(students.get_students())
print(f'{students.get_min_rating()=}')
print(f'{students.get_max_rating()=}')
print(f'{students.get_avg_rating()=}')
f'{students.count_student_rating_bigger_avg()=}'
print(f'{students.count_student_rating_bigger_avg()=}')
print(f'{students.count_student_rating_smaller_avg()=}')
print(f'{students.count_students_with_rating_excellent()=}')
print(f'{students.count_students_with_rating_very_good()=}')
print(f'{students.count_students_with_rating_good()=}')
print(f'{students.count_students_with_rating_satisfactory()=}')
print(students.students_list)
print(students)
