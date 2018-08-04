class teacher:

    def __init__(self, teacher_ID, teacher_name, teacher_course_assigned, teacher_batch_assigned,
                 teacher_max_working_hour):
        self.teacher_ID = teacher_ID
        self.teacher_name = teacher_name
        self.teacher_course_assigned = teacher_course_assigned
        self.teacher_batch_assigned = teacher_batch_assigned
        self.teacher_max_working_hour = int(teacher_max_working_hour)
        self.teacher_consecutive = 0
        self.teacher_taught = []
        self.current_busy = 0
        self.teacher_course_current_index=0
        self.teacher_last_time=-1

    def teacher_set_course(self, teacher_course_assigned):
        self.teacher_course_assigned = teacher_course_assigned

    def set_batch(self, teacher_batch_assigned):
        self.teacher_batch_assigned = teacher_batch_assigned

    def teacher_occupy(self, course_ID):
        self.teacher_consecutive = self.teacher_consecutive + 1
        self.teacher_max_working_hour = self.teacher_max_working_hour - 1
        # self.teacher_taught =list.append(course_ID)
        self.teacher_taught.append(course_ID)
        self.current_busy = 1
    def check_teacher_available(self, course_ID):
        #print("Consecutive Hours="+str(self.teacher_consecutive)+"Teacher Remaining Working Hour="+str(self.teacher_max_working_hour)+"Course Assigned="+self.teacher_course_assigned[self.teacher_course_current_index]+"Course assigned index="+str(self.teacher_course_current_index))

        if self.teacher_consecutive >= 2 or self.teacher_max_working_hour == 0 or course_ID in self.teacher_taught:
        # ********************removed "or course_ID in self.teacher_taught"
        #if self.teacher_consecutive >= 2 or self.teacher_max_working_hour == 0:
            #*****************CHANGE MADE BELOW
            self.teacher_consecutive=0
            return False
        else:
            return True

    def get_teacherId(self):
        return self.teacher_ID

    def get_teacher_Name(self):
        return self.teacher_name

    def __str__(self):
        return 'Name :' + self.teacher_name + \
               '\nID number: ' + self.teacher_ID + \
               '\nCourses assigned : ' + self.teacher_course_assigned + \
               '\n Batches : ' + self.teacher_batch_assigned


class courses:

    def __init__(self, course_ID, course_Name, course_type, course_credit, course_teacher_ID):
        self.course_ID = course_ID
        self.course_Name = course_Name
        self.course_type = course_type
        self.course_credit = course_credit
        self.course_teacher_ID = course_teacher_ID
        self.course_credit_remaining= int(course_credit)

    def course_studied(self):
        self.course_credit_remaining = self.course_credit_remaining-1

    def check_course_credit_remaining(self):
        if self.course_credit_remaining > 0:
            return True
        else:
            return False

    def __str__(self):
        return 'Course name:' + self.course_Name + \
               '\n Course ID :' + self.course_ID + \
               '\n Course Type : ' + self.course_type + \
               '\n Contact hours : ' + self.course_credit + \
               '\n Teacher Id of teacher assigned :' + self.course_teacher_ID
