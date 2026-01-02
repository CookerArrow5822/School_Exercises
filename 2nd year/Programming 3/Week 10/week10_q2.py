def basic_hash(string):
    total = 0
    for ch in string:
        total += ord(ch)
    return total


def compress(hash_code, buckets):
    return hash_code % len(buckets)


def insert(string, buckets):
    h = basic_hash(string)
    index = compress(h, buckets)
    buckets[index].append(string)

buckets = [[] for _ in range(10)]

insert('stop', buckets)
insert('tops', buckets)
insert('pots', buckets)
insert('spot', buckets)

print(buckets)

#question 3


def insert_single(string, buckets):
    h = basic_hash(string)
    size = len(buckets)

    for i in range(size):
        index = (h + i) % size

        if buckets[index] == []:
            buckets[index].append(string)
            return

    print("No empty bucket found!")

buckets_q3 = [[] for _ in range(10)]

insert_single('stop', buckets_q3)
insert_single('tops', buckets_q3)
insert_single('pots', buckets_q3)
insert_single('spot', buckets_q3)

print(buckets_q3)