# coding: utf-8
# This file was used to generate the first patients.csv version

# state in (isolated, released, deceased)
# infection_reason in (contact with patient, visit to $COUNTRY)

import pandas as pd

#==============================================================================

columns = ('sex', 'age', 'country', 'province', 'disease', 'group', 'exposure_start',
 'exposure_end', 'infection_reason', 'infection_order', 'infected_by',
 'contact_number', 'confirmed_date', 'released_date', 'deceased_date', 'state')

df = pd.DataFrame(columns=columns)

##########################################################################################
# 2 March
df = df.append({'confirmed_date': '3/2/20', 'infection_reason': 'visit to Italy', 'state': 'isolated'}, ignore_index=True)

# 5 March
df = df.append({'confirmed_date': '3/5/20', 'infection_reason': 'visit to Italy', 'state': 'isolated', 'sex': 'female', 'age': 89}, ignore_index=True)

# 10 March
df = df.append({'confirmed_date': '3/10/20', 'infection_reason': 'visit to France', 'state': 'isolated', 'province': 'Marrakech', 'sex': 'male'}, ignore_index=True)

# 11 March
df = df.append({'confirmed_date': '3/11/20', 'infection_reason': 'contact with patient', 'state': 'isolated', 'sex': 'female'}, ignore_index=True)
df = df.append({'confirmed_date': '3/11/20', 'infection_reason': 'contact with patient', 'state': 'isolated', 'sex': 'female'}, ignore_index=True)
df = df.append({'confirmed_date': '3/11/20', 'infection_reason': 'visit to France', 'state': 'isolated', 'sex': 'female', 'age': 64}, ignore_index=True)

# 13 March
df = df.append({'confirmed_date': '3/13/20', 'infection_reason': 'visit to Spain', 'state': 'isolated', 'province': 'Casablanca', 'sex': 'male'}, ignore_index=True)
df = df.append({'confirmed_date': '3/13/20', 'infection_reason': 'visit to France', 'state': 'isolated', 'province': 'Taroudant', 'sex': 'female'}, ignore_index=True)

# 14 March
# province = Tétouan, Casablanca, Rabat, Fès et Khouribga
# confirmed_date d'entree au Maroc entre le 25 février et le 12 mars 2020
df = df.append({'confirmed_date': '3/14/20', 'infection_reason': 'visit to Spain', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/14/20', 'infection_reason': 'visit to Spain', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/14/20', 'infection_reason': 'visit to Spain', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/14/20', 'infection_reason': 'visit to Spain', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/14/20', 'infection_reason': 'visit to Italy', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/14/20', 'infection_reason': 'visit to Italy', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/14/20', 'infection_reason': 'visit to Italy', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/14/20', 'infection_reason': 'visit to France', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/14/20', 'infection_reason': 'contact with patient', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/14/20', 'infection_reason': 'visit to Europe', 'state': 'isolated', 'sex': 'male'}, ignore_index=True) # M. Amara

# 15 March
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to Italy', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to Italy', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to France', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to France', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to Spain', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to Spain', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to Spain', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to Spain', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to Spain', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to Spain', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/15/20', 'infection_reason': 'visit to Austria', 'state': 'isolated'}, ignore_index=True)

# 16 March
df = df.append({'confirmed_date': '3/16/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/16/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/16/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/16/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/16/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/16/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/16/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/16/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/16/20', 'state': 'isolated'}, ignore_index=True)

# 17 March
df = df.append({'confirmed_date': '3/17/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/17/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/17/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/17/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/17/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/17/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/17/20', 'state': 'isolated'}, ignore_index=True)

# 18 March
df = df.append({'confirmed_date': '3/18/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/18/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/18/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/18/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/18/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/18/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/18/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/18/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/18/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/18/20', 'state': 'isolated'}, ignore_index=True)

# 19 March
df = df.append({'confirmed_date': '3/19/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/19/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/19/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/19/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/19/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/19/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/19/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/19/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/19/20', 'state': 'isolated'}, ignore_index=True)

# 20 March
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/20/20', 'state': 'isolated'}, ignore_index=True)

# 21 March
df = df.append({'confirmed_date': '3/21/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/21/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/21/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/21/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/21/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/21/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/21/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/21/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/21/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/21/20', 'state': 'isolated'}, ignore_index=True)

# 22 March
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/22/20', 'state': 'isolated'}, ignore_index=True)

# 23 March
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)
df = df.append({'confirmed_date': '3/23/20', 'state': 'isolated'}, ignore_index=True)

#############################################
# save into csv file

df.to_csv('patients.csv')
