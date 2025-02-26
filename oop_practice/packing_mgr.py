def packaging(items: list[int]):
    known = {
        "Blue": [("L", 1)],
        "Cam": [("M", 1), ("L", 2)],
        "Game": [("L", 2)]
    }
    
    item_count = {}
    for item in items:
        if item not in item_count:
            item_count[item] = 1
        else:
            item_count[item] += 1
    
    result = []
    
    for item, count in item_count.items():
        box_limits = known[item]
        remaining = count
        
        for i, (box_type, capacity) in enumerate(box_limits):
            if remaining <= 0:
                break
            num_full = remaining // capacity
            if num_full > 0:
                result.extend([(box_type, [item] * capacity)] * num_full)
                