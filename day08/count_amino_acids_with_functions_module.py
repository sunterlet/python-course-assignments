import sys
from amino_utils import codon_table, build_codon_map, read_sequence, count_amino_acids, print_counts

# Check usage
if len(sys.argv) != 2:
    print("Usage: python count_amino_acids.py <fasta_file>")
    sys.exit(1)

# Get filename and process sequence
filename = sys.argv[1]

codon_map = build_codon_map(codon_table)
sequence = read_sequence(filename)
counts = count_amino_acids(sequence, codon_map)
print_counts(counts)
