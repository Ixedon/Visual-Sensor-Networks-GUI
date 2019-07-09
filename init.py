import zmq, cv2, numpy, imutils
import threading, time, argparse
from tkinter import Tk, Label, Button, Canvas, NW, Frame, StringVar
from PIL import Image, ImageTk, ImageDraw
from Message_pb2 import ImageInfo, AdditionalControl
from google.protobuf.message import DecodeError