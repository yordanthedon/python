length = int(input())
wide = int(input())
heigh = int(input())
percent = float(input())
aquarium = length * wide * heigh
aq_liters = aquarium / 1000
f_aq = percent / 100
need_lit = aq_liters * (1-f_aq)
print(need_lit)