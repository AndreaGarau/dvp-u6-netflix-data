
# coding: utf-8

# # Introduction
# 
# In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the "Netflix Stock Profile" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. 
# 
# For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:
# + The distribution of the stock prices for the past year
# + Netflix's earnings and revenue in the last four quarters
# + The actual vs. estimated earnings per share for the four quarters in 2017
# + A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 
# 
# Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).
# 
# During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.
# 
# After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:
# 
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual earnings per share
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 
# Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)
# 

# ## Step 1
# 
# Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 2

# Let's load the datasets and inspect them.

# Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.
# 
# Hint: Use the `pd.read_csv()`function).
# 
# Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day.

# In[2]:


netflix_stocks = pd.read_csv("NFLX.csv")
print(netflix_stocks)


# Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.
# 
# Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
# 

# In[3]:


dowjones_stocks = pd.read_csv("DJI.csv")
print(dowjones_stocks)


# Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.
# 

# In[4]:


netflix_stocks_quarterly = pd.read_csv("NFLX_daily_by_quarter.csv")
print(netflix_stocks_quarterly)


# ## Step 3

# Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.
#  - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly
#  - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
#  - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 
#  
# Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer.

# What year is represented in the data? Look out for the latest and earliest date.

# In[5]:


def Date(data):
    """data is just order
    return 1st and last value
    of date: year-month-day"""
    date = list(data["Date"])
    earliest = date[0]
    latest = date[-1]
    return earliest, latest

# What year is represented in the data? Look out for the latest and earliest date.
er_net_sto, lat_net_sto = Date(netflix_stocks)
print("Netflix Stocks earliest date:\t{0}\nNetflix Stocks latest date:\t{1}\n".format(er_net_sto, lat_net_sto))
er_dow_sto, lat_dow_sto = Date(dowjones_stocks)
print("Dowjones Stocks earliest date:\t{0}\nDowjones Stocks latest date:\t{1}\n".format(er_dow_sto, lat_dow_sto))
er_net_sto_qua, lat_net_sto_qua = Date(netflix_stocks_quarterly)
print("Netflix Stocks Quarterly earliest date:\t{0}\nNetflix Stocks Quarterly latest date:\t{1}\n".format(er_net_sto_qua, lat_net_sto_qua))


# + Is the data represented by days, weeks, or months? 
# + In which ways are the files different? 
# + What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?

# In[6]:


# 1. 
# Netflix Stocks is represented by months, the 1st of the month for 12 months
# Dowjones Stocks is represented by months, the 1st of the month for 12 months
# Netflix Stocks Quarterly is rapresented by days.
# 2.
# The first two sets of data: Netflix Stocks, Dowjones Stocks are sampled the first of the month
# the other set of values: Netflix Stocks Quarterly is sampled about every 5 days.
# 3. 
# The Netflix Stocks Quarterly has one column more: Quarter
# in the Netflix Stocks the values are sampled the 1st of the month on the other hand in the 
# Netflix Stocks Quarterly every 5 days about.


# In[7]:


print("Netflix Stocks columns values are:\t{0}".format(netflix_stocks.columns.values))
print("Netflix Stocks Quarterly columns values are:\t{0}".format(netflix_stocks_quarterly.columns.values))
print()
print(netflix_stocks.head())
print()
print(netflix_stocks_quarterly.head())


# # Step 4
# 
# Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. 

# In[8]:


netflix_stocks.head()


# What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! 
# 
# The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
# 
# This means this is the column with the true closing price, so these data are very important.
# 
# Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.
# 
# Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.
# Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).
# 

# In[9]:


netflix_stocks.rename(inplace=True, columns={"Adj Close":"Price"})
netflix_stocks_quarterly.rename(inplace=True, columns={"Adj Close":"Price"})
dowjones_stocks.rename(inplace=True, columns={"Adj Close":"Price"})


# Run `netflix_stocks.head()` again to check your column name has changed.

# In[10]:


netflix_stocks.head()


# Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`.

# In[11]:


dowjones_stocks.head()


# In[12]:


netflix_stocks_quarterly.head()


# ## Step 5
# 
# In this step, we will be visualizing the Netflix quarterly data! 
# 
# We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!
# 
# 
# 1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.
# 2. Use `sns.violinplot()` and pass in the following arguments:
# + The `Quarter` column as the `x` values
# + The `Price` column as your `y` values
# + The `netflix_stocks_quarterly` dataframe as your `data`
# 3. Improve the readability of the chart by adding a title of the plot. Add `"Distribution of 2017 Netflix Stock Prices by Quarter"` by using `ax.set_title()`
# 4. Change your `ylabel` to "Closing Stock Price"
# 5. Change your `xlabel` to "Business Quarters in 2017"
# 6. Be sure to show your plot!
# 

# In[13]:


