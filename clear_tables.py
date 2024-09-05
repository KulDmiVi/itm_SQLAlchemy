from sqlalchemy import text
from models import Base


def truncate_db(session):

    target_metadata = Base.metadata
    for table in target_metadata.sorted_tables:
        session.execute(text(f'ALTER TABLE "{table.name}" DISABLE TRIGGER ALL;'))
        session.execute(table.delete())
        session.execute(text(f'ALTER TABLE "{table.name}" ENABLE TRIGGER ALL;'))
    session.commit()