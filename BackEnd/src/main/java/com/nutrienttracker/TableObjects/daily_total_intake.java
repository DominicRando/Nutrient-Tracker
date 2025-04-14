package com.nutrienttracker.TableObjects;

public class daily_total_intake {
    private int intake_id;
    private long nutrient_id;
    private String nutrient_name;
    private int age_min;
    private int age_max;
    private String sex;
    private String life_stage;
    private double recommended_amount;
    private String unit;
    private String unit_name;

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

    public String getNutrient_name() {
        return nutrient_name;
    }
    public void setNutrient_name(String nutrient_name) {
        this.nutrient_name = nutrient_name;
    }

    public int getAge_min() {
        return age_min;
    }
    public void setAge_min(int age_min) {
        this.age_min = age_min;
    }

    public int getAge_max() {
        return age_max;
    }
    public void setAge_max(int age_max) {
        this.age_max = age_max;
    }

    public String getSex() {
        return sex;
    }
    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getLife_stage() {
        return life_stage;
    }
    public void setLife_stage(String life_stage) {
        this.life_stage = life_stage;
    }

    public double getRecommended_amount() {
        return recommended_amount;
    }
    public void setRecommended_amount(double recommended_amount) {
        this.recommended_amount = recommended_amount;
    }

    public String getUnit() {
        return unit;
    }
    public void setUnit(String unit) {
        this.unit = unit;
    }

    public String getUnit_name() {
        return unit_name;
    }
    public void setUnit_name(String unit_name) {
        this.unit_name = unit_name;
    }
}
