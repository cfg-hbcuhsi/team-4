import csv

def print_info(college_name):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
            if lines[1] == college_name:
                i=0
                for item_list in  sections:

                    print(item_list,':',lines[i])
                    i+=1
                break




def get_colleges_in_state(state):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
            if lines[5] == state:
                print(lines[1])

def get_colleges_in_city(city):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
            if lines[4] == city:
                print(lines[1])






def get_tuition_and_fees(college_name):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
            if lines[1] == college_name:
                if lines[6] :
                    print(college_name, "Tuition and fees are $",lines[6])
                else:
                    print("No data available for this section.")
                break




def TP_for_out_of_state_on_campus(college_name):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
            if lines[1] == college_name:
                if lines[8] :
                    print("Total price for out-of-state students living on campus at ",college_name, "is $",lines[8])

                else:
                    print("No data available for this section.")
                break



def TP_for_in_of_state_on_campus(college_name):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
            if lines[1] == college_name:
                if lines[7] :
                    print("Total price for in-state students living on campus at ",college_name, "is $",lines[7])

                else:
                    print("No data available for this section.")
                break



def TP_for_in_state_on_campus_nf(college_name):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
            if lines[1] == college_name:
                if lines[9]:
                    print("Total price for in-state students living off campus (not with family) at ",college_name, "is $",lines[9])

                else:
                    print("No data available for this section.")
                break


def TP_for_out_of_state_on_campus_nf(college_name):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
                if lines[1] == college_name:
                    if lines[10]:
                        print("Total price for out-of-state students living off campus (not with family) at ",college_name, "is $",lines[10])

                    else:
                        print("No data available for this section.")
                    break



def TP_for_in_state_off_campus_wf(college_name):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
            if lines[1] == college_name:
                if lines[11]:
                    print("Total price for in-state students living off campus (with family) at ",college_name, "is $",lines[11])

                else:
                    print("No data available for this section.")
                break



def TP_for_out_of_state_off_campus_wf(college_name):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
            if lines[1] == college_name:
                if lines[12]:
                    print("Total price for out-of-state students living off campus (with family) at ",college_name, "is $",lines[12])

                else:
                    print("No data available for this section.")
                break


def get_colleges_with_lower_tuition_than(number):
    with open('lll.csv', mode='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file, delimiter=',')
        sections=file.readline().split(',')

        for lines in csvFile:
            if lines[6]:
                if int(lines[6]) <= number:
                    print(lines[1], "Tuition and fees are $",lines[6])


#print_info("Harvard University")

#get_tuition_and_fees("Harvard University")

#TP_for_out_of_state_on_campus("Harvard University")
#TP_for_in_of_state_on_campus("Harvard University")
#TP_for_in_state_on_campus_nf("Harvard University")
#TP_for_out_of_state_on_campus_nf("Harvard University")
#TP_for_out_of_state_off_campus_wf("Harvard University")


get_colleges_with_lower_tuition_than(5000)