
f = open('spam.txt', 'r')
a = f.read()
sham_va = eval(a)
#print(sham_va)
f = open('ham.txt', 'r')
a = f.read()
ham_va = eval(a)

sham_va_word = []
sham_va_p=[]
sum  = 0
for word in sham_va:
    sum = sum + word[1]
for word in sham_va:
    sham_va_word.append(word[0])
    sham_va_p.append(word[1]/sum)

ham_va_word = []
ham_va_p = []
sum1 = 0
for word in ham_va:
    sum1 = sum1+word[1]
for word in ham_va:
    ham_va_word.append(word[0])
    ham_va_p.append(word[1]/sum1)
print(ham_va_p)
print(sham_va_p)
sump=0
for p in sham_va_p:
    sump = sump + p
print(sump)