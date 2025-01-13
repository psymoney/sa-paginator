from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from test.models import User
from src import BaseColumn


e = create_engine("sqlite:///example.db")
session_factory = sessionmaker(bind=e)


class UserColumn(BaseColumn):
    name = "name", User.name
    id = "id", User.id
    value = "value", User.value
    value_2 = "value_2", User.value_2
    total = "total", User.value + User.value_2


col_id: UserColumn = UserColumn["id"]
col_name: UserColumn = UserColumn["name"]
col_value: UserColumn = UserColumn["value"]
col_total: UserColumn = UserColumn["total"]


def test_eq():
    session = session_factory()
    
    query = (
        select(User)
    )
    
    query = query.where(col_name == "Tester")
    
    result = session.scalar(query)
    
    assert result.id == 1
    assert result.name == "Tester"
    

def test_ne():
    session = session_factory()
    
    query = select(User).where(col_value != 30)
    
    results = session.scalars(query).fetchall()
    
    assert len(results) == 3
    for result in results:
        assert result.value != 30
        

def test_ge():
    session = session_factory()
    
    query = select(User).where(col_value >= 30)
    
    results = session.scalars(query).fetchall()
    
    assert len(results) == 3
    for result in results:
        assert result.value >= 30
    

def test_gt():
    session = session_factory()
    
    query = select(User).where(col_value > 30)
    
    results = session.scalars(query).fetchall()
    
    assert len(results) == 2
    for result in results:
        assert result.value > 30
    

def test_le():
    session = session_factory()
    
    query = select(User).where(col_value <= 30)
    
    results = session.scalars(query).fetchall()
    
    assert len(results) == 2
    for result in results:
        assert result.value <= 30
    

def test_lt():
    session = session_factory()
    
    query = select(User).where(col_value < 30)
    
    results = session.scalars(query).fetchall()
    
    assert len(results) == 1
    for result in results:
        assert result.value < 30
    

def test_like():
    session = session_factory()
    
    query = select(User)
    
    query = query.where(col_name.like("Ma"))
    
    result = session.scalars(query).fetchall()
    
    assert len(result) == 2


def test_name_asc():
    session = session_factory()
    
    results = session.scalars(select(User).order_by(col_name.asc)).fetchall()
    
    assert results[0].id == 4
    assert results[1].id == 2
    assert results[2].id == 1
    assert results[3].id == 3
    
    
def test_name_desc():
    session = session_factory()
    
    results = session.scalars(select(User).order_by(col_name.desc)).fetchall()
    
    assert results[0].id == 3
    assert results[1].id == 1
    assert results[2].id == 2
    assert results[3].id == 4
    

def test_id_desc():
    session = session_factory()
    
    results = session.scalars(select(User).order_by(col_id.asc)).fetchall()
    
    assert results[0].id == 1
    assert results[1].id == 2
    assert results[2].id == 3
    assert results[3].id == 4

    
def test_id_desc():
    session = session_factory()
    
    results = session.scalars(select(User).order_by(col_id.desc)).fetchall()
    
    assert results[0].id == 4
    assert results[1].id == 3
    assert results[2].id == 2
    assert results[3].id == 1


def test_func_col():
    session = session_factory()
    result = session.scalar(
        select(User)
        .where(col_value == 30)
    )
    
    assert result.value == 30
    

def test_func_sum_col():
    session = session_factory()
    result = session.scalar(
        select(User)
        .where(col_total == 40)
    )
    
    assert result.value == 30
