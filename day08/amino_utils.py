# amino_utils.py: module for amino acid counting utilities

# Codon table mapping amino acids to codons
codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

# Invert the codon table to map each codon to its amino acid

def build_codon_map(table):
    """
    Build and return a dictionary mapping each codon (e.g. 'AUG') to its amino acid name (e.g. 'Met').
    """
    codon_map = {}
    for amino_acid, codons in table.items():
        for codon in codons:
            codon_map[codon] = amino_acid
    return codon_map


def read_sequence(filename):
    """
    Read a FASTA file and return the concatenated sequence as a single string.
    Lines starting with '>' are treated as headers and skipped.
    """
    sequence = ''
    with open(filename) as f:
        for line in f:
            if line.startswith('>'):
                continue
            sequence += line.strip().upper()
    return sequence


def count_amino_acids(sequence, codon_map):
    """
    Count occurrences of amino acids in the sequence using the provided codon_map.
    Returns a dictionary: amino_acid -> count.
    """
    counts = {}
    # Walk through the sequence in steps of 3 bases
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        amino_acid = codon_map.get(codon)
        if amino_acid:
            counts[amino_acid] = counts.get(amino_acid, 0) + 1
    return counts


def print_counts(counts):
    """
    Print the amino acid counts sorted alphabetically by amino acid name.
    """
    for amino_acid in sorted(counts):
        print(f"{amino_acid:<5} {counts[amino_acid]}")
