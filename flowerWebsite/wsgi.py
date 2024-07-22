from flask import Flask, render_template_string, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    flowerButton ="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flower Generator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
            }
            header {
                background-color: #666;
                padding: 30px;
                font-size: 35px;
                color: white;
            }
            .button-container {
                width: 50%; /* Adjust width of container */
                max-width: 300px; /* Max width of container */
            }
            button {
                width: 100%; /* Make button width 100% of its container */
                padding: 10px; /* Adjust padding */
                font-size: 16px; /* Adjust font size */
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 20px;
            }
            button:hover {
                background-color: #45a049;
            }
            img {
                margin-top: 20px;
                max-width: 100%;
                height: auto;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }
        </style>
    </head>
    <body>
        
        <div class="button-container">
            <button onclick="showImage()">Click me</button>
        </div>
        <p id="demo"></p>
        <img id="myImage" style="display:none;" alt="Roses Image">
        <script>
            function showImage() {
                let randomNum = Math.floor(Math.random() * 4);
                if(randomNum == 0){
                    var img = document.getElementById('myImage');
                    img.src = "{{ url_for('static', filename='roses.jpg') }}";
                    img.style.display = 'block';
                
                    var message = document.getElementById('demo');
                    message.innerHTML = "Have a nice day <3";
                }
                else if(randomNum == 1){
                    var img = document.getElementById('myImage');
                    img.src = "{{ url_for('static', filename='sunflowers.jpg') }}";
                    img.style.display = 'block';
                
                    var message = document.getElementById('demo');
                    message.innerHTML = "Have a nice day <3";
                }
                else if(randomNum == 2){
                    var img = document.getElementById('myImage');
                    img.src = "{{ url_for('static', filename='lilies.jpg') }}";
                    img.style.display = 'block';
                
                    var message = document.getElementById('demo');
                    message.innerHTML = "Have a nice day <3";
                }
                else if(randomNum == 3){
                    var img = document.getElementById('myImage');
                    img.src = "{{ url_for('static', filename='orchids.jpg') }}";
                    img.style.display = 'block';
                
                    var message = document.getElementById('demo');
                    message.innerHTML = "Have a nice day <3";
                }
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(flowerButton)


@app.route("/test_image")
def test_image():
    return url_for('static', filename='roses.jpg')

if __name__ == "__main__":
    app.run(debug=True)