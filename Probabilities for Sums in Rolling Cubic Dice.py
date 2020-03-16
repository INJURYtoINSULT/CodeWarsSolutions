from numpy.polynomial import polynomial as P

def rolldice_sum_prob(sum_, dice_amount):
    return (P.polypow([1, 1, 1, 1, 1, 1], dice_amount)).item(sum_ - dice_amount) / (6**dice_amount) if (sum_ <= 6 * dice_amount) else 0.0
