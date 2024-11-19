from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

file_details = [
    {
        "file_path": "static/files/RemoteHiringList1.pdf",  # Path relative to the Flask app directory
        "file_name": "Remote Hiring List 1",
        "file_description": "Collection of 700+ companies actively hiring remotely"
    },
    {
        "file_path": "static/files/RemoteHiringList2.pdf",  # Path relative to the Flask app directory
        "file_name": "Remote Hiring List 2",
        "file_description": "Collection of 500+ companies actively hiring remotely"
    },
    {
        "file_path": "static/files/geometrybookfull.pdf",  # Path relative to the Flask app directory
        "file_name": "Geometry Book for CP",
        "file_description": "Full book on geometry for competitive programming. Free."
    },
    {
        "file_path": "static/files/systemdesign.pdf",  # Path relative to the Flask app directory
        "file_name": "System Design Notes",
        "file_description": "Full system design notes from a Google SDE II."
    },
    {
        "file_path": "static/files/remotework.pdf",  # Path relative to the Flask app directory
        "file_name": "Job hunt made easy",
        "file_description": "Top job hunt avenues that are underrated"
    },
]

@app.route('/')
def index():
    return render_template('index.html', file_details=file_details)

@app.route('/download/<int:file_index>')
def download_file(file_index):
    if 0 <= file_index < len(file_details):
        file_path = file_details[file_index]['file_path']
        # Get just the filename from the path for the download
        download_name = os.path.basename(file_path)
        try:
            return send_file(
                file_path,
                as_attachment=True,
                download_name=download_name
            )
        except FileNotFoundError:
            return f"Error: File {download_name} not found.", 404
    return "Invalid file index.", 404

if __name__ == '__main__':
    # Create the static/files directory if it doesn't exist
    os.makedirs('static/files', exist_ok=True)
    app.run(debug=True)