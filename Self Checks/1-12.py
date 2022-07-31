import random

def gen_string():
    alphabet = "qwertyuiopasd fghjklzxcvbnm"
    return "".join(random.choices(alphabet, k=28))

def score_string(rand_string):
    score = 0
    sentence = "methinks it is like a weasel"
    correct_idx = []

    for i in range(0, len(sentence)):
        if rand_string[i] == sentence[i]:
            score += 1
            correct_idx.append(i)

    return score, rand_string, correct_idx

best_score = 0
best_str = ""
count = 0
length = 28

while best_score < length:
    if best_score == 0:
        score_list = tuple(score_string(gen_string()))

    else:
        rand_string = gen_string()
        best_str_rand = ""
        for i in range(0, length):
            if i not in score_list[2]:
                best_str_rand += rand_string[i]
            else:
                best_str_rand += best_str[i]

        score_list = tuple(score_string(best_str_rand))

    if score_list[0] > best_score:
        best_score = score_list[0]
        best_str = score_list[1]

    count += 1
    if count % 10 == 0:
        print("Count:", count)
        print("Best string:", best_str)
        print(f"Score: {best_score} / 28")

print(f"The random string generator reached its goal in {count} attempts.")