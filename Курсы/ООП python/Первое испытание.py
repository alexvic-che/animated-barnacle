class Server:
    IP = 0
    def __init__(self):
        self.ip = Server.IP + 1
        Server.IP = self.ip
        self.buffer = []
        self.router = None

    def get_ip(self):
        return self.ip

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)
    def get_data(self):
        a = self.buffer[:]
        self.buffer = []
        return a


class Router:
    def __init__(self):
        self.servers = []
        self.buffer = []

    def link(self,server):
        self.servers.append(server)
        server.router = self



    def unlink(self,server):
        self.servers.remove(server)
        server.router = None
    def send_data(self):
        for d in self.buffer:
            for server in self.servers:
                if d.ip == server.ip:
                    server.buffer.append(d)
        self.buffer = []



class Data:

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv1 = Server()
sv2 = Server()
router.link(sv1)
router.link(sv2)
print(router.servers)
router.link(Server())
router.link(Server())
sv3 = Server()
router.link(sv3)
sv1.send_data(Data("Hello", sv3.get_ip()))
sv2.send_data(Data("Hello", sv3.get_ip()))
sv3.send_data(Data("Hi", sv1.get_ip()))
print(router.buffer)
router.send_data()
print(router.buffer)

msg_lst_from = sv1.get_data()

msg_lst_to = sv3.get_data()


