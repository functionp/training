# 制御処理




# 問題 1

num = int(input("what number do you want to look at?"))
# inputされるデータはstringであることに注意する。
def judge_odd_even(n):
    if n % 2 == 1:
        return "odd"
    else:
        return "even"

print(judge_odd_even(num))





# 問題 2

def count_even(list):
    count = 0
    for i in list:
        if judge_odd_even(i) == "even":
            count += 1
    return count


print(count_even([1, 3, 4, 2, 7, 10]))
# >>> 3

print(count_even([]))
# >>> 0



# オマケ問題（問題２を一行で書け）

# 1行にはなってませんが...短くなったので提出します

def count_even(a):
    return len(list(filter(lambda n: n % 2 == 0, a)))

print(count_even([1, 2, 3, 4, 5, 6, 7, 8]))




# 問題 3

def list_contain(name, list):
    if name in list:
        return True
    else:
        return False

print(list_contain("Tom", ["Tom", "Michael", "Tony", "Mike", "John"]))
# >>> True
