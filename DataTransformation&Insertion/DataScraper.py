import csv
import psycopg2
import os
from dotenv import load_dotenv

#table has since been edited 
class daily_total_intake_Table1:
    def __init__(self, intake_id,nutrient_id,age_range,women_intake,men_intake,age_range_for_max,max_safe_amount,unit_of_measurement) :
        self.intake_id = intake_id
        self.nutrient_id = nutrient_id
        self.age_range = age_range
        self.women_intake = women_intake
        self.men_intake = men_intake
        self.age_range_for_max = age_range_for_max
        self.max_safe_amount = max_safe_amount
        self.unit_of_measurement = unit_of_measurement
    def __str__(self) :
        return (
            f"intake_id: {self.intake_id}, "
            f"nutrient_id: {self.nutrient_id}"
            f"Age Range: {self.age_range}, "
            f"Women Intake: {self.women_intake} {self.unit_of_measurement}, "
            f"Men Intake: {self.men_intake} {self.unit_of_measurement}, "
            f"Max Safe Amount (Age {self.age_range_for_max or 'N/A'}): {self.max_safe_amount or 'Not known'} {self.unit_of_measurement}"
        )
    
class measurement_description_Table2: 
    def __init__(self, unit_name, unit_of_measurement, unit_description) :
        self.unit_name = unit_name
        self.unit_of_measurement = unit_of_measurement
        self.unit_description = unit_description
    def __str__(self) :
        return f"Name: {self.unit_name}, Unit of Measurment: {self.unit_of_measurement}, Description: {self.unit_description}"

