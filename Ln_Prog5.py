total_gallons = 0
total_miles = 0

while True:
    gallons = float(input("Enter gallons used (-1 to quit): "))

    if gallons == -1:
        break
    else:
        miles = float(input("Enter miles driven: "))
        mpg = miles/gallons

        print("MPG: {:0.2f}\n".format(mpg))

        total_gallons = gallons + total_gallons
        total_miles = miles + total_miles

averagempg = total_miles/total_gallons
print("average MPG:", round(averagempg, 2))
