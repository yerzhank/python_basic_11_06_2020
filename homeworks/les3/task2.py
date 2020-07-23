def show_person_data(name: str, lastname: str, birthdate: str,
                     city: str, email: str, phone: str) -> str:
    result = '{0} {1} {2} {3} {4} {5}'.format(name, lastname, birthdate, city, email, phone)
    return result


x = show_person_data(
    name='Ержан',
    lastname='Кудайбергенов',
    birthdate='09.07.1980',
    city='Астана',
    email='yerzhank@gmail.com',
    phone='+77077770407'
)

print(x)