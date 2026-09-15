#!/usr/bin/env python3
import os

A = float(os.getenv("A", "0"))
B = float(os.getenv("B", "0"))

result = A + B
print("A value is", A)
print("B value is", B)
print(f"Result: {result}")

# Export result for Harness
env_file = os.getenv("DRONE_OUTPUT")
if env_file:
    with open(env_file, "a") as f:
        f.write(f"RESULT={result}\n")
