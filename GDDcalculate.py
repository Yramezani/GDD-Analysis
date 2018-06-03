def GDDcalculate(tempmin, tempmax, tbase, tupper):
    GDD = [None] * len(tempmax)

    for day in range(len(tempmax)):
        min_to_use = min(tupper, max(tempmin[day], tbase))  # If temperature was below base it will set as base
        max_to_use = min(tupper, max(tempmax[day], tbase))  # If temperature was above upper it will set as upper
        GDD[day] = ((min_to_use + max_to_use) / 2) - tbase
    return GDD
