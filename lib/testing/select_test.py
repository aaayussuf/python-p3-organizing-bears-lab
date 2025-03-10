#!/usr/bin/env python3

import pytest
import sqlite3
from lib.sql_queries import (
    select_all_female_bears_return_name_and_age,
    select_all_bears_names_and_orders_in_alphabetical_order,
    select_oldest_bear,
    select_youngest_bear,
    select_all_alive_bears,
    select_all_dead_bears
)

@pytest.fixture
def connection():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    with open("lib/create.sql") as create_file:
        cursor.executescript(create_file.read())
    
    with open("lib/seed.sql") as seed_file:
        cursor.executescript(seed_file.read())
    
    yield conn
    conn.close()

def test_select_all_female_bears(connection):
    cursor = connection.cursor()
    cursor.execute(select_all_female_bears_return_name_and_age)
    results = cursor.fetchall()
    assert results != []

def test_select_all_bears_names_and_orders_in_alphabetical_order(connection):
    cursor = connection.cursor()
    cursor.execute(select_all_bears_names_and_orders_in_alphabetical_order)
    results = cursor.fetchall()
    assert results != []

def test_select_oldest_bear(connection):
    cursor = connection.cursor()
    cursor.execute(select_oldest_bear)
    result = cursor.fetchone()
    assert result is not None

def test_select_youngest_bear(connection):
    cursor = connection.cursor()
    cursor.execute(select_youngest_bear)
    result = cursor.fetchone()
    assert result is not None

def test_select_all_alive_bears(connection):
    cursor = connection.cursor()
    cursor.execute(select_all_alive_bears)
    results = cursor.fetchall()
    assert results != []

def test_select_all_dead_bears(connection):
    cursor = connection.cursor()
    cursor.execute(select_all_dead_bears)
    results = cursor.fetchall()
    assert results != []
