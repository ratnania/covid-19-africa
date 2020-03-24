# coding: utf-8
# This file was used to generate the first patients.csv version

import os
import pandas as pd

#==============================================================================
def mkdir_p(folder):
    if os.path.isdir(folder):
        return
    os.makedirs(folder, exist_ok=True)

#==============================================================================

columns = ['Region', 'Date', 'Local', 'Origin', 'Status', 'Age', 'Gender']

df = pd.DataFrame(columns=columns)

##########################################################################################
# 2 March
df = df.append({'Date': '3/2/20', 'Local': False, 'Origin': 'Italy', 'Status': 'Confirmed'}, ignore_index=True)

# 5 March
df = df.append({'Date': '3/5/20', 'Local': False, 'Origin': 'Italy', 'Status': 'Confirmed', 'Gender': 'F', 'Age': 89}, ignore_index=True)

# 10 March
df = df.append({'Date': '3/10/20', 'Local': False, 'Origin': 'France', 'Status': 'Confirmed', 'Region': 'Marrakech', 'Gender': 'M'}, ignore_index=True)

# 11 March
df = df.append({'Date': '3/11/20', 'Local': False, 'Origin': 'France', 'Status': 'Confirmed', 'Gender': 'F'}, ignore_index=True)
df = df.append({'Date': '3/11/20', 'Local': False, 'Origin': 'France', 'Status': 'Confirmed', 'Gender': 'F'}, ignore_index=True)
df = df.append({'Date': '3/11/20', 'Local': False, 'Origin': 'France', 'Status': 'Confirmed', 'Gender': 'F', 'Age': 64}, ignore_index=True)

# 13 March
df = df.append({'Date': '3/13/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed', 'Region': 'Casablanca', 'Gender': 'M'}, ignore_index=True)
df = df.append({'Date': '3/13/20', 'Local': False, 'Origin': 'France', 'Status': 'Confirmed', 'Region': 'Taroudant', 'Gender': 'F'}, ignore_index=True)

# 14 March
# Region = Tétouan, Casablanca, Rabat, Fès et Khouribga
# Date d'entree au Maroc entre le 25 février et le 12 mars 2020
df = df.append({'Date': '3/14/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/14/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/14/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/14/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/14/20', 'Local': False, 'Origin': 'Italy', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/14/20', 'Local': False, 'Origin': 'Italy', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/14/20', 'Local': False, 'Origin': 'Italy', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/14/20', 'Local': False, 'Origin': 'France', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/14/20', 'Local': True, 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/14/20', 'Local': False, 'Origin': 'Europe', 'Status': 'Confirmed', 'Gender': 'M'}, ignore_index=True) # M. Amara

# 15 March
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'Italy', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'Italy', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'France', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'France', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'Spain', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/15/20', 'Local': False, 'Origin': 'Austria', 'Status': 'Confirmed'}, ignore_index=True)

# 16 March
df = df.append({'Date': '3/16/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/16/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/16/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/16/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/16/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/16/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/16/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/16/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/16/20', 'Status': 'Confirmed'}, ignore_index=True)

# 17 March
df = df.append({'Date': '3/17/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/17/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/17/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/17/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/17/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/17/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/17/20', 'Status': 'Confirmed'}, ignore_index=True)

# 18 March
df = df.append({'Date': '3/18/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/18/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/18/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/18/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/18/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/18/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/18/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/18/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/18/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/18/20', 'Status': 'Confirmed'}, ignore_index=True)

# 19 March
df = df.append({'Date': '3/19/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/19/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/19/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/19/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/19/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/19/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/19/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/19/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/19/20', 'Status': 'Confirmed'}, ignore_index=True)

# 20 March
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/20/20', 'Status': 'Confirmed'}, ignore_index=True)

# 21 March
df = df.append({'Date': '3/21/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/21/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/21/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/21/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/21/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/21/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/21/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/21/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/21/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/21/20', 'Status': 'Confirmed'}, ignore_index=True)

# 22 March
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/22/20', 'Status': 'Confirmed'}, ignore_index=True)

# 23 March
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)
df = df.append({'Date': '3/23/20', 'Status': 'Confirmed'}, ignore_index=True)

#############################################
# save into csv file

mkdir_p('datasets')
df.to_csv('datasets/morocco.csv')
