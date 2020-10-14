# 11-1. City, Country
'''
def city_country(city_name, country_name, population):
    if population:
        city_and_country = f"{city_name}, {country_name} - Population {population}"
    else:
        city_and_country = f"{city_name}, {country_name}"
    return city_and_country.title()

print(city_country("santiago", "chile", 50000))
# 11-2. Population : Add a 3rd variable to city country
# Make sure it works with test_cities.py

'''

# 11-3 Employee

class Employee():

    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
        print(annual_salary)

    def give_raise(self, salary_raise):
        self.salary_raise = salary_raise
        if salary_raise:
            self.annual_salary = 5000
        else:
            self.annual_salary += salary_raise

name = Employee(first='daniel', last='ver')
print(name)