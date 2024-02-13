print(*sorted([x for i, x in enumerate(map(int, input().split())) if (i + 1) % 6 == 0 and x % 6 == 0]))
