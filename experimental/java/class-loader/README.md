# Simple Java ClassLoader Project

This project is a hands-on laboratory for exploring how **Java ClassLoaders** work. It demonstrates dynamic class loading by allowing the user to switch between different versions of a class at runtime without recompiling the main application.

## Purpose

The main goal is to understand:
1. How to use `URLClassLoader` to load classes from specific filesystem locations.
2. How to implement an interface (`ColourGenerator`) and load different implementations dynamically.
3. How class visibility and `ProtectionDomain` work in Java.

## Project Structure

- `Test.java`: The main entry point that uses a custom `URLClassLoader`.
- `ColourGenerator.java`: The interface defining the contract.
- `module/colour/v1/`: Contains the standard implementation of `RedColourGenerator`.
- `module/colour/v2/`: Contains an alternative implementation with a different string prefix.

## Usage Guide

### 1. Compilation
The project is already compiled into `Test.jar`. To recompile everything manually:
```bash
javac ColourGenerator.java Test.java
javac -cp . module/colour/v1/RedColourGenerator.java
javac -cp . module/colour/v2/RedColourGenerator.java
jar cfe Test.jar Test Test.class ColourGenerator.class
```

### 2. Execution
Run the JAR file and pass either `v1` or `v2` as a command-line argument to load the respective version:

**To load Version 1:**
```bash
java -jar Test.jar v1
```
*Output: Shows the class name, its filesystem location, and "red".*

**To load Version 2:**
```bash
java -jar Test.jar v2
```
*Output: Shows the class name, its filesystem location, and "My clour is: red".*

**Invalid Version:**
```bash
java -jar Test.jar v3
# Output: Can't find a version: v3
```
