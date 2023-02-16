# python3
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))
        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack:
                if are_matching(opening_brackets_stack[-1].char, next):
                    opening_brackets_stack.pop()
                else:
                    return i + 1
            else:
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position

    return "Success"


def main():
    text = input()
    print(f"input: {text}")
    if "F" in text :
        for i in range(0,6,1):
            with open(f"test/{i}") as f:
                text = f.read()
                mismatch = find_mismatch(text)
                print(mismatch)
    elif "I" in text:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)

if __name__ == "__main__":
    main()
