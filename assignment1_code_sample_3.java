package assignment3.linted;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

/**
 * Example Java application demonstrating user input, API calls,
 * email sending, and database storage.
 */
public class VulnerableApp {

    /** Database URL. */
    private static final String DB_URL = "jdbc:mysql://mydatabase.com/mydb";

    /** Database username. */
    private static final String DB_USER = "admin";

    /** Database password. */
    private static final String DB_PASSWORD = "secret123";

    /** Private constructor to satisfy Checkstyle utility class rule. */
    private VulnerableApp() { }

    /**
     * Prompt user for their name and return it.
     *
     * @return the user’s input
     */
    public static String getUserInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        return scanner.nextLine();
    }

    /**
     * Send an email using a system command.
     *
     * @param to      recipient email
     * @param subject email subject
     * @param body    email body
     */
    public static void sendEmail(
        final String to, final String subject, final String body) {
        try {
            String command = String.format(
                "echo %s | mail -s \"%s\" %s",
                body,
                subject,
                to
            );
            Runtime.getRuntime().exec(command);
        } catch (Exception e) {
            System.out.println("Error sending email: " + e.getMessage());
        }
    }

    /**
     * Fetch data from an external API.
     *
     * @return API response content as a string
     */
    public static String getData() {
        StringBuilder result = new StringBuilder();

        try {
            URL url = new URL("http://insecure-api.com/get-data");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");

            InputStream inputStream = conn.getInputStream();
            BufferedReader reader = new BufferedReader(
                new InputStreamReader(inputStream)
            );

            String line;
            while ((line = reader.readLine()) != null) {
                result.append(line);
            }

            reader.close();
        } catch (Exception e) {
            System.out.println("Error fetching data: " + e.getMessage());
        }

        return result.toString();
    }

    /**
     * Save API data to the database.
     *
     * @param data data to be stored
     */
    public static void saveToDb(final String data) {
        String query = "INSERT INTO mytable (column1, column2) VALUES ('"
            + data + "', 'Another Value')";

        try (
            Connection conn = DriverManager.getConnection(
                DB_URL, DB_USER, DB_PASSWORD);
            Statement stmt = conn.createStatement()
        ) {
            stmt.executeUpdate(query);
            System.out.println("Data saved to database.");
        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
        }
    }

    /**
     * Entry point for the application.
     *
     * @param args command-line arguments
     */
    public static void main(final String[] args) {
        String userInput = getUserInput();
        String data = getData();
        saveToDb(data);
        sendEmail("admin@example.com", "User Input", userInput);
    }
}
