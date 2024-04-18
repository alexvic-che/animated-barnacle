class CPU:

    def __init__(self, name , fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = [*args]

    def get_config(self):
        config = []
        memory_spis =[]
        config.append(f"Материнская плата: {self.name}")
        config.append(f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}")
        config.append(f'Слотов памяти: {self.total_mem_slots}')
        for memory in self.mem_slots:
            if memory == self.mem_slots[-1]:
                memory_spis.append(f"{memory.name} - {memory.volume}")
            else:
                memory_spis.append(f"{memory.name} - {memory.volume};")
        config.append(f"Память: {' '.join(memory_spis)}")

        return config

cpu = CPU('intel', 1400)
mem1 = Memory('krusial', 2000)
mem2 = Memory('krusial', 2000)

mb = MotherBoard("мать", cpu ,mem1, mem2)


for el in mb.get_config():
    print(el)