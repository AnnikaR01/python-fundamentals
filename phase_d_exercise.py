def trend(current, previous):
    if current > previous:
        return "increased"
    elif current < previous:
        return "decreased"
    else:
        return "equaled"
years = [2018, 2019, 2022]
diagnoses = [37377, 36337, 37981]
for i in range(1, len(diagnoses)):
    label = trend(diagnoses[i], diagnoses[i-1])
    print(f"{years[i]}: {label} compared to {years[i-1]}")