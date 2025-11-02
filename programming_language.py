"""Programming Language"""

"""
Estimated Time: 30minute
Start time:8:00
End time:8:50
"""

class ProgrammingLanguage:
    def __init__(self, name = "", typing = "Static",reflection =False, year = 0):

        self.name = name
        self.year = year
        self.typing = typing
        self.reflection = reflection

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def has_reflection(self):
            return self.reflection == True

    def __str__(self):
        return f"{self.name}, {self.typing} typing, reflection = {self.reflection}, First appeared in {self.year}"







