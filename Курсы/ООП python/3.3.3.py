class Model:
    def __init__(self):
        self.d = {}
    def query(self, **kwargs):
        self.d = kwargs
        print(self.d)
    def __str__(self):
        if self.d:
            st = "Model:"
            for key, value in self.d.items():
                st += f"{key}={value},"

            return st.strip(",")
        else:
            return "Model"



model = Model()

model.query(id=1, fio='Sergey', old=33)
print(model)




