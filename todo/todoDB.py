from DBcm import UseDatabase

config = {'host': '127.0.0.1',  # mysql connection config
          'user': 'root',
          'password': 'toor',
          'database': 'todolist', }


def log_request(task: str) -> None:  # load task to database
    with UseDatabase(config) as cursor:
        _SQL = """insert into todo
                (task)
                values
                (%s)"""
        cursor.execute(_SQL, (task))


def view_the_tasks() -> list:  # load taks from database
    with UseDatabase(config) as cursor:
        _SQL = """select * from todo"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    return [str(task)[3:len(task)-4] for task in contents]
