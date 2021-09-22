import sys
path = sys.argv[1]

arr = []
with open(path) as f:
  s = f.read()
  arr = s.split("======\n")

print(arr[1])
for i in range(len(arr)):
  with open('./CHAPTER-{}.md'.format(i+2), mode='w') as f:
    f.write("  \n".join(arr[i].split('\n')))
