class VideoItem:
    def __init__(self,title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()

class VideoRating:
    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, r):
        if not 0<=r<=5:
            raise ValueError('неверное присваиваемое значение')
        self.__rating = r

v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
