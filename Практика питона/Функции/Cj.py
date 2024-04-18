def show_massage(spisok):
    for el in spisok:
        print(el)

def send_massage(spisok):
    sent_massage =[]
    while spisok:
        el = spisok.pop(0)
        print(el)
        sent_massage.append(el)
    return sent_massage




soo = ["sdasd", 'asdasda','ssss']

print(send_massage(soo))
print(soo)