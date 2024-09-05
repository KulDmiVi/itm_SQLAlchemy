from db_utils import get_session
from db_select import test_selects
from insert_data import insert_providers, insert_employees, insert_clients, insert_suply
from clear_tables import truncate_db


def insert_data(session):
    providers = insert_providers()
    session.add_all(providers)
    employees = insert_employees()
    session.add_all(employees)
    clients = insert_clients()
    session.add_all(clients)
    session.commit()
    suply = insert_suply(session)
    session.add_all(suply)
    session.commit()


def test_db():
    session, engine = get_session()
    print("Вставка данных")
    insert_data(session)

    print("\nРазличные запросы к бд данных")
    test_selects(session)

    print("\nОчистка таблиц")
    truncate_db(session)
    session.close()


if __name__ == "__main__":
    test_db()
