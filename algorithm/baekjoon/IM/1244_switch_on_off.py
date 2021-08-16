# https://www.acmicpc.net/problem/1244

# 스위치를 바꾸는 함수
# switch 0 -> 1, 1 -> 0
def turn_switch(lst, idx):
    lst[idx] = (lst[idx] + 1) % 2
    return lst


switch_num = int(input())
switch_status = list(map(int, input().split()))
students_num = int(input())

while students_num > 0:
    student = list(map(int, input().split()))

    student_sex = student[0]  # 성별 변수
    student_num = student[1]  # 받은 숫자

    if student_sex == 1:  # 남자면

        for i in range(switch_num):

            if not (i + 1) % student_num:  # i로 나누어 떨어지면
                turn_switch(switch_status, i)
                # switch_status[i] = (switch_status[i] + 1) % 2  # 0은 1로 1은 0으로

    elif student_sex == 2:  # 여자면

        turn_switch(switch_status, student_num - 1)  # 해당 번호 스위치를 바꿈

        # 해당 번호 양 옆을 비교 (왼쪽과 오른쪽 중 최솟값까지 범위 지정)
        for j in range(1, min(student_num - 1, switch_num - student_num) + 1):
            if switch_status[student_num - 1 - j] == switch_status[student_num - 1 + j]:  # 양 옆이 같으면
                turn_switch(switch_status, student_num - 1 - j)
                turn_switch(switch_status, student_num - 1 + j)
            else:
                break

    students_num -= 1


# 20개 씩 출력하기 위함
quotient = switch_num // 20

temp_idx = 0
while temp_idx < quotient:

    switch_for_print = switch_status[temp_idx * 20 : temp_idx * 20 + 20]
    print(" ".join(map(str, switch_for_print)))

    temp_idx += 1

if temp_idx == quotient:
    switch_for_print = switch_status[temp_idx * 20 :]
    print(" ".join(map(str, switch_for_print)))
