class Note:
    note_name = ( 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    note_ton = (-1,1,0)
    def __init__(self,name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == "_name":
            if not value in self.note_name:
                raise ValueError('недопустимое значение аргумента')
        if key == '_ton':
            if not value in self.note_ton:
                raise ValueError('недопустимое значение аргумента')
        super().__setattr__(key, value)

class Notes:
    __is_instance = None
    __slots__ = ('_do','_re','_mi','_fa','_solt','_la','_si')

    def __new__(cls, *args, **kwargs):
        if cls.__is_instance is None:
            cls.__is_instance = super().__new__(cls, *args, **kwargs)
        return cls.__is_instance

    def __del__(self):
        Notes.__is_insatnce = None

    def __init__(self):
        self._do = Note('до',0)
        self._re = Note('ре', 0)
        self._mi = Note('ми', 0)
        self._fa = Note('фа', 0)
        self._solt = Note('соль', 0)
        self._la = Note('ля', 0)
        self._si = Note('си', 0)

    def check_index(self,indx):
        if type(indx) != int:
            raise IndexError('недопустимый индекс')
        if not 0<=indx<=6:
            raise IndexError('недопустимый индекс')
    def __getitem__(self, item):
        self.check_index(item)
        notes_tup = (self._do, self._re, self._mi, self._fa, self._solt, self._la, self._si)
        return notes_tup[item]

notes = Notes()

