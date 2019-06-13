#!/usr/bin/python

import argparse

def find_max_profit(prices):
  lowest_price_so_far = prices[0]
  max_profit = 0
  
  for price in prices: 
    if price <= lowest_price_so_far:
      lowest_price_so_far = price
    
    for next_price in prices[1:len(prices) -1]:
      if max_profit < next_price - lowest_price_so_far:
        max_profit = next_price - lowest_price_so_far

  return max_profit

  



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))