class productInformation_Table3:
    def __init__(self, product_id, product_name, Food_Group, Calories, Fat_g, SaturatedFats_g, Protein_g, Carbohydrate_g, Sugars_g, Fiber_g,
                 Cholesterol_mg, Added_Sugar_g, Net_Carbs_g, Calcium_mg, Iron_mg, Potassium_mg, Magnesium_mg, Phosphorus_mg, Sodium_mg, Zinc_mg,
                 Copper_mg, Manganese_mg, Selenium_mcg, VitaminA_RAE_mcg, VitaminC_mg, VitaminD_mcg, VitaminE_mg, VitaminK_mcg,
                 Thiamin_B1_mg, Riboflavin_B2_mg, Niacin_B3_mg, Pantothenic_acid_B5_mg, VitaminB6_mg, Biotin_B7_mcg, Folate_DFE_mcg,
                 VitaminB12_mcg, Choline_mg, Omega3s_mg, Omega6s_mg, Trans_Fatty_Acids_g, Water_g, Caffeine_mg, Alcohol_g,
                 Fatty_acids_total_monounsaturated_mg, Fatty_acids_total_polyunsaturated_mg,
                 Serving_Weight1_g, Serving_Description1_g, Serving_Weight2_g, Serving_Description2_g,
                 Serving_Weight3_g, Serving_Description3_g, Serving_Weight4_g, Serving_Description4_g,
                 Serving_Weight5_g, Serving_Description5_g, Serving_Weight6_g, Serving_Description6_g,
                 Serving_Weight7_g, Serving_Description7_g, Serving_Weight8_g, Serving_Description8_g,
                 Serving_Weight9_g, Serving_Description_9_g, CalorieWeight_g):

        self.product_id = product_id
        self.product_name = product_name
        self.Food_Group = Food_Group
        self.Calories = Calories
        self.Fat_g = Fat_g
        self.SaturatedFats_g = SaturatedFats_g
        self.Protein_g = Protein_g
        self.Carbohydrate_g = Carbohydrate_g
        self.Sugars_g = Sugars_g
        self.Fiber_g = Fiber_g
        self.Cholesterol_mg = Cholesterol_mg
        self.Added_Sugar_g = Added_Sugar_g
        self.Net_Carbs_g = Net_Carbs_g
        self.Calcium_mg = Calcium_mg
        self.Iron_mg = Iron_mg
        self.Potassium_mg = Potassium_mg
        self.Magnesium_mg = Magnesium_mg
        self.Phosphorus_mg = Phosphorus_mg
        self.Sodium_mg = Sodium_mg
        self.Zinc_mg = Zinc_mg
        self.Copper_mg = Copper_mg
        self.Manganese_mg = Manganese_mg
        self.Selenium_mcg = Selenium_mcg
        self.VitaminA_RAE_mcg = VitaminA_RAE_mcg
        self.VitaminC_mg = VitaminC_mg
        self.VitaminD_mcg = VitaminD_mcg
        self.VitaminE_mg = VitaminE_mg
        self.VitaminK_mcg = VitaminK_mcg
        self.Thiamin_B1_mg = Thiamin_B1_mg
        self.Riboflavin_B2_mg = Riboflavin_B2_mg
        self.Niacin_B3_mg = Niacin_B3_mg
        self.Pantothenic_acid_B5_mg = Pantothenic_acid_B5_mg
        self.VitaminB6_mg = VitaminB6_mg
        self.Biotin_B7_mcg = Biotin_B7_mcg
        self.Folate_DFE_mcg = Folate_DFE_mcg
        self.VitaminB12_mcg = VitaminB12_mcg
        self.Choline_mg = Choline_mg
        self.Omega3s_mg = Omega3s_mg
        self.Omega6s_mg = Omega6s_mg
        self.Trans_Fatty_Acids_g = Trans_Fatty_Acids_g
        self.Water_g = Water_g
        self.Caffeine_mg = Caffeine_mg
        self.Alcohol_g = Alcohol_g
        self.Fatty_acids_total_monounsaturated_mg = Fatty_acids_total_monounsaturated_mg
        self.Fatty_acids_total_polyunsaturated_mg = Fatty_acids_total_polyunsaturated_mg
        self.Serving_Weight1_g = Serving_Weight1_g
        self.Serving_Description1_g = Serving_Description1_g
        self.Serving_Weight2_g = Serving_Weight2_g
        self.Serving_Description2_g = Serving_Description2_g
        self.Serving_Weight3_g = Serving_Weight3_g
        self.Serving_Description3_g = Serving_Description3_g
        self.Serving_Weight4_g = Serving_Weight4_g
        self.Serving_Description4_g = Serving_Description4_g
        self.Serving_Weight5_g = Serving_Weight5_g
        self.Serving_Description5_g = Serving_Description5_g
        self.Serving_Weight6_g = Serving_Weight6_g
        self.Serving_Description6_g = Serving_Description6_g
        self.Serving_Weight7_g = Serving_Weight7_g
        self.Serving_Description7_g = Serving_Description7_g
        self.Serving_Weight8_g = Serving_Weight8_g
        self.Serving_Description8_g = Serving_Description8_g
        self.Serving_Weight9_g = Serving_Weight9_g
        self.Serving_Description_9_g = Serving_Description_9_g
        self.CalorieWeight_g = CalorieWeight_g

    def __str__(self):
        return (
            f"product_id: {self.product_id}, product_name: {self.product_name}, Food_Group: {self.Food_Group}, Calories: {self.Calories}, "
            f"Fat_g: {self.Fat_g}, SaturatedFats_g: {self.SaturatedFats_g}, Protein_g: {self.Protein_g}, Carbohydrate_g: {self.Carbohydrate_g}, "
            f"Sugars_g: {self.Sugars_g}, Fiber_g: {self.Fiber_g}, Cholesterol_mg: {self.Cholesterol_mg}, Added_Sugar_g: {self.Added_Sugar_g}, "
            f"Net-Carbs_g: {self.Net_Carbs_g}, Calcium_mg: {self.Calcium_mg}, Iron_mg: {self.Iron_mg}, Potassium_mg: {self.Potassium_mg}, "
            f"Magnesium_mg: {self.Magnesium_mg}, Phosphorus_mg: {self.Phosphorus_mg}, Sodium_mg: {self.Sodium_mg}, Zinc_mg: {self.Zinc_mg}, "
            f"Copper_mg: {self.Copper_mg}, Manganese_mg: {self.Manganese_mg}, Selenium_mcg: {self.Selenium_mcg}, VitaminA_RAE_mcg: {self.VitaminA_RAE_mcg}, "
            f"VitaminC_mg: {self.VitaminC_mg}, VitaminD_mcg: {self.VitaminD_mcg}, VitaminE_mg: {self.VitaminE_mg}, VitaminK_mcg: {self.VitaminK_mcg}, "
            f"Thiamin_B1_mg: {self.Thiamin_B1_mg}, Riboflavin_B2_mg: {self.Riboflavin_B2_mg}, Niacin_B3_mg: {self.Niacin_B3_mg}, Pantothenic_acid_B5_mg: {self.Pantothenic_acid_B5_mg}, "
            f"VitaminB6_mg: {self.VitaminB6_mg}, Biotin_B7_mcg: {self.Biotin_B7_mcg}, Folate_DFE_mcg: {self.Folate_DFE_mcg}, VitaminB12_mcg: {self.VitaminB12_mcg}, "
            f"Choline_mg: {self.Choline_mg}, Omega3s_mg: {self.Omega3s_mg}, Omega6s_mg: {self.Omega6s_mg}, Trans_Fatty_Acids_g: {self.Trans_Fatty_Acids_g}, "
            f"Water_g: {self.Water_g}, Caffeine_mg: {self.Caffeine_mg}, Alcohol_g: {self.Alcohol_g}, "
            f"Fatty_acids_total_monounsaturated_mg: {self.Fatty_acids_total_monounsaturated_mg}, Fatty_acids_total_polyunsaturated_mg: {self.Fatty_acids_total_polyunsaturated_mg}, "
            f"Serving_Weight1_g: {self.Serving_Weight1_g}, Serving_Description1_g: {self.Serving_Description1_g}, Serving_Weight2_g: {self.Serving_Weight2_g}, "
            f"Serving_Description2_g: {self.Serving_Description2_g}, Serving_Weight3_g: {self.Serving_Weight3_g}, Serving_Description3_g: {self.Serving_Description3_g}, "
            f"Serving_Weight4_g: {self.Serving_Weight4_g}, Serving_Description4_g: {self.Serving_Description4_g}, Serving_Weight5_g: {self.Serving_Weight5_g}, "
            f"Serving_Description5_g: {self.Serving_Description5_g}, Serving_Weight6_g: {self.Serving_Weight6_g}, Serving_Description6_g: {self.Serving_Description6_g}, "
            f"Serving_Weight7_g: {self.Serving_Weight7_g}, Serving_Description7_g: {self.Serving_Description7_g}, Serving_Weight8_g: {self.Serving_Weight8_g}, "
            f"Serving_Description8_g: {self.Serving_Description8_g}, Serving_Weight9_g: {self.Serving_Weight9_g}, Serving_Description_9_g: {self.Serving_Description_9_g}, "
            f"CalorieWeight_g: {self.CalorieWeight_g}"
        )

