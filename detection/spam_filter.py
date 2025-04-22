# detection/spam_filter.py
SPAM_KEYWORDS = spam_keywords = [
    "urgent", "congratulations", "winner", "you've won", "cash prize", "free money", "jackpot", "lucky draw",
    "claim your prize", "click here", "verify your account", "limited time", "earn money fast", "exclusive offer",
    "lottery", "claim", "free gift", "act now", "guaranteed", "risk free", "win big", "special promotion",
    "instant cash", "cheap meds", "no credit check", "100% free", "trial offer", "access now", "earn extra income",
    "save big", "double your income", "you have been selected", "final notice", "this won’t last", "apply now",
    "call now", "credit card required", "winner selected", "only few left", "as seen on", "make money from home",
    "urgent response needed", "money back", "pre-approved", "amazing deal", "unlimited access", "limited offer",
    "order now", "hidden charges", "click to buy", "act immediately", "lowest price ever", "easy loan", "exclusive deal",
    "get rich", "big payout", "fast cash", "lowest rates", "extra income", "buy now", "limited stock", "special reward",
    "zero cost", "don’t miss this", "investment opportunity", "dear user", "you are selected", "great news", "low price"
]


def is_spam(text):
    text = text.lower()
    return any(keyword in text for keyword in SPAM_KEYWORDS)
