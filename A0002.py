import sys

def solve():
    # INPUT.TXT dan o'qish (yoki standart kirish)
    try:
        line = sys.stdin.read().strip()
        if not line:
            return
        year = int(line)
    except EOFError:
        return

    # Kabisa yili sharti:
    # 400 ga bo'linsa YOKI (4 ga bo'linib 100 ga bo'linmasa)
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    if is_leap:
        # Kabisa yilida 256-kun: 12-sentabr
        # :04d yilni 4 xonali qilib (oldiga nol qo'yib) chiqaradi
        print(f"12/09/{year:04d}")
    else:
        # Oddiy yilda 256-kun: 13-sentabr
        print(f"13/09/{year:04d}")

if __name__ == "__main__":
    solve()