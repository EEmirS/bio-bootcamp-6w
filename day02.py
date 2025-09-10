#Function to read a FASTA file
def read_fasta(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()                 # Read all lines from the file into a list
        header = lines[0].strip()             # The first line is the FASTA header (starts with '>')
        sequence = "".join(line.strip() for line in lines[1:])  # Combine the remaining lines into a single DNA string
    return header, sequence                    # Return the header and sequence


#File path and reading the FASTA
file_path = r"C:\biyoinformatik\bio_bootcamp_6w\data\Day02\DeinococcusradioduransR1chromosome 1.fasta"
header, sequence = read_fasta(file_path)


#Print FASTA information
print("Header:", header)
print("Sequence length:", len(sequence))
print("First 100 bases:", sequence[:100])

#Function to count bases
def count_bases(sequence):
    return {base: sequence.count(base) for base in "ATGC"}


#Function to calculate GC content
def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    return (g + c) / len(seq) * 100


#Main script to print information

if __name__ == "__main__":
    header, seq = read_fasta(file_path)

    print("Header:", header)
    print("Length:", len(seq))
    print("Base counts:", count_bases(seq))
    print("GC content:", round(gc_content(seq), 2), "%")

#Writing results to a file (Windows compatible)
report_path = r"C:\biyoinformatik\bio_bootcamp_6w\reports\day02_results.txt"
with open(report_path, "w") as out:
    out.write(f"Header: {header}\n")
    out.write(f"Length: {len(seq)}\n")
    out.write(f"Base counts: {count_bases(seq)}\n")
    out.write(f"GC content: {round(gc_content(seq), 2)}%\n")
