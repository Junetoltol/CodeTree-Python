secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
# 정보 담는 클래스 정의
class SecretMission:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

# 객체 생성
mission = SecretMission(secret_code, meeting_point, time)

# 출력
print(f"secret code : {mission.secret_code}")
print(f"meeting point : {mission.meeting_point}")
print(f"time : {mission.time}")
