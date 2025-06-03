# 사람 정보를 담는 클래스
class Person:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

# 입력 받기
n = int(input())
people = []

# n명의 사람 정보를 입력받아서 Person 객체로 리스트에 저장
for _ in range(n):
    name, street_address, region = input().split()
    person = Person(name, street_address, region)
    people.append(person)

# 이름이 가장 느린 사람 찾기 (사전순으로 제일 뒤)
slowest_person = max(people, key=lambda p: p.name)

# 문제에서 요구한 출력 형식으로 출력
print(f"name {slowest_person.name}")
print(f"addr {slowest_person.street_address}")
print(f"city {slowest_person.region}")
