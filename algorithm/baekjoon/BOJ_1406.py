# link:https://www.acmicpc.net/problem/1406
import sys
input = sys.stdin.readline

# 스택 두가지를 이용해 구현
s1 = list(input().strip())
s2 = []

n = int(input().strip())

for _ in range(n):
  t = input().split()

  if t[0] == 'L':
    if s1: s2.append(s1.pop())
    else: continue
  elif t[0] == 'D':
    if s2: s1.append(s2.pop())
    else: continue
  elif t[0] == 'B':
    if s1: s1.pop()
    else: continue
  elif t[0] == 'P':
    s1.append(t[1])
  
s = ''.join(s1 + list(reversed(s2)))

print(s)

# index로 코드를짜면 실행은 잘 되지만 시간초과 문제가 생김.
# idx = len(s1)

# for _ in range(n):
#   t = input().split()

#   if t[0] == 'L':
#     if not idx == 0:
#       idx -= 1
#     continue
   
#   elif t[0] == 'D':
#     if not idx == len(s1):
    
#       idx += 1
#     continue

#   elif t[0] == 'B':
#     if not idx == 0:
#       s1 = s1[:idx-1] + s1[idx:]
    
#       idx -= 1
#     continue

#   elif t[0] == 'P': 
#     s1 = s1[:idx] + t[1] + s1[idx:]
  
#     idx += 1
#     continue
