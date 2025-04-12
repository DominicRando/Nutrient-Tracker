package com.nutrienttracker.TableObjects;

public class daily_total_intake {
    private int intake_id;
    private long nutrient_id;
    private String age_range;
    private String women_intake;
    private String men_intake;
    private String age_range_for_max;
    private String max_safe_amount;
    private String unit_of_measurement;

    public int getIntake_id() {
        return intake_id;
    }
    public void setIntake_id(int intake_id) {
        this.intake_id = intake_id;
    }

    public long getNutrient_id() {
        return nutrient_id;
    }
    public void setNutrient_id(long nutrient_id) {
        this.nutrient_id = nutrient_id;
    }

    public String getAge_range() {
        return age_range;
    }
    public void setAge_range(String age_range) {
        this.age_range = age_range;
    }

    public String getWomen_intake() {
        return women_intake;
    }
    public void setWomen_intake(String women_intake) {
        this.women_intake = women_intake;
    }

    public String getMen_intake() {
        return men_intake;
    }
    public void setMen_intake(String men_intake) {
        this.men_intake = men_intake;
    }

    public String getAge_range_for_max() {
        return age_range_for_max;
    }
    public void setAge_range_for_max(String age_range_for_max) {
        this.age_range_for_max = age_range_for_max;
    }

    public String getMax_safe_amount() {
        return max_safe_amount;
    }
    public void setMax_safe_amount(String max_safe_amount) {
        this.max_safe_amount = max_safe_amount;
    }

    public String getUnit_of_measurement() {
        return unit_of_measurement;
    }
    public void setUnit_of_measurement(String unit_of_measurement) {
        this.unit_of_measurement = unit_of_measurement;
    }
}
