package com.nutrienttracker.TableObjects;

public class measurement_description {
    private String unit_name;
    private String unit_of_measurement;
    private String unit_description;

    public String getUnit_name() {
        return unit_name;
    }
    public void setUnit_name(String unit_name) {
        this.unit_name = unit_name;
    }

    public String getUnit_of_measurement() {
        return unit_of_measurement;
    }
    public void setUnit_of_measurement(String unit_of_measurement) {
        this.unit_of_measurement = unit_of_measurement;
    }

    public String getUnit_description() {
        return unit_description;
    }
    public void setUnit_description(String unit_description) {
        this.unit_description = unit_description;
    }
}
