class Morph:
    def __init__(self, *args):
        self.morphs = [*args]

    def add_word(self,word):
        if word not in self.morphs:
            self.morphs.append(word)
    def get_words(self):
        return tuple(self.morphs)

    def __eq__(self, other):
        for el in self.morphs:
            if el in other.lower():
                return True

        return False

dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов',
                    'векторам', 'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов',
                    'эффектам', 'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
              ]
text = input()
i = 0

for el in text.split():
    for m in dict_words:
        if el == m:
            i+=1

print(i)
