dna_to_rna_transcription = {'G':'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def to_rna(dna_strand):
    rna_strand = ''
    for nucleotide in dna_strand:
        rna_strand += dna_to_rna_transcription[nucleotide]
    return rna_strand
