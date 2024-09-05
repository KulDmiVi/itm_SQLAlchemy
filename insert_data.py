import datetime

from models import Provider, Employees, Client, Supply
from db_select import get_providers


def insert_providers():
    providers = [
        Provider(
            name_of_provider='ООО Рога и Копыта',
            phone='8911111111',
            address='Россия',
            representative='Рога и Копыта',
            speak_to='fdvbfsdggfds fdgfsd fdgdfg'),
        Provider(
            name_of_provider='ООО Рога и Копыта2',
            phone='8911111111',
            address='Россия',
            representative='Рога и Копыта2',
            speak_to='fdvbfsdggfds fdgfsd fdgdfg'),
        Provider(
            name_of_provider='ООО Рога и Копыта3',
            phone='8911111111',
            address='Россия',
            representative='Рога и Копыта3',
            speak_to='fdvbfsdggfds fdgfsd fdgdfg'),
        Provider(
            name_of_provider='ООО Рога и Копыта4',
            phone='8911111111',
            address='Россия',
            representative='Рога и Копыта4',
            speak_to='fdvbfsdggfds fdgfsd fdgdfg'),
        Provider(
            name_of_provider='ООО Рога и Копыта5',
            phone='8911111111',
            address='Россия',
            representative='Рога и Копыта5',
            speak_to='fdvbfsdggfds fdgfsd fdgdfg')]
    return providers


def insert_employees():
    employees = [
        Employees(
            family='Иванов',
            name='Иван',
            suraname='Иванович',
            job_title='Менеджер',
            address='Роосия ул. Тестовая',
            home_phone='9111111111',
            birthday='1990-01-01'),
        Employees(
            family='Иванов',
            name='Иван',
            suraname='Иванович',
            job_title='Менеджер',
            address='Роосия ул. Тестовая',
            home_phone='9111111111',
            birthday='1990-01-01'),
        Employees(
            family='Иванов',
            name='Иван',
            suraname='Иванович',
            job_title='Менеджер',
            address='Роосия ул. Тестовая',
            home_phone='8111111111',
            birthday='1990-01-01'),
        Employees(
            family='Иванов',
            name='Иван',
            suraname='Иванович',
            job_title='Менеджер',
            address='Роосия ул. Тестовая',
            home_phone='9111111111',
            birthday='1990-01-01'),
        Employees(
            family='Иванов',
            name='Иван',
            suraname='Иванович',
            job_title='Менеджер',
            address='Роосия ул. Тестовая',
            home_phone='9111111111',
            birthday='1990-01-01')]
    return employees


def insert_clients():
    clients = [
        Client(
            fullname="Иванов Иван Иванович",
            address="Россия",
            phone="9111111111"), Client(
            fullname="Иванов Иван Иванович",
            address="Россия",
            phone="9111111111"
        ),
        Client(
            fullname="Иванов Иван Иванович",
            address="Россия",
            phone="8111111111"
        ),
        Client(
            fullname="Иванов Иван Иванович",
            address="Россия",
            phone="9111111111"
        ),
        Client(
            fullname="Иванов Иван Иванович",
            address="Россия",
            phone="9111111111"
        )]
    return clients


def insert_suply(session):
    suplies = []
    providers = get_providers(session)
    for provider in providers:
        suplies.append(
            Supply(
                id_provider=provider.id_provider,
                data_of_supply=datetime.date.today()
            )

        )
    return suplies
