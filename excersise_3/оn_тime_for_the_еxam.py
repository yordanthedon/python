hour_exam = int(input())
min_exam = int(input())
hour_arrive = int(input())
min_arrive = int(input())

total_min_exam = (hour_exam * 60) + min_exam
total_min_arrive = (hour_arrive * 60) + min_arrive

diff = abs (total_min_exam - total_min_arrive)
if total_min_exam < total_min_arrive:
    print("Late")
    if diff >= 60:
        hour = diff // 60
        minutes = diff % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff} minutes after the start")
elif total_min_exam == total_min_arrive or diff <= 30:
    print("On time")
    if diff > 0:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff >= 60:
        hour = diff // 60
        minutes = diff % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff} minutes before the start")