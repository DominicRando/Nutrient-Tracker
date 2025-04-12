package com.nutrienttracker;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import io.github.cdimascio.dotenv.Dotenv;

@SpringBootApplication
public class MainApplication {
    public static void main(String[] args) {
        // Load environment variables from .env
        Dotenv dotenv = Dotenv.configure().ignoreIfMissing().load();
        System.setProperty("DB_URL", dotenv.get("DB_URL"));
        System.setProperty("DB_USERNAME", dotenv.get("DB_USERNAME"));
        System.setProperty("DB_PASSWORD", dotenv.get("DB_PASSWORD"));

        System.out.println("DB_URL: '" + System.getProperty("DB_URL") + "'");
        System.out.println("DB_USERNAME: '" + System.getProperty("DB_USERNAME") + "'");
        System.out.println("DB_PASSWORD: '" + System.getProperty("DB_PASSWORD") + "'");

        System.out.println("✅ PostgreSQL driver found!");

        SpringApplication.run(MainApplication.class, args);
    }
}
