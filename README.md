## Disclaimer

The information provided by this program is for demonstrative purposes only and should not be considered as financial or investment advice. The program is not intended to provide personalized investment advice or recommendations for any specific individual or portfolio. 

The program is not affiliated with Yahoo Finance API or any other financial institution. The use of the Yahoo Finance API is subject to their terms and conditions, which are solely the responsibility of the user.

Investing in stocks carries risk, and the performance of individual stocks and the overall stock market can be volatile and unpredictable. Before making any investment decisions, you should do your own research and consult with a licensed financial advisor or professional.

The author of this program is not responsible for any investment decisions or actions taken based on the information provided by this program. By using this program, you agree to release the author from any liability or damages resulting from your investment decisions or actions.

# Project Title

Automated Equal-Weight S&P 500 Index Fund Portfolio Optimization

## Description

This project is designed to automate the process of creating an equal-weight S&P 500 index fund portfolio for a given portfolio size. It uses Python, together with various libraries such as Pandas, Numpy, Requests, and Xlsxwriter. The program fetches stock information for all S&P 500 constituents from Yahoo Finance API, calculates the number of shares to buy based on equal-weight position size, and outputs a recommended trades Excel file.

## Purpose

The purpose of this project is to provide a simple and automated way to create an equal-weight S&P 500 index fund portfolio for investors. The program fetches the latest stock information from Yahoo Finance API, calculates the number of shares to buy based on equal-weight position size, and outputs a recommended trades file that can be used to buy the selected stocks.

## Getting Started

### Dependencies

* Python 3.x
* Pandas
* Numpy
* Requests
* Xlsxwriter
* yfinance
* requests_cache
* requests_ratelimiter
* pyrate_limiter

### Installing

* Install Python from the official website: [https://www.python.org/downloads/ ↗](https://www.python.org/downloads/)
* Install the necessary dependencies using pip, for example:
```
pip install pandas
pip install yfinance
pip install requests_cache
pip install requests_ratelimiter
pip install pyrate_limiter
```

### Executing program

* Clone the repository to your local machine
* Open a terminal or command prompt and navigate to the directory containing the project files
* Run the following command to execute the program:
```
python SnPy_500.py
```
* Follow the prompts to enter the value of your portfolio and wait for the program to finish running
* The recommended trades Excel file will be saved in the same directory as `Recommended Trades.xlsx`

### Note on Cache

This program uses a caching mechanism provided by the `requests_cache` library to store the stock information fetched from Yahoo Finance API. This is to prevent excessive API calls and reduce the load on the Yahoo Finance servers.

However, if you need to rerun the program with updated information, you have to delete the cache to ensure that the latest stock information is fetched. This can be done by deleting the `yfinance.cache` file in the same directory as the program.

## Limitations

While this program provides a easy and automated way to create an equal-weight S&P 500 index fund portfolio, it has some limitations that you should be aware of:

* **Limited to S&P 500 Constituents**: The program only fetches stock information for the S&P 500 constituents listed on Yahoo Finance. Additionally, the S&P 500 constituents may change over time, so it is important to update the stock list periodically to ensure that your portfolio reflects the latest changes.

* **Dependent on Yahoo Finance API**: The program relies on the Yahoo Finance API to fetch stock information. The API calls may take a while to complete (15 - 20 minutes), especially if you are running the program for the first time or if the cache has been cleared. If the API is down or experiences issues, the program may not be able to retrieve the necessary information.

* **Margin of Error**: The program rounds down the number of shares to buy to account for possible fractional shares. However, this may result in a slight margin of error in the final portfolio composition.


## Credits

The program references the "Algorithmic Trading Using Python - Full Course" on YouTube, which can be found at [https://www.youtube.com/watch?v=xfzGZB4HhEE, ↗](https://www.youtube.com/watch?v=xfzGZB4HhEE,) and utilizes some of the concepts and techniques covered in the course, such as using Python to fetch stock data from APIs, calculating position sizes, and generating trade recommendations. 

We would like to give credit to the creators of the course for providing valuable insights and knowledge on algorithmic trading and using Python for finance. However, please note that this program is not affiliated with the course or its creators.

## Authors

* [Sujin Gurung ↗](https://github.com/Syddhartha-99)

## License

This project is licensed under the [MIT License ↗](https://opensource.org/licenses/MIT) - see the LICENSE.md file for details.
