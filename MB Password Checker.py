def check_password(password):
    """Check password against basic CISA standards"""
    common_passwords = [
    # Top most common passwords
    '123456', 'password', '123456789', '12345', '12345678',
    'qwerty', '1234567', '111111', '1234567890', '123123',
    
    # Number sequences
    '1234', '123456a', '123abc', '123321', '123456q',
    '123456789a', '12345678a', '1234567a', '123456qwerty',
    '123456654321',
    
    # Keyboard patterns
    'qwertyuiop', 'asdfghjkl', 'zxcvbnm', '1qaz2wsx', '1q2w3e4r',
    'qazwsx', 'qwerty123', 'qwe123', '1q2w3e', '1q2w3e4r5t',
    
    # Common words/phrases
    'iloveyou', 'admin', 'welcome', 'login', 'passw0rd',
    'master', 'hello', 'sunshine', 'letmein', 'monkey',
    'password1', 'password123', 'welcome1', 'football', 'baseball',
    'dragon', 'superman', 'batman', 'starwars', 'pokemon',
    
    # Simple variations
    'password!', 'password@', 'password#', 'password$', 'password%',
    'password1!', 'password123!', 'qwerty!', 'qwerty123', 'admin123',
    
    # Seasons/years
    'summer', 'winter', 'spring', 'autumn', '2023',
    '2022', '2021', '2020', '2019', '2018',
    
    # Sports related
    'soccer', 'football', 'basketball', 'baseball', 'hockey',
    'tennis', 'golf', 'swimming', 'running', 'cycling',
    
    # Common names
    'michael', 'jennifer', 'thomas', 'jessica', 'daniel',
    'robert', 'sarah', 'david', 'lisa', 'chris',
    
    # Tech terms
    'wifi', 'internet', 'computer', 'google', 'microsoft',
    'apple', 'samsung', 'android', 'iphone', 'windows',
    
    # Animals
    'dragon', 'monkey', 'tiger', 'lion', 'elephant',
    'panda', 'bear', 'dog', 'cat', 'bird',
    
    # Simple patterns
    'aaaaaa', 'abcdef', 'abc123', 'aaa111', 'a1b2c3',
    'aaabbb', 'abcd1234', 'test123', 'pass123', 'adminadmin'
]
    common_passwords = [
        'password', '123456', '123456789', 'qwerty', 'abc123',
        'letmein', 'admin', 'welcome', 'football', 'monkey',
        'password1', '12345678', '123123', '111111', 'sunshine'
    ]
    
    special_chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    
    issues = []
    
    # Check minimum length (15 characters)
    if len(password) < 15:
        issues.append("Must be at least 15 characters")
    
    # Check for at least 1 special character
    if not any(char in special_chars for char in password):
        issues.append("Must contain at least 1 special character (!@#$%^&* etc.)")
    
    # Check against common passwords
    if password.lower() in common_passwords:
        issues.append("Password is too common")
    
    # Check for simple patterns
    if password.isnumeric():
        issues.append("Contains only numbers")
    elif password.isalpha():
        issues.append("Contains only letters")
    
    # Check for repeated characters
    if any(c * 4 in password for c in password):
        issues.append("Has repeating character patterns")
    
    # Check for sequential patterns (123, abc, etc.)
    sequences = ['123', '234', '345', '456', '567', '678', '789',
                'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi']
    if any(seq in password.lower() for seq in sequences):
        issues.append("Contains sequential patterns")
    
    return issues

def main():
    print("\nPassword Checker (Basic CISA Standards)")
    print("--------------------------------------")
    print("Requirements:")
    print("- Minimum 15 characters")
    print("- At least 1 special character")
    print("- Not a common password")
    print("- No simple patterns\n")
    
    while True:
        password = input("\nEnter password to check (or 'quit' to exit): ").strip()
        
        if password.lower() == 'quit':
            break
            
        issues = check_password(password)
        
        if not issues:
            print("\n✅ STRONG PASSWORD - Meets all basic CISA standards")
        else:
            print("\n❌ WEAK PASSWORD - Issues found:")
            for issue in issues:
                print(f"• {issue}")
            
            print("\nRecommendations:")
            print("- Use a passphrase with 15+ characters")
            print("- Include special characters (e.g., ! @ # $)")
            print("- Avoid common words and sequential patterns")
            print("- Example: 'PurpleTurtleJumps@42'")

if __name__ == "__main__":
    main()
