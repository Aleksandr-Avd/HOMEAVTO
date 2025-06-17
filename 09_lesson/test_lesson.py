import pytest
from sqlalchemy import create_engine, text

db_connection_string = "postgresql://postgres:Sanja13579@localhost:5432/QA"
db = create_engine(db_connection_string)

@pytest.fixture(scope='function')
def connection():
    conn = db.connect()
    trans = conn.begin()  # Начинаем транзакцию
    yield conn
    trans.rollback()  # Откатываем изменения после теста
    conn.close()

def test_create_subjects(connection):
    # Вставка новой записи
    sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)")
    connection.execute(sql, {"id": 17, "title": "Russian"})

    # Проверка, что запись была добавлена
    result = connection.execute(text("SELECT subject_title FROM subject WHERE subject_id = :id"), {"id": 17})
    title = result.fetchone()
    assert title[0] == "Russian"  # Проверяем, что запись добавлена

def test_update_subject_name(connection):
    # Сначала создаем запись для обновления
    connection.execute(text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"), {"id": 17, "title": "Russian"})

    # Обновление записи
    sql = text("UPDATE subject SET subject_title = :title WHERE subject_id = :id")
    connection.execute(sql, {"title": "Football", "id": 17})

    # Проверка, что запись была обновлена
    result = connection.execute(text("SELECT subject_title FROM subject WHERE subject_id = :id"), {"id": 17})
    title = result.fetchone()
    assert title[0] == "Football"  # Проверяем, что запись обновлена

def test_delete_subject(connection):
    # Сначала создаем запись для удаления
    connection.execute(text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"), {"id": 17, "title": "Russian"})

    # Удаление записи
    sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(sql, {"id": 17})

    # Проверка, что запись была удалена
    result = connection.execute(text("SELECT subject_title FROM subject WHERE subject_id = :id"), {"id": 17})
    title = result.fetchone()
    assert title is None  # 
