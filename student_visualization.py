import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("student_performance.csv")

# Set style
sns.set(style="whitegrid")

# 1. Bar Chart: Average Marks by Subject
avg_subject = data.groupby("Subject")["Marks"].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(
    data=avg_subject,
    x="Subject",
    y="Marks"
)
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# 2. Line Chart: Semester-wise Performance
avg_semester = data.groupby("Semester")["Marks"].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.lineplot(
    data=avg_semester,
    x="Semester",
    y="Marks",
    marker="o"
)
plt.title("Semester-wise Average Performance")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()

# 3. Box Plot: Marks Distribution by Subject
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=data,
    x="Subject",
    y="Marks"
)
plt.title("Marks Distribution by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()
