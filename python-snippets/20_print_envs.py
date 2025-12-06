import os

# Print all environment variables
for key, value in os.environ.items():
    print(f"{key}={value}")

# Or filtered (security-focused)
print("\n--- Security-relevant vars ---")
security_vars = ["PATH", "HOME", "USER", "SHELL", "PWD", "API_KEY", "PASSWORD"]
for var in security_vars:
    if var in os.environ:
        print(f"{var}={os.environ[var]}")
