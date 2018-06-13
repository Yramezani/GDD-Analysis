def GDDcalculate(tempmin, tempmax, tbase, tupper, length):
    '''CALCULATES GDD: takes two lists ( minimum temperature and maximum temperature) and 3 numbers (Base tem.;
    Upper temp. and length of one of those lists) then replaces all temperatures lower than Tbase with Tbase and all
    temperatures higher than Tupper with Tupper. then calculates each day's GDD using formula:
    GDD=(((Minimum temperature + Maximum temperature) / 2) - Tbase'''
    import numpy as np
    GDD = [np.nan] * len(tempmax)

    for day in range(length):
        min_to_use = min(tupper, max(tempmin[day], tbase))  # If temperature was below base it will be set as base
        max_to_use = min(tupper, max(tempmax[day], tbase))  # If temperature was above upper it will be set as upper
        GDD[day] = ((min_to_use + max_to_use) / 2) - tbase
    return GDD
