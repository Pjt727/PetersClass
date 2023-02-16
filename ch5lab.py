# exercise 4

user_input: str = input("Type out an accronym: ").upper()
arr_words: list[str] = user_input.split()
accronym_abbreviated: str = ""
for word in arr_words:
    accronym_abbreviated += word[0]



print(f"Here is the abbreivation: {accronym_abbreviated}")