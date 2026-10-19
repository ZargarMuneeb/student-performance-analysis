

import numpy as np


subjects = ["Python", "DBMS", "Networking", "AI"]


def calculate_totals_and_averages(df):
    
    marks = df[subjects].to_numpy(dtype=float)

   
    df["Total_Marks"] = np.sum(marks, axis=1)
    df["Average_Marks"] = np.round(np.mean(marks, axis=1), 2)
    return df


def assign_grade(avg):
    # 90+ A+, 80+ A, 70+ B, 60+ C, 50+ D, below 50 F
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def assign_result(row):

    for sub in subjects:
        if row[sub] < 40:
            return "Fail"

    if row["Attendance"] < 40:
        return "Fail"

    return "Pass"


def subject_analysis(df):
    result = []

    for sub in subjects:
        info = {
            "Subject": sub,
            "Average_Marks": round(float(np.mean(df[sub].to_numpy())), 2),
            "Highest_Mark": int(df[sub].max()),
            "Lowest_Mark": int(df[sub].min()),
        }
        result.append(info)

    return result