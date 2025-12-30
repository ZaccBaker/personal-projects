package calculator;

import java.io.IOException;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class QuickController {
    @FXML
    private Button quickButton;

    @FXML
    private void switchToDetailed() throws IOException {
        App.setRoot("DetailedCalc");
    }
}
