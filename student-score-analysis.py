import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


students = ["Azra", "Ayşe", "Ece", "Ela", "Deniz"]

np.random.seed(42)
scores = np.random.randint(50, 101, size=5)

df = pd.DataFrame({
    "Student": students,
    "Score": scores
})

def letter_grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

df["Letter Grade"] = df["Score"].apply(letter_grade)

print("Student Scores")
print(df)

print("\nStatistics")
print("Average:", round(df["Score"].mean(), 2))
print("Highest:", df["Score"].max())
print("Lowest:", df["Score"].min())


plt.figure(figsize=(8,5))
plt.bar(df["Student"], df["Score"])
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Score")
plt.ylim(0, 100)

for i, score in enumerate(df["Score"]):
    plt.text(i, score + 1, str(score), ha="center")

plt.show()