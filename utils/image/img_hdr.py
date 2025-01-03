import mimetypes

def get_image_type(file_path):
  mime_type, _ = mimetypes.guess_type(file_path)
  if mime_type and mime_type.startswith('image/'):
    return mime_type.split('/')[1]  
  return None
