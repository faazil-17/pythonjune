employee={"name":"hari",
          "dept":"r&d",
          "salary":50000,
          "combo_offer":1000,
          "extra_working_days":3
          }


for k,v in employee.items():

    print(k,v)


if "extra_working_days" in employee:


    net_pay=employee.get("salary")+employee.get("combo_offer")*employee.get("extra_working_days")


    print(net_pay)

else:

    net_pay=employee.get("salary")

    print(net_pay)