def get_array(hmm_filenames):                                                                            
    import numpy as np
    from pyhmmer.plan7 import HMMFile

    # Initialize a list to store reordered log probability arrays
    all_reordered_arrays = []

    # Define the reordering mapping
    old_order = "ACDEFGHIKLMNPQRSTVWY"
    new_order = "ARNDCQEGHILKMFPSTWYV"
    reorder_indices = [old_order.index(aa) for aa in new_order]

    for item in hmm_filenames:
        if isinstance(item, str):  # If the item is a filename
            filepath = f"output/hmm_profiles/{item}"  # Prepend the directory path

            # Load the HMM file
            with HMMFile(filepath) as hmm_file:
                hmms = [hmm for hmm in hmm_file]

            # Now, the HMMs are loaded into the hmms list.
            for hmm in hmms:
                print("HMM name:", hmm.name.decode())  # Decode the name from bytes to string

                # Get the emission probabilities
                emission_probabilities = hmm.match_emissions  # Get all rows

                # Convert the emission probabilities to a NumPy array
                probability_array = np.array(emission_probabilities)

                # Normalize the probabilities so they sum to 1 for each position
                normalized_probability_array = probability_array / np.sum(probability_array, axis=1, keepdims=True)

                # Round the probabilities to 3 decimal places
                rounded_probability_array = np.round(normalized_probability_array, 3)

                # Add a small positive value to avoid log(0)
                epsilon = 1e-6
                rounded_probability_array += epsilon

                # Convert to log probabilities
                log_probability_array = np.log(rounded_probability_array)

                # Reorder the columns based on the custom ordering
                reordered_log_probability_array = log_probability_array[:, reorder_indices]

                # Remove the first row from the array
                reordered_log_probability_array = reordered_log_probability_array[1:, :]

                # Append the reordered array to the list
                all_reordered_arrays.append(reordered_log_probability_array)

        elif isinstance(item, int):  # If the item is an integer
            # Create an array with rows where all 20 amino acids have equal probability
            equal_prob_row = np.full((item, 20), 1 / 20)  # 20 columns for 20 amino acids
            log_equal_prob_row = np.log(equal_prob_row)

            # Append the equal probability array to the list
            all_reordered_arrays.append(log_equal_prob_row)

    # Concatenate all arrays along the first axis (rows)
    concatenated_array = np.concatenate(all_reordered_arrays, axis=0)

    return concatenated_array

