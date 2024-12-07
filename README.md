# SSR_fragmentation_accuracy

This project demonstrates genome fragmentation and the insertion of random characters into DNA sequences to analyze the impact of genome quality on SSR identification.

---

## Features

### 1. **Random Sequence Modification**
The `xInsert.pl` script reads a FASTA-formatted input file containing DNA sequences, randomly inserts 'X' characters into each sequence, and writes the modified sequences to an output file.

### 2. **Genome Fragmentation**
The `xCutter.pl` script fragments sequences wherever an 'X' is present. Each fragment is assigned a unique header, representing its position within the original sequence.

### 3. **FASTA File Reformatting Tool**
Many tools require single-line FASTA files for processing. This project includes an awk command to efficiently reformat multi-line FASTA files into single-line format for compatibility.

### 4. **Microsatellite Identification Using PERF**
The `PERF` tool is used to identify microsatellites from the test genome and fragmented genome and evaluate SSR detection accuracy.

---

## Prerequisites

Ensure you have the following installed:

- **Perl:** Required for running the core scripts (`xInsert.pl` and `xCutter.pl`).  
- **Bash:** For running the FASTA formatting utility.
- **QUAST:** For genome assembly quality assessment.
- **PERF:** For microsatellite detection.

---

## Step-by-Step Workflow

### **Step 1: Convert Multi-Line FASTA to Single-Line**
FASTA files with multi-line sequences must be reformatted before using the scripts. Use the following awk command:
```bash
$ awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);} END {printf("\n");}' < input.fa > single_line.fa
```
- Input: `input.fa` - Multi-line FASTA file.
- Output: `single_line.fa` - Reformatted single-line FASTA file.

### **Step 2: Insert Random 'X' Characters**
Run the  `xInsert.pl ` script to introduce random 'X' characters into sequences.
```bash
perl scripts/xInsert.pl single_line.fa output_x_inserted.fa num_insertions
```
- Input: `single_line.fa` - Reformatted single-line FASTA file.
- Output: `output_x_inserted.fa` - Sequences with random 'X' insertions.
- Parameter: `num_insertions` - Number of 'X' characters to insert per sequence (eg- 10, 15, 100)

### **Step 3: Fragment Sequences**
Run the  `xCutter.pl ` script to split sequences at each 'X' position.
```bash
perl scripts/nCutter.pl < output_x_inserted.fa > output_fragments.fa  
```
- Input: `output_x_inserted.fa` - Sequences with inserted 'X'.
- Output: `output_fragments.fa` - Fragmented sequences with unique headers.

### **Step 4: Identify Microsatellites Using PERF**
Run the `PERF` tool to identify microsatellites in the sequences.
```bash
PERF -i input.fasta -o perf_ssr.tsv -a -u repeat_units.txt
```
- Input: `input.fasta`- a valid FASTA file
- Output: `perf_ssr.tsv`- Detected microsatellites and related statistics
- Additional Input: `repeat_units.txt`- A file specifying the minimum number of repeat motifs required for a sequence to be identified as SSR by PERF.
```bash
1	  10
2	  6
3	  4
4	  3
5	  2
6	  2 
```
Options:
- `-a`: Generate a summary HTML report
- `-u`: Specifies the file containing minimum number of repeat units to search for.

---
