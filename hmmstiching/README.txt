Use this code to stitch .hmm files together

Both getarray.py and aaprobtohmm.py should be placed in the same folder that you ran Modelangelo in
i.e. the parent folder to 'output'
getarray.py will look in ./output/hmm_profiles for the .hmm files that you requested to stitch

Please edit aaprobstohmm.py to select which .hmm files you'd like to stitch.

#Define the list of .hmm filenames and integers
hmm_filenames = ["BG.hmm",2,"A0.hmm"]

# Call get_array and get the concatenated array
concatenated_array = get_array(hmm_filenames)

# Use the concatenated array as input to dump_aa_logits_to_hmm_file
dump_aa_logits_to_hmm_file(aa_logits=concatenated_array, output_file="heavyassembled.hmm")

For the example above you have requested to stitch BG.hmm followed by two random amino acids followed by A0.hmm
This will generate a new .hmm that will have the name heavyassembled.hmm
