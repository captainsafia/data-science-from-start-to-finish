### "import"
import pandas as pd

### "load"
crimes = pd.read_csv("crimes_final.csv", header = None)

### "inspect-data"
crimes.head(5)

### "append-header"
 crimes.columns = [
     "id",
     "case_number",
     "date",
     "block",
     "iucr",
     "primary_type",
     "description",
     "location_descriptions",
     "arrest",
     "domestic",
     "beat",
     "district",
     "ward",
     "community_area",
     "fbi_code",
     "x_coordinate",
     "y_coordinate",
     "year",
     "updated_on",
     "latitude",
     "longitude"
 ]

### "lowercase-columns"
for column in crimes.columns:
    if crimes[column].dtypes == object:
        crimes[column] = crimes[column].str.lower()

### "whats-missing"
len(crimes.index)
crimes.isnull().sum()

### "remove-empty-cols"
del crimes["district"]
crimes.drop("ward", axis = 1, inplace = True)
crimes = crime.drop("community_area", axis = 1)

### "c

### "save-file"
cimes.to_csv("crimes_cleaned.csv")
