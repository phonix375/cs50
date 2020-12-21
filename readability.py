import cs50

text = cs50.get_string("Text :")
words = text.count(" ") + 1
latters = len(''.join(i for i in text if i.isalpha()))
sentance = text.count(".")+ text.count("!")+text.count("?")
grade = (0.0588 * (latters / words * 100)) - (0.296 * (sentance / words) * 100) - 15.8
if grade < 1 :
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print("Grade " + str(round(grade)))