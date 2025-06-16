import sys

# Build codon→amino acid map
def build_codon_map(codon_table):
    codon_map = {}
    for aa, codons in codon_table.items():
        for codon in codons:
            codon_map[codon] = aa
    return codon_map

# Read a FASTA file and return sequence string
def read_sequence(filename):
    sequence = ''
    with open(filename) as f:
        for line in f:
            if line.startswith('>'):
                continue
            sequence += line.strip().upper()
    return sequence

# Count amino acids in sequence using codon map
def count_amino_acids(sequence, codon_map):
    counts = {}
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        aa = codon_map.get(codon)
        if aa:
            counts[aa] = counts.get(aa, 0) + 1
    return counts

# Print counts sorted by amino acid name
def print_counts(counts):
    for aa in sorted(counts):
        print(f"{aa:<5} {counts[aa]}")

# Main script logic
def main():
    if len(sys.argv) != 2:
        print("Input a valid FASTA file")
        sys.exit(1)

    filename = sys.argv[1]

    # Original codon table
    codon_table = {
        'Phe': ['TTT', 'TTC'],
        'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
        'Ile': ['ATT', 'ATC', 'ATA'],
        'Met': ['ATG'],
        'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
        'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
        'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
        'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
        'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
        'Tyr': ['TAT', 'TAC'],
        'His': ['CAT', 'CAC'],
        'Gln': ['CAA', 'CAG'],
        'Asn': ['AAT', 'AAC'],
        'Lys': ['AAA', 'AAG'],
        'Asp': ['GAT', 'GAC'],
        'Glu': ['GAA', 'GAG'],
        'Cys': ['TGT', 'TGC'],
        'Trp': ['TGG'],
        'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
        'STOP': ['TAA', 'TAG', 'TGA']
    }

    codon_map = build_codon_map(codon_table)
    sequence = read_sequence(filename)
    counts = count_amino_acids(sequence, codon_map)
    print_counts(counts)

if __name__ == "__main__":
    main()
