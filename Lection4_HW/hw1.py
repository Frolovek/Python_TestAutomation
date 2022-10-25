"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without -
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes
you want.
"""
from datetime import datetime, timedelta


class Homework:
    def __init__(self, hw_text: str, hw_deadline: int):
        self.hw_text = hw_text
        self.hw_deadline = hw_deadline
        self.creation_date = datetime.now()

    def check_deadline(self):
        return self.creation_date + timedelta(days=self.hw_deadline) < datetime.now()


class Student:
    def __init__(self, st_first_name: str, st_last_name: str):
        self.st_first_name = st_first_name
        self.st_last_name = st_last_name

    def do_homework(self, hw, hw_solution: str):
        if hw.check_deadline():
            raise DeadlineError("You are late")
        else:
            return ResultHomework(hw, self, hw_solution)


class ResultHomework:
    def __init__(self, hw, author, hw_solution):
        self.hw = hw
        self.author = author
        self.hw_solution = hw_solution


class Teacher:
    homework_done = dict()

    def __init__(self, tch_first_name: str, tch_lst_name: str):
        self.tch_first_name = tch_first_name
        self.tch_lst_name = tch_lst_name

    @staticmethod
    def create_homework(hw_text, hw_deadline):
        return Homework(hw_text, hw_deadline)

    @classmethod
    def check_homework(cls, solved_homework):
        if solved_homework.hw in cls.homework_done:
            if solved_homework in cls.homework_done[solved_homework.hw]:
                return True
            elif len(solved_homework.hw_solution) > 5:
                cls.homework_done[solved_homework.hw].append(solved_homework)
                return True
            else:
                return False
        else:
            cls.homework_done[solved_homework.hw] = []
            if len(solved_homework.hw_solution) > 5:
                cls.homework_done[solved_homework.hw].append(solved_homework)
                return True
            else:
                return False

    @classmethod
    def reset_results(cls, hw=None):
        if hw:
            del cls.homework_done[hw]
        else:
            cls.homework_done.clear()


class DeadlineError(Exception):
    """Raises DeadlineError if deadline has passed"""
    pass
