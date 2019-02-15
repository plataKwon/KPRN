import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_dir', required=True)
parser.add_argument('-v', '--vocab_dir', required=True)

args = parser.parse_args()
input_dir = args.input_dir
vocab_dir = args.vocab_dir

def getNumber(str, song_min, song_max, user_min, user_max, relation_min, relation_max, person_min, person_max) :
    num = int(str[1:])
    if str[0] == 's' :
        if song_min > num :
            song_min = num
        if song_max < num :
            song_max = num
    elif str[0] == 'u' :
        if user_min > num :
            user_min = num
        if user_max < num :
            user_max = num
    elif str[0] == 'r' :
        if relation_min > num :
            relation_min = num
        if relation_max < num :
            relation_max = num
    elif str[0] == 'p' :
        if person_min > num :
            person_min = num
        if person_max < num :
            person_max = num
    return song_min, song_max, user_min, user_max, relation_min, relation_max, person_min, person_max

train_files = ['/positive_matrix.tsv.translated', '/negative_matrix.tsv.translated', '/test_matrix.tsv.translated']
song_min = 100000000
song_max = 0
user_min = 100000000
user_max = 0
relation_min = 100000000
relation_max = 0
person_min = 100000000
person_max = 0
for counter, input_file in enumerate(train_files):
    input_file = input_dir+input_file
    with open(input_file) as f:
        for entity_count, line in enumerate(f):  # each entity pair
            split = line.split('\t')
            e1 = split[0].strip()
            song_min, song_max, user_min, user_max, relation_min, relation_max, person_min, person_max = getNumber(e1, song_min, song_max, user_min, user_max, relation_min, relation_max, person_min, person_max)
            e2 = split[1].strip()
            song_min, song_max, user_min, user_max, relation_min, relation_max, person_min, person_max = getNumber(e2, song_min, song_max, user_min, user_max, relation_min, relation_max, person_min, person_max)
            paths = split[2].strip()
            split = paths.split('###')
            for path in split:
                path_each = path.split('-')
                for each in path_each :
                    song_min, song_max, user_min, user_max, relation_min, relation_max, person_min, person_max = getNumber(each, song_min, song_max, user_min, user_max, relation_min, relation_max, person_min, person_max)

print(song_min, song_max, user_min, user_max, relation_min, relation_max, person_min, person_max)

all_entity_id_output_file = vocab_dir+"/all_entity_id.txt"
entity_to_type_output_file = vocab_dir+"/entity_to_type.txt"
all_relation_id_output_file = vocab_dir+"/all_relation_id.txt"

open(all_entity_id_output_file, 'w')
open(entity_to_type_output_file, 'w')
open(all_relation_id_output_file, 'w')


################################################################################
######################################song######################################
################################################################################
for idx in range(song_min, song_max + 1) :
    entity_line = 's' + str(idx)

    all_entity_id = entity_line + '\t' + str(idx)
    all_entity_id = all_entity_id.strip()
    entity_to_type = entity_line + '\t' + 'song'
    entity_to_type = entity_to_type.strip()

    with open(all_entity_id_output_file, 'a') as out:
        out.write(all_entity_id+'\n')
    with open(entity_to_type_output_file, 'a') as eout :
        eout.write(entity_to_type+'\n')

################################################################################
######################################user######################################
################################################################################
for idx in range(user_min, user_max + 1) :
    entity_line = 'u' + str(idx)

    all_entity_id = entity_line + '\t' + str(idx)
    all_entity_id = all_entity_id.strip()
    entity_to_type = entity_line + '\t' + 'user'
    entity_to_type = entity_to_type.strip()

    all_entity_id_output_file = vocab_dir+"/all_entity_id.txt"
    entity_to_type_output_file = vocab_dir+"/entity_to_type.txt"

    with open(all_entity_id_output_file, 'a') as out:
        out.write(all_entity_id+'\n')
    with open(entity_to_type_output_file, 'a') as eout :
        eout.write(entity_to_type+'\n')

################################################################################
#####################################person#####################################
################################################################################
for idx in range(person_min, person_max + 1) :
    entity_line = 'p' + str(idx)

    all_entity_id = entity_line + '\t' + str(idx)
    all_entity_id = all_entity_id.strip()
    entity_to_type = entity_line + '\t' + 'person'
    entity_to_type = entity_to_type.strip()

    all_entity_id_output_file = vocab_dir+"/all_entity_id.txt"
    entity_to_type_output_file = vocab_dir+"/entity_to_type.txt"

    with open(all_entity_id_output_file, 'a') as out:
        out.write(all_entity_id+'\n')
    with open(entity_to_type_output_file, 'a') as eout :
        eout.write(entity_to_type+'\n')

################################################################################
####################################relation####################################
################################################################################
for idx in range(relation_min, relation_max + 1) :
    entity_line = 'r' + str(idx) + '\t' + str(idx - 1)
    entity_line = entity_line.strip()

    with open(all_relation_id_output_file, 'a') as out:
        out.write(entity_line+'\n')

with open(all_relation_id_output_file, 'a') as out:
    out.write('#UNK_RELATION\t6\n#PAD_TOKEN\t7\n#END_RELATION\t8\n')
################################################################################
print("END")
