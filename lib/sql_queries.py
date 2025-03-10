# Select all female bears' names and ages
select_all_female_bears_return_name_and_age = """
    SELECT name, age FROM bears WHERE sex = 'F';
"""

# Select all bears' names and order them alphabetically
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name FROM bears ORDER BY name ASC;
"""

# Select the oldest bear
select_oldest_bear = """
    SELECT name FROM bears ORDER BY age DESC LIMIT 1;
"""

# Select the youngest bear
select_youngest_bear = """
    SELECT name FROM bears ORDER BY age ASC LIMIT 1;
"""

# Select all bears that are alive
select_all_alive_bears = """
    SELECT * FROM bears WHERE alive = 1;
"""

# Select all bears that are not alive
select_all_dead_bears = """
    SELECT * FROM bears WHERE alive = 0;
"""
