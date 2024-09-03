#  calculate monthly emi


# emi=loan_amount*intrest_rate(1+intrest_rate)**tenure/((1+intrest_rate)**tenure-1)


loan_amount=1000000
tenure=12
interest_rate=9

print(f"loan_amount={loan_amount}")
print(f"tenure={tenure}")
print(f"interest_rate={interest_rate}")

intrestpermnth=interest_rate/(12*100)

tenure_in_month=tenure*12
print(tenure_in_month)

emi=loan_amount*intrestpermnth*(1+intrestpermnth)**tenure_in_month/((1+intrestpermnth)**tenure_in_month-1)

print(f"monthly emi={emi}")


total_amount_payable=emi*tenure_in_month
print(f"total payment={total_amount_payable}")

total_interest=total_amount_payable-loan_amount
print(f"total_intrest={total_interest}")
