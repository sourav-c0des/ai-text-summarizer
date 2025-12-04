print("test file started running")

from app.summarizer import summarize_text

print("import done, calling summarize_text()")

long_text = """
The global shift toward artificial intelligence is accelerating faster than expected.
Many industries—from healthcare to finance—are integrating AI to automate tasks, 
analyze massive datasets, and optimize operations. Hospitals now use AI to detect 
diseases earlier, while investment firms rely on machine-learning models to 
predict stock trends more accurately.

However, this rapid adoption also comes with challenges. Experts worry about data 
privacy, algorithmic bias, and the future of human jobs. Governments worldwide are 
rushing to create regulatory frameworks to ensure that AI technologies are used 
responsibly. Some fear that without proper oversight, AI could deepen inequalities 
or lead to unintended consequences.

Despite these concerns, innovation continues. AI is expected to become a core driver 
of economic growth, potentially adding trillions to the global economy over the 
next decade. Companies that adapt early are likely to gain a competitive advantage, 
while those that resist may fall behind.
"""

summary = summarize_text(long_text, max_length=60, min_length=20)

print("Original text:\n", long_text)
print("\nSummary:\n", summary)
