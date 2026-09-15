#!/usr/bin/env python3
import os

A = float(os.getenv("A", "0"))
B = float(os.getenv("B", "0"))

RESULT = A + B

print("A value is", A)
print("B value is", B)
print(f"Result: {RESULT}")

# Export RESULT for Harness
env_file = os.environ["DRONE_OUTPUT"]

with open(env_file, "a") as f:
    f.write(f"RESULT={RESULT}\n")
