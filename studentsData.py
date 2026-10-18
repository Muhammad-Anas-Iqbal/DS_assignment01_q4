
import pandas as pd

data = {
    "Name": ["Muhammad Anas Iqbal", "Ali", "Ahmed", "Sara", "Ayesha", "Usman"],
    "Section": ["A", "A", "B", "B", "A", "B"],
    "City": ["Rawalpindi", "Lahore", "Karachi", "Islamabad", "Lahore", "Peshawar"],
    "Marks": [85, 65, 72, 90, 55, 78]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# (i) Students with marks greater than 70
print("\n(i)Students with marks greater than 70:")
print(df[df["Marks"] > 70])

# (ii) Average marks of each section
print("\n(ii)Average marks of each section:")
print(df.groupby("Section")["Marks"].mean())

# (iii) Add Grade column
df["Grade"] = "C"

df.loc[df["Marks"] >= 60, "Grade"] = "B"
df.loc[df["Marks"] >= 80, "Grade"] = "A"

print("\n(iii)DataFrame with Grade:")
print(df)

# (iv) Sort by marks in descending order
print("\n(iv)DataFrame sorted by marks:")
print(df.sort_values("Marks", ascending=False))
