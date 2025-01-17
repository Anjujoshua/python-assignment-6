class Course:
    def _init_(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display(self):
        print(f"{self.course_code}: {self.course_name} ({self.credit_hours} Credit Hours)")
class CoreCourse(Course):
    def _init_(self, course_code, course_name, credit_hours, required_for_major):
        super()._init_(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display(self):
        super().display()
        status = "Required" if self.required_for_major else "Not Required"
        print(f"- Core Course ({status} for Major)")


# Subclass: ElectiveCourse
class ElectiveCourse:
    pass


class ElectiveCourse(Course):
    def _init_(self, course_code, course_name, credit_hours, elective_type):
        super()._init_(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display(self):
        super().display()
        print(f"- Elective Course (Type: {self.elective_type})")



    core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
    elective_course = ElectiveCourse("ENG201", "Creative Writing", 2, "Liberal Arts")

    core_course.display()
    print()
    elective_course.display()
