# Questions section
Explain the design pattern used in following:
```
interface Vehicle {
  int set_num_of_wheels()
  int set_num_of_passengers()
  boolean has_gas()
}
```
a) Explain how can you use the pattern to create car and plane class?
b) Use a different design pattern for this solution.

## My Assumption
Design Patterns are used to solve some common problems in Object Oriented Software design.
For the above example, I am assuming we are going to solve the following two problems
  b) Though we are going to create vehicle, we may find that there are some behaviours that do not exist on both instance. For example Plane can fly but car can't. If we implte fly() method on parent class and override on chieldclass it will not be possible to change this behavior dynamically (It will not possible to change car to flying car). For this kind of issue we can create Strategy desing pattern with composition to add appropriate behaviour for particular instance.
  
  b) We need to create a very complex object with many parameters. 
    So we are going to constructs complex objects using step-by-step approach using builder patter
  
  
  ## Psudocode for Stategy pattern
  ```code
  public class Vehicle {
    private int numberOfPassenger;
    private int numberOfWheels;
    private double speed;
	
    // Instead of using an interface in a traditional way
    // we use an instance variable that is a subclass
    // of the Flys interface.
    
    // Vehicle doesn't care what flyingType does, it just
    // knows the behavior is available to its subclasses
    
    // This is known as Composition : Instead of inheriting
    // an ability through inheritance the class is composed
    // with Objects with the right ability
    
    // Composition allows you to change the capabilities of 
    // objects at run time!
    
    public Flys flyingType;
    
    public void setNumOfWheels(int numOfWheels){ this.numberOfWheels = numOfWheels; }
    public void setNumOfPassengers(int numOfPassengers){ this.numOfPassengers = numOfPassengers; }
    public void setSpeed(int speed){ this.speed = speed; }
    
    public int getNumOfWheels(int numOfWheels){ this.numberOfWheels = numOfWheels; }
    public int getNumOfPassengers(int numOfPassengers){ this.numOfPassengers = numOfPassengers; }
    public double getSpeed(){ return this.speed; }

    // Vehicle pushes off the responsibility for flying to flyingType
    public String tryToFly(){
      return flyingType.fly();
    }
    
    // we can create setter method for changing fly behaviour dynamically
    public void setFlyingAbility(Flys newFlyType){
      this.flyingType = newFlyType;
    }
	
}

// implementation of Car
public class Car extends Vehicle{
	public Car(){
		super();
		setNumOfWheels(4);
		setNumOfPassengers(5);
    setSpeed(150);

		// We set the Flys interface polymorphically
		// This sets the behavior as a non-flying Vehicle
		flyingType = new CantFly();
	}
}

// implementation of Plane
public class Plane extends Vehicle{
	public Plane(){
		super();
		setNumOfWheels(3);
		setNumOfPassengers(50);
    setSpeed(322);

		// We set the Flys interface polymorphically
		// This sets the behavior as a flying Vehicle
		flyingType = new Flys();
	}
}

public interface Flys {
   String fly();
}

// Class used if the Vehicle can fly
class ItFlys implements Flys{
	public String fly() {
		return "Flying High";
	}
}

//Class used if the Vehicle can't fly
class CantFly implements Flys{
	public String fly() {
		return "I can't fly";
	}
}
```

## Psudocode for Builder pattern
In the above solution we have create Vehicle with dynamic fly behaviour not we want to simplify complex object cretion using builder pattern. For this solution we are going to use above Car, Plane, Vehicle class
```
public interface Builder {
   Builder withNuberOfPassenger(int n)
   Builder withNumOfWheels(int n)
   Builder withSpeed(float speen)
   Builder withFly(Flys fly)
   Vehicle build()
}

public class CarBuilder implements Builder {
  private int numberOfPassenger;
  private int numberOfWheels;
  private double speed;
  privat Flys flyingType;

  Builder withNuberOfPassenger(int n){
    this.numberOfPassenger = n
    return this
  }

  Builder withNumOfWheels(int n) {
    this.numberOfWheels = n
    return this
  }

  Builder withSpeed(float speed){
    this.speed = speed
    return this
  }

  Builder withFly(Flys fly){
    this.flyingType = fly
    return this
  }

  Vehicle build(){
    // here we can set default value car properties
    car = new Car()
    car.setNumOfWheels(numberOfWheels);
		car.setNumOfPassengers(numberOfPassenger);
    car.setSpeed(speed);
    car.setFlyingAbility(flyingType || new CantFly())
		return car
  }
}

// now we can build car with CarBuilder
Car car = new Carbuilder()
          .withNuberOfPassenger(5)
          .withNumOfWheels(4)
          .withSpeed(200)
          .build()


// similarly we can create PlaneBuilder and use that to create Plane with default values
public class PlaneBuilder implements Builder {
  private int numberOfPassenger;
  private int numberOfWheels;
  private double speed;
  privat Flys flyingType;

  Builder withNuberOfPassenger(int n){
    this.numberOfPassenger = n
    return this
  }

  Builder withNumOfWheels(int n) {
    this.numberOfWheels = n
    return this
  }

  Builder withSpeed(float speed){
    this.speed = speed
    return this
  }

  Builder withFly(Flys fly){
    this.flyingType = fly
    return this
  }

  Vehicle build(){
    // here we can set default value plane properties
    plane = new Plane()
    plane.setNumOfWheels(numberOfWheels);
		plane.setNumOfPassengers(numberOfPassenger);
    plane.setSpeed(speed);
    plane.setFlyingAbility(flyingType || new CanFly())
		return plane
  }
}

// now we can build car with CarBuilder
Plane plane = new Planebuilder()
          .withNuberOfPassenger(5)
          .withNumOfWheels(4)
          .withSpeed(200)
          .withFly(new CanFly())
          .build()
```
 