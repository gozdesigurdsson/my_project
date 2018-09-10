years_str = input("Years: ") # do not change this line
years_int = int(years_str)

#birth_min = float(60 // 7)
#birth_hour = float(birth_min * 60)
#birth_day = float(birth_hour * 24)
#birth_year = float(birth_day * 365)

#death_min = float(60 // 13)
#death_hour = float(death_min * 60)
#death_day = float(death_hour * 60)
#death_year = float(death_day * 365)

#Immigrates_min = float(60 // 35)
#Immigrates_hour = float(Immigrates_min * 60)
#Immigrates_day = float(Immigrates_hour * 24)
#Immigrates_year = float(Immigrates_day * 365)

#Population = float(307357870)

birth = 31536000 // 7
death = 31536000 // 13
immigration = 31536000 // 35
population = 307357870

new_population = population + (years_int * (birth + immigration - death))


#new_population = Population + (float(years_int) * (Immigrates_year + birth_year - death_year))

print("New population after", years_int, " years is ", int(new_population)) # do not change this line

