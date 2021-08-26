# https://www.acmicpc.net/problem/13300
# Unsolved

N, K = map(int, input().split())
students = [[0 for _ in range(2)] for _ in range(6)]

for _ in range(N):
    S, Y = map(int, input().split())
    students[S][Y] += 1

print(students)


# room = 0
# for sex_group in students:
#     grade = sex_group[0]
#     n = 0
#     for student_grade in sex_group:
#         if grade != student_grade:
#             room += 1
#             n = 1

#         else:
#             n += 1

#             if n > K:
#                 room += 1
#                 n = 1

# print(room)


# room = 0
# for sex_group in students:
#     room += 1
#     grade = sex_group[0]
#     cnt = 0

#     for student_grade in sex_group:

#         if grade != student_grade:
#             room += 1
#             grade = student_grade
#             cnt = 1

#         else:
#             if cnt < K:
#                 cnt += 1

#             else:
#                 room += 1
#                 cnt = 1
#         # print(grade)
# print(room)
