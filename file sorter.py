from pathlib import Path
 
dirs = {
    '.mp3': 'Musique',
    '.wav': 'Musique',
    '.flac': 'Musique',
    '.avi': 'Videos',
    '.mp4': 'Videos',
    '.gif': 'Videos',
    '.bmp': 'Images',
    '.png': 'Images',
    '.jpg': 'Images',
    '.txt': 'Documents',
    '.pptx': 'Documents',
    '.csv': 'Documents',
    '.xls': 'Documents',
    '.odp': 'Documents',
    '.pages': 'Documents',
}
p = Path.cwd()
data = p / 'data'
 
files = [f for f in data.iterdir() if f.is_file()]
for file in files:
    dir_output = data / dirs.get(file.suffix, 'Divers')
    dir_output.mkdir(exist_ok=True)
    file.rename(dir_output / file.name)
