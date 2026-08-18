years = [2018, 2019, 2022]
diagnoses = [37377, 36337, 37981]
for i in range(1, len(diagnoses)):
    current = diagnoses[i]
    previous = diagnoses[i-1]
    if current > previous:
        trend = "increased"
    elif current < previous:
        trend = "decreased"
    else:
        trend = "equaled"
    print(f"{years[i]}: {trend} compared to {years[i-1]}")