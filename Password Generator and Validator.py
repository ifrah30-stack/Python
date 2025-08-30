# Secure password generator and strength validator
import random
import string
import re

class PasswordManager:
    @staticmethod
    def generate_password(length=12, use_special=True):
        characters = string.ascii_letters + string.digits
        if use_special:
            characters += string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    @staticmethod
    def validate_password(password):
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters long")
        
        # Uppercase check
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        # Lowercase check
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        # Digit check
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        # Special character check
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("Add special characters")
        
        strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"][score]
        
        return {
            'score': score,
            'strength': strength,
            'feedback': feedback
        }

# Usage
pm = PasswordManager()
password = pm.generate_password(16)
validation = pm.validate_password(password)
print(f"Generated: {password}")
print(f"Strength: {validation['strength']}")
print("Feedback:", validation['feedback'])
