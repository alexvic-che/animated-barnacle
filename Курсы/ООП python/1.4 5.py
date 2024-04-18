class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        for d in self.data:
            if d>=0 and d<=10:
                print(d, end=' ')



data = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]

graph_1 = Graph()

graph_1.set_data(data)

graph_1.draw()