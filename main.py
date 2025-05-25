import cv2
import os
import re
import easyocr
import json

from glob import glob
from tqdm import tqdm
from loguru import logger

class PlateDataAnalysis:
  def __init__(self) -> None:
    self.plates = []
    self.reader = easyocr.Reader(['en'])

  def convert_video_to_images(self, video_path:str, images_folder:str):
    cam = cv2.VideoCapture(video_path)

    try:
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
            first_time = True
        else:
          first_time = False
          logger.info('Path already exists')

    except OSError:
        logger.error(f'Error: Creating directory of {images_folder}')


    if first_time:
      currentframe = 0
      while cam.isOpened():
          ret, frame = cam.read()

          if ret:
              name = f'./{images_folder}/frame_{str(currentframe)}.jpg'
              logger.info(f'Processing Frame: {currentframe}')

              cv2.imwrite(name, frame)
              cam.set(cv2.CAP_PROP_POS_FRAMES, currentframe)
              currentframe += 15
          else:
              cam.release()
              break

      cam.release()
      cv2.destroyAllWindows()
      return True

    return False

  def is_valid_plate(self, plate):
    pattern = r"^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$"
    return bool(re.fullmatch(pattern, plate))

  def read_text_from_image(self, path_image:str, decoder:str):
      try:
          results = self.reader.readtext(path_image, decoder=decoder)
          return results
      except Exception as e:
          logger.error(e)
          return None

  def filter_plates(self, text_items:str):
      for item in text_items:
          text = item[1].replace('-','').replace(' ','').upper()
          precision = item[2]

          logger.info(f'extracted text: {text} precision {precision}')

          is_plate = self.is_valid_plate(text)
          if precision > 0.75 and is_plate:
            data = {
              "plate": text,
              "precision": precision
            }
            return data
      return None

  def list_images(self, path:str):
     jpgs = glob(path)
     return jpgs

if __name__ == '__main__':
  # options are 'greedy', 'beamsearch' and 'wordbeamsearch'
  decoder = 'greedy'

  plate_analysis = PlateDataAnalysis()
  plate_analysis.convert_video_to_images('./sample1.mp4', 'images')
  images_list = plate_analysis.list_images('./images/*')

  plates_list = {}

  for image in tqdm(images_list):
      texts = plate_analysis.read_text_from_image(image, decoder)
      text_plate = plate_analysis.filter_plates(texts)
      logger.info(f'plate text:  {text_plate}')

      if text_plate and text_plate['precision'] > plates_list.get(text_plate['plate'], 0):
          plates_list[text_plate['plate']] = text_plate['precision']
      logger.info('Not a valid plate')

  with open(f'./plates_{decoder}.json', 'w') as file:
    json.dump(plates_list, file, indent=4)

logger.info('Processing Finished')