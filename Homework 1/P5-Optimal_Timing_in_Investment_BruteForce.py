function findBestProfit(prices, start, end):

    # Base case: If there's only one price or no prices
    if start >= end:
        return 0

    # Divide the array into two halves
    mid = (start + end) / 2

    # Recursively find the maximum profit in the left and right halves
    left_profit = findBestProfit(prices, start, mid)
    right_profit = findBestProfit(prices, mid + 1, end)

    # Find the minimum price in the left
    left_min = min(prices[start:mid+1])

    # Find the maximum price in the right
    right_max = max(prices[mid+1:end+1])

    # Calculate the cross profit (buy in left, sell in right)
    cross_profit = right_max - left_min

    # Return the maximum of the three profits
    return max(left_profit, right_profit, cross_profit)