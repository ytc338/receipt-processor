from decimal import Decimal, ROUND_CEILING
from app.models import Receipt

def calc_points(receipt: Receipt):
    pts = 0
    total = Decimal(receipt.total)

    for c in receipt.retailer:
        if c.isalnum():
            pts += 1
    
    # if the denominator of irreducible fraction is 1, total is an interger
    if total.as_integer_ratio()[1] == 1:
        pts += 50
    
    if total % Decimal('.25') == 0:
        pts += 25

    pts += 5 * (len(receipt.items) // 2)

    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            pts += (Decimal(item.price) * Decimal('0.2')).to_integral_value(rounding=ROUND_CEILING)

    if receipt.purchaseDate.day % 2:
        pts += 6

    if 14 <= receipt.purchaseTime.hour < 16:
        pts += 10
    
    return pts
