import imageio 
import os  # To do paths

clip = os.path.abspath('small_video.mp4')  # Gives it the absolute path

def gifMaker(inputPath, targetFormat):  # inputPath is the actual clip, targetFormat is the format type
    outputPath = os.path.splitext(inputPath)[0] + targetFormat  # splitext splits the inputPath into a list

    print(f'converting {inputPath} \n to {outputPath}')
    
    reader = imageio.get_reader(inputPath)    # To grab images from inputPath       
    fps = reader.get_meta_data()['fps']  # reads the metadata of video and gives the fps 

    writer = imageio.get_writer(outputPath, fps = fps)  # returns a writer object which can be used to write data and meta data to the specified line

    for frames in reader:
        writer.append_data(frames)  # Appending the framees from reader to the writer
        print(f'Frame {frames}')  # Printing the frames

    print('Done!')
    writer.close()  # closes the writer, saying we don't want to write anymore (flush and close reader/writer)

gifMaker(clip, '.gif')  # Calling the function gifMaker()
