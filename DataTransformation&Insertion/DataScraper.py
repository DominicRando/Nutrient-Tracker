import csv
import psycopg2

class daily_total_intake_Table1:
    def __init__(self, nutrient_name, daily_rec_amount_total, unit_of_measurement) :
        self.nutrient_name = nutrient_name
        self.daily_rec_amount_total = daily_rec_amount_total
        self.unit_of_measurement = unit_of_measurement
    def __str__(self) :
        return f"Nutrient Name: {self.nutrient_name}, Daily Rec Amount Total: {self.daily_rec_amount_total}, Unit of Measurement: {self.unit_of_measurement}"
    
class measurement_description_Table2: 
    def __init__(self, unit_of_measurement, description) :
        self.unit_of_measurement = unit_of_measurement
        self.description = description

class productInformation_Table3: 
    def __init__(self, ID, name, food_group, calories, fat_g, protein_g, carbs_g, netCarbs_g, fiber_g, naturalSugars_g, addedSugars_g, starch_g, sucrose_g, dextrose_g, 
                 fructose_g, lactose_g, cholesteral_mg, sodium_mg, calcium_mg, iron_mg, magnesium_mg, zinc_mg, copper_mg, manganese_mg, flouride_mcg, vitaminA_IU, 
                 vitaminC_mg, vitaminD_mcg, vitaminK_mcg, vitaminB5_mg, vitaminB6_mg, biotinB7_mcg, folateB9_mcg, folicAcid_mcg, omega3_mg, omega6_mg, PRAL_score, 
                 acids_g, water_g, caffine_mg, servingSize_g, serving_size_ratio, serving_size_description):
        self.ID = ID
        self.name = name
        self.food_group = food_group
        self.calories = calories
        self.fat_g = fat_g
        self.protein_g = protein_g
        self.carbs_g = carbs_g
        self.netCarbs_g = netCarbs_g
        self.fiber_g = fiber_g
        self.naturalSugars_g = naturalSugars_g
        self.addedSugars_g = addedSugars_g
        self.starch_g = starch_g
        self.sucrose_g = sucrose_g
        self.dextrose_g = dextrose_g
        self.fructose_g = fructose_g
        self.lactose_g = lactose_g
        self.cholesteral_mg = cholesteral_mg
        self.sodium_mg = sodium_mg
        self.calcium_mg = calcium_mg
        self.iron_mg = iron_mg
        self.magnesium_mg = magnesium_mg
        self.zinc_mg = zinc_mg
        self.copper_mg = copper_mg
        self.manganese_mg = manganese_mg
        self.flouride_mcg = flouride_mcg
        self.vitaminA_IU = vitaminA_IU
        self.vitaminC_mg = vitaminC_mg
        self.vitaminD_mcg = vitaminD_mcg
        self.vitaminK_mcg = vitaminK_mcg
        self.vitaminB5_mg = vitaminB5_mg
        self.vitaminB6_mg = vitaminB6_mg
        self.biotinB7_mcg = biotinB7_mcg
        self.folateB9_mcg = folateB9_mcg
        self.folicAcid_mcg = folicAcid_mcg
        self.omega3_mg = omega3_mg
        self.omega6_mg = omega6_mg
        self.PRAL_score = PRAL_score
        self.acids_g = acids_g
        self.water_g = water_g
        self.caffine_mg = caffine_mg
        self.servingSize_g = servingSize_g
        self.serving_size_ratio = serving_size_ratio
        self.serving_size_description = serving_size_description
    def __str__(self):
        return (f"ID: {self.ID}, Name: {self.name}, Food Group: {self.food_group}, Calories: {self.calories}, Fat (g): {self.fat_g}, "
            f"Protein (g): {self.protein_g}, Carbs (g): {self.carbs_g}, Net Carbs (g): {self.netCarbs_g}, Fiber (g): {self.fiber_g}, "
            f"Natural Sugars (g): {self.naturalSugars_g}, Added Sugars (g): {self.addedSugars_g}, Starch (g): {self.starch_g}, "
            f"Sucrose (g): {self.sucrose_g}, Dextrose (g): {self.dextrose_g}, Fructose (g): {self.fructose_g}, Lactose (g): {self.lactose_g}, "
            f"Cholesterol (mg): {self.cholesteral_mg}, Sodium (mg): {self.sodium_mg}, Calcium (mg): {self.calcium_mg}, Iron (mg): {self.iron_mg}, "
            f"Magnesium (mg): {self.magnesium_mg}, Zinc (mg): {self.zinc_mg}, Copper (mg): {self.copper_mg}, Manganese (mg): {self.manganese_mg}, "
            f"Fluoride (mcg): {self.flouride_mcg}, Vitamin A (IU): {self.vitaminA_IU}, Vitamin C (mg): {self.vitaminC_mg}, "
            f"Vitamin D (mcg): {self.vitaminD_mcg}, Vitamin K (mcg): {self.vitaminK_mcg}, Vitamin B5 (mg): {self.vitaminB5_mg}, "
            f"Vitamin B6 (mg): {self.vitaminB6_mg}, Biotin B7 (mcg): {self.biotinB7_mcg}, Folate B9 (mcg): {self.folateB9_mcg}, "
            f"Folic Acid (mcg): {self.folicAcid_mcg}, Omega-3 (mg): {self.omega3_mg}, Omega-6 (mg): {self.omega6_mg}, "
            f"PRAL Score: {self.PRAL_score}, Acids (g): {self.acids_g}, Water (g): {self.water_g}, Caffeine (mg): {self.caffine_mg}, "
            f"Serving Size (g): {self.servingSize_g}, Serving Size Ratio: {self.serving_size_ratio}, Serving Size Description: {self.serving_size_description}")

