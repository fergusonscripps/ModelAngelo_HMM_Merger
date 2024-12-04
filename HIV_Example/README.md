# HIV Example

This folder contains the maps and data from the original Sequence from Structure paper  
*From structure to sequence: Antibody discovery using cryoEM*  
*Antanasijevic et al.*    
[DOI: 10.1126/sciadv.abk2039](https://doi.org/10.1126/sciadv.abk2039)

# Folder Contents

**pAbC-2** - parent folder - The folder that ModelAngelo analysis was run in  
&nbsp;&nbsp;&nbsp;&nbsp;**Note:** This folder should contain the hmm merging scripts  
  
**output** - ModelAngelo output folder - The folder that contains output.cif and hmm_profiles folder  
  
**hmm_output** - ModelAngelo HMMER output folder - Contains .hhr and .a2m files after running HMMER (due to size constraints results are zipped)
  
**sequencedatabase** - contains the *zipped* .fasta file of antibdodies from *Antanasijevic et al.*
  
# Example Case

In our paper ()  
ModelAngelo provided a fragmented model for the output of pAbC-2  
To see this model please open pAbC-2/output/output.cif in chimeraX  
To run MA yourself you will need to unzip large sequence files included here  
and download the pAb map found at [EMD-23232](https://www.emdataresource.org/EMD-23232)
  
For pAbC-2 you need to merge the following chains together:  
  
**Heavy chain:** BG, and A0  
**Light chain:** Bv ,(2) ,A7 ,f ,BX and BF  
  
Note: that chains are case sensitive.  
  
For the light chain the two in brackets represents 2 unknown amino acids.  
ModelAngelo did build Q between Bv and A7, however, this chain is reversed.  
As such we chose not to use this chain in our paper.  
  
You can see in file aaprobtohmm.py how we merged these hmm files together for the HMMER search.  

