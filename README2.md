# **Polymorphism in Python: Animals & Vehicles Movement** 🚗✈️🐕  

## **Description**  
This Python program demonstrates **polymorphism** by defining a `move()` method in different classes. The method behaves differently for **animals** and **vehicles**, showcasing **dynamic method overriding**.  

## **Features**  
✅ **Polymorphism** → Same method `move()` works differently in each subclass  
✅ **Encapsulation** → Uses base classes (`Animal` & `Vehicle`) for a common interface  
✅ **Code Reusability** → Easily extendable to add more animal or vehicle types  

## **How It Works**  
1. **Defines a base class** (`Animal` & `Vehicle`) with a `move()` method.  
2. **Subclasses override** `move()` with their own behavior (e.g., `Dog.move()` → "Running 🐕", `Plane.move()` → "Flying ✈️").  
3. **Objects are stored in a list** and dynamically call `move()` for polymorphic behavior.  

## **Example Output**  
```
Dog: Running 🐕
Bird: Flying 🐦
Car: Driving 🚗
Plane: Flying ✈️
```

## **Usage**  
1. Save the script as `polymorphism.py`.  
2. Run the script using:  
   ```sh
   python polymorphism.py
   ```
3. Observe how different objects respond to `move()`.  
