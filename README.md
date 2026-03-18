# smart-transaction-risk-detector

SRM University AP
Department of Computer Science and Engineering
Course Code CSE205
Subject Hands on Python
Challenge Code2Xplore 60 Days Challenge
Day 6
Concerned Faculty Dr Yasir Afaq

---Project Description---

This project is developed as part of the Code2Xplore 60 Days Challenge.
The program analyzes financial transactions made by a user in a day and detects suspicious spending patterns.
The system checks invalid values, categorizes valid transactions into different levels, and applies personalized risk detection logic to generate a final financial risk report.

---Problem Statement---

The program accepts a list of integer values representing transaction amounts.
Each transaction is classified using conditional statements and processed using a for loop.
The program must
Accept transaction amounts
Classify each transaction
Store categorized transactions
Apply personalized risk logic
Generate a final financial risk report

---Base Classification Rules---

If transaction ≤ 0 → Invalid Transaction
If transaction between 1 and 500 → Normal
If transaction between 501 and 2000 → Large
If transaction greater than 2000 → High Risk

---Personalization Logic---

The program checks three conditions

Frequent Transactions → more than 5 valid transactions
Large Spending → total transaction value greater than 5000
Suspicious Pattern → three or more high risk transactions

If all three conditions are true → High Risk
If suspicious transactions or large spending occurs → Moderate Risk
Otherwise → Low Risk

This logic makes the system stricter and reduces false alerts.

---Program Output---

The program displays

Categorized transactions
Valid transactions list
Total transaction value
Number of valid transactions
Transaction summary tuple
Final risk classification
 
---Constraints Followed---

Used list
Used for loop
Used conditional statements
Used dictionary for classification
Used list comprehension
Used tuple for summary
Did not use sorting
Did not hard code output
