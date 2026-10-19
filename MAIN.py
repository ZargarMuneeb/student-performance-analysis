

import os
import pandas as pd
from functions import calculate_totals_and_averages, assign_grade, assign_result, subject_analysis

folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(folder, "students.csv")


def show_heading(text):
    print()
    print("=" * 60)
    print(text)
    print("=" * 60)


def main():
    
    if not os.path.exists(csv_path):
        print("students.csv not found, put it in the same folder as main.py")
        return

    # load the data
    df = pd.read_csv(csv_path)
    show_heading("STUDENT PERFORMANCE ANALYSIS")
    print("Total students:", len(df))
    print("Columns:", list(df.columns))
    print()
    print(df.head().to_string(index=False))

    # totals, averages, grade and result
    df = calculate_totals_and_averages(df)
    df["Grade"] = df["Average_Marks"].apply(assign_grade)
    df["Result"] = df.apply(assign_result, axis=1)

    # student wise results, best first
    show_heading("STUDENT WISE RESULTS")
    cols = ["Student_ID", "Name", "Department", "Total_Marks",
            "Average_Marks", "Grade", "Attendance", "Result"]
    ranked = df[cols].sort_values(by="Average_Marks", ascending=False)
    print(ranked.to_string(index=False))

    # class summary
    show_heading("CLASS SUMMARY")
    top = df.loc[df["Average_Marks"].idxmax()]
    low = df.loc[df["Average_Marks"].idxmin()]
    passed = (df["Result"] == "Pass").sum()
    failed = (df["Result"] == "Fail").sum()

    print("Class average:", round(df["Average_Marks"].mean(), 2))
    print("Highest:", top["Name"], "-", round(top["Average_Marks"], 2))
    print("Lowest:", low["Name"], "-", round(low["Average_Marks"], 2))
    print("Passed:", passed)
    print("Failed:", failed)
    print("Pass percentage:", round(passed / len(df) * 100, 2), "%")

    # subject wise
    show_heading("SUBJECT WISE PERFORMANCE")
    subjects = pd.DataFrame(subject_analysis(df))
    print(subjects.to_string(index=False))
    best = subjects.loc[subjects["Average_Marks"].idxmax(), "Subject"]
    print("Best subject (by class average):", best)

    # students with average 80 or more
    show_heading("TOP STUDENTS (average >= 80)")
    toppers = df[df["Average_Marks"] >= 80].sort_values(by="Average_Marks", ascending=False)
    if len(toppers) == 0:
        print("Nobody scored 80 or above.")
    else:
        print(toppers[["Student_ID", "Name", "Average_Marks", "Grade"]].to_string(index=False))

    # save results
    df.to_csv(os.path.join(folder, "student_results.csv"), index=False)
    subjects.to_csv(os.path.join(folder, "subject_analysis.csv"), index=False)
    print()
    print("Saved student_results.csv and subject_analysis.csv")


if __name__ == "__main__":
    main()