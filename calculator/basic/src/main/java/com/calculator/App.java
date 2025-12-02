package com.calculator;

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
        scene = new Scene(loadFXML("primary"), 300, 390);
        scene.getStylesheets().add(
            getClass().getResource("/com/calculator/style.css").toExternalForm()
        );
        stage.setScene(scene);
        windowSettings(stage, false);
        stage.show();
    }

    public static void windowSettings(Stage stage, boolean fixed){
        if (fixed) {
            stage.setResizable(false);
        } else {
            stage.setMinWidth(300);
            stage.setMaxWidth(600);
            stage.setMinHeight(390);
            stage.setMaxHeight(390);
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