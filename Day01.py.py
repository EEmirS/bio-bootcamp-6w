#day01.py
#pyhton basics - Bioinformatics Bootcamp
#Lists
# Nucleotides list and loop
nucleotides = ["A", "T", "G", "C"]
print("Nucleotides:", nucleotides)
for n in nucleotides:
    print("Nucleotide:", n)

# Reverse complement function
def reverse_complement(seq):
    complements = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(complements[base] for base in seq[::-1])

dna = "ATGCTAGC"
print("DNA sequence:", dna)
print("Reverse complement:", reverse_complement(dna))

# String slicing
seq = "ATGCTTAGC"
print("Original sequence:", seq)
print("First 3 bases:", seq[:3])
print("Last 3 bases:", seq[-3:])
print("Every second base:", seq[::2])

# Counting nucleotides
def count_bases(seq):
    return {base: seq.count(base) for base in "ATGC"}

print("Base counts:", count_bases(seq))

# GC content
def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    return (g + c) / len(seq) * 100

print("GC content of seq:", gc_content(seq), "%")

# File handling (reading a FASTA file)
file_path = r"C:\biyoinformatik\bio_bootcamp_6w\scripts\Day01.py\Data\Deinococcus radioduransdna.fasta"
with open(file_path, "r") as file:
    file_seq = file.read().strip()

print("Sequence from file:", file_seq)
print("Base counts (file):", count_bases(file_seq))
print("GC content (file):", gc_content(file_seq), "%")
print("Reverse complement (file):", reverse_complement(file_seq))
