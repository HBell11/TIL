import sys
input = sys.stdin.readline

n = int(input().strip())

# n만큼 실행
for k in range(n):

  # 문자열 입력받기
  s = input().split()
  new_s = []

  # 문자열의 단어 수 만큼 반복문 실행
  for i in range(len(s)):
    t = list(s[i])
    u,v = [], []
    
    # 각 단어별 글자 수 만큼 반복문 실행
    for j in range(len(s[i])):
      
      # 역순으로 대입
      u.append(t[len(t)-1-j])
    
    # 대입한 글자 리스트를 단어로 변환하여 추가
    v.append(''.join(u))
    new_s.append(v[0])
  
  # 변환한 리스트를 문자형으로 출력
  print(' '.join(new_s))
