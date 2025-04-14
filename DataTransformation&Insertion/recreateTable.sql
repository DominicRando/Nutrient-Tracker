-- -- 0. Create table if not exists
DROP TABLE IF EXISTS daily_total_intake;

CREATE TABLE daily_total_intake (
    intake_id INT PRIMARY KEY,
    nutrient_id BIGINT NOT NULL,
    nutrient_name TEXT,
    age_min INT,
    age_max INT,
    sex TEXT,
    life_stage TEXT,
    recommended_amount FLOAT,
    unit TEXT,
    unit_name TEXT
);
