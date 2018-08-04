class teacher:

    def __init__(self, teacher_ID, teacher_name, teacher_course_assigned, teacher_batch_assigned,teacher_max_working_hour):
        self.teacher_ID = teacher_ID
        self.teacher_name = teacher_name
        self.teacher_course_assigned = teacher_course_assigned
        self.teacher_batch_assigned = teacher_batch_assigned
        self.teacher_max_working_hour = int(teacher_max_working_hour)
        self.teacher_consecutive = 0
        self.teacher_taught=[]

    def teacher_set_course(self,teacher_course_assigned):
        self.teacher_course_assigned = teacher_course_assigned

    def set_batch(self,teacher_batch_assigned):
        self.teacher_batch_assigned = teacher_batch_assigned

    def teacher_occupy(self,course_ID):
        self.teacher_consecutive =self.teacher_consecutive+1
        self.teacher_max_working_hour = self.teacher_max_working_hour-1
    #    print(course_ID)
        for i in course_ID:
            if(i in self.teacher_course_assigned):
                self.teacher_taught =self.teacher_taught + course_ID
            else:
                print("Not eligible")

    def check_teacher_available(self,course_ID):
        if self.teacher_consecutive >=2 or self.teacher_max_working_hour == 0 or course_ID in self.teacher_taught :
            return False
        else:
            return True

    def get_teacherId(self):
        return self.teacher_ID

    def get_teacher_Name(self):
        return self.teacher_name

    def __str__(self):
     return 'Name :' +str(self.teacher_name) + \
            '\nID number: ' + str(self.teacher_ID) + \
            '\nCourses assigned : ' + str(self.teacher_course_assigned) + \
            '\n Batches : ' + str(self.teacher_batch_assigned)

class courses:

    def __init__(self,course_ID,course_Name,course_type,course_credit,course_teacher_ID):
        self.course_ID=course_ID
        self.course_Name=course_Name
        self.course_type=course_type
        self.course_credit = course_credit
        self.course_teacher_ID = course_teacher_ID

    def __str__(self):
        return 'Course Name : ' + str(self.course_ID) + \
                '\n course_Name :' + str(self.course_Name)+\
                '\n course type : ' + str(self.course_type)+\
                '\n course credit count : ' + str(self.course_credit)+\
                '\n teachers teaching this Subject: ' + str(self.course_teacher_ID)
#class rooms:

    #def __init__(self,room_ID,room_Type,room_capacity,):
