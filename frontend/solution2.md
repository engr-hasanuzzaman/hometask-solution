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
  a) We need to create a very complex object with many parameters. 
    So we are going to constructs complex objects using step-by-step approach using builder patter
  
  b) Though we are going to create vehicle, we may find that there are some behaviours that do not exist on both instance. For example Plane can fly but car can't. For this kind of issue we can create Strategy desing pattern with composition to add appropriate behaviour for particular instance.


  ## Psudocode for Builder pattern
  ```

  ```

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

        
    /* BAD
    * You don't want to add fly methods to the super class.
    * You need to separate what is different between subclasses
    * and the super class
    * For exmaple. Till now no car can fly so we override fly() method on Car class. If in near future
    * some car can fly and some does not then our implementation will not work in that situation
    public void fly(){
      
      System.out.println("I'm flying");
      
    }
    */
    
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