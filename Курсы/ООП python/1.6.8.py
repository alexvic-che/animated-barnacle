TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"
    def __init__(self, name):
        self.name = name

class DialogLinux:
    name_class = "DialogLinux"
    def __init__(self, name):
        self.name = name
class Dialog:

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            dlg = DialogWindows(*args)
        elif TYPE_OS == 2:
            dlg = DialogLinux(*args)
        else:
            dlg = super().__new__(cls)
        return dlg
    def __init__(self, name):
        self.name = name
