# Halite-II-Submission
Bot submission for the Halite-II Challenge in Python

# Observations, Interpretation and Conclusions
We have observed one particular "enemy" bot that was sending some ships flying near the border clockwise. They triggered our own ships. Imagine the situation: One of our own is already chasing it and another friendly ship is more or less orthogonally positioned to it; it gets triggered and persues the ship. Because it will try to reach the current position of the enemy, the angle between our ships will close and one will destroy the other one. We conclude: When you want to intercept a ship don't fly to the current position but anticipate the future position!
