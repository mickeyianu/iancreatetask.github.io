questions = [
{
"question": "In the Davy Back Fight against Foxy, which
unstated but consistently exploited loophole most accurately explains
how match integrity is undermined despite the presence of an official
referee?",
"options": [
"\tA. The referee's authority is absolute, even when
contradicting written rules",
"\tB. The rules rely entirely on mutual enforcement
between crews rather than an external system",
"\tC. Penalties cannot be applied retroactively once a
round concludes",
"\tD. The definition of 'combatant' is flexible, allowing
non-participants to influence outcomes"
],
"answer": "B"
},
{
"question": "What is the most structurally significant reason
Iceburg entrusted the Pluton blueprints to Franky (Cutty Flam),
rather than preserving them within Galley-La Company?",
"options": [
"\tA. Franky's outlaw status reduced the likelihood of
World Government scrutiny",
"\tB. The blueprints were meant to exist outside formal
institutions to prevent systemic corruption",
"\tC. Iceburg anticipated CP9 infiltration specifically
within Galley-La's hierarchy",
"\tD. Franky alone possessed the technical creativity to
reinterpret the weapon if necessary"
],
"answer": "B"
},
{
"question": "What is the least explicitly stated but
logically necessary condition that allows the Straw Hats to
successfully escape Enies Lobby after activating the Buster Call?",
"options": [
"\tA. The fragmentation of Marine command structure
during the Call",
"\tB. The pre-existing damage to Enies Lobby's main
bridge system",
"\tC. The timing mismatch between judicial protocol and
military response",
"\tD. The unintended consequences of the Gates of Justice
being opened simultaneously"
],
"answer": "D"
},
{
"question": "Following Enies Lobby, what deep narrative
inversion is embodied in the interaction between Monkey D. Garp and
Monkey D. Luffy?",
"options": [
"\tA. Justice is portrayed as subordinate to familial
bonds",
"\tB. Authority figures acknowledge but do not suppress
rebellion",
"\tC. The Marine hero figure openly tolerates the very
piracy he opposes",
"\tD. Institutional power is shown to be incapable of
enforcing personal morality"
],
"answer": "C"
}
]
def quiz(questions):
# Track of score and question number
score = 0
question_number = 1
# Asks each question
for qa in questions:
print("\nQuestion " + str(question_number) + ": " +
qa["question"])
# Display option to quiz takers
for option in qa["options"]:
print(option)
answer = input("Answer [A/B/C/D]: ").strip().upper()
# Output based on quiz taker's answer
if answer == qa["answer"]:
print("Correct!")
score = score + 1
else:
print("Wrong! The correct answer was " + qa["answer"] +
".")
question_number = question_number + 1
print("\nQuiz over! Your final score is " + str(score) + "/" +
str(len(questions)) + ".")
print("One Piece Quiz\n")
quiz(questions)  