# Donor Tracker - Discord Bot

**Donor Tracker** is a Python-based Discord bot that helps you track donations and contributions within your server. It integrates seamlessly with NQN (Not Quite Nocturnal) to generate custom donation-related images, making it perfect for charity campaigns, fundraising, or community donation tracking.

## Features

- **Donation Tracking**: Track all donations made by server members and keep a log of each donation.
- **NQN Integration**: Automatically generate custom donation-related images using NQN, perfect for sharing donation stats and messages creatively.
- **Donation Leaderboards**: Display a leaderboard to recognize and encourage top donors.
- **Customizable Commands**: Tailor the bot's commands and notifications to suit your server's needs.
- **Real-Time Updates**: Get real-time updates when donations are made, keeping the community informed.

## Installation

To get started with **Donor Tracker**, follow these steps to install and configure the bot in Python:

### Prerequisites

1. A **Discord bot token** from the [Discord Developer Portal](https://discord.com/developers/applications).
2. Python 3.8+ installed on your system.
3. A valid **NQN API key** for integration with NQN.
4. **pip** (Python package manager) installed.

### Steps to Set Up

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/donor-tracker.git
   cd donor-tracker
   ```

2. **Create a virtual environment** for the project (recommended):

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory of your project to store your environment variables:

   ```env
   DISCORD_TOKEN=your-discord-bot-token
   NQN_API_KEY=your-nqn-api-key
   ```

6. Run the bot:

   ```bash
   python bot.py
   ```

Your **Donor Tracker** bot should now be up and running and ready to track donations!

## Contributing

We welcome contributions to **Donor Tracker**! If you have ideas for improvements or new features, feel free to open a pull request or report an issue.

### How to Contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Make your changes.
4. Commit and push your changes.
5. Open a pull request with a description of your changes.

## License

**Donor Tracker** is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

## Support

If you have any questions or need help, feel free to join our [support server](https://discord.gg/tgk) or open an issue on GitHub.

