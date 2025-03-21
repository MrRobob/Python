import random

name = input("Geben Sie einen Namen ein: ")
ort = input("Geben Sie einen Ort ein: ")
vergangenheitsverb = input("Geben Sie ein Vergangenheitsverb ein: ")
berühmte_person = input("Geben Sie eine berühmte Person ein: ")

farben = [input("Geben Sie eine Farbe ein: ") for i in range(2)]
emotion_beschreibungen = [input("Geben Sie eine Emotion/Beschreibung ein: ") for i in range(5)]
kleidungsstücke = [input("Geben Sie ein Kleidungsstück ein: ") for i in range(2)]
accessoires = [input("Geben Sie ein Accessoire ein: ") for i in range(2)]
objekte = [input("Geben Sie ein Objekt ein: ") for i in range(3)]

def random_choice_and_remove(list):
    random_word = random.choice(list)
    list.remove(random_word)
    return random_word

farbe = random_choice_and_remove(farben)
emotion_beschreibung = random_choice_and_remove(emotion_beschreibungen)
kleidungsstück = random_choice_and_remove(kleidungsstücke)
accessoire = random_choice_and_remove(accessoires)
objekt = random_choice_and_remove(objekte)

story = f"Ein trüber, verregneter Tag brach an, als {name}, die/der berüchtigte {emotion_beschreibung} {kleidungsstück} trug, \
beschloss, dass das Leben einfach zu langweilig geworden war. Es war also höchste Zeit für ein Abenteuer. \
Ausgerüstet mit nur einer {accessoire}, machte sich {name} auf den Weg. Die Reise führte sie/ihn schließlich zum unheimlichen {ort}, \
einem geheimen Ort, der bekannt war für seine {emotion_beschreibung} {objekt}. Schon beim Betreten des Ortes schlich sich ein \
seltsames Gefühl der Beklommenheit in {name}'s Bauch - als ob sie/er gerade {vergangenheitsverb} wäre. Mit einem tiefen Atemzug \
und einer Prise Wahnsinn, betrat {name} den tiefsten Teil von {ort}. Plötzlich ertönte ein lautes Geräusch hinter ihr/ihm. \
Sie/er drehte sich um und sah {berühmte_person}, die/der {farbe} {kleidungsstück} und eine {emotion_beschreibung} {accessoire} \
in der Hand hielt und sie/ihn mit einem verschmitzten Lächeln begrüßte. 'Willkommen in meinem Reich!', rief {berühmte_person} \
mit einer theatralischen Geste, 'Ich habe hier auf dich gewartet. Endlich jemand, der versteht, wie {emotion_beschreibung} \
das Leben wirklich sein kann.' Ohne zu zögern, schnappte sich {name} das {objekt} und fügte es stolz ihrer/seiner Sammlung hinzu, \
die bereits seltsame und gruselige Gegenstände wie einen {emotion_beschreibung} {objekt} und einen {farbe} {accessoire} beinhaltete. \
In diesem Moment realisierte {name}, dass dies der Beginn eines noch absurder werdenden Kapitels in ihrem/seinem Leben war. \
Mit einem ironischen Grinsen auf den Lippen und einem Hauch von schwarzem Humor in der Seele, kehrte sie/er zurück in den Nebel \
von {ort} und dachte sich: 'Manchmal muss man einfach mit dem Wahnsinn tanzen.'"

print(story)