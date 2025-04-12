package com.nutrienttracker.TableObjects;

public class product_nutrients {
    private long product_id;
    private long nutrient_id;
    private double amount;
    private String unit;

    public long getProduct_id() {
        return product_id;
    }
    public void setProduct_id(long product_id) {
        this.product_id = product_id;
    }

    public long getNutrient_id() {
        return nutrient_id;
    }
    public void setNutrient_id(long nutrient_id) {
        this.nutrient_id = nutrient_id;
    }

    public double getAmount() {
        return amount;
    }
    public void setAmount(double amount) {
        this.amount = amount;
    }

    public String getUnit() {
        return unit;
    }
    public void setUnit(String unit) {
        this.unit = unit;
    }
}