ax = sns.violinplot(data=netflix_stocks_quarterly, x="Quarter", y="Price")
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
ax.grid()
ax.set_ylabel("Closing Stock Price")
ax.set_xlabel("Business Quarters in 2017")
plt.show()


# ## Graph Literacy
# - What are your first impressions looking at the visualized data?
# 
# - In what range(s) did most of the prices fall throughout the year?
# 
# - What were the highest and lowest prices? 

# In[14]:


# 1.
# The prices grow during the year, the charts are different from each other
# 2.
# In the Q3 quarter we have the most range of the prices
# 3.


#  

# In[15]:


def Min_Max(data):
    Min_Av = data[data["Quarter"] == "Q1"]["Price"].mean()
    Max_Av = data[data["Quarter"] == "Q4"]["Price"].mean()
    Min = data["Price"].min()
    Max = data["Price"].max()
    return Min, Max, Min_Av, Max_Av

Min, Max, Min_Av, Max_Av = Min_Max(netflix_stocks_quarterly)
print("Min:\t{0}\nMax:\t{1}\nMin Average:\t{2}\nMax Average:\t{3}".format(Min, Max, Min_Av, Max_Av))


# ## Step 6
# 
# Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. 
# 
# 1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.
# 2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color
# 
# 3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.
# 4. Add a legend by using `plt.legend()` and passing in a list with two strings `["Actual", "Estimate"]`
# 
# 5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`
# 6. Assing "`"Earnings Per Share in Cents"` as the title of your plot.
# 

# In[16]:


x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
plt.scatter(x_positions, earnings_actual, c="red")
plt.scatter(x_positions, earnings_estimate, c="blue", alpha=.5)
plt.grid()
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.title("Earnings Per Share in Cents")
plt.show()


# ## Graph Literacy
# 
# + What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.
# 

# In[17]:


# That the estimate is correct.


# ## Step 7

# Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).
# 
# As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. 
# 
# 1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars
# 2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data
# 3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars
# 4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data
# 5. Create a legend for your bar chart with the `labels` provided
# 6. Add a descriptive title for your chart with `plt.title()`
# 7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`
# 8. Be sure to show your plot!
# 

# In[18]:


# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = .8 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]
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
plt.grid()
plt.xticks(middle_x, quarter_labels)
plt.show()


# ## Graph Literacy
# What are your first impressions looking at the visualized data?
# 
# - Does Revenue follow a trend?
# - Do Earnings follow a trend?
# - Roughly, what percentage of the revenue constitutes earnings?

# In[19]:


# Earnings and Revenue are different: Revenue are bigger than Earnings
# 1.
# Yes, it does. Revenue follows a trend
# 2.
# Yes, it does. Earnings follow a trend
# 3.


# In[20]:


def Percentage(revenue, earnings):
    result = [100/revenue[i]*earnings[i] for i in range(len(revenue))]
    return result

earn_perc = Percentage(revenue_by_quarter, earnings_by_quarter)
print("The Earnings '1Q2018' is {0:.2f}% of Revenue".format(earn_perc[-1]))


# ## Step 8
# 
# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. 
# 
# Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.
# - We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot
#     - `1`-- the number of rows for the subplots
#     - `2` -- the number of columns for the subplots
#     - `1` -- the subplot you are modifying
# 
# - Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)
# - Assign "Netflix" as a title to this subplot. Hint: `ax1.set_title()`
# - For each subplot, `set_xlabel` to `"Date"` and `set_ylabel` to `"Stock Price"`
# - Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)
# - Assign "Dow Jones" as a title to this subplot. Hint: `plt.set_title()`
# - There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`
# - Be sure to `.show()` your plots.
# 

# In[21]:


# Left plot Netflix
# ax1 = plt.subplot(total number rows, total number columns, index of subplot to modify)
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks["Date"], netflix_stocks["Price"])
ax1.set_title("Price Netflix Stocks")
plt.xticks(rotation=90)
ax1.set_xlabel("Date")
ax1.set_ylabel("Stock Price")
plt.grid()

# Right plot Dow Jones
# ax2 = plt.subplot(total number rows, total number columns, index of subplot to modify)
ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks["Date"], dowjones_stocks["Price"])
ax2.set_title("Price Dow Jones Stocks")
plt.xticks(rotation=90)
ax2.set_xlabel("Date")
ax2.set_ylabel("Stock Price")
plt.grid()
plt.subplots_adjust(wspace=.5)
plt.show()


# - How did Netflix perform relative to Dow Jones Industrial Average in 2017?
# - Which was more volatile?
# - How do the prices of the stocks compare?

# In[22]:


# 1.
# Both are growing, but Netflix is uneven compared to Dow Jones
# 2. 
# Netflix Stocks was more volatile
# 3.
# For the same abscissa (date) we compare the value of the ordinates (price).


# # Step 9
# 
# It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig("filename.png")`.
# 
# As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!
# 
# Remember that your slideshow must include:
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual earnings per share
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 
