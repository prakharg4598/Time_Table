import csv
import ww

################################333
#########reduce the if statements in the main() for teacher
###################################################

def main():
    teachers = []
    with open('test_tt.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            teachers.append(ww.teacher(row[0], row[1], row[2].split(), row[3].split(), row[4]))
    courses = []
    with open('test_ct.csv', 'r') as g:
        reader1 = csv.reader(g)
        for row1 in reader1:
            courses.append(ww.courses(row1[0], row1[1], row1[2], row1[3], row1[4].split()))

    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
    rooms = ['G1','G2', 'G3']
    #rooms = {'G1': 90, 'G2': 90} // For occupying batches of sizes accordingly

    # teacher1 = tt.teacher(1,'SKS', ['CI121','CI232','CI565'], ['B1,B2,B3','B3,B5,B6','B4,B2,B1'],4);
    # print(teacher1)
    # print('')
    # teacher1.teacher_occupy(['CI121'])
    # print(teacher1.teacher_batch_assigned[1])
    # print(teacher1.teacher_taught)
    """for t in teachers:
        print(t)
        print("")
        print(t.teacher_batch_assigned[0])
    for c in courses:
        print(c)
        print("")"""
    checking_time_to_free_teachers=0
    checking_day_to_free_teachers=0
    assign = [[[0] * len(rooms)] * 8] * 7
    for day in range(len(days)):
        #print("The Day is: " + days[day])

        if day==5:
            for time in range(4):
                #print("\nThe Time is: " + str(time))
                for room in range(len(rooms)):
                    #print("The Room is: " + str(room))

                    for teacher in teachers:
                        if day>checking_day_to_free_teachers:
                            #print("New Day")
                            checking_day_to_free_teachers=day
                            #print("\n\nFreeing all Teachers")
                            checking_time_to_free_teachers = time
                            #print("\n\nResetting course indices")

                            for teacher1 in teachers:
                                teacher1.current_busy = 0
                                teacher1.teacher_max_working_hour = 4
                                teacher1.teacher_last_time = -1
                                teacher1.teacher_taught=[]
                                teacher1.teacher_course_current_index=0

                        if time>checking_time_to_free_teachers:
                            #print("\n\nFreeing all Teachers")
                            checking_time_to_free_teachers = time
                            for teacher1 in teachers:
                                teacher1.current_busy = 0

                        #print("\nThe Teacher is:" + teacher.teacher_name + " with remaining working hours = "+str(teacher.teacher_max_working_hour))
                        #print("Teacher Current Course Index = "+str(teacher.teacher_course_current_index)+"\nNumber of Courses Assigned = "+str(len(teacher.teacher_course_assigned)))
                        #print("\n*************CHECKING Teacher*****************")
                        #if teacher.teacher_course_current_index < len(teacher.teacher_course_assigned):
                            #print(str(teacher.teacher_course_current_index) + "<" + str(len(teacher.teacher_course_assigned)) + " AND " + str(teacher.check_teacher_available(teacher.teacher_course_assigned[teacher.teacher_course_current_index])) + " = TRUE (Teacher Available) " + " AND " + str(teacher.current_busy) + " != 1 (Busy)")
                        #else:
                            #print("Number of courses crossed by: "+str(teacher.teacher_name))

                        #print("**********************************************\n")

                        #print(str(teacher.teacher_course_current_index) + "<" +str(len(teacher.teacher_course_assigned)))

                        if teacher.teacher_course_current_index < len(teacher.teacher_course_assigned) and teacher.check_teacher_available(teacher.teacher_course_assigned[teacher.teacher_course_current_index]) and teacher.current_busy != 1:
                            for course in courses:
                                #print("\nThe Course is:" + course.course_ID + " with "+str(course.course_credit_remaining)+" remaining credits.")
                                #print("\n*************CHECKING*****************")
                                #if teacher.teacher_course_current_index < len(teacher.teacher_course_assigned):
                                    #print(str(course.course_ID)+" =? "+str(teacher.teacher_course_assigned[teacher.teacher_course_current_index])+" AND "+str(course.check_course_credit_remaining())+" = TRUE (Course Credit Remaining?)"+" AND "+str(teacher.current_busy)+" != 1 (Busy)"+" AND "+str(teacher.teacher_last_time) + " != " + str(time)+" LastTime")
                                #else:
                                    #print("Number of courses crossed by: " + str(teacher.teacher_name))
                                #print("**************************************\n")

                                #if course.course_ID == teacher.teacher_course_assigned[teacher.teacher_course_current_index] and course.check_course_credit_remaining() and teacher.current_busy != 1 and teacher.teacher_last_time != time:
                                if teacher.teacher_course_current_index < len(teacher.teacher_course_assigned) and course.course_ID == teacher.teacher_course_assigned[teacher.teacher_course_current_index] and course.check_course_credit_remaining() and teacher.current_busy != 1 and teacher.teacher_last_time != time:
                                    assign[day][time][room] = teacher.teacher_ID
                                    teacher.teacher_last_time = time
                                    teacher.teacher_occupy(teacher.teacher_course_assigned[teacher.teacher_course_current_index])
                                    # j = j + 1
                                    if teacher.teacher_course_current_index+1 < len(teacher.teacher_course_assigned):
                                        teacher.teacher_course_current_index = teacher.teacher_course_current_index + 1
                                        #print("Current Course Index="+str(teacher.teacher_course_current_index))
                                    if time<4:
                                        print(days[day], (time + 9) % 13, ":00", rooms[room], teacher.teacher_name,
                                              teacher.teacher_course_assigned[teacher.teacher_course_current_index])
                                    else:
                                        print(days[day], (time + 11) % 13, ":00", rooms[room], teacher.teacher_name,
                                              teacher.teacher_course_assigned[teacher.teacher_course_current_index])
                                        #break at 1:00PM
                                    course.course_studied()
                                    break
                                if teacher.teacher_course_current_index < len(teacher.teacher_course_assigned) and course.course_ID==teacher.teacher_course_assigned[teacher.teacher_course_current_index] and not course.check_course_credit_remaining():
                                    #print("\nCourse Credit for: "+course.course_ID+" is Finished")
                                    teacher.teacher_course_current_index = teacher.teacher_course_current_index + 1
                            break
        else:
            for time in range(7):
                #print("\nThe Time is: " + str(time))
                for room in range(len(rooms)):
                    #print("The Room is: " + str(room))

                    for teacher in teachers:
                        if day>checking_day_to_free_teachers:
                            #print("New Day")
                            checking_day_to_free_teachers=day
                            #print("\n\nFreeing all Teachers")
                            checking_time_to_free_teachers = time
                            #print("\n\nResetting course indices")

                            for teacher1 in teachers:
                                teacher1.current_busy = 0
                                teacher1.teacher_max_working_hour = 4
                                teacher1.teacher_last_time = -1
                                teacher1.teacher_taught=[]
                                teacher1.teacher_course_current_index=0

                        if time>checking_time_to_free_teachers:
                            #print("\n\nFreeing all Teachers")
                            checking_time_to_free_teachers = time
                            for teacher1 in teachers:
                                teacher1.current_busy = 0

                        #print("\nThe Teacher is:" + teacher.teacher_name + " with remaining working hours = "+str(teacher.teacher_max_working_hour))
                        #print("Teacher Current Course Index = "+str(teacher.teacher_course_current_index)+"\nNumber of Courses Assigned = "+str(len(teacher.teacher_course_assigned)))
                        #print("\n*************CHECKING Teacher*****************")
                        #if teacher.teacher_course_current_index < len(teacher.teacher_course_assigned):
                            #print(str(teacher.teacher_course_current_index) + "<" + str(len(teacher.teacher_course_assigned)) + " AND " + str(teacher.check_teacher_available(teacher.teacher_course_assigned[teacher.teacher_course_current_index])) + " = TRUE (Teacher Available) " + " AND " + str(teacher.current_busy) + " != 1 (Busy)")
                        #else:
                            #print("Number of courses crossed by: "+str(teacher.teacher_name))

                        #print("**********************************************\n")

                        #print(str(teacher.teacher_course_current_index) + "<" +str(len(teacher.teacher_course_assigned)))

                        if teacher.teacher_course_current_index < len(teacher.teacher_course_assigned) and teacher.check_teacher_available(teacher.teacher_course_assigned[teacher.teacher_course_current_index]) and teacher.current_busy != 1:
                            for course in courses:
                                #print("\nThe Course is:" + course.course_ID + " with "+str(course.course_credit_remaining)+" remaining credits.")
                                #print("\n*************CHECKING*****************")
                                #if teacher.teacher_course_current_index < len(teacher.teacher_course_assigned):
                                    #print(str(course.course_ID)+" =? "+str(teacher.teacher_course_assigned[teacher.teacher_course_current_index])+" AND "+str(course.check_course_credit_remaining())+" = TRUE (Course Credit Remaining?)"+" AND "+str(teacher.current_busy)+" != 1 (Busy)"+" AND "+str(teacher.teacher_last_time) + " != " + str(time)+" LastTime")
                                #else:
                                    #print("Number of courses crossed by: " + str(teacher.teacher_name))
                                #print("**************************************\n")

                                #if course.course_ID == teacher.teacher_course_assigned[teacher.teacher_course_current_index] and course.check_course_credit_remaining() and teacher.current_busy != 1 and teacher.teacher_last_time != time:
                                if teacher.teacher_course_current_index < len(teacher.teacher_course_assigned) and course.course_ID == teacher.teacher_course_assigned[teacher.teacher_course_current_index] and course.check_course_credit_remaining() and teacher.current_busy != 1 and teacher.teacher_last_time != time:
                                    assign[day][time][room] = teacher.teacher_ID
                                    teacher.teacher_last_time = time
                                    teacher.teacher_occupy(teacher.teacher_course_assigned[teacher.teacher_course_current_index])
                                    # j = j + 1
                                    if teacher.teacher_course_current_index+1 < len(teacher.teacher_course_assigned):
                                        teacher.teacher_course_current_index = teacher.teacher_course_current_index + 1
                                        #print("Current Course Index="+str(teacher.teacher_course_current_index))
                                    if time<4:
                                        print(days[day], (time + 9) % 13, ":00", rooms[room], teacher.teacher_name,
                                              teacher.teacher_course_assigned[teacher.teacher_course_current_index])
                                    else:
                                        print(days[day], (time + 11) % 13, ":00", rooms[room], teacher.teacher_name,
                                              teacher.teacher_course_assigned[teacher.teacher_course_current_index])
                                        #break at 1:00PM
                                    course.course_studied()
                                    break
                                if teacher.teacher_course_current_index < len(teacher.teacher_course_assigned) and course.course_ID==teacher.teacher_course_assigned[teacher.teacher_course_current_index] and not course.check_course_credit_remaining():
                                    #print("\nCourse Credit for: "+course.course_ID+" is Finished")
                                    teacher.teacher_course_current_index = teacher.teacher_course_current_index + 1
                            break






main()
