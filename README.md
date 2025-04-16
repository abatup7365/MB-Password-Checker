markdown
# 🔐 MB Password Checker  

Hey there! I'm Marcel, a Cybersecurity student passionate about cybersecurity. This simple but powerful tool helps you create stronger passwords based on CISA and good practiv=ce standards.

 What It Does  
- Checks if your password is **15+ characters** (as recommended by CISA)  
- Requires **1+ special character** (!@# etc.)  
- Blocks **100+ common passwords** (like "123456" or "password")  
- Detects **weak patterns** (repeating/sequential characters)  

 How to Use  
1. Clone the repo:  
   bash  
   git clone https://github.com/yourusername/MB-Password-Checker.git  
     
2. Run it:  
   bash  
   python MB_Password_Checker.py  
     
3. Type a password - it'll give instant feedback!  

  Why I Built This  
After learning about the **80% of hacking-related breaches** caused by weak passwords (Verizon DBIR), I wanted to create a tool that makes security *accessible*. Perfect for:  
- Students learning Python  
- Developers validating user passwords  
- Anyone who wants to stay safe online  

 Quick Example  
```  
Enter password: hello123  
❌ Weak! Issues:  
• Too short (need 15+ chars)  
• No special character  
• Common password  
```  

 Tech Used  
- Pure Python (no dependencies!)  
- Regex for pattern detection  
- CISA/NIST guidelines  

---
🔒 **Pro Tip**: Pair this with a password manager!  

Let me know if you'd like any tweaks!
