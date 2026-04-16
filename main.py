import random

ans = []
X = ["when","where","who","how","do"]

def add(N):
  f = open(N + 'list.txt', 'a')
  f.write(input() + " ")
  f.close()

def generate():
  for S in X:
    words = open(S + 'list.txt', 'r')
    A = words.read().split()
    ans.append(random.choice(A))
    words.close()

while True:
  N = str(input())

  if (N == "when") or (N == "who") or (N == "where") or (N == "how") or (N == "do"):
    add(N)

## ここから下がランダム生成コード
  elif (N == "generate"):
    ans = []
    generate()
    print(str(ans).replace(" ","").replace("'","").replace("[","").replace("]",""))

## ここまで
  elif (N == "exit"):
    break

  else:
    print("It is unsupport word")
