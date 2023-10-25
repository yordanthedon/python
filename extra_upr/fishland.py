scumria = float(input())
caca = float(input())
palamud = float(input())
safrid = float(input())
midi_k = int(input())
palamud_k = scumria + scumria * 0.6
palamud_sum = palamud_k * palamud
safrid_k = caca + caca * 0.8
safrid_sum = safrid_k * safrid
midi = midi_k * 7.5
total = palamud_sum + safrid_sum + midi
print(f"{total: .2f}")