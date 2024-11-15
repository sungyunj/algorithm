import java.io.*;
import java.math.BigDecimal;
import java.math.RoundingMode;

public class double1 {
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new FileReader("double1.inp"));
            BufferedWriter bw = new BufferedWriter(new FileWriter("double1.out"));

            int n = Integer.parseInt(br.readLine().trim());
            
            for (int i = 0; i < n; i++) {
                String expression = br.readLine().trim();
                BigDecimal result = evaluateExpression(expression);
                bw.write(formatResult(result));
                bw.newLine();
            }
            
            br.close();
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static BigDecimal evaluateExpression(String expression) {
        String[] tokens = expression.split(" ");
        BigDecimal num1 = new BigDecimal(tokens[0]);
        String operator = tokens[1];
        BigDecimal num2 = new BigDecimal(tokens[2]);

        switch (operator) {
            case "+":
                return num1.add(num2);
            case "-":
                return num1.subtract(num2);
            case "*":
                return num1.multiply(num2);
            case "/":
                return num1.divide(num2, 0, RoundingMode.DOWN);
            default:
                throw new IllegalArgumentException("Unknown operator: " + operator);
        }
    }

    private static String formatResult(BigDecimal result) {
        result = result.stripTrailingZeros();
        return result.scale() <= 0 ? result.toPlainString() : result.toPlainString();
    }
}
