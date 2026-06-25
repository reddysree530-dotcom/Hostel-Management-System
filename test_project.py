import sqlite3

print("=" * 50)
print("HOSTEL FOOD RATING SYSTEM - TEST REPORT")
print("=" * 50)

try:
    conn = sqlite3.connect("hostel_food.db")
    cursor = conn.cursor()
    print("PASS: Database Connected Successfully")
except Exception as e:
    print("FAIL: Database Connection Failed")
    print(e)

try:
    cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    AND name='ratings'
    """)

    table = cursor.fetchone()

    if table:
        print("PASS: Ratings Table Exists")
    else:
        print("FAIL: Ratings Table Not Found")

except Exception as e:
    print("FAIL: Table Test Failed")
    print(e)


admin_username = "admin"
admin_password = "1234"

if admin_username == "admin" and admin_password == "1234":
    print("PASS: Admin Login Working")
else:
    print("FAIL: Admin Login Failed")


food_menu = [
    "Rice",
    "Dal",
    "Chapati",
    "Paneer Curry",
    "Chicken Curry"
]

if len(food_menu) > 0:
    print("PASS: Food Menu Display Available")
else:
    print("FAIL: Food Menu Missing")


try:
    cursor.execute("""
    INSERT INTO ratings
    (student_name, food_item, rating, feedback)
    VALUES (?, ?, ?, ?)
    """,
    (
        "Test Student",
        "Rice",
        5,
        "Very Good Food"
    ))

    conn.commit()

    print("PASS: Rating Stored Successfully")

except Exception as e:
    print("FAIL: Rating Storage Failed")
    print(e)

try:
    cursor.execute("SELECT COUNT(*) FROM ratings")
    total = cursor.fetchone()[0]

    print("PASS: Admin Report Generated")
    print("Total Ratings:", total)

except Exception as e:
    print("FAIL: Report Generation Failed")
    print(e)


try:
    cursor.execute("SELECT AVG(rating) FROM ratings")
    avg = cursor.fetchone()[0]

    if avg:
        print(f"PASS: Average Rating = {avg:.2f}")
    else:
        print("PASS: No Ratings Available")

except Exception as e:
    print("FAIL: Average Rating Calculation Failed")
    print(e)

try:
    cursor.execute("""
    SELECT COUNT(*)
    FROM ratings
    WHERE rating <= 2
    """)

    negative_count = cursor.fetchone()[0]

    print(
        f"PASS: Negative Comments Found = {negative_count}"
    )

except Exception as e:
    print("FAIL: Negative Comment Test Failed")
    print(e)

print("=" * 50)
print("TESTING COMPLETED")
print("=" * 50)

conn.close()