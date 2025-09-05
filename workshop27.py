# คำสั่ง break , continue
# break หากถูกทำงาน จะถือว่าจบ loop ทันที
# continue หากถูกทำงาน จะถือว่าจบ รอบ นั้นและไปรอบต่อไปทันที

for i in range (5) :
    if i == 3 :
        break
    print (i,'Hi...')

print ('-----------------')

for i in range (5) :
    if i == 3 :
        continue
    print (i,'Hey...')