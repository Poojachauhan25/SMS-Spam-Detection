# detection/spam_filter.py
SPAM_KEYWORDS = [ "urgent","Congratulations","Winner","You've won","Cash prize","Free money","Jackpot","Lucky draw","Claim your prize", "winner", "free money", "cash prize", "urgent", "click here",
    "verify your account", "limited time", "earn money fast",
    "exclusive offer", "jackpot", "lottery", "claim your prize"]

def is_spam(text):
    text = text.lower()
    return any(keyword in text for keyword in SPAM_KEYWORDS)
