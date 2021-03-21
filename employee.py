class Employee:
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
    def print_info(self):
        print(self.name, self.surname, self.age, self.salary)
            		

with open('dataset1.csv') as file:
    employees = []
    for line in file.readlines()[1:]:
        parsed_line = line.strip().split(',')
        temp_emp = Employee(parsed_line[0], parsed_line[1], int(parsed_line[2]), int(parsed_line[3]))
        employees.append(temp_emp)
    lowest_sal_employee = min(employees, key = lambda emp: emp.salary)
    oldest_employee = max(employees, key = lambda emp: emp.age)


print('Employee with the lowest salary: ', end = '')
lowest_sal_employee.print_info()
print('The oldest employee: ', end = '')
oldest_employee.print_info()
