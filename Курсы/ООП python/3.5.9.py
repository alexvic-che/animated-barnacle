filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc",
             "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
class FileAcceptor:
    def __init__(self, *args):
        self.exts = args

    def __call__(self,filename):
        return any(map(lambda x: x in filename, self.exts))

    def __add__(self, other):
        new_exts = tuple(set(self.exts) | set(other.exts))
        return FileAcceptor(*new_exts)

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)