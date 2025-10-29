import employee_info as ei

def test_age_range():
    result=[]
    result=ei.get_employees_by_age_range(24,36)
    ans = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    assert(result==ans)

def test_average_salary():
    result=0
    result=ei.calculate_average_salary()
    ans=180500/3
    assert(ans==result)

def test_department():
    result=[]
    result=ei.get_employees_by_dept("Sales")
    ans = employee_data = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    assert(ans==result)
    

