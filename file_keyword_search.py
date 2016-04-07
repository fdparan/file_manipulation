from __future__ import print_function

import re
import sys

# Python 3: raw_input => input
if sys.version_info.major == 3:
    raw_input = input


def search(in_file, word):
    with open(in_file) as f:
        for i, l in enumerate(f):
            if re.search(r"\b%s\b" % word, l):
                print("%d: %s" % (i, l))


def replace(in_file, old_word, new_word):

    lst = []

    with open(in_file) as f:
        # lst = [re.sub(r"\b%s\b" % old_word, new_word, l) for l in f]

        for l in f:
            lst.append(re.sub(r"\b%s\b" % old_word, new_word, l))

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
    file_name, keyword = "rsso.cfg", "foo"
else:
    script, file_name, keyword = sys.argv

# search(file_name, "yars912")
# replace(file_name, keyword, "Config")
# search(file_name, "yars912")

copy("rsso.cfg", "samp.txt")
