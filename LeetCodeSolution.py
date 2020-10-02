from re import sub
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
newParaWithoutPuntuations = sub("[!?',;.]", ' ', paragraph).lower().split()
newParaWithoutBannedWords = list(
    filter(lambda e: e not in banned, newParaWithoutPuntuations))
print(max(newParaWithoutBannedWords, key=newParaWithoutBannedWords.count))
