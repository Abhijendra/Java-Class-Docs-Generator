public class Car {

    private int wheels;

    private double price;

    private String color;

    private String model;


    public Car(int wheels, double price, String color, String model) {
        this.wheels = wheels;
        this.price = price;
        this.color = color;
        this.model = model;
    }   

    public Car() {
    }

    public int getWheels() {
        return wheels;
    }

    public void setWheels(int wheels) { 
        this.wheels = wheels;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }       

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    


}