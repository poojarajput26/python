# [1] E-commerce Website: Order Discount System

def apply_discount(user_type, total_amount):
    if user_type == "VIP":
        discount = 0.20  # 20% discount
    elif user_type == "Regular":
        discount = 0.10  # 10% discount
    elif user_type == "New":
        discount = 0.05  # 5% discount
    else:
        discount = 0  # No discount

    final_amount = total_amount - (total_amount * discount)
    return final_amount

# Example usage
print(apply_discount("VIP", 1000))  # Output: 800.0




# [2] Healthcare System: Patient Risk Assessment

def assess_patient_risk(temperature, oxygen_level, age):
    if temperature > 102 and oxygen_level < 90:
        return "High Risk - Immediate Attention Needed"
    elif temperature > 100 and oxygen_level < 95:
        return "Moderate Risk - Doctor Consultation Required"
    elif temperature <= 100 and oxygen_level >= 95:
        return "Low Risk - Home Care Sufficient"
    else:
        return "Normal Condition"

# Example usage
print(assess_patient_risk(101, 93, 45))  # Output: Moderate Risk - Doctor Consultation Required



# [3] Banking System: Loan Eligibility Check :

def check_loan_eligibility(credit_score, income):
    if credit_score >= 750 and income > 50000:
        return "Eligible for premium loan"
    elif credit_score >= 650 and income > 30000:
        return "Eligible for standard loan"
    elif credit_score >= 550 and income > 20000:
        return "Eligible for basic loan"
    else:
        return "Not eligible for a loan"

# Example usage
print(check_loan_eligibility(700, 40000))  # Output: Eligible for standard loan
