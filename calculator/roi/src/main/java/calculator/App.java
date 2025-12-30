package calculator;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;


public class App extends Application {

    private static Scene scene;

    @Override
    public void start(Stage stage) throws IOException {
        scene = new Scene(loadFXML("DetailedCalc"), 640, 480);
        stage.setTitle("ROI Calculator");
        stage.setScene(scene);
        fixedWindow(stage, true);
        stage.show();
    }

    static void fixedWindow(Stage stage, boolean option) {
        if (option == true) {
            stage.setResizable(false);
        } else {
            stage.setMinWidth(600);
            stage.setMinHeight(400);
            stage.setMaxWidth(800);
            stage.setMaxHeight(400);
        }
    }

    static void setRoot(String fxml) throws IOException {
        scene.setRoot(loadFXML(fxml));
    }

    private static Parent loadFXML(String fxml) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(App.class.getResource(fxml + ".fxml"));
        return fxmlLoader.load();
    }

    public static void main(String[] args) {
        launch();
    }

}