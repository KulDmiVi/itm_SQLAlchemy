from sqlalchemy import func, or_

from models import Provider, Employees, Client, Supply


def get_providers(session):
    return session.query(Provider).all()


def get_clients(session):
    return session.query(Client).all()


def get_providers_filter(session):
    return session.query(Provider).filter(Provider.name_of_provider.like('%2%')).all()


def get_employees_order(session):
    return session.query(Employees).order_by(Employees.id_employee.desc())


def get_clients_count(session):
    return session.query(Client.phone, Client.fullname, func.count().label('user_count')).group_by(Client.phone,
                                                                                                   Client.fullname)


def get_clients_distinct(session):
    return session.query(Client.phone, Client.fullname).distinct(Client.phone)


def get_supply(session):
    return session.query(Supply, Provider). \
        join(Provider, Supply.id_provider == Provider.id_provider). \
        filter(
        or_(Provider.name_of_provider == 'ООО Рога и Копыта2', Provider.name_of_provider == 'ООО Рога и Копыта3')). \
        all()


def delete_client(session):
    return session.query(Client).filter(Client.phone.like('8%')).delete()


def test_selects(session):


    print('Поставщики')
    for provider in get_providers(session):
        print(provider.id_provider, provider.name_of_provider)
        for supply in provider.supplies:
            print(supply.id_supply)

    print('Сотрудники')
    for employee in get_employees_order(session):
        print(employee.id_employee, employee.family, employee.name, employee.suraname, employee.job_title)

    print('Количество покупателей сгруппированных по номеру телефона')
    for client in get_clients_count(session):
        print(client.phone, client.user_count)

    print('Уникальных номеров покупателей')
    for client in get_clients_distinct(session):
        print(client.fullname, client.phone)

    print('Удаление покупателя')
    delete_client(session)

    print('Количество покупателей')
    for client in get_clients_count(session):
        print(client.user_count)

    print('Поставщики где в имени есть 2')
    for provider in get_providers_filter(session):
        print(provider.id_provider, provider.name_of_provider)

    print('Поступления join Поставщик')
    for supply, provider in get_supply(session):
        print(supply.id_supply, supply.id_provider, supply.data_of_supply, provider.name_of_provider)
