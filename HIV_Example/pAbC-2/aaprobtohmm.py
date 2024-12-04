from model_angelo.utils.aa_probs_to_hmm import dump_aa_logits_to_hmm_file
from getarray import get_array

#Define the list of .hmm filenames and integers
hmm_filenames = ["BG.hmm","A0.hmm"]

# Call get_array and get the concatenated array
concatenated_array = get_array(hmm_filenames)

# Use the concatenated array as input to dump_aa_logits_to_hmm_file
dump_aa_logits_to_hmm_file(aa_logits=concatenated_array, output_file="heavyassembled.hmm")

# Define the list of .hmm filenames and integers
hmm_filenames = ["Bv.hmm",2,"A7.hmm","f.hmm","BX.hmm","BF.hmm"]

# Call get_array and get the concatenated array
concatenated_array = get_array(hmm_filenames)

# Use the concatenated array as input to dump_aa_logits_to_hmm_file
dump_aa_logits_to_hmm_file(aa_logits=concatenated_array, output_file="lightassembled.hmm")

