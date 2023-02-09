from growmax import tinyweb

# Create web server application
app = tinyweb.webserver()

# Index page
@app.route('/')
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    # Send actual HTML page
    await response.send('<html><body><h1>Hello, world!</h1></html>\n')



def run():
    app.run(host='0.0.0.0', port=80)

