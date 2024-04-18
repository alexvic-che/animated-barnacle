a, b, c = map(int, input().split())

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

a_n = ("#"+m[a-1] if m[a-1] == "до" or m[a-1] == "фа" else m[a-1])
b_n = ("#"+m[b-1] if m[b-1] == "до" or m[b-1] == "фа" else m[b-1])
c_n = ("#"+m[c-1] if m[c-1] == "до" or m[c-1] == "фа" else m[c-1])
print(a_n, b_n, c_n)