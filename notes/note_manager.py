from collections import UserDict


class Notes(UserDict):
    def __init__(self, notes_namager):
        super().__init__()
        self.notes_namager = notes_namager

    def add_note(self, value, tags=None): # tags=None if we need it(if not, delit it)
        pass
