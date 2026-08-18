regions_hiv_millions = {
    "Eastern and southern Africa": 21.1,
    "Asia and the Pacific": 6.9,
    "Western and central Africa": 5.2,
    "Latin America": 2.5,
    "Western and Central Europe and North America": 2.4,
}
total = 0
for region, millions in regions_hiv_millions.items():
    print(f"{region}: {millions} million people living with HIV (2024)")
    total = total + millions
print(f"Combined total across these regions: {total} million")