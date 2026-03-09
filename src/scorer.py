def score_deal(predicted_price, asking_price):
    difference = predicted_price - asking_price
    pct_diff = (difference / predicted_price) * 100

    if pct_diff > 10:
        score = 'Great Deal'
    
    elif pct_diff < -10:
        score = "Overpriced"
    
    else:
        score = "Fair Price"

    return {"difference" : difference, "pct_difference" : pct_diff, "score" : score}