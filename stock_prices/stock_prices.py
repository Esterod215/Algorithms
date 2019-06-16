#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #firs-pass attempt (incorrect)
  
  # lowest_price_so_far = prices[0]
  # max_price_so_far = prices[1]
  # max_profit = prices[1] - prices[0]
  
  # for price in prices[:len(prices)-1]: 
  #   if price < lowest_price_so_far and price < max_price_so_far:
  #     lowest_price_so_far = price
  #     max_profit = max_price_so_far - lowest_price_so_far
  #     print("p",max_profit)
  #     print("l", lowest_price_so_far)
    
  #   for next_price in prices[1:len(prices)]:
  #     if next_price > max_price_so_far:
  #       max_price_so_far = next_price
  #       print("m",max_price_so_far)
  #       max_profit = max_price_so_far - lowest_price_so_far
  #       print("p",max_profit)
  max_price = prices[1]
  max_profit = prices[1] - prices[0]
  
  if len(prices) == 1: #edge case
    return prices[0]
  
  elif len(prices) == 0: #empty array
    return
  
  else:
    
    for i in range(1,len(prices)):
      max_price = prices[i]
      
      
      for j in range(i):
        if max_profit < max_price - prices[j]:
          max_profit = max_price - prices[j]



  return max_profit

  



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))