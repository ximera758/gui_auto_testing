import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('EN')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 20),
        department=faker_ru.job(),
        salary=random.randint(300, 600),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile_number='3809' + str(random.randint(30000000, 99999999)),
        subject='Maths'
    )


def generated_file():
    path = rf'D:\filetest{random.randint(0, 999)}.txt'

    file = open(path, 'w+')
    file.write(f"Hello World{random.randint(0, 999)}")
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White']
    )

def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00",
    )
