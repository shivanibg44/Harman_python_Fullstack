def words(str1):
    word = ""
    words1 = []
    str1 = str1 + " "
    for i in range(0, len(str1)):
        if (str1[i] != ' '):
            word = word + str1[i]
        else:
            words1.append(word)
            word = ""

    small = large = words1[0]

    # Find smallest and largest word in the str1
    for k in range(0, len(words1)):
        if (len(small) > len(words1[k])):
            small = words1[k]
        if (len(large) < len(words1[k])):
            large = words1[k]
    return small, large


str1 = "Hi this is Shivani from Davanagere"
print("STRING IS:", str1)
small, large = words(str1)
print("Smallest word: " + small)
print("Largest word: " + large)