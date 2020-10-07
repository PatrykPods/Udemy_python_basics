#zadanie 1

initial_capital = 20000
percent = 0.03
max_time_years = 10
x = 0

while x <= max_time_years:
    initial_capital = round(initial_capital + initial_capital * percent,2)
    print(f"account summary: {initial_capital}")
    x+= 1
else:
    print(f"total account summary:{initial_capital}")

#zadanie 2

number = 20730906
x = number
sum = 0
while x > 0:
    digit = x % 10
    sum+= digit
    x = x//10
else:
    print(sum)

#zadanie 3

text = '''United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.'''

words = text.split(' ')
word_length = 6
short_words = 0
long_words = 0
print(words)

for word in words:
    if len(word) > word_length:
        long_words+=1
    else:
        short_words+=1

print(f'long words:{long_words} short words:{short_words}')

#zadanie 4

Fibonacci = [0]
a1 = 0
a2 = 1
a3 = 0

for x in range(0,21):
    a1 = a2
    a2 = a3
    a3 = a1 + a2
    Fibonacci.append(a3)
print(Fibonacci)

#zadanie 5

text = '''Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.'''

words_with_p = []
list_of_words = text.lower().split(' ')

for word in list_of_words:
    if "p" in word:
        words_with_p.append(word)
print(words_with_p)

#zadanie 6

dictionary = {
    'a':'80%-100%',
    'b':'60%-80%',
    'c':'50%-60%',
    'd':'less then 50%'
}

for x in dictionary:
    print(x,'-',dictionary[x])

#zadanie 7

text = '''Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.'''

list_of_words = text.lower().split(' ')
word_dictionary = {}

for word in list_of_words:
    if word in word_dictionary.keys():
        word_dictionary[word] += 1
        continue
    word_dictionary[word] = 1

print(word_dictionary)
