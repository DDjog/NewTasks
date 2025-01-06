import enchant

try:
    d = enchant.Dict("pl_PL")
    print("Spellchecking works:", d.check("test"))  # Powinno zwrócić True lub False
except Exception as e:
    print("Error:", e)

