# solar_system_simulation

A solar system simulation built in **Python**, using the **pygame** library for real-time graphics and orbital rendering.

### Features

- Simulates orbital mechanics using Newtonian gravity
- Realistic planetary parameters (mass, velocity, distance)
- Scaled AU distances and 2D visualization
- Draws orbit trails for each planet
- Pause and exit functionality

### Libraries

- `pygame`
- `math`

### Data Source
 
Planetary constants (mass, radius, orbital distance, velocity) were based on data from NASA’s Planetary Fact Sheet:  
[https://nssdc.gsfc.nasa.gov/planetary/factsheet/](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)

### Notes

- Physics based on gravitational force:  
  `F = G × (m₁ × m₂) / r²`
- Uses astronomical units (AU), gravitational constant (G), and a timestep of one simulated day
- A solid exercise in applying physics, logic, and vector math in code

> This is a prototype created for educational purposes and is not fully polished or feature-complete. That said, feel free to use, modify, or build upon this project.
