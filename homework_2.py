import numpy as np
import matplotlib.pyplot as plt
import stocks as st

"""
Finds the mean of the stock values with the built-in numpy function
and returns the array of each stock index's relevance to the mean and
in a percentage form

Args: array of stock values

Returns: array of percentages of the mean of each of those stock values 
"""
def percent_of_mean(stock_values):
    mean = np.mean(stock_values)
    return stock_values / mean * 100


"""
Plotting the graph by getting the three stock index arrays djia, nasdaq,
and s&p500 and running them through the percent of mean function first
to get the values needed to graph
"""
djia = percent_of_mean(st.djia)
nasdaq = percent_of_mean(st.nasdaq)
sp500 = percent_of_mean(st.sp500)
plt.plot(st.trading_days, percent_of_mean(st.djia), label = 'DJIA')
plt.plot(st.trading_days, percent_of_mean(st.nasdaq), label = 'NASDAQ')
plt.plot(st.trading_days, percent_of_mean(st.sp500), label = 'S&P500')
plt.xlabel("Trading Days Since Jun 1, 2016")
plt.ylabel("Percent Of Mean")
plt.title("Indices as Percent of Their Means")
plt.legend()

plt.show()





"""
Takes the stock values array and calculates the difference between each
element and the element that precedes it, then divides the difference by
the preceding stock value. The multiplication by 100 is to get the numbers
into a percent form. It then takes that change in percent and compares it
to the given percent, returning the sum of all of these occurrences.

Args:
Array of stock values
percentage to compare the change to

Returns:
Amount of occurrences when the stock change surpassed the percent given
"""
def num_days_big_percent_chg(stock_values, percent):
    stock_values = np.array(stock_values)
    percent_changes = (stock_values[1:] - stock_values[:-1]) / stock_values[:-1] * 100
    return np.sum(np.abs(percent_changes) > percent)

percent_thresholds = [0.2, 0.4, 0.6, 0.8, 1.0]

"""
Simply a helper method to reduce the task of calculating how many days
each stock index value crossed the threshold. Traverses a loop and calls
on the previous method to do the actual dirty work.

Args:
Array of stock values
Array of percent thresholds

Returns:
Array of all occurrences of the dramatic change, meaning over the threshold
"""
def calc_num_of_days(stock_values, percent_thresholds):
    num_days_list = []
    for threshold in percent_thresholds:
        num_days_list.append(num_days_big_percent_chg(stock_values, threshold))
    return num_days_list

stock1 = calc_num_of_days(st.djia, percent_thresholds)
stock2 = calc_num_of_days(st.nasdaq, percent_thresholds)
stock3 = calc_num_of_days(st.sp500, percent_thresholds)
plt.plot(percent_thresholds, stock1, label = 'DJIA')
plt.plot(percent_thresholds, stock2, label = 'NASDAQ')
plt.plot(percent_thresholds, stock3, label = 'S&P500')
plt.xlabel('Percent Change Threshold Magnitude')
plt.ylabel('Number of Days')
plt.title('Number of Days the Daily Percent Change Exceeded a Threshold Magnitude')
plt.legend()

plt.show()

"""
This function  calculates the three-day simple moving average for each day in
the stock index and returns a list of these moving average values, excluding
the first two days since they don't have enough historical data to calculate
the moving average. It traverses through a loop and determines the average of
the stock values of the current stock, and the previous two and appends it to
the array of averages.

Args:
Array of stock values

Returns:
Array of averages of the stock values in subsets of 3
"""
def moving_average(stock_values):
    moving_averages = []
    for i in range(2, len(stock_values)):
        avg = (stock_values[i] + stock_values[i - 1] + stock_values[i - 2]) / 3
        moving_averages.append(avg)

    return moving_averages


# Graph 1
plt.plot(st.trading_days[2:], moving_average(st.djia), label = 'MA')
plt.plot(st.trading_days[2:], st.djia[2:], label = 'Non-MA')
plt.xlabel('Trading Days Since Jun 1, 2016')
plt.ylabel('Moving Average of Index')
plt.title('Three-Day Moving Average of DJIA')
plt.legend()
plt.show()

#Graph 2
plt.plot(st.trading_days, moving_average(st.nasdaq), label = 'MA')
plt.plot(st.trading_days, moving_average(st.nasdaq), label = 'Non-MA')
plt.xlabel('Trading Days Since Jun 1, 2016')
plt.ylabel('Moving Average of Index')
plt.title('Three-Day Moving Average of NASDAQ')
plt.legend()
plt.show()

#Graph 3
plt.plot(st.trading_days, moving_average(st.sp500), label = 'MA')
plt.plot(st.trading_days, moving_average(st.sp500), label = 'Non-MA')
plt.xlabel('Trading Days Since Jun 1, 2016')
plt.ylabel('Moving Average of Index')
plt.title('Three-Day Moving Average of S&P500')
plt.legend()
plt.show()