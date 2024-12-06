**Genome Fragmentation and SSR Study**

This project investigates the effects of genome fragmentation and random sequence modifications on genome assembly quality and SSR (Simple Sequence Repeat) identification accuracy. By simulating real-world 	challenges such as sequencing errors and fragmented assemblies, the provided tools empower researchers to explore the robustness of assembly pipelines and SSR analysis workflows.

**Features**
1. Random Sequence Modification
The xInsert.pl script reads a FASTA-formatted input file containing DNA sequences, randomly inserts 'X' characters into each sequence, and writes the modified sequences to an output file.

2. Genome Fragmentation
The nCutter.pl script fragments sequences wherever an 'X' is present. Each fragment is assigned a unique header, representing its position within the original sequence.

3. FASTA File Reformatting Tool
Many tools require single-line FASTA files for processing. This project includes an awk command to efficiently reformat multi-line FASTA files into single-line format for compatibility.


**Usage**

#Prerequisites
Ensure you have the following installed:

-Perl: Required for running the core scripts (xInsert.pl and nCutter.pl).
-Bash: For running the FASTA formatting utility.

##Step-by-Step Workflow
Step 1: Convert Multi-Line FASTA to Single-Line
FASTA files with multi-line sequences must be reformatted before using the scripts. Use the following awk command:
```bash
$ awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);} END {printf("\n");}' < input.fa > single_line.fa
```
Input:
input.fa - Multi-line FASTA file.
Output:
single_line.fa - Reformatted single-line FASTA file.

Step 2: Insert Random 'X' Characters
Run the xInsert.pl script to introduce random 'X' characters into sequences.
```bash
perl scripts/xInsert.pl single_line.fa output_x_inserted.fa num_insertions
```
Input:
single_line.fa - Reformatted single-line FASTA file.
Output:
output_x_inserted.fa - Sequences with random 'X' insertions.
Parameter:
<num_insertions> - Number of 'X' characters to insert per sequence (eg- 10, 15,..)

Step 3: Fragment Sequences
Run the nCutter.pl script to split sequences at each 'X' position.
```bash
perl scripts/nCutter.pl < output_x_inserted.fa > output_fragments.fa  
```
Input:
output_x_inserted.fa - Sequences with inserted 'X'.
Output:
output_fragments.fa - Fragmented sequences with unique headers.
