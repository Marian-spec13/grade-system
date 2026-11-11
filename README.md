# STUDENT GRADE MANAGEMENT SYSTEM

**Project:** Student Grade Management System  
**Developer:** Marian Jemal  
**Programming Language:** Python  
**Start Date:** Thursday, 22 October 2026  
**End Date:** Thursday, 29 October 2026  
**Code Repository:** [GitHub - Student Grade System](https://github.com/Marian-spec13/grade-system)

---

## PROJECT LOG

**Work Schedule:** Multi-day development process incorporating time, defect, and job tracking.

### 1. JOBS IDENTIFICATION
Before writing the program, I divided the work into five jobs. This gave me a clear order to follow and helped me estimate the effort needed for each part.

| Job No. | Job Name | Description |
| :---: | :--- | :--- |
| **1** | Requirements Analysis | Identify what the program needs to do, including inputs, outputs, boundary rules, and validation criteria. |
| **2** | Design | Plan the program structure, menu options, calculation formulas, and CLI layout. |
| **3** | Implementation | Write the Student Grade Management System in Python (`student_grades.py`). |
| **4** | Testing | Run test suites with edge cases, invalid inputs, and environment configurations. |
| **5** | Documentation | Prepare the time logs, defect tracking logs, and final assignment report. |

---

### 2. TIME AND WORK-PRODUCT ESTIMATES
These were the estimates made before the work began. They represent initial planning figures for comparison against actual time spent.

| Job No. | Job Name | Estimated Time (min) | Expected Work Product |
| :---: | :--- | :---: | :--- |
| **1** | Requirements Analysis | 30 | 1 Requirements Outline Document |
| **2** | Design | 45 | 1 System Design Blueprint |
| **3** | Implementation | 45 | 40–50 Lines of Python Code |
| **4** | Testing | 30 | Execution of Test Cases & Input Checks |
| **5** | Documentation | 15 | 2 Process Logs (Time & Defect Logs) |
| | **TOTAL** | **165** | |

---

### 3. DAILY TIME LOG
The time log records activities across the development sessions. Realistic breaks and interruptions (including an overnight pause during environment setup) are captured separately.

| Job # | Job / Task Description | Date | Start Time | End Time | Plan Time (min) | Actual Time (min) | Interruption (min) | Notes / Activity |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | Requirements Analysis | 2026-10-22 | 14:00 | 14:35 | 30 | 35 | 5 | Identified project brief, input requirements (0-100 marks), and grade criteria. *Interruption: Quick text message check.* |
| **2** | Design | 2026-10-22 | 14:30 | 15:20 | 45 | 50 | 5 | Designed script logic structure, calculations, and CLI output format. *Interruption: Water break.* |
| **3** | Implementation | 2026-10-25 | 10:00 | 11:15 | 45 | 75 | 15 | Wrote Python script (`student_grades.py`) for input loops and calculations. *Interruption: Looked up float division syntax & answered phone call.* |
| **4** | Testing | 2026-10-28 | 23:00 | 07:30 | 30 | 510 | 450 | Resolved PowerShell PATH issue and executed test run for Asha (Marks: 75, 92, 81). *Interruption: 7.5-hour overnight sleep break before completing setup.* |
| **5** | Documentation | 2026-10-29 | 08:00 | 08:35 | 15 | 35 | 10 | Created and finalized project logs and documentation. *Interruption: Email notification distraction.* |

#### Summary & Totals
- **Total Planned Time:** 165 minutes (~2.75 hours)
- **Total Actual Duration:** 705 minutes (~11.75 hours including overnight break)
- **Total Interruption Time:** 485 minutes (~8.1 hours)
- **Net Working Time:** 220 minutes (~3.6 hours)

---

### 4. JOB NUMBER LOG: PLANNED VS. ACTUAL
After completing the work, original planning figures were evaluated against recorded time and actual work products.

| Job | Job Name | Planned (min) | Actual (min) | Planned Work Product | Recorded Work Product |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | Requirements Analysis | 30 | 35 | 1 Document | 1 Document (9 Requirements) |
| **2** | Design | 45 | 50 | 1 Document | 1 Document (Flow & Functions) |
| **3** | Implementation | 45 | 75 | 40 LOC | 50 LOC (`student_grades.py`) |
| **4** | Testing | 30 | 510 | Test Cases | Test Suite & PATH Fixes |
| **5** | Documentation | 15 | 35 | 2 Logs | 3 Process Logs & Report |
| | **TOTAL** | **165** | **705** | | |

#### 4.1 Cumulative (To Date) Summary
Cumulative totals reflect cumulative actual time vs. planned targets.

| Job Completed | Cumulative Planned (min) | Cumulative Actual (min) | Difference (min) | Note |
| :---: | :---: | :---: | :---: | :--- |
| **Job 1** | 30 | 35 | +5 | Requirements review took slightly longer to verify grade bounds. |
| **Job 2** | 75 | 85 | +10 | Detailed flow design added 10 minutes. |
| **Job 3** | 120 | 160 | +40 | Implementation included additional input validation loops. |
| **Job 4** | 150 | 670 | +520 | Testing phase spanned overnight due to environment/PATH resolution. |
| **Job 5** | 165 | 705 | +540 | Finalizing detailed process logs required extra time. |

---

### 5. DEFECT LOG
The following defects were recorded, tracked, and resolved during system development:

| Defect # | Date | Phase Injected | Phase Removed | Fix Time (min) | Description & Root Cause | Solution / Resolution |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **1** | 2026-10-22 | Requirements | Design | 15 | Misinterpreted boundary rules: assumed passing grade started at 50 instead of 40 based on specification. | Updated design logic table and grade scale boundaries (A: >=70, B: 60-69, C: 50-59, D: 40-49, F: <40). |
| **2** | 2026-10-25 | Implementation | Implementation | 10 | `TypeError` in average calculation: marks were collected as strings from `input()` without float conversion. | Wrapped user input in `float()` casting during collection loop in `student_grades.py`. |
| **3** | 2026-10-25 | Implementation | Implementation | 10 | Unhandled exception: program crashed with `ValueError` when non-numeric text was entered. | Added `try-except ValueError` block inside a `while` loop to re-prompt until valid mark is entered. |
| **4** | 2026-10-28 | Environment Setup | Testing | 45 | PowerShell threw `CommandNotFoundException` for `python` command due to missing PATH settings. | Configured Python installer PATH setting, disabled Windows App Execution Aliases, and restarted environment. |
| **5** | 2026-10-29 | Testing | Testing | 5 | Input validation check: verified program calculates correct averages for non-integer marks. | Verified calculation logic via test run for Asha (Marks: 75, 92, 81 -> Avg: 82.67, Grade: B). |
| **6** | 2026-10-29 | Testing | Testing | 10 | Output formatting issue: average display showed raw unformatted floats (e.g., `82.66666666666667`). | Formatted average string using `:.2f` precision (e.g., `82.67`) in final CLI output. |

---

### 6. WHAT I LEARNED (REFLECTION)
* **Environment Configuration Matters:** Environment bugs (such as system PATH configuration) can impact overall project schedules if not accounted for during initial setup.
* **Defect Log Discipline:** Tracking defects across phases highlighted the value of early input validation checks, preventing runtime crashes during formal testing.
* **Plan vs. Actual Variance:** Breaking down work into small, distinct job phases provided clear insight into where actual effort deviated from planned estimates.

---

### 7. REQUIREMENTS LIST
The system fulfills the following functional requirements:
1. The program accepts student identity details and rejects empty inputs.
2. The program collects subject counts as positive integers.
3. Subject marks are accepted as floating-point numbers between 0 and 100.
4. Input validation handles non-numeric inputs gracefully without terminating execution.
5. Average marks are calculated accurately across all submitted subjects.
6. Grades are assigned based on standard evaluation scale (A, B, C, D, F).
7. Summary outputs format floating-point values to 2 decimal places.

---

### 8. DESIGN NOTES & FUNCTION LIST

#### Program Flow
* **Step 1:** Program initiation & welcome header.
* **Step 2:** Prompt for student details and subject quantity.
* **Step 3:** Loop through subjects with robust `try-except` error handling for mark entry (0–100).
* **Step 4:** Calculate total marks, calculate average percentage, and determine letter grade.
* **Step 5:** Output formatted student summary card.

#### Function Summary
| Function / Module | Purpose |
| :--- | :--- |
| `main()` | Controls execution flow and input collection loops. |
| `get_valid_mark()` | Validates user numeric inputs between 0 and 100. |
| `calculate_average()` | Evaluates total mark sum against total subject count. |
| `determine_grade()` | Maps calculated average percentage to letter grade scale. |