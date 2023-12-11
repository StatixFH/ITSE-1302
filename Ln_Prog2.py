
# amount of miles and gas input
miles_driven = 0
gas_gallons_used = 0
mpg = 0

miles_driven = float(input('Enter number of miles driven: '))
gas_gallons_used = float(input('Enter gallons of gas used: '))


#  miles driven being calculated against amount of gas used
mpg = miles_driven / gas_gallons_used

# miles driven and amount of gas calculation printed (miles per gallon)
print('Miles per gallon =', round(mpg, 2))
