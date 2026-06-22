import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic student dataset
student_id=np.arange(1,21)
gender=np.random.choice(['Female','Male'],20)
std=np.random.choice(['10th'],20)

# Generate marks for 5 subjects (range: 30–100)
math=np.random.randint(30,100,20)
english=np.random.randint(30,100,20)
science=np.random.randint(30,100,20)
sst=np.random.randint(30,100,20)
computer=np.random.randint(30,100,20)

# Generate attendance (%) and previous performance
attendance=np.random.randint(20,100,20)
previous_per=np.random.randint(30,100,20)

# Create DataFrame
df=pd.DataFrame(
    {
        'StudentID': student_id,
        'Gender': gender,
        'STD':std,
        'Math_marks':math,
        'Eng_marks':english,
        'Sci_marks':science,
        'Sst_marks':sst,
        'Comp_marks':computer,
        'Attendance':attendance,
        'Previous_per':previous_per       
    }
)

# Display dataset
df

# Basic information about dataset (data types, nulls)
df.info()

# Statistical summary (mean, min, max, etc.)
df.describe()

# Count of students by gender
df['Gender'].value_counts()

# Visualize gender distribution
sns.countplot(x=df['Gender'])
plt.title("Gender Distribution")
plt.show()

# Check missing values
df.isnull().sum()

# Check duplicate records
df.duplicated().sum()

# Calculate total marks (sum of all subjects)
df['Total']= df['Math_marks'] + df['Eng_marks'] + df['Sci_marks'] + df['Sst_marks'] + df['Comp_marks']
df

# Bar chart of total marks per student
plt.bar(df['StudentID'],df['Total'],color='orange',edgecolor='black')
plt.xlabel("Student ID")
plt.ylabel("Total Marks")
plt.title("Total marks of Students")
plt.show()

# Calculate percentage
df['Percentage']=df['Total']/500*100
df

# Histogram of percentage distribution
plt.hist(df['Percentage'], bins=5,color='skyblue')
plt.xlabel("Percentage")
plt.ylabel("Frequency")
plt.title("Distribution of Student Percentage")
plt.show()

# Filter students from 9th (will be empty here)
df[(df['STD'])=='9th']

# Filter students from 10th
df[(df['STD'])=='10th']

# Attendance visualization using seaborn
sns.barplot(
    x=df['StudentID'],
    y=df['Attendance'],
    palette='viridis'
)

# Students scoring more than 90 in Science
df[(df['Sci_marks'])>90]

# Plot count of students with Science marks > 90
sns.countplot(x='StudentID', data=df[df['Sci_marks'] > 90], color="violet")
plt.title("Student IDs with Science Marks > 90")
plt.show()

# Students with percentage between 60 and 90
df[(df['Percentage']>60) & (df['Percentage']<90)]

# Filter students with good percentage and attendance
df_filtered=df[(df['Percentage']>60) & (df['Attendance']>60)]
df_filtered

# Scatter plot: Attendance vs Percentage
sns.scatterplot(data=df_filtered,x='Attendance',y='Percentage',hue='STD')
plt.title("Students with Percentage >60 and Attendance >60")
plt.xlabel("Attendance")
plt.ylabel("Percentage")
plt.show()

# Assign result (ATKT, Fail, Pass)
df['Status']=np.where((df[['Math_marks','Eng_marks','Sci_marks','Sst_marks','Comp_marks']] < 35).any(axis=1),"ATKT",np.where(df['Percentage']<35,"Fail","Pass"))
df

# Rename column
df=df.rename(columns={'Status':'Result'})
df

# Pie chart of result distribution
result_counts = df['Result'].value_counts()
plt.pie(result_counts,labels=result_counts.index,autopct='%1.1f%%')
plt.title("Student Result Status Distribution")
plt.show()

# Sort students by percentage (descending)
df = df.sort_values(by='Percentage', ascending=False)
df

# Assign rank (only for passing students)
df['Rank'] = df[df['Result']=="Pass"]['Percentage'].rank(ascending=False, method='dense')

# Convert rank to integer type
df['Rank'] = df['Rank'].astype('Int64') 
df['Rank'] = df['Rank'].astype(str) + df['Rank'].map({1:'st Rank',2:'nd Rank',3:'rd Rank'})
df

# Fill missing ranks (failed students)
df['Rank']=df['Rank'].fillna('--')
df

# Extract top 3 ranked students
top3 = df[df['Rank'].isin(['1st Rank','2nd Rank','3rd Rank'])]
top3

# Bar plot for top 3 students
sns.barplot(data=top3,x='Rank',y='Percentage',palette='viridis',edgecolor='black')
plt.title("Top 3 Student Ranks")
plt.xlabel("Ranks")
plt.ylabel("Percentage")
plt.show()

# Assign grades based on percentage
df['Grade']=np.where(
    df['Result']=="ATKT","F",
    np.where(
        df['Percentage']>=80,"A",
        np.where(
            (df['Percentage']<80) & (df['Percentage']>=70),"B",
            np.where(
                (df['Percentage']<70) & (df['Percentage']>=50),"C",
                np.where(
                    (df['Percentage']<50) & (df['Percentage']>=35),"D","F"
                )
            )
        )
    )
)
df

# Plot grade distribution
sns.countplot(data=df, x='Grade', order=['A','B','C','D','F'] ,palette='rainbow')
plt.title("Student Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.show()

# Filter female students
df[(df['Gender'])=='Female'] 

# Female students who passed
df[(df['Gender']=="Female") & (df['Result']=="Pass")]

