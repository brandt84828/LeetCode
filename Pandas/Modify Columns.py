import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.salary *= 2
    return employees

    #employees['salary'] = employees['salary'] * 2
    #return employees

    #employees.assign(salary=2 * employees['salary'])