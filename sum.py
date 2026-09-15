#!/usr/bin/env python3
import os

# Read inputs from environment variables
A = float(os.getenv("A", "0"))
B = float(os.getenv("B", "0"))

# Perform calculation
RESULT = A + B

# Print values for logs
print("A value is", A)
print("B value is", B)
print(f"Result: {RESULT}")

# Export RESULT for Harness
# Write RESULT into Harness output file
with open(os.getenv("DRONE_OUTPUT", "/tmp/output"), "w") as f:
    f.write(f"RESULT={RESULT}")
