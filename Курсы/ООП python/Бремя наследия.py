class Vertex:
    def __init__(self):
        self._links = []
    @property
    def links(self):
        return self._links


class Link:
    def __init__(self,v1,v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1
    @property
    def v2(self):
        return self._v2
    @property
    def dist(self):
        return self._dist
    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self,v):
        if v not in self._vertex:
            self._vertex.append(v)
    def __check_vertex(self,vertex_in_list, new_vertex):
        vil1 = vertex_in_list.v1
        vil2 = vertex_in_list.v2
        v1 = new_vertex.v1
        v2 = new_vertex.v2
        if (v1 == vil1 or v1 == vil2) and (v2 == vil1 or v2 == vil2):
            return True
        return False

    def add_link(self,link):

        check = list(filter(lambda x: self.__check_vertex(x, link),self._links))
        if not check:
            self._links.append(link)
            v1 = link.v1
            v2 = link.v2
            self.add_vertex(v1)
            self.add_vertex(v2)

    def find_path(self, start_v, stop_v):
        self._start_v = start_v
        self._stop_v = stop_v
        return self._next(self._start_v,None,[],[])
    def _dist_path(self,links):
        return sum([x.dist for x in links if x is not None])

    def _next(self, current, link_prev, current_path, current_links):
        current_path += [current]
        if link_prev:
            current_links += [link_prev]

        if current == self._stop_v:
            return current_path, current_links

        len_path = -1
        best_path = []
        best_links = []
        for link in self._links:  # Используем все связи
            path = []
            links = []
            if link.v1 == current and link not in current_links:
                path, links = self._next(link.v2, link, current_path[:], current_links + [link])
            elif link.v2 == current and link not in current_links:
                path, links = self._next(link.v1, link, current_path[:], current_links + [link])

            if self._stop_v in path and (len_path > self._dist_path(links) or len_path == -1):
                len_path = self._dist_path(links)
                best_path = path[:]
                best_links = links[:]

        return best_path, best_links

class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self,v1, v2, dist):
        super().__init__(v1, v2)
        self.dist = dist

map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path)    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
 # 7
print(sum([x.dist for x in path[1]]))