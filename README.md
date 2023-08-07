# Negotiation Bot

The Negotiation Bot is a simple interactive chatbot that assists users in negotiating prices with suppliers based on historical data and pricing information from other suppliers. It uses a basic price prediction model to suggest a target price for negotiations.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- tkinter

## Installation

1. Clone the repository or download the ZIP file.
2. Install the required libraries using the following command:

## Usage

1. Run the `negotiation_bot.py` script using Python 3.x:

2. A graphical user interface (GUI) window will appear.
3. Enter the current supplier quote  and click the "Submit" button.
4. The negotiation bot will process the entered quote and provide the negotiation result.

## How It Works

The negotiation bot uses historical data from the current supplier and pricing information from other suppliers to make predictions. It applies a simple linear regression model to predict the expected price based on historical trends. The bot also analyzes the lowest competitor price to establish a target price for negotiations.

If the current supplier's initial quote is lower than or equal to the target price, the negotiation is successful, and the bot will display the final price. Otherwise, the bot will prompt the supplier to provide a revised price. The supplier can choose to exit the negotiation by leaving the revised price window empty.

## Limitations

- The bot uses a basic price prediction model, and the accuracy of predictions may vary depending on the complexity of the data.
- The provided historical and competitive data are samples and do not represent real-world scenarios.

## Customization

The negotiation bot can be customized and enhanced in various ways, such as using more advanced prediction models, integrating real-time data sources, and adding additional negotiation strategies.

## Contributions

Contributions to this project are welcome. Feel free to create a pull request or submit issues for bug reports or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

