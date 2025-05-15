# HIV Example pAbC-2 Using ModelAngelo v1.0.1

This folder contains the maps and data from the original Sequence from Structure paper  
*From structure to sequence: Antibody discovery using cryoEM*  
*Antanasijevic et al.*    
[DOI: 10.1126/sciadv.abk2039](https://doi.org/10.1126/sciadv.abk2039)

# Folder Breakdown

**pAbC-2** - parent folder - The folder that ModelAngelo analysis was run in  
&nbsp;&nbsp;&nbsp;&nbsp;**Note:** This folder should contain the hmm merging scripts  
  
**output** - ModelAngelo output folder - The folder that contains output.cif and hmm_profiles folder  
  
**hmm_output** - ModelAngelo HMMER output folder - Contains .hhr and .a2m files after running HMMER (due to size constraints results are zipped)
  
**sequencedatabase** - contains the *zipped* .fasta file of antibdodies from *Antanasijevic et al.*
  
# Fragements Merged for pAbC-2 

In our [Modelangelo SFS method paper](https://www.biorxiv.org/content/10.1101/2024.12.06.627063v1)  
ModelAngelo provided a fragmented model for the output of pAbC-2  
To see this model open pAbC-2/output/output.cif in chimeraX  
To run MA unzip large sequence files included in **sequencedatabase**
and download the pAb map found at [EMD-23232](https://www.emdataresource.org/EMD-23232)
  
For pAbC-2 you need to merge the following chains together:  
  
**Heavy chain:** BG, and A0  
**Light chain:** Bv ,(2) ,A7 ,f ,BX and BF  
  
Note: that chains are case sensitive.  
  
For the light chain the two in brackets represents 2 unknown amino acids.  
ModelAngelo did build a chain "Q" between chains Bv and A7, however, ModelAngelo built chain Q in reverse likely due to poor quality map data in this region so we chose not to use this chain in our paper and is why we inserted 2 random amino acids to preserve the chain length in the .hmm file.   
  
You can see in file aaprobtohmm.py how we merged these hmm files together for the HMMER search.  

