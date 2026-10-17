#!/usr/bin/env python3
"""Simple password strength checker."""
import sys
import re

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters (12+ recommended)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\"::{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    print(f"Strength: {strength[min(score, 5)]}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f"  - {f}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python password_check.py <password>")
        sys.exit(1)
    check_password(sys.argv[1])
