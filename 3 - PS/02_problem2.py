letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", "Jude").replace("<|Date|>", "7th February, 2026"))