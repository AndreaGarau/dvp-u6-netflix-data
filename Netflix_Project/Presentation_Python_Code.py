from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def Date(data):
    """data is just order
    return 1st and last value
    of date: year-month-day"""
    date = list(data["Date"])
    earliest = date[0]
    latest = date[-1]
    return earliest, latest

# Load Data
netflix_stocks = pd.read_csv("../Netflix+Stocks+Capstone/Netflix Stocks Capstone/NFLX.csv")
dowjones_stocks = pd.read_csv("../Netflix+Stocks+Capstone/Netflix Stocks Capstone/DJI.csv")
netflix_stocks_quarterly = pd.read_csv("../Netflix+Stocks+Capstone/Netflix Stocks Capstone/NFLX_daily_by_quarter.csv")

er_net_sto, lat_net_sto = Date(netflix_stocks)
print("Netflix Stocks earliest date:\t{0}\nNetflix Stocks latest date:\t{1}\n".format(er_net_sto, lat_net_sto))
er_dow_sto, lat_dow_sto = Date(dowjones_stocks)
print("Dowjones Stocks earliest date:\t{0}\nDowjones Stocks latest date:\t{1}\n".format(er_dow_sto, lat_dow_sto))
er_net_sto_qua, lat_net_sto_qua = Date(netflix_stocks_quarterly)
print("Netflix Stocks Quarterly earliest date:\t{0}\nNetflix Stocks Quarterly latest date:\t{1}\n".format(er_net_sto_qua, lat_net_sto_qua))

netflix_stocks.rename(inplace=True, columns={"Adj Close":"Price"})
netflix_stocks_quarterly.rename(inplace=True, columns={"Adj Close":"Price"})
dowjones_stocks.rename(inplace=True, columns={"Adj Close":"Price"})

def Min_Max(data):
    Min_Av = data[data["Quarter"] == "Q1"]["Price"].mean()
    Max_Av = data[data["Quarter"] == "Q4"]["Price"].mean()
    Min = data["Price"].min()
    Max = data["Price"].max()
    return Min, Max, Min_Av, Max_Av

Min, Max, Min_Av, Max_Av = Min_Max(netflix_stocks_quarterly)
print("Min:\t{0}\nMax:\t{1}\nMin Average:\t{2}\nMax Average:\t{3}".format(Min, Max, Min_Av, Max_Av))

plt.close("all")
ax = sns.violinplot(data=netflix_stocks_quarterly, x="Quarter", y="Price")
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
ax.grid()
ax.set_ylabel("Closing Stock Price")
ax.set_xlabel("Business Quarters in 2017")
plt.savefig("Distribution_2017_Netflix_Stock_Prices_Quarter_0.png")
ax.annotate("Max\nAbsolute",
            color="orange",
            xy=(3, 207),
            xytext=(3.5, 180),
            arrowprops=dict(color='orange', shrink=.1),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
ax.annotate("Min\nAbsolute",
            color="orange",
            xy=(0, 124),
            xytext=(.8, 119),
            arrowprops=dict(color='orange', shrink=.08),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
plt.savefig("Distribution_2017_Netflix_Stock_Prices_Quarter_1.png")
ax.annotate("Max\nAverage",
            color="red",
            xy=(3, Max_Av+1),
            xytext=(1, 204),
            arrowprops=dict(color='red', shrink=.01),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
ax.annotate("Min\nAverage",
            color="red",
            xy=(0, Min_Av+1),
            xytext=(.4, 170),
            arrowprops=dict(color='red', shrink=.01),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
plt.savefig("Distribution_2017_Netflix_Stock_Prices_Quarter_2.png")
ax.annotate("The Most\nRange Price",
            color="green",
            xy=(2, 150),
            xytext=(3, 130),
            arrowprops=dict(color="green", shrink=.01),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
plt.savefig("Distribution_2017_Netflix_Stock_Prices_Quarter_3.png")

#
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q","2Q","3Q","4Q"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
plt.close("all")
plt.scatter(x_positions, earnings_actual, c="red")
plt.scatter(x_positions, earnings_estimate, c="blue", alpha=.5)
plt.grid()
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.title("Earnings Per Share in Cents Year: 2017")
plt.savefig("Earnings_Share_Cents_0.png")
plt.annotate("Estimate = Actual",
            color="orange",
            xy=(4, .4),
            xytext=(3, .2),
            arrowprops=dict(facecolor="orange", shrink=.01),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
plt.annotate("",
            color="orange",
            xy=(2.05, .15),
            xytext=(3, .2),
            arrowprops=dict(facecolor="orange", shrink=.01),
            )
plt.savefig("Earnings_Share_Cents_1.png")

# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q\n2017","3Q\n2017","4Q\n2017", "1Q\n2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = .8 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]
plt.close("all")
plt.bar(bars1_x, revenue_by_quarter)

# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = .8 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]
plt.bar(bars2_x, earnings_by_quarter)
labels = ["Revenue", "Earnings"]
plt.legend(labels)
plt.title("The Earnings and Revenue Reported by Netflix")

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]

plt.xticks(middle_x, quarter_labels)
plt.grid()
plt.savefig("Earnings_Revenue_Reported_Netflix_0.png")
plt.annotate("The Earnings\n7.84%\nof Revenue",
            color="blue",
            xy=(7.7, .1),
            xytext=(7.5, 1.2),
            arrowprops=dict(facecolor="cyan", shrink=.01),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
plt.savefig("Earnings_Revenue_Reported_Netflix_1.png")
# Trend
slope, intercept = np.polyfit(bars1_x, revenue_by_quarter, 1)
trendline = [intercept + (slope * i) for i in bars1_x]
plt.plot(bars1_x, trendline, color="blue", marker="o")
slope, intercept = np.polyfit(bars2_x, earnings_by_quarter, 1)
trendline = [intercept + (slope * i) for i in bars2_x]
plt.plot(bars2_x, trendline, color="orange", marker="o")
plt.savefig("Earnings_Revenue_Reported_Netflix_2.png")

def Percentage(revenue, earnings):
    result = [100/revenue[i]*earnings[i] for i in range(len(revenue))]
    return result

earn_perc = Percentage(revenue_by_quarter, earnings_by_quarter)
print("The Earnings '1Q2018' is {0:.2f}% of Revenue".format(earn_perc[-1]))

# 8
# Left plot Netflix
# ax1 = plt.subplot(total number rows, total number columns, index of subplot to modify)

year = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}
def Read_Date(data):
    result = [year[int(i.split("-")[1])] for i in data["Date"]]
    return result

plt.close("all")
ax1 = plt.subplot(1, 2, 1)
date = Read_Date(netflix_stocks)
plt.plot(date, netflix_stocks["Price"], marker="o")
ax1.set_title("Price Netflix Stocks 2017")
plt.xticks(rotation=45)
ax1.set_ylabel("Stock Price")
plt.grid()

# Right plot Dow Jones
# ax2 = plt.subplot(total number rows, total number columns, index of subplot to modify)
ax2 = plt.subplot(1, 2, 2)
date = Read_Date(dowjones_stocks)
plt.plot(date, dowjones_stocks["Price"], marker="o")
ax2.set_title("Price Dow Jones Stocks 2017")
plt.xticks(rotation=45)
ax2.set_ylabel("Stock Price")
plt.subplots_adjust(wspace=.5)
plt.grid()
plt.savefig("Netflis_DowJones_Stocks.png")
