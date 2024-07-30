class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        ##Farklı bir dosyaya bunu koyarsam şu kodları yazarak çağırmam gerek;


from dosyaadi import Question
^ ^ ^ ^
sorular = ["ilki: ", "ikincisi: ", "üçüncüsü:", "dördüncüsü: "]
cevaplar = [
    Sinifim(sorular[0], "a"),
    Sinifim(sorular[1], "b"),
    Sinifim(sorular[2], "c"),
    Sinifim(sorular[3], "d")
]


def run(cevaplar):
    skor = 0
    for a in cevaplar:
        secim = input(a.prompt)  ##a.prompt dememin sebebi her bir elemente a dememden. Her bir soru a.
        if secim.lower() == a.answer:  ### a objecti
            skor += 1
    print(str(len(sorular)) + " sorudan " + str(skor) + " soruyu bildiniz!")


run(cevaplar)

^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ Hazır ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 333


##Öncelikle farklı bir dosyaya "Questions" adında bir class oluşturdum;
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def __str__(self):
        return (str(self.prompt) + str(self.answer))


##Sonra kendi dosyama bunları ekledim;
from Questions import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n ",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow \n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def runtest(questions):
    score = 0
    for question1 in questions:
        answer = input(question1.prompt)
        if answer == question1.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


runtest(questions)
print(questions[0], questions[1], questions[2], questions[3])
