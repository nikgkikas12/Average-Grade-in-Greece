name = input("Πώς σε λένε; ")

print("Δώσε τους βαθμούς σου για τα παρακάτω μαθήματα:")
math = float(input("Μαθηματικά: "))
physics = float(input("Φυσική: "))
literature = float(input("Λογοτεχνία: "))

average = (math + physics + literature) / 3

print(f"{name}, ο μέσος όρος των βαθμών σου είναι: {average:.2f}")

if average >= 18 and average <= 20:
    print("A")
elif average >= 16 and average <= 18:
    print("B")
elif average >= 14 and average <= 16:
    print("C")
elif average >= 10 and average <= 14:
    print("D")
elif average >= 5 and average <= 10:
    print("F")
elif average >= 0 and average <= 5:
    print("F-")
else:
    print("0-20 Μπούφο")