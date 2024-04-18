TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog:

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            dlg = DialogWindows()
        elif TYPE_OS == 2:
            dlg = DialogLinux()
        return 
    def __init__(self, name):
        self.name = name