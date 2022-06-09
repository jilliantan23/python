# Calculating Population Change Over Time

city_name = "Istanbul, Turkey"
pop_1927 = 691000
pop_2017 = 15029231

# Calculate the annual percentage growth rate
pop_change = pop_2017 - pop_1927

# Percentage growth rate
percentage_gr = (pop_change)/pop_1927 * 100

# Annual percentage growth
annual_gr = percentage_gr / (2017 - 1927)

def population_growth(year_one, year_two, population_one, population_two):
  annual_percentage_gr = (((population_two - population_one)/population_one) * 100)/(year_two - year_one)
  growth_rate = annual_percentage_gr
  return growth_rate

print(annual_gr)

set_one = population_growth(1927, 2017, 691000, 15029231)
print("Set 1: " + str(set_one))

set_two = population_growth(1950, 2000, 983000, 8831800)
print("Set 2: " + str(set_two))

report = "The population size in Istanbul in the year 1927 was 691000, while the population size in the year 2017 was 15029231. The population growth rate from 1927 to 2017 is "

print(report + str(round(set_one, 2)))