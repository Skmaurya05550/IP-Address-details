# IP Address Tracker

A simple web-based IP Address Tracker that allows users to input an IP address and retrieve details such as the city, region, country, and geographical location of the IP. This tracker uses the [ipinfo.io](https://ipinfo.io/) API to fetch IP information.

## Features

- Track the location of any IP address.
- Displays details like city, region, country, and location coordinates.
- Simple and clean user interface.

## Screenshot

![IP Address Tracker](https://ibb.co/QNqxknj)

## How to Use

1. Clone or download this repository.
2. Open the `index.html` file in your browser.
3. Enter any IP address in the input field and click **Track IP**.
4. The location details of the IP will be displayed below.

## Installation and Setup

1. Register at [ipinfo.io](https://ipinfo.io/) to get an API token.
2. Replace `YOUR_TOKEN_HERE` in the `index.html` file with your API key.
3. Run the HTML file locally in your browser to track IP addresses.

## Sample Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IP Address Tracker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 300px;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button {
            padding: 10px 20px;
            border: none;
            background-color: #007BFF;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .result {
            margin-top: 20px;
        }

        #ipDetails {
            word-wrap: break-word;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>IP Address Tracker</h1>
        <label for="ipInput">Enter IP address:</label>
        <input type="text" id="ipInput" placeholder="Enter an IP address">
        <button onclick="getLocation()">Track IP</button>

        <div class="result">
            <h2>Location Details:</h2>
            <p id="ipDetails"></p>
        </div>
    </div>

    <script>
        async function getLocation() {
            const ipAddress = document.getElementById('ipInput').value;
            const result = document.getElementById('ipDetails');

            if (ipAddress === '') {
                result.textContent = 'Please enter an IP address.';
                return;
            }

            try {
                const response = await fetch(`https://ipinfo.io/${ipAddress}/json?token=YOUR_TOKEN_HERE`);
                if (!response.ok) {
                    throw new Error('Unable to track IP');
                }

                const data = await response.json();
                result.innerHTML = `
                    <strong>IP Address:</strong> ${data.ip} <br>
                    <strong>City:</strong> ${data.city} <br>
                    <strong>Region:</strong> ${data.region} <br>
                    <strong>Country:</strong> ${data.country} <br>
                    <strong>Location:</strong> ${data.loc}
                `;
            } catch (error) {
                result.textContent = 'Error: ' + error.message;
            }
        }
    </script>

</body>
</html>

