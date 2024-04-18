filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg",
             "forest.jpeg", "eq_1.png",
             "eq_2.png", "my.html", "data.shtml"]

class ImageFileAcceptor:

    def __init__(self,extensions):
        self.extensions = extensions

    def __call__(self, filename, *args, **kwargs):
        sp = filename.split(".")
        for el in sp:
            if el in self.extensions:
                return True
        return False

acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
