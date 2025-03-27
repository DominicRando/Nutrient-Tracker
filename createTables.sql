DROP TABLE IF EXISTS daily_total_intake, measurement_description, product_information, product_nutrients, nutrient_name;

CREATE TABLE nutrient_name (
    nutrient_id BIGINT PRIMARY KEY,
    nutrient_name TEXT NOT NULL
);

CREATE TABLE product_nutrients (
    product_id BIGINT NOT NULL,
    nutrient_id BIGINT NOT NULL,
    amount NUMERIC,
    unit TEXT,
    FOREIGN KEY (product_id) REFERENCES product_information (product_id),
    FOREIGN KEY (nutrient_id) REFERENCES nutrient_name (nutrient_id)
);

CREATE TABLE product_information (
    product_id BIGINT NOT NULL,
    product_name TEXT,
    Food_Group TEXT,
    Calories NUMERIC(6,5),
    Fat_g NUMERIC(6,5),
    SaturatedFats_g NUMERIC(6,5),
    Protein_g NUMERIC(6,5),
    Carbohydrate_g NUMERIC(6,5),
    Sugars_g NUMERIC(6,5),
    Fiber_g NUMERIC(6,5),
    Cholesterol_mg NUMERIC(6,5),
    Added_Sugar_g NUMERIC(6,5),
    Net-Carbs_g NUMERIC(6,5),
    Calcium_mg NUMERIC(6,5),
    Iron_mg NUMERIC(6,5),
    Potassium_mg NUMERIC(6,5),
    Magnesium_mg NUMERIC(6,5),
    Phosphorus_mg NUMERIC(6,5),
    Sodium_mg NUMERIC(6,5),
    Zinc_mg NUMERIC(6,5),
    Copper_mg NUMERIC(6,5),
    Manganese_mg NUMERIC(6,5),
    Selenium_mcg NUMERIC(6,5),
    VitaminA_RAE_mcg NUMERIC(6,5),
    VitaminC_mg NUMERIC(6,5),
    VitaminD_mcg NUMERIC(6,5),
    VitaminE_mg NUMERIC(6,5),
    VitaminK_mcg NUMERIC(6,5),
    Thiamin_B1_mg NUMERIC(6,5),
    Riboflavin_B2_mg NUMERIC(6,5),
    Niacin_B3_mg NUMERIC(6,5),
    Pantothenic_acid_B5_mg NUMERIC(6,5),
    VitaminB6_mg NUMERIC(6,5),
    Biotin_B7_mcg NUMERIC(6,5),
    Folate_DFE_mcg NUMERIC(6,5),
    VitaminB12_mcg NUMERIC(6,5),
    Choline_mg NUMERIC(6,5),
    Omega3s_mg NUMERIC(6,5),
    Omega6s_mg NUMERIC(6,5),
    Trans_Fatty_Acids_g NUMERIC(6,5),
    Water_g NUMERIC(6,5),
    Caffeine_m NUMERIC(6,5),
    Fatty_acids,total_monounsaturated_mg NUMERIC(6,5),
    Fatty_acids,total_polyunsaturated_mg NUMERIC(6,5),
    Serving_Weight1_g TEXT,
    Serving_Description1_g TEXT,
    Serving_Weight2_g TEXT,
    Serving_Description2_g TEXT,
    Serving_Weight3_g TEXT,
    Serving_Description3_g TEXT,
    Serving_Weight4_g TEXT,
    Serving_Description4_g TEXT,
    Serving_Weight5_g TEXT,
    Serving_Description5_g TEXT,
    Serving_Weight6_g TEXT,
    Serving_Description6_g TEXT,
    ServingWeight7_g TEXT,
    Serving_Description7_g TEXT,
    Serving_Weight8_g TEXT,
    Serving_Description8_g TEXT,
    Serving_Weight9_g TEXT,
    Serving_Description_9_g TEXT,
    CalorieWeight_g NUMERIC(6,5)
);

CREATE TABLE measurement_description (
    unit_name TEXT PRIMARY KEY,
    unit_of_measurement TEXT,
    unit_description TEXT
);

CREATE TABLE daily_total_intake (
    intake_id INT PRIMARY KEY,
    nutrient_id BIGINT NOT NULL,
    age_range TEXT,
    women_intake NUMERIC(7,2),
    men_intake NUMERIC(7,2),
    age_range_for_max TEXT,
    max_safe_amount TEXT,
    unit_of_measurement TEXT,
    FOREIGN KEY (nutrient_id) REFERENCES nutrient_name(nutrient_id),
    FOREIGN KEY (unit_of_measurement) REFERENCES measurement_description (unit_name)
);



