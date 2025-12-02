package com.calculator;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.Button;

public class PrimaryController {

    @FXML
    private Label calculation_output;   // top label (expression)
    @FXML
    private Label total_output;        // bottom label (current value)

    private StringBuilder currentInput = new StringBuilder();
    private double accumulator = 0.0;
    private String pendingOperator = null;
    private boolean startNewNumber = true;

    @FXML
    private void initialize() {
        // set initial display
        total_output.setText("0");
        calculation_output.setText("");
    }

    @FXML
    private void onDigit(javafx.event.ActionEvent event) {
        Button source = (Button) event.getSource();
        String digit = source.getText(); // "0"–"9" or "."

        if (startNewNumber) {
            currentInput.setLength(0);
            startNewNumber = false;
        }

        // only one decimal point
        if (digit.equals(".") && currentInput.toString().contains(".")) {
            return;
        }

        currentInput.append(digit);
        total_output.setText(currentInput.toString());
    }

    @FXML
    private void onOperator(javafx.event.ActionEvent event) {
        Button source = (Button) event.getSource();
        String op = source.getText(); // "+", "-", "*", "/"

        // If this is the first operator press, set accumulator from input
        if (!startNewNumber) {
            double value = parseCurrentInput();
            if (pendingOperator == null) {
                accumulator = value;
            } else {
                accumulator = applyOperation(accumulator, value, pendingOperator);
            }
        }

        pendingOperator = op;
        startNewNumber = true;

        calculation_output.setText(formatNumber(accumulator) + " " + pendingOperator);
        total_output.setText(formatNumber(accumulator));
    }

    @FXML
    private void onEquals() {
        if (pendingOperator == null || startNewNumber) {
            // nothing to do
            return;
        }

        double value = parseCurrentInput();
        double result = applyOperation(accumulator, value, pendingOperator);

        calculation_output.setText(
                formatNumber(accumulator) + " " + pendingOperator + " " + formatNumber(value) + " =");
        total_output.setText(formatNumber(result));

        // prepare for next operation
        accumulator = result;
        currentInput.setLength(0);
        currentInput.append(formatNumber(result));
        pendingOperator = null;
        startNewNumber = true;
    }

    @FXML
    private void onClear() {
        currentInput.setLength(0);
        accumulator = 0.0;
        pendingOperator = null;
        startNewNumber = true;

        calculation_output.setText("");
        total_output.setText("0");
    }

    @FXML
    private void onBackspace() {
        if (startNewNumber) {
            return;
        }
        if (currentInput.length() > 0) {
            currentInput.deleteCharAt(currentInput.length() - 1);
        }
        if (currentInput.length() == 0) {
            total_output.setText("0");
            startNewNumber = true;
        } else {
            total_output.setText(currentInput.toString());
        }
    }

    // Helpers

    private double parseCurrentInput() {
        if (currentInput.length() == 0) {
            return 0.0;
        }
        try {
            return Double.parseDouble(currentInput.toString());
        } catch (NumberFormatException e) {
            return 0.0;
        }
    }

    private double applyOperation(double a, double b, String op) {
    switch (op) {
        case "+": return a + b;
        case "-": return a - b;
        case "*": return a * b;
        case "/": return b == 0 ? 0 : a / b;
        default: return b;
        }
    }

    private String formatNumber(double value) {
        if (value == (long) value) {
            return String.format("%d", (long) value);
        } else {
            return String.valueOf(value);
        }
    }
}
