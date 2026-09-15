#!/usr/bin/env python3
import os

A = float(os.getenv("A", "0"))
B = float(os.getenv("B", "0"))

RESULT = A + B

print("A value is", A)
print("B value is", B)
print(f"Result: {RESULT}")

# Export RESULT for Harness - write to DRONE_OUTPUT
env_file = os.getenv("DRONE_OUTPUT")
if env_file:
    with open(env_file, "a") as f:  # Use 'a' (append) instead of 'w'
        f.write(f"RESULT={RESULT}\n")
