DROP TABLE IF EXISTS daily_total_intake, measurement_description, product_information, product_nutrients, nutrient_name;

CREATE TABLE nutrient_name (
    nutrient_id BIGINT PRIMARY KEY,
    nutrient_name TEXT NOT NULL
);

CREATE TABLE product_information (
    product_id BIGINT PRIMARY KEY NOT NULL,
    product_name TEXT,
    Food_Group TEXT,
    Calories TEXT,
    Fat_g TEXT,
    SaturatedFats_g TEXT,
    Protein_g TEXT,
    Carbohydrate_g TEXT,
    Sugars_g TEXT,
    Fiber_g TEXT,
    Cholesterol_mg TEXT,
    Added_Sugar_g TEXT,
    Net_Carbs_g TEXT,
    Calcium_mg TEXT,
    Iron_mg TEXT,
    Potassium_mg TEXT,
    Magnesium_mg TEXT,
    Phosphorus_mg TEXT,
    Sodium_mg TEXT,
    Zinc_mg TEXT,
    Copper_mg TEXT,
    Manganese_mg TEXT,
    Selenium_mcg TEXT,
    VitaminA_RAE_mcg TEXT,
    VitaminC_mg TEXT,
    VitaminD_mcg TEXT,
    VitaminE_mg TEXT,
    VitaminK_mcg TEXT,
    Thiamin_B1_mg TEXT,
    Riboflavin_B2_mg TEXT,
    Niacin_B3_mg TEXT,
    Pantothenic_acid_B5_mg TEXT,
    VitaminB6_mg TEXT,
    Biotin_B7_mcg TEXT,
    Folate_DFE_mcg TEXT,
    VitaminB12_mcg TEXT,
    Choline_mg TEXT,
    Omega3s_mg TEXT,
    Omega6s_mg TEXT,
    Trans_Fatty_Acids_g TEXT,
    Water_g TEXT,
    Caffeine_mg TEXT,
    Alcohol_g TEXT,
    Fatty_acids_total_monounsaturated_mg TEXT,
    Fatty_acids_total_polyunsaturated_mg TEXT,
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
    Serving_Weight7_g TEXT,
    Serving_Description7_g TEXT,
    Serving_Weight8_g TEXT,
    Serving_Description8_g TEXT,
    Serving_Weight9_g TEXT,
    Serving_Description_9_g TEXT,
    CalorieWeight_g TEXT
);

CREATE TABLE product_nutrients (
    product_id BIGINT NOT NULL,
    nutrient_id BIGINT NOT NULL,
    amount NUMERIC,
    unit TEXT,
    FOREIGN KEY (product_id) REFERENCES product_information (product_id),
    FOREIGN KEY (nutrient_id) REFERENCES nutrient_name (nutrient_id)
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
    women_intake TEXT,
    men_intake TEXT,
    age_range_for_max TEXT,
    max_safe_amount TEXT,
    unit_of_measurement TEXT,
    FOREIGN KEY (nutrient_id) REFERENCES nutrient_name(nutrient_id)
);



