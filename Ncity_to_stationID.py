
# coding: utf-8

# In[ ]:


def Ncity_to_stationID(Namecity, year):

    stations1 = {'St. John\'s': 50089, 

                'Yellowknife': 51058,

                'Charlottetown': 50621, 

                'Halifax': 50620,

                'Fredericton': 48568, 

                'Ottawa': 49568,

                'Winnepeg': 51097,

                'Regina': 28011,

                'Edmonton': 50149,

                'Victoria': 51337,
                  'Toronto':51459,

                'Quebec City': 26892,

                'Whitehorse': 50842,

                'Montreal':51157,

                'Iqaluit': 42503}

    stations2 = {'St. John\'s': 6720,
                'Toronto':5097,

                'Yellowknife': 1706,

                'Charlottetown': 6526, 

                'Halifax': 6358,

                'Fredericton': 6157, 

                'Ottawa': 49568,

                'Winnepeg': 51097,

                'Regina': 3002,

                'Edmonton': 1865,

                'Victoria': 118,

                'Quebec City': 26892,

                'Whitehorse': 1617,

                'Montreal':51157,

                'Iqaluit': 1758}

    if year >= 2012 :
        return stations1[Namecity]
    else:
        return stations2[Namecity]

