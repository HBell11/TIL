# link: https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline

n = int(input().strip())
s = []

# 수열 입력받기
for _ in range(n):
  s.append(int(input().strip()))

def numeric():
  ans = []
  prt = []
  k = 1
  
  # i는 수열 s의 인덱스 역할
  for i in range(n):
    
    # 스택 끝 숫자보다 수열의 수가 작으면 NO 반환
    # s[i] in ans[:-1] 일 경우 값은 동일하나 시간초과 오류
    if ans != [] and s[i] < ans[-1]:
      return 'NO'

    else:
      
      # 순차적인 숫자를 k로 활용
      while True:
        
        # pop 하는 경우
        if ans != [] and s[i] == ans[-1]:
          ans.pop()
          prt.append('-')
          break

        # push 하는 경우 (값을 스택에 추가했으므로 k값을 증가)
        else:
          ans.append(k)
          prt.append('+')
          k = k + 1

  return '\n'.join(prt)

print(numeric())