# newline="" -> Ensures that newline characters are handled consistently across different operating systems. It prevents Python from adding extra blank lines when reading CSV files.
# encoding="utf-8" -> Specifies that the file should be read using UTF-8 encoding, which helps prevent errors when dealing with special characters.
# "r" -> Read mode (default): Opens the file for reading only. If the file does not exist, it raises an error.
class DataScrapper :
    # This is the constructor method, which gets called automatically when you create an instance of DataScrapper
    # Creates an empty list called daily_total_intake_Table1_list to store nutrient objects
    # self is a reference to the instance of the class, so this list belongs to each DataScrapper object
    def __init__(self):
      self.daily_total_intake_Table1_list = []  # Stores nutrient data
      self.measurement_description_Table2_list = [] # Stores unit descriptions
      self.product_information_Table3_list = [] # Stores product details

    def daily_intake_T1_info(self, file_name):
        with open(file_name, mode="r", newline="", encoding="utf-8") as file : 
            # Each row in the CSV file is stored as a dictionary, where:
            # 1. The keys are taken from the header row (first row of the CSV).
            # 2. The values are the data from each row.
            reader = csv.DictReader(file) # Reads the CSV as dictionaries instead of a list of lists
            for row in reader :
                nutrient = daily_total_intake_Table1(row["nutrient_name"], row["daily_rec_amount_total"], row["unit_of_measurement"])
                self.daily_total_intake_Table1_list.append(nutrient)
    
    def measurement_description_T2_info(self, file_name):
        with open(file_name, mode="r", newline="", encoding="utf-8") as file :
            reader = csv.DictReader(file)
            for row in reader :
                measurement = measurement_description_Table2(row["unit_of_measurement"], row["description"])
                self.measurement_description_Table2_list.append(measurement)
    
    def productInformation_T3_info(self, file_name):
        with open(file_name, mode="r", newline="", encoding="utf-8") as file :
            reader = csv.DictReader(file)
            for row in reader :
                product = productInformation_Table3(
                    row["ID"],
                    row["Name"],
                    row["Food_Group"],
                    row["Calories"],
                    row["Fat_g"],
                    row["Protein_g"],
                    row["Carbohydrate_g"],
                    row["Net-Carbs_g"],
                    row["Fiber_g"],
                    row["Sugars_g"],  # Assuming "Sugars_g" corresponds to naturalSugars_g
                    row["Added_Sugar_g"],
                    row["Starch_g"],
                    row["Sucrose_g"],
                    row["Glucose_(Dextrose)_g"],
                    row["Fructose_g"],
                    row["Lactose_g"],
                    row["Cholesterol_mg"],
                    row["Sodium_mg"],
                    row["Calcium_mg"],
                    row["Iron_mg"],
                    row["Magnesium_mg"],
                    row["Zinc_mg"],
                    row["Copper_mg"],
                    row["Manganese_mg"],
                    row["Fluoride_mcg"],
                    row["VitaminA_IU"],
                    row["VitaminC_mg"],
                    row["VitaminD_mcg"],
                    row["VitaminK_mcg"],
                    row["Pantothenic_acid_B5_mg"],  # B5
                    row["VitaminB6_mg"],  # B6
                    row["Biotin_B7_mcg"],
                    row["Folate_B9_mcg"],
                    row["Folic_acid_mcg"],
                    row["Omega3s_mg"],
                    row["Omega6s_mg"],
                    row["PRAL_score"],
                    row["Fatty_acids,total_polyunsaturated_mg"],  # Assuming this corresponds to acids_g
                    row["Water_g"],
                    row["Caffeine_mg"],
                    row["Serving_Weight1_g"],  # Assuming primary serving size
                    row["Serving_Weight2_g"],  # Serving size ratio placeholder
                    row["Serving_Description1_g"]  # Serving size description
                )
                self.product_information_Table3_list.append(product)

    def printList(self, list_name) :
        numStop = 1
        for item in list_name :
            if numStop < 11 :
                print(item)
                numStop+=1
            else :
                break


# Calling the method:
#This initializes scraper with an empty list for storing data.
scraper = DataScrapper() # Create an instance of DataScrapper

# This reads data from "test.csv", creates daily_total_intake_Table1 objects, and stores them in daily_total_intake_Table1_list
scraper.productInformation_T3_info("NutritionData.csv")

# This prints each nutrient's details
scraper.printList(scraper.product_information_Table3_list)

### connecting to postgresqul and inserting data into tables

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="localhost",
    port="5432"
)

#Create a cursor
cur = conn.cursor()

#Insert an object into table
insert_query="""
INSERT INTO ....
"""

data_to_insert = ("value1", )

cur.execute()