class productNutrients_Table4 :
    def __init__(self, product_id, nutrient_id, nutrient_name, amount, unit):
        self.product_id = product_id
        self.nutrient_id = nutrient_id
        self.nutrient_name = nutrient_name
        self.amount = amount
        self.unit = unit

    def __str__(self):
        return (f"Product ID: {self.product_id}, Nutrient ID: {self.nutrient_id}, "
                f"Nutrient Name: {self.nutrient_name}, Amount: {self.amount}, Unit: {self.unit}")

class nutrientNames_Table5 :
    def __init__(self, nutrient_id, nutrient_name) :
        self.nutrient_id = nutrient_id
        self.nutrient_name = nutrient_name
    
    def __str__(self):
        return (f"nutrient_id: {self.nutrient_id}, nutrient_name: {self.nutrient_name}")

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
      self.product_nutrients_Table4_list = [] # Stores the product nutrients pivot table
      self.nutrient_name_Table5_list = [] # Stores all nutrient names
    
    def daily_intake_T1_info(self, file_name):
        with open(file_name, mode="r", newline="", encoding="utf-8") as file : 
            # Each row in the CSV file is stored as a dictionary, where:
            # 1. The keys are taken from the header row (first row of the CSV).
            # 2. The values are the data from each row.
            reader = csv.DictReader(file) # Reads the CSV as dictionaries instead of a list of lists
            for row in reader :
                nutrient = daily_total_intake_Table1(row["intake_id"],row["nutrient_id"],row["age_range"],row["women_intake"],row["men_intake"],row["age_range_for_max"],row["max_safe_amount"],row["unit_of_measurement"])
                self.daily_total_intake_Table1_list.append(nutrient)

    def measurement_description_T2_info(self, file_name):
        with open(file_name, mode="r", newline="", encoding="utf-8") as file :
            reader = csv.DictReader(file)
            for row in reader :
                measurement = measurement_description_Table2(row["unit_name"], row["unit_of_measurement"], row["unit_description"])
                self.measurement_description_Table2_list.append(measurement)
    
    def productInformation_T3_info(self, file_name):
        with open(file_name, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = productInformation_Table3(
                    row["product_id"],
                    row["product_name"],
                    row["Food_Group"],
                    row["Calories"],
                    row["Fat_g"],
                    row["SaturatedFats_g"],
                    row["Protein_g"],
                    row["Carbohydrate_g"],
                    row["Sugars_g"],
                    row["Fiber_g"],
                    row["Cholesterol_mg"],
                    row["Added_Sugar_g"],
                    row["Net-Carbs_g"],
                    row["Calcium_mg"],
                    row["Iron_mg"],
                    row["Potassium_mg"],
                    row["Magnesium_mg"],
                    row["Phosphorus_mg"],
                    row["Sodium_mg"],
                    row["Zinc_mg"],
                    row["Copper_mg"],
                    row["Manganese_mg"],
                    row["Selenium_mcg"],
                    row["VitaminA_RAE_mcg"],
                    row["VitaminC_mg"],
                    row["VitaminD_mcg"],
                    row["VitaminE_mg"],
                    row["VitaminK_mcg"],
                    row["Thiamin_B1_mg"],
                    row["Riboflavin_B2_mg"],
                    row["Niacin_B3_mg"],
                    row["Pantothenic_acid_B5_mg"],
                    row["VitaminB6_mg"],
                    row["Biotin_B7_mcg"],
                    row["Folate_DFE_mcg"],
                    row["VitaminB12_mcg"],
                    row["Choline_mg"],
                    row["Omega3s_mg"],
                    row["Omega6s_mg"],
                    row["Trans_Fatty_Acids_g"],
                    row["Water_g"],
                    row["Caffeine_mg"],
                    row["Alcohol_g"],
                    row["Fatty_acids_total_monounsaturated_mg"],
                    row["Fatty_acids_total_polyunsaturated_mg"],
                    row["Serving_Weight1_g"],
                    row["Serving_Description1_g"],
                    row["Serving_Weight2_g"],
                    row["Serving_Description2_g"],
                    row["Serving_Weight3_g"],
                    row["Serving_Description3_g"],
                    row["Serving_Weight4_g"],
                    row["Serving_Description4_g"],
                    row["Serving_Weight5_g"],
                    row["Serving_Description5_g"],
                    row["Serving_Weight6_g"],
                    row["Serving_Description6_g"],
                    row["Serving_Weight7_g"],
                    row["Serving_Description7_g"],
                    row["Serving_Weight8_g"],
                    row["Serving_Description8_g"],
                    row["Serving_Weight9_g"],
                    row["Serving_Description_9_g"],
                    row["CalorieWeight_g"]
                )
                self.product_information_Table3_list.append(product)

    def product_nutrients_T4_info(self, file_name):
        with open(file_name, mode="r", newline="", encoding="utf-8") as file :
            reader = csv.DictReader(file)
            for row in reader :
                productNutrients = productNutrients_Table4(row["product_id"],row["nutrient_id"],row["nutrient_name"],row["amount"],row["unit"])
                self.product_nutrients_Table4_list.append(productNutrients)

    def nutrient_name_T5_info(self, file_name) :
        with open(file_name, mode="r", newline="", encoding="utf-8") as file :
            reader = csv.DictReader(file)
            for row in reader :
                nutrients = nutrientNames_Table5(row["nutrient_id"],row["nutrient_name"])
                self.nutrient_name_Table5_list.append(nutrients)

    def printList(self, list_name) :
        numStop = 1
        for item in list_name :
            if numStop < 11 :
                print(item)
                numStop+=1
            else :
                break

def databaseConnection() :
    load_dotenv()
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    #Create a cursor
    cur = conn.cursor()
    return conn, cur

### connecting to postgresqul and inserting data into tables
def insert_all_data(scraper, conn, cur) :
    try :
        # 1. Insert nutrient_name table
        nutrient_data = [(item.nutrient_id, item.nutrient_name) for item in scraper.nutrient_name_Table5_list]
        cur.executemany("""
        INSERT INTO nutrient_name (
            nutrient_id, nutrient_name
        )
        VALUES (%s, %s)
        """, nutrient_data)
        
        # 2. Insert measurement_description table
        measurement_data = [(item.unit_name, item.unit_of_measurement, item.unit_description) 
                            for item in scraper.measurement_description_Table2_list]
        cur.executemany("""
            INSERT INTO measurement_description (unit_name, unit_of_measurement, unit_description)
            VALUES (%s, %s, %s)
        """, measurement_data)

        # 3. Insert daily_total_intake table
        daily_intake_data = [(int(item.intake_id), int(item.nutrient_id), item.age_range, item.women_intake,
        item.men_intake, item.age_range_for_max, item.max_safe_amount, item.unit_of_measurement)
                             for item in scraper.daily_total_intake_Table1_list]
        cur.executemany("""
            INSERT INTO daily_total_intake (
                intake_id, nutrient_id, age_range, women_intake, men_intake, age_range_for_max, max_safe_amount, unit_of_measurement
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, daily_intake_data)

        # 4. Insert product_information table
        product_info_data = []
        for item in scraper.product_information_Table3_list:
            product_info_data.append((
                item.product_id, item.product_name, item.Food_Group, item.Calories, item.Fat_g, item.SaturatedFats_g,
                item.Protein_g, item.Carbohydrate_g, item.Sugars_g, item.Fiber_g, item.Cholesterol_mg, item.Added_Sugar_g,
                item.Net_Carbs_g, item.Calcium_mg, item.Iron_mg, item.Potassium_mg, item.Magnesium_mg, item.Phosphorus_mg,
                item.Sodium_mg, item.Zinc_mg, item.Copper_mg, item.Manganese_mg, item.Selenium_mcg, item.VitaminA_RAE_mcg,
                item.VitaminC_mg, item.VitaminD_mcg, item.VitaminE_mg, item.VitaminK_mcg, item.Thiamin_B1_mg,
                item.Riboflavin_B2_mg, item.Niacin_B3_mg, item.Pantothenic_acid_B5_mg, item.VitaminB6_mg,
                item.Biotin_B7_mcg, item.Folate_DFE_mcg, item.VitaminB12_mcg, item.Choline_mg, item.Omega3s_mg,
                item.Omega6s_mg, item.Trans_Fatty_Acids_g, item.Water_g, item.Caffeine_mg, item.Alcohol_g,
                item.Fatty_acids_total_monounsaturated_mg, item.Fatty_acids_total_polyunsaturated_mg,
                item.Serving_Weight1_g, item.Serving_Description1_g, item.Serving_Weight2_g, item.Serving_Description2_g,
                item.Serving_Weight3_g, item.Serving_Description3_g, item.Serving_Weight4_g, item.Serving_Description4_g,
                item.Serving_Weight5_g, item.Serving_Description5_g, item.Serving_Weight6_g, item.Serving_Description6_g,
                item.Serving_Weight7_g, item.Serving_Description7_g, item.Serving_Weight8_g, item.Serving_Description8_g,
                item.Serving_Weight9_g, item.Serving_Description_9_g, item.CalorieWeight_g
            ))
        
        cur.executemany("""
            INSERT INTO product_information (
                product_id, product_name, Food_Group, Calories, Fat_g, SaturatedFats_g, Protein_g, Carbohydrate_g,
                Sugars_g, Fiber_g, Cholesterol_mg, Added_Sugar_g, Net_Carbs_g, Calcium_mg, Iron_mg, Potassium_mg,
                Magnesium_mg, Phosphorus_mg, Sodium_mg, Zinc_mg, Copper_mg, Manganese_mg, Selenium_mcg,
                VitaminA_RAE_mcg, VitaminC_mg, VitaminD_mcg, VitaminE_mg, VitaminK_mcg, Thiamin_B1_mg,
                Riboflavin_B2_mg, Niacin_B3_mg, Pantothenic_acid_B5_mg, VitaminB6_mg, Biotin_B7_mcg,
                Folate_DFE_mcg, VitaminB12_mcg, Choline_mg, Omega3s_mg, Omega6s_mg, Trans_Fatty_Acids_g,
                Water_g, Caffeine_mg, Alcohol_g, Fatty_acids_total_monounsaturated_mg, Fatty_acids_total_polyunsaturated_mg,
                Serving_Weight1_g, Serving_Description1_g, Serving_Weight2_g, Serving_Description2_g,
                Serving_Weight3_g, Serving_Description3_g, Serving_Weight4_g, Serving_Description4_g,
                Serving_Weight5_g, Serving_Description5_g, Serving_Weight6_g, Serving_Description6_g,
                Serving_Weight7_g, Serving_Description7_g, Serving_Weight8_g, Serving_Description8_g,
                Serving_Weight9_g, Serving_Description_9_g, CalorieWeight_g
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, product_info_data)

        # 5. Insert product_nutrients table
        nutrients_data = [(item.product_id, item.nutrient_id, item.amount, item.unit) 
                          for item in scraper.product_nutrients_Table4_list]
        cur.executemany("""
            INSERT INTO product_nutrients (product_id, nutrient_id, amount, unit)
            VALUES (%s, %s, %s, %s)
        """, nutrients_data)

        conn.commit()
        print("All data inserted successfully!")

    except Exception as e:
        conn.rollback()
        print("Error during insertion:", e)


def createTables(file_path, conn, cur):
    with open(file_path, mode="r") as sql_file:
        sql_script = sql_file.read()
        cur.execute(sql_script)

    print("SQL script executed successfully")


if __name__ == "__main__":
    conn, cur = databaseConnection()
    createTables("../createTables.sql", conn, cur)

    scraper = DataScrapper() # Create an instance of DataScrapper
    # Load CSV files into lists
    scraper.daily_intake_T1_info("../Data/daily_total_intake.csv")
    scraper.measurement_description_T2_info("../Data/measurement_description.csv")
    scraper.productInformation_T3_info("../Data/product_information.csv")
    scraper.product_nutrients_T4_info("../Data/product_nutrients.csv")
    scraper.nutrient_name_T5_info("../Data/nutrient_name.csv")

    # Insert all data
    insert_all_data(scraper, conn, cur)


    cur.close()
    conn.close()