slovo = list(input().lower())
slovoR = slovo[:]
slovo.reverse()


msg = 'палиндром' if slovo == slovoR  else 'не палиндром'
print(msg)