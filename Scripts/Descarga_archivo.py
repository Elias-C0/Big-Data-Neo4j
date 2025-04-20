import kagglehub

# Download latest version
path = kagglehub.dataset_download("andrewmvd/spotify-playlists")

print("Path to dataset files:", path)
