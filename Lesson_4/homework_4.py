adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

paragraph_space = adventures_of_tom_sawer.replace("\n", " ")
print("Результат заміни:", paragraph_space)

# task 02 ==
""" Замініть .... на пробіл
"""
dots_space = adventures_of_tom_sawer.replace("....", " ")
print("Результат заміни точок:", dots_space)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
spaces = dots_space.split()
result = " ".join(spaces)

print("No more than one space:", result)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
counting_h = adventures_of_tom_sawer.count("h")

print ("Кількість літер h:", counting_h)
# task 05

""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
splitting_words = adventures_of_tom_sawer.split()
count = sum(
    1 for w in splitting_words if w.lstrip('"(')[0].isupper()
)
print ("Cкільки слів у тексті починається з Великої літери: ", count)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_word = adventures_of_tom_sawer.find("Tom")
second_word = adventures_of_tom_sawer.find("Tom", first_word + 1)
print("Позиція на якій слово Tom зустрічається вдруге: ", second_word)

# task 07
""" Розділіть змінну adventures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawer_sentences
"""
clean_text = adventures_of_tom_sawer.replace("....", "")

clean_text = clean_text.replace("\n", " ")

clean_text = " ".join(clean_text.split())

clean_text = clean_text.replace(".", "|").replace(";", "|")

raw_sentences = clean_text.split("|")

adventures_of_tom_sawer_sentences = list(filter(None, (s.strip() for s in raw_sentences)))

print(adventures_of_tom_sawer_sentences)
print("Кількість речень:", len(adventures_of_tom_sawer_sentences))



# task 08
""" Виведіть четверте речення з adventures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adventures_of_tom_sawer_sentences[3]
print("Четверте речення з нижнім регістром: ", fourth_sentence.lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

started_with = " ".join(adventures_of_tom_sawer_sentences)
print("By the time" in started_with)


# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawer_sentences.
"""
words_counting = len(adventures_of_tom_sawer_sentences[-1].split())
print("Кількість слів останнього речення: ", words_counting)