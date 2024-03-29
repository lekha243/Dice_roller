def calculate_probability():
    results = {}
    
    for die_a in range(1, 7):
        for die_b in range(1, 7):
            total_sum = die_a + die_b
            if total_sum in results:
                results[total_sum] += 1
            else:
                results[total_sum] = 1
    
    total_combinations = 6 * 6
    probabilities = {sumd: count / total_combinations for sumd, count in results.items()}
    
    # Print the probabilities in tabular form
    print("| Sum | Probability |")
    print("|-----|-------------|")
    for sumd, prob in probabilities.items():
        print(f"| {sumd} | {prob} |")

calculate_probability()
