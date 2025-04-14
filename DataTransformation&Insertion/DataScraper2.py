import csv
import os
from dotenv import load_dotenv
import psycopg2
from DataScraper import databaseConnection, createTables


class daily_total_intake_Table1_NEW:
    def __init__(self, intake_id, nutrient_id, nutrient_name, age_min, age_max, sex, life_stage, recommended_amount, unit, unit_name):
        self.intake_id = intake_id
        self.nutrient_id = nutrient_id
        self.nutrient_name = nutrient_name
        self.age_min = age_min
        self.age_max = age_max
        self.sex = sex
        self.life_stage = life_stage
        self.recommended_amount = recommended_amount
        self.unit = unit
        self.unit_name = unit_name

    def __str__(self):
        return (
            f"Intake ID: {self.intake_id}, "
            f"Nutrient ID: {self.nutrient_id}, "
            f"Nutrient Name: {self.nutrient_name}, "
            f"Age Range: {self.age_min}-{self.age_max}, "
            f"Sex: {self.sex}, "
            f"Life Stage: {self.life_stage}, "
            f"Recommended Amount: {self.recommended_amount} {self.unit} ({self.unit_name})"
        )

class DataScraper2: 
    def __init__(self):
        self.daily_total_intake_Table1_NEW_list = []
    
    def daily_intake_T1_NEW_info(self, file_name):
        with open(file_name, mode="r", newline="", encoding="utf-8") as file :
            reader = csv.DictReader(file)
            for row in reader:
                nutrient = daily_total_intake_Table1_NEW(
                    row["intake_id"],row["nutrient_id"],row["nutrient_name"],row["age_min"],row["age_max"],
                    row["sex"],row["life_stage"],row["recommended_amount"],row["unit"],row["unit_name"]
                )
                self.daily_total_intake_Table1_NEW_list.append(nutrient)


def insert_data(scraper, conn, cur):
    try:
        daily_intake_data = [(int(item.intake_id), int(item.nutrient_id), item.nutrient_name, int(item.age_min),
                              int(item.age_max), item.sex, item.life_stage, float(item.recommended_amount),
                              item.unit, item.unit_name) for item in scraper.daily_total_intake_Table1_NEW_list  
                            ]
        cur.executemany("""
            INSERT INTO daily_total_intake (
                intake_id,nutrient_id,nutrient_name,age_min,age_max,sex,life_stage,recommended_amount,unit,unit_name
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, daily_intake_data)

        conn.commit()
        print("All data inserted successfully!")

    except Exception as e:
        conn.rollback()
        print("Error during insertion:", e)

conn,cur = databaseConnection()
# Building the Database tables
createTables("recreateTable.sql", conn, cur)

# Load CSV files into lists
scraper = DataScraper2()
scraper.daily_intake_T1_NEW_info("../Data/daily_total_intake.csv")

insert_data(scraper, conn, cur)
cur.close()
conn.close()
