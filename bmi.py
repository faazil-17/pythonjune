#write a program to calculate bm1

#bmi=(weight_in_kg/height_in_meter square)

weight_in_kg=72

height_in_cm=165

height_in_meter=height_in_cm/100

print(f"height in meter={height_in_meter}")

height_in_metersquare=height_in_meter**2

print(f"height in metersquare={height_in_metersquare}")


bmi=weight_in_kg/height_in_metersquare

print(f"bmi={bmi}")