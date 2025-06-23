class EmptyVariableError(Exception):

    def __init__(self, variable_name=None):
        self.msg = f"Переменная '{variable_name}' пуста" if variable_name else ""

    def __str__(self):
        return self.msg
