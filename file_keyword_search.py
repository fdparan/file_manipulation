from __future__ import print_function

import re
import sys

# Python 3: raw_input => input
if sys.version_info.major == 3:
    raw_input = input


def search(in_file, word):
    with open(in_file) as f:
        print("Searching for '{}' in {}".format(word, in_file))
        print("".join("%d: %s" % (i, l) for i, l in enumerate(f) if re.search(r"\b%s\b" % word, l)))


def replace(in_file, old_word, new_word, line_by_line=False):
    print("Replacing '{}' with '{}' in '{}'".format(old_word, new_word, in_file))

    pattern = r"\b%s\b"

    lst = []

    with open(in_file) as f:
        for i, l in enumerate(f):
            matches = re.search(pattern % old_word, l)
            line = l

            if matches:
                before = l
                line = re.sub(pattern % old_word, new_word, before)

                print("\nline {}:".format(i+1))
                print("<<< {}".format(before.strip("\n")))
                print(">>> {}".format(line).strip("\n"))

                if line_by_line and raw_input("Would you like to replace?: ").lower() != 'y':
                    line = before

            lst.append(line)

    with open(in_file, "w") as f:
        f.writelines(lst)


def copy(from_file, to_file, line_by_line=False):

    out_file = open(to_file, "w")

    try:
        with open(from_file) as in_file:

            for line in in_file:
                print(line.strip("\n"))

                if line_by_line:
                    raw_input()
                out_file.write(line)

    finally:
        out_file.flush()
        out_file.close()

if __name__ == "__main__":
    # script, file_name, keyword = sys.argv
    file_name, keyword = "ars.cfg", "ars912"

    # search(file_name, keyword)
    search(file_name, "yars912")
    # replace(file_name, keyword, "yars912")
    # copy("rsso.cfg", "samp.txt")
