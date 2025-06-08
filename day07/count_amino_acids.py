import sys

# Check for correct usage
if len(sys.argv) != 2:
    print("Input a valid FASTA file")
    sys.exit(1)

filename = sys.argv[1]

# Codon table mapping amino acids to codons
decode = {
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

# Invert to map codon -> amino acid
codon_map = {}
for aa, codons in decode.items():
    for codon in codons:
        codon_map[codon] = aa

# Read FASTA and build full sequence
sequence = ''
with open(filename) as f:
    for line in f:
        if line.startswith('>'):
            continue
        sequence += line.strip().upper()

# Count amino acids
counts = {}
for i in range(0, len(sequence) - 2, 3):
    codon = sequence[i:i+3]
    if codon in codon_map:
        aa = codon_map[codon]
        if aa in counts:
            counts[aa] += 1
        else:
            counts[aa] = 1

# Print results sorted by amino acid name
for aa in sorted(counts):
    print(f"{aa:<5} {counts[aa]}")
