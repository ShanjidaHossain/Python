s = int(input())
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))


def min_in_segment(start, end, prev, s, prev_min):
    if s == 1:
        return a[start]
    else:
        if prev == -1 or prev_min == -2:
            return min(a[start:end + 1])
        elif prev_min != -2:
            if prev != prev_min:
                if a[end] < prev_min:
                    return a[end]
                else:
                    return prev_min
            else:
                return min(a[start:end + 1])


msf = -1
prev = -1
prev_min = -2
for i in range(n - s + 1):
    new_min = min_in_segment(i, i + s - 1, prev, s, prev_min)
    msf = max(msf, new_min)
    prev = a[i]
    prev_min = new_min
print(msf)