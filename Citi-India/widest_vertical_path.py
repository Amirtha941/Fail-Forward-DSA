def widest_vertical_path(X, Y):
    # Get unique X-coordinates and sort them
    unique_x = sorted(set(X))
    
    # Find maximum gap between consecutive X values
    max_gap = 0
    for i in range(1, len(unique_x)):
        gap = unique_x[i] - unique_x[i-1]
        max_gap = max(max_gap, gap)
    
    return max_gap

# Example usage
X = [1, 8, 7, 3, 4, 1, 8]
Y = [6, 4, 1, 8, 5, 1, 7]

print("Maximum width of vertical path:", widest_vertical_path(X, Y))
