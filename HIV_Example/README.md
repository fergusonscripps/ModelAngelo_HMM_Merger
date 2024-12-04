# HIV Example

This folder contains the maps and data from the original Sequence from Structure paper  
*Antanasijevic et al.*  
*From structure to sequence: Antibody discovery using cryoEM*  
[DOI: 10.1126/sciadv.abk2039](https://doi.org/10.1126/sciadv.abk2039)

# Folder Contents

pAbC-1 - parent folder - The folder that ModelAngelo analysis was run in  
Note: This folder should contain the hmmmerging scripts

output - ModelAngelo output folder - The folder that contains output.cif and hmm_profiles folder  

hmm_output - ModelAngelo HMMER output folder - Contains .hhr and .a2m files after running HMMER

sequencedatabase - contains the .fasta file of antibdodies from *Antanasijevic et al.*

# Example Case

In our paper ()
ModelAngelo provided a fragmented model for the output of pAbC-2  
To see this model please open pAbC-2/output/output.cif  
Here you will see that you need to merger the following chains together:  
Heavy chain: BG, and A0  
Light chain: Bv ,(2) ,A7 ,f ,BX and BF  
  
Note that chains are case sensitive.  
For the light chain the two in brackets represents 2 unknown amino acids.  
ModelAngelo did build Q between Bv and A7, however, this chain is reversed.  
As such we chose not to use this chain in our paper.  

You can see in file aaprobtohmm.py how we merge these hmm files together.

