from DBcm import UseDatabase

config = {'host': '127.0.0.1',  # mysql connection config
          'user': 'root',
          'password': 'toor',
          'database': 'todolist', }


def log_task(new_task: str) -> None:  # load task to database
    with UseDatabase(config) as cursor:
        _SQL = """insert into todo
                (task)
                values
                (%s)"""
        cursor.execute(_SQL, (new_task,))


def delete_task(selection: str) -> None:  # delete task from DB
    with UseDatabase(config) as cursor:
        _SQL = """delete from todo
                where task=%s"""
        cursor.execute(_SQL, (selection,))


def view_the_tasks() -> list:  # load tasks from database
    with UseDatabase(config) as cursor:
        _SQL = """select * from todo"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    return [str(task)[3:len(task)-4] for task in contents]