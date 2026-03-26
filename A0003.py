# INPUT.TXT dan ma'lumotlarni o'qish
# Foydalanuvchi konsoldan kiritishi mumkin
# Agar fayldan o'qish kerak bo'lsa, tegishli funksiyalardan foydalanish lozim
try:
    numbers = list(map(int, input().split()))
    if len(numbers) != 5:
        print("Iltimos, beshta butun son kiriting.")
    else:
        numbers.sort()
        min_sum = sum(numbers[:4])
        max_sum = sum(numbers[1:])
        # OUTPUT.TXT ga ma'lumotlarni chop etish
        print(min_sum, max_sum)
except ValueError:
    print("Faqat butun sonlarni kiriting.")