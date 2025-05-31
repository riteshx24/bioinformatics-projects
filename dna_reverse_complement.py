def reverse_complement(seq):
    complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join(complement.get(base, base) for base in reversed(seq))

print(reverse_complement("ATGC"))
