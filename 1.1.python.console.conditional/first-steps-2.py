from time import sleep

dolly = ('овца', 'овцы', 'овец')
count = 0
end = int(input('До скольки будем считать перед сном: '))
while True:
    count += 1
    if count == end + 1:
        break
    elif count % 10 == 1 and count != 11:
        n = 0
    elif count % 10 in [2, 3, 4] and count not in [12, 13, 14]:
        n = 1
    else:
        n = 2
    print('{} {}'.format(count, dolly[n]))
    sleep(1)
