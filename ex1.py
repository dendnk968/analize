import json
import argparse

import matplotlib.pyplot as plt

# create parser
parser = argparse.ArgumentParser()
 
# add arguments to the parser
parser.add_argument("input_json_file")
parser.add_argument("output_dir")

args = parser.parse_args()
data = []
with open(args.input_json_file) as json_data:
    data = json.load(json_data)


with open(args.output_dir + "/more_then_two_post.txt", "w") as out:
    for it in filter(lambda it: it['count_post'] >= 2, data):
        out.write(it['name'])
        out.write("\n")


with open(args.output_dir + "/max_post.txt", "w") as out:
    out.write(str(max(data, key=lambda it: it['count_post'])['count_post']))


with open(args.output_dir + "/count_with_academic_degry.txt", "w") as out:
    out.write(str(len(list(filter(lambda it: it['academic_degree'] != None, data)))))

with open(args.output_dir + "/academic_degry.txt", "w") as out:
    academic_degree = set(map(lambda it: it['academic_degree'], data))
    academic_degree.remove(None)
    for it in academic_degree:
        out.write(it)
        out.write('\n')


count_publication_to_count_people = dict()

for it in data:
    count_publication_to_count_people[it['count_publication']] = count_publication_to_count_people.get(it['count_publication'], 0) + 1
fig, ax = plt.subplots()
