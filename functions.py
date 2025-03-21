from yt_dlp import YoutubeDL as yt
from yt_dlp.utils import DownloadError
from tkinter import messagebox

def download(url, type):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best' if type == 'video' else 'bestaudio/best' ,  # Descargar el mejor video y audio por separado
        'postprocessors': [{ 
            'key': 'FFmpegVideoConvertor' if type == 'video' else 'FFmpegExtractAudio' # Convertir video a mp4 o extraer audio 
        }],
        'outtmpl': '%(title)s.%(ext)s', # Nombre del archivo
    }
    
    if type == 'video': 
        ydl_opts['postprocessors'][0]['preferedformat'] = 'mp4'  # Preferir formato mp4 para video 
        ydl_opts['merge_output_format'] = 'mp4'  # Formato de salida para video
    else: 
        ydl_opts['postprocessors'][0]['preferredcodec'] = 'mp3' # Preferir formato mp3 para audio
        ydl_opts['postprocessors'][0]['preferredquality'] = '192' # Calidad de audio
    
    ydl = yt(ydl_opts)
    
    try:
        ydl.download([url])
        print("\nDownload completed.")
        messagebox.showinfo("Download completed", "The download has been completed successfully.")
    except DownloadError as e:
        messagebox.showerror("Error", f"An error occurred while downloading the video: {e.exc_info[1]}")