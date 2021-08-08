# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
eng_nums = set([int(i) for i in input().split()])
fr = int(input())
fr_nums = set([int(j) for j in input().split()])

print(len(eng_nums.union(fr_nums)))
