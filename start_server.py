import http.server
import socketserver
import os
import webbrowser

PORT = 8000
DIRECTORY = os.path.dirname(os.path.realpath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Pokus o otevření prohlížeče
def open_browser():
    try:
        webbrowser.open_new_tab(f"http://localhost:{PORT}/rice_chart.html")
    except Exception as e:
        print(f"Could not automatically open browser: {e}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("------------------------------------------------------")
    print(f"  Starting local server in directory: {DIRECTORY}")
    print(f"  Serving at: http://localhost:{PORT}")
    print("------------------------------------------------------")
    print("\n  Your RICE Chart application should now be open in your web browser.")
    print("  If not, please open this URL manually:")
    print(f"  ==> http://localhost:{PORT}/rice_chart.html <==")
    print("\n  To stop the server, press Ctrl+C in this terminal.")
    
    # Otevřeme prohlížeč po krátké chvíli
    import threading
    threading.Timer(1, open_browser).start()
    
    httpd.serve_forever()
