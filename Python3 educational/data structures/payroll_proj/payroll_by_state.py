import csv, datetime
#csv format:
#payroll date, work state, last name, first name, job title, regular pay, taxes, employee total cost (A-H)
class Employee:
    def __init__(self, payroll_date, work_state, last_name, first_name, job_title, regular_pay, taxes, employee_total_cost):
        self.payroll_date = payroll_date
        if work_state == "":
            self.work_state = 'CA'
        else:
            self.work_state = work_state
        self.last_name = last_name
        self.first_name = first_name
        self.job_title = job_title
        self.regular_pay = regular_pay
        self.taxes = taxes
        self.employee_total_cost = employee_total_cost

    def __repr__(self):
        return "\nInitializing employee: " +str(self.first_name) + " " + str(self.last_name) + '('+str(self.job_title) + ')'+ " worked in " + str(self.work_state) + " for the payroll date of " + str(self.payroll_date) + '.' + "**Company cost**: " + str(self.employee_total_cost)



payroll_date = []
work_state = []
last_name = []
first_name = []
job_title = []
regular_pay = []
taxes = []
employee_total_cost = []
#state payrolls

total_company_payroll = []


with open('payroll_dummy_project.csv') as csvfile, open('payroll_dummy_project_keys.csv') as csvkeys:
    payroll = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in payroll:
        payroll_date.append(row[i])
        work_state.append(row[i + 1])
        last_name.append(row[i + 2])
        first_name.append(row[i + 3])
        job_title.append(row[i + 4])
        regular_pay.append(row[i + 5])
        taxes.append(row[i + 6])
        employee_total_cost.append(row[i + 7])

    relocation = csv.reader(csvkeys, delimiter=',')
    for row in relocation:
        print(row)

#global functions


def print_payroll():
     return ("Total employer cost over " + str(payroll_date[1]) + " to " + str(payroll_date[30]) + ' is: $' + str(total_payroll))


print(payroll_date)
print(employee_total_cost)
print(len(payroll_date))
print(len(employee_total_cost))

for i in range(len(payroll_date)):
    if(i==0):
        i += 1
        continue
    else:
        temp = Employee(payroll_date[i], work_state[i], last_name[i], first_name[i], job_title[i], regular_pay[i], taxes[i], employee_total_cost[i])
        total_company_payroll.append(temp)
        i += 1

total_payroll = 0
for i in range(1,31):
    total_payroll += int(employee_total_cost[i])

print(print_payroll())
print(total_company_payroll)