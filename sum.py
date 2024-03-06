# N/6 takes longer than an hour... stopped the proccess and demonstrated for a smaller number:
# stoppingCondition = 1.098e27/6
stoppingCondition = 100000000
tot=0
x = 0
while x <= stoppingCondition:
    x+=1
    tot += x**2
print(tot)
# outputs: 333333348333333550000001
print((stoppingCondition*(stoppingCondition + 1))/2)
# outputs: 5000000050000000

# Using Maple software to do this faster for the full number of electrons gives 
# 1.7*10^52 for the first sum, and 2*10^29 for the second formula for the sum of x. Shown in "Maple.png"
