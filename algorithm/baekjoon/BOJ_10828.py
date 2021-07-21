import sys
input = sys.stdin.readline

n = int(input().strip())

arr = []
order = ''

for i in range(n):
  s = input().strip().split(' ')

  order = s[0]

  # push 명령일 경우 추려내기 위한 코드
  if len(s) == 2:
    x = int(s[1])
  
  if order == 'push':
    arr.append(x)

  elif order == 'pop':
    if len(arr) > 0:
      m = arr[len(arr)-1]
      arr.pop()
      print(m)
    else:
      print(-1)

  elif order == 'size':
    print(len(arr))

  elif order == 'empty':
    if len(arr) == 0:
      print(1)
    else:
      print(0)

  elif order == 'top':
    if len(arr) == 0:
      print(-1)
    else:
      print(arr[len(arr)-1])
