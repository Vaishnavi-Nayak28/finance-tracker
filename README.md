# Money Metrics - Personal Finance Tracker

A comprehensive personal finance management application built with Python and Streamlit. Designed to provide users with real-time insights into their financial activities through interactive data visualization and intuitive transaction management.

## Live Application

Access the deployed application: **[money-metrics.streamlit.app](https://money-metrics.streamlit.app/)**

## Overview

Money Metrics is a web-based financial tracking solution that enables users to monitor income and expenses, analyze spending patterns, and make data-driven financial decisions. The application leverages modern data visualization techniques to transform raw transaction data into actionable insights.

## Core Features

### Transaction Management
- Streamlined input interface for recording income and expense transactions
- Flexible categorization system supporting multiple transaction types
- Date-based transaction tracking with chronological ordering
- Optional transaction descriptions for detailed record-keeping

### Data Visualization
- Real-time dashboard displaying key financial metrics
- Interactive pie charts illustrating expense distribution by category
- Comparative bar charts for income versus expense analysis
- Time-series line graphs tracking financial trends over specified periods

### Data Operations
- CSV export functionality for external data analysis
- Session-based data persistence during active user sessions
- Bulk data management with clear-all functionality
- Responsive design optimized for desktop and mobile devices

## Technical Stack

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core application logic |
| Streamlit | Web framework and UI components |
| Pandas | Data manipulation and analysis |
| Plotly | Interactive data visualization |

## Installation and Setup

### System Requirements
- Python 3.8 or higher
- pip package manager
- Git version control system


## Usage Guide

### Adding Transactions
Navigate to the sidebar input panel and complete the following fields:
- Transaction type (Income/Expense)
- Amount in USD
- Category selection
- Optional description
- Transaction date

### Dashboard Navigation
The application interface consists of three primary tabs:

**Overview**: Displays aggregate financial metrics and visual breakdowns of income and expenses by category.

**Transactions**: Provides a tabular view of all recorded transactions with sorting capabilities and CSV export options.

**Trends**: Presents time-series visualizations showing spending and income patterns over time.

## Project Structure

```
finance-tracker/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore rules
└── venv/                 # Virtual environment (not tracked)
```

## Development Roadmap

### Planned Enhancements
- **Authentication System**: Implement user accounts with secure login functionality
- **Cloud Database Integration**: Persistent storage using PostgreSQL or MongoDB
- **Budget Management**: Goal-setting features with automated alerts and notifications
- **Recurring Transactions**: Support for scheduled, repeating transactions
- **Advanced Analytics**: Machine learning-based spending predictions and insights
- **Multi-currency Support**: International currency tracking and conversion
- **API Integration**: Direct bank account connectivity for automated transaction imports
- **Reporting Module**: Comprehensive monthly and annual financial reports

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full license text.

## Author

**Vaishnavi Nayak**

- GitHub: [@Vaishnavi-Nayak28](https://github.com/Vaishnavi-Nayak28)
- Repository: [finance-tracker](https://github.com/Vaishnavi-Nayak28/finance-tracker)

## Acknowledgments

This project utilizes the following open-source technologies:
- [Streamlit](https://streamlit.io/) for rapid web application development
- [Plotly](https://plotly.com/) for interactive visualization capabilities
- [Pandas](https://pandas.pydata.org/) for efficient data manipulation

---

**Note**: This application stores data in session state and does not persist data between sessions. For production use with persistent storage, database integration is recommended.
