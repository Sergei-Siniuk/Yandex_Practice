sms = dict()

for i in range(1, int(input()) + 1):
    a = input()
    if a == "0":
        sms[input()] = [str(i)]
        input()
    else:
        input()
        for key, values in sms.items():
            if a in values:
                # sms[key] = sms.setdefault(key)+([str(i)])
                sms[key] = sms.get(key) + [str(i)]

sms = tuple(sms.items())
sms = sorted(sms, key=lambda x: len(x[1]), reverse=True)
print(sms[0][0])
