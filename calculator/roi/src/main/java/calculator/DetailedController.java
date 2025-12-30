package calculator;

import java.io.IOException;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class DetailedController {
    @FXML
    private Button detailedButton;

    @FXML
    private void switchToQuick() throws IOException {
        App.setRoot("QuickCalc");
    }
}
