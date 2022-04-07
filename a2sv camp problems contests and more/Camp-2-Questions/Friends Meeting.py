diff = abs(int(input()) - int(input()))

tiredness = ((diff // 2) *(diff//2 + 1))

if diff % 2 == 1:
    tiredness += (diff // 2) + 1

print(tiredness)