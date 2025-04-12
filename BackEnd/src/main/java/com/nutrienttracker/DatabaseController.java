// This declares the package name. It should match your folder structure.
package com.nutrienttracker;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

// Import Spring classes needed for dependency injection and REST API functionality.
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.*;

import com.nutrienttracker.TableObjects.nutrient_name;
import com.nutrienttracker.TableObjects.product_information;

// Allows any origin point (IP) to access this class
@CrossOrigin(origins = "*")
// Marks this class as a REST controller, so Spring Boot knows it should handle HTTP requests.
@RestController

// Maps all routes in this controller under the "/api" path.
// So this controller will handle requests like "/api/ping-db"
@RequestMapping("/api")
public class DatabaseController {

    // Spring will automatically inject an instance of JdbcTemplate at runtime.
    // JdbcTemplate lets you run SQL queries against your database.
    @Autowired
    private JdbcTemplate jdbcTemplate;

    // This method handles GET requests to "/api/ping-db"
    @GetMapping("/ping-db")
    public String pingDatabase() {
        try {
            List<Map<String, Object>> rows = jdbcTemplate.queryForList("SELECT * FROM daily_total_intake");
            for (Map<String,Object> row :rows) {
                System.out.println("Row:");
                for (Map.Entry<String, Object> entry : row.entrySet()) {
                    System.out.println("  " + entry.getKey() + ": " + entry.getValue());
                }
            }
            // If the query works, return a success message with the result
            return "✅ Query executed. Check your console for printed results";
        } catch (Exception e) {
            // If anything goes wrong (like DB isn't connected), catch the exception and return an error message
            return "❌ Failed to connect to database: " + e.getMessage();
        }
    }

    @GetMapping("/nutrients")
    public List<nutrient_name> getNutrients() {
        String sql = "SELECT nutrient_id, nutrient_name FROM nutrient_name";

        // Query and map each row to a nutrient_name object
        return jdbcTemplate.query(sql, (rs, rowNum) -> {
            nutrient_name nutrient = new nutrient_name();
            nutrient.setNutrient_id(rs.getLong("nutrient_id"));
            nutrient.setNutrient_name(rs.getString("nutrient_name"));
            return nutrient;
        });
    }

    @GetMapping("/products")
    public List<product_information> getProducts(@RequestParam(required=false) String name) {
        if (name == null || name.trim().isEmpty()) {
            // Return empty list if no name is provided
            return new ArrayList<>();
        }

        // Otherwise, search by name (case-insensitive)
        String sql = "SELECT product_id, product_name FROM product_information WHERE product_name ILIKE ?";
        String likePattern = "%" + name + "%";

        return jdbcTemplate.query(sql, new Object[]{likePattern}, (rs, rowNum) -> {
            product_information product = new product_information();
            product.setProduct_id(rs.getLong("product_id"));
            product.setProduct_name(rs.getString("product_name"));
            return product;
        });
    }

    @GetMapping("/hello")
    public String getHello() {
        return "Hello World test!";
    }
}

