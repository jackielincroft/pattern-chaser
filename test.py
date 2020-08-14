def results():
    # TODO: change placeholder code once we actually have an algorithm to determine recommended patterns
    # best_pats is a dictionary, where the keys are patterns and the values are likeability scores
    best_pats = {}
    
    # Get a random sample of 50 eligible patterns
    eligible_pats_ids = API().list_of_ids_random_pg(user.presets_query)
    random_sample_ids = random.sample(eligible_pats_ids, 50)

    # Go through the random sample, and find the top 5 that the user is most likely to enjoy
    min = 0
    for pat_id in random_sample_ids:
        pat = Pattern(pat_id)
        score = float(pat.likeability_score(user.prefs))
  
        # add first 5 scores regardless
        if len(best_pats) < 5: 
            best_pats[pat] = score
        # after first 5, only replace patterns with better ones (higher scores)
        else:
            if score > min(float(sub) for sub in best_pats.values()):
                best_pats.pop(min(float(sub) for sub in best_pats.values())) # remove the fifth best
                best_pats[pat] = score # add this pattern and its score